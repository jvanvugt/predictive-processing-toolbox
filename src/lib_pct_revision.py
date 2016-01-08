import numpy
from scipy.optimize import minimize, minimize_scalar, brute, basinhopping
from matplotlib.pyplot import plot, xlim, ylim, scatter, figure
from mpl_toolkits.mplot3d import Axes3D
import itertools

from lib_pct_inference import *
from lib_pct_read_network import *
from lib_pct_build_network import *
from lib_pct_tools import *


def belief_revision1(network, hypothesis_nodes, prediction_nodes, observations, method='Local Min'):
	if len(hypothesis_nodes) > 1:
		raise ValueError("Only one hypothesis node.")
	for hyp in hypothesis_nodes:
		if network.get_node_parents(network, hyp) != []:
			raise ValueError(hyp + " is not a hypothesis node.")
	h = hypothesis_nodes[0]
	for pred in prediction_nodes:
		if network.get_node_children(pred) != []:
			raise ValueError(pred + " is not a prediction node.")
	h_outcomes = network.get_node_outcomes(h)
	dim = len(h_outcomes)
	x0 = numpy.ones(dim) / dim
	bounds = tuple([(0,1) for i in range(dim)])
	xplotx = []
	xploty = []
	xplotz = []
	def p_minimize(x, disp=False, plotting=True):
		if any(x < numpy.zeros_like(x)):
			return 100
		if sum(x) == 0:
			x = 1.0 / dim * numpy.ones_like(x)
		else:
			x = x / sum(x)
		network.set_probabilities(h, list(x))
		outcomes, probs = P(network, prediction_nodes, [])
		if plotting:
			xplotx.append(x[0])
			xploty.append(x[1])
			xplotz.append(x[2])
		if disp:
			print "Hyp", x, sum(x)
			print "Pred", probs[0]
			print "Obs", observations
		return KL(probs[0], observations)

	if method == 'Local Min' or method == 0:
		res = minimize(p_minimize, x0, args=(False, True), method = 'SLSQP', constraints=({'type':'eq','fun': lambda x: sum(x)-1}), bounds=bounds)
		xmin = numpy.asarray([xplotx[-1], xploty[-1], xplotz[-1]])

	elif method == 'Basinhopping' or method == 1:
		minimizer_kwargs = dict(method='SLSQP', constraints=({'type':'eq','fun': lambda x: sum(x)-1}), args=(False,True), bounds=bounds)
		res = basinhopping(p_minimize, x0, minimizer_kwargs=minimizer_kwargs, niter_success=10)
		xmin = numpy.asarray([xplotx[-1], xploty[-1], xplotz[-1]])

	elif Method == 'Brute' or Method == 2:
		ns = 10
		step = 1.0 / ns
		xdims = []
		for i in range(dim):
			xdims.append(numpy.arange(0, 1, step))
		X = itertools.product(*xdims)
		Px = numpy.zeros(Ns**dim)
		Dmin = 100
		xmin = []
		i = 0
		for x in X:
			if not x:
				xmin=x
			Px[i] = p_minimize(x, False, True)
			if Px[i] < Dmin:
				Dmin = Px[i]
				if sum(x) == 0:
					xmin = 1.0 / dim * numpy.ones_like(xmin)
				else:
					xmin = x / sum(x)
			i += 1

	fig = figure()
	ax = fig.add_subplot(111, projection='3d')
	if method != 'Brute' and method != 2:
		ax.plot(xplotx, xploty, xplotz,'-o')
	else:
		ax.scatter(xplotx, xploty, xplotz, c=Px, s=20)
	print xmin
	ax.scatter(xmin[0], xmin[1], xmin[2], c='k', marker='^', s=200)
	ax.set_xlim([0,1])
	ax.set_ylim([0,1])
	ax.set_zlim([0,1])
	return xmin, p_minimize(numpy.asarray(xmin), disp=False, plotting=False)


def belief_revision(network, hypothesis_nodes, prediction_nodes, observations, method='Local Min', searchgrid=5, full_output=False, plotting3d=False):
	dim = 0
	hyp_outcome_number = []
	for hyp in hypothesis_nodes:
		if network.get_node_parents(hyp) != []:
			raise ValueError(hyp + " is not a hypothesis node.")
		outcome_number = len(network.get_node_outcomes(hyp))
		dim += outcome_number
		hyp_outcome_number.append(outcome_number)

	for pred in prediction_nodes:
		if network.get_node_children(pred) != []:
			raise ValueError(pred + " is not a prediction node.")
	# TODO also check number of outcomes in predictions TODO #
	# TODO check sum of observations=1 TODO #
	ih = 0
	idim = 0
	x0 = numpy.ones(dim) / dim
	while True:
		node_dim = hyp_outcome_number[ih]
		x0[idim : (idim + node_dim)] = numpy.ones(node_dim) / node_dim
		ih += 1
		idim += node_dim
		if idim == dim:
			break
	bounds = tuple([(0,1) for i in range(dim)])
	xplotx=[]
	xploty=[]
	xplotz=[]
	def p_minimize(x, disp=False, plotting=True):
		if any( x < numpy.zeros_like(x)):
			return 100

		ih = 0
		idim = 0
		while True:
			node_dim = hyp_outcome_number[ih]
			x_node = x[idim : (idim + node_dim)]
			if disp:
				print "Node sum", ih, sum(x_node)
			if sum(x_node) == 0:
				x_node = 1.0 / node_dim * numpy.ones_like(x_node)
			else:
				x_node = x_node / sum(x_node)
			network.set_probabilities(hypothesis_nodes[ih], list(x_node))
			if ih==0:
				if plotting:
					xplotx.append(x_node[0])
					xploty.append(x_node[1])
					xplotz.append(x_node[2])
				if disp:
					print "Hyp", x_node, sum(x_node)
					print "Pred", Probs[0]
					print "Obs", Observations
			ih += 1
			idim += node_dim
			if idim == dim:
				break
		outcomes, probs = P(network, prediction_nodes, [])
		return KL(probs[0][0], observations)

	def constraints(x):
		ih = 0
		idim = 0
		totalsum = 0
		while True:
			node_dim = hyp_outcome_number[ih]
			x_node = x[idim : (idim + node_dim)]
			totalsum += sum(x_node)
			ih+=1
			idim += node_dim
			if idim == dim:
				break
		return totalsum - len(hyp_outcome_number)

	mult_constraints = ()
	ih = 0
	idim = 0
	mult_constraints = {'type': 'eq', 'fun': lambda x: constraints(x) }
	if method == 'Local Min' or method == 0:
		res = minimize(p_minimize, x0, args=(full_output, plotting3d), method='SLSQP', constraints=mult_constraints, bounds=bounds)
		xmin = res.x
		KLmin = res.fun

	elif method == 'Basinhopping' or method == 1:
		minimizer_kwargs = dict(method='SLSQP', constraints=mult_constraints, args=(full_output, plotting3d), bounds=bounds)
		res = basinhopping(p_minimize, x0, minimizer_kwargs=minimizer_kwargs, niter_success=10)
		xmin = res.x
		KLmin = res.fun

	elif method == 'Brute' or method == 2:
		ns = Searchgrid
		step = 1.0 / ns
		xdims = []
		for i in range(dim):
			xdims.append(numpy.arange(0, 1, step))
		X = itertools.product(*xdims)
		Px = numpy.zeros(Ns ** dim)
		Dmin = 100
		xmin = numpy.zeros(dim)
		i = 0
		for x in X:
			Px[i] = p_minimize(x, full_output, plotting3d)
			if Px[i] < Dmin:
				Dmin = Px[i]
				ih = 0
				idim = 0
				while True:
					node_dim = hyp_outcome_number[ih]
					if sum(x[idim : (idim + node_dim)]) == 0:
						xmin[idim : (idim + node_dim)] = 1.0/node_dim * numpy.ones(node_dim)
					else:
						xmin[idim : (idim + node_dim)]= x[idim : (idim + node_dim)]/sum(x[idim : (idim + node_dim)])
					ih+=1
					idim+=node_dim
					if idim == dim:
						break
			i += 1
		KLmin = Dmin

	ih = 0
	idim = 0
	while True:
		node_dim = hyp_outcome_number[ih]
		xmin[idim : (idim + node_dim)]= xmin[idim : (idim + node_dim)]/sum(xmin[idim : (idim + node_dim)])
		ih += 1
		idim += node_dim
		if idim == dim:
			break
	if plotting3d:
		fig = figure()
		ax = fig.add_subplot(111, projection='3d')
		if method != 'Brute' and method != 2 :
			ax.plot(xplotx, xploty, xplotz, '-o')
		else:
			ax.scatter(xplotx, xploty, xplotz, c=Px, s=20)
		ax.scatter(xmin[0], xmin[1], xmin[2], c='k', marker='^', s=200)
		ax.set_xlim([0,1])
		ax.set_ylim([0,1])
		ax.set_zlim([0,1])

	return xmin, KLmin

def model_revision(network, hypothesis_nodes, prediction_nodes, revision_nodes, observations, method='Local Min', searchgrid=5):
	for hyp in hypothesis_nodes:
		if network.get_node_parents(hyp) != []:
			raise ValueError(hyp + " is not a hypothesis node.")
	for pred in prediction_nodes:
		if network.get_node_children(pred) != []:
			raise ValueError(pred + " is not a prediction node.")
	# TODO also check number of outcomes in predictions TODO #
	# TODO check sum of observations=1 TODO #


	dim = 0
	rev_node_number = len(revision_nodes)
	parent_number = []
	parent_outcome_number = []
	rev_outcome_number = []
	for rev in revision_nodes:
		parents = network.get_node_parents(rev)
		parent_number.append(len(parents))
		parentoutcomes = 1
		for par in parents:
			parentoutcomes *= len(network.get_node_outcomes(par))
		parent_outcome_number.append(parentoutcomes)
		outcome_number = len(network.get_node_outcomes(rev))
		for ip in range(parentoutcomes):
			dim += outcome_number
			rev_outcome_number.append(outcome_number)
	print rev_node_number, parent_number, parent_outcome_number

	ih = 0
	idim = 0
	x0 = numpy.ones(dim) / dim
	while True:
		node_dim = rev_outcome_number[ih]
		x0[idim : (idim + node_dim)] = numpy.ones(node_dim)/node_dim
		ih += 1
		idim += node_dim
		if idim == dim:
			break
	bounds = tuple([(0,1) for i in range(dim)])
	xplotx=[]
	xploty=[]
	xplotz=[]
	def p_minimize(x, disp=False, plotting=True):
		if any(x<numpy.zeros_like(x)):
			return 100

		pn = 0
		po = 0
		ron = 0
		ir = 0
		ipo = 0
		iron = 0
		newp = parent_outcome_number[ipo] * rev_outcome_number[iron]
		newn = 1
		for ipn in range(parent_number[ir]):
			newn *= parent_outcome_number[ipn]
		idim = 0
		problist = []
		while True:
			pn = parent_number[ir]
			po = parent_outcome_number[ipo]
			ron = rev_outcome_number[iron]

			x_node = x[idim : (idim + ron)]
			if sum(x_node) == 0:
				x_node = 1.0 / ron * numpy.ones_like(x_node)
			else:
				x_node = x_node / sum(x_node)
			problist = problist + list(x_node)

			if iron == 0:
				if plotting:
					xplotx.append(x_node[0])
					xploty.append(x_node[1])
					xplotz.append(x_node[2])
				if disp:
					print "Hyp", x_node, sum(x_node)
					print "Pred", probs[0]
					print "Obs", observations
			idim += ron
			iron +=1
			if idim == newp:
				network.set_probabilities(revision_nodes[ir], problist)
				ipo +=1
				if idim == dim:
					break
				newp += parent_outcome_number[ipo] * rev_outcome_number[iron]
			if idim == newn:
				ir += 1
				newn = 1
				for ipn in range(parent_number[ir]):
					newn *= parent_outcome_number[ipn]
				newn += idim
			if idim == dim:
				break

		outcomes, probs = P(network,prediction_nodes, [])
		return KL(probs[0], observations)

	def constraints(x):
		ih = 0
		idim = 0
		totalsum = 0
		while True:
			node_dim = rev_outcome_number[ih]
			x_node = x[idim : (idim + node_dim)]
			totalsum += sum(x_node)
			ih+=1
			idim += node_dim
			if idim == dim:
				break
		return totalsum - len(rev_outcome_number)

	mult_constraints = ()
	ih = 0
	idim = 0
	mult_constraints = {'type':'eq', 'fun': lambda x: constraints(x)}
	if method=='Local Min' or method == 0:
		res = minimize(p_minimize, x0, args=(False, True), method='SLSQP', constraints=mult_constraints, bounds=bounds)
		xmin = res.x
		KLmin = res.fun

	elif method == 'Basinhopping' or method == 1:
		minimizer_kwargs = dict(method = 'SLSQP', constraints = mult_constraints, args=(False, True), bounds=bounds)
		res = basinhopping(p_minimize, x0, minimizer_kwargs=minimizer_kwargs, niter_success=10)
		xmin = res.x
		KLmin = res.fun

	elif method == 'Brute' or method == 2:
		ns = Searchgrid
		step = 1.0 / ns
		xdims = []
		for i in range(dim):
			xdims.append(numpy.arange(0, 1, step))
		X = itertools.product(*xdims)
		Px = numpy.zeros(ns ** dim)
		Dmin = 100
		xmin = numpy.zeros(dim)
		i = 0
		for x in X:
			Px[i] = p_minimize(x, False, True)
			if Px[i] < Dmin:
				Dmin = Px[i]
				ih = 0
				idim = 0
				while True:
					node_dim = rev_outcome_number[ih]
					if sum(x[idim : (idim + node_dim)]) == 0:
						xmin[idim : (idim + node_dim)] = 1.0 / node_dim * numpy.ones(node_dim)
					else:
						xmin[idim : (idim + node_dim)] = x[idim : (idim + node_dim)]/sum(x[idim : (idim + node_dim)])
					ih += 1
					idim += node_dim
					if idim == dim:
						break
			i+=1
		KLmin = Dmin

	fig = figure()
	ax = fig.add_subplot(111, projection='3d')
	if method != 'Brute' and method != 2:
		ax.plot(xplotx,xploty, xplotz,'-o')
	else:
		ax.scatter(xplotx,xploty,xplotz,c=Px, s=20)

	ih = 0
	idim = 0
	while True:
		node_dim = rev_outcome_number[ih]
		xmin[idim : (idim + node_dim)] = xmin[idim : (idim + node_dim)]/sum(xmin[idim : (idim + node_dim)])
		ih += 1
		idim+=node_dim
		if idim == dim:
			break

	ax.scatter(xmin[0], xmin[1], xmin[2], c='k', marker='^', s=200)
	ax.set_xlim([0,1])
	ax.set_ylim([0,1])
	ax.set_zlim([0,1])
	return xmin, KLmin



def add_observation(network, hypothesis_nodes, prediction_nodes, observable_nodes, pred_observations, full_output=False):
	dim = 0
	hyp_outcome_number = []
	for hyp in hypothesis_nodes:
		if network.get_node_parents(hyp) != []:
			raise ValueError(Hyp + " is not a hypothesis node.")
	for Pred in PredictionNodes:
		if network.get_node_children(pred) != []:
			raise ValueError(Pred + " is not a prediction node.")

	obs_outcomes = []
	for node in observable_nodes:
		outcomes = network.get_node_outcomes(node)
		obs_outcomes.append(outcomes)

	KL_list = []
	obs_list = []
	comb_list = []

	for i in range(len(observable_nodes)+1):
		X = itertools.combinations(observable_nodes, i)
		for x in X:
			outcomes, probs = P(network,prediction_nodes, list(x))
			for probs, outs in zip(probs, outcomes):
				KL_list.append(KL(probs,PredObservations))
				obs_list.append(x)
				comb_list.append(outs)

	if full_output:
		for kls, combs, obs in zip(KL_list, comb_list, obs_list):
			print obs, combs, kls

	m = KL_list.index(min(KL_list))
	return obslist[m], comb_list[m], KL_list[m]



def intervention(network, hypothesis_nodes, prediction_nodes, intervention_nodes, pred_observations, full_output=False):
	return add_observation(network, hypothesis_nodes, prediction_nodes, intervention_nodes, pred_observations, full_output)
