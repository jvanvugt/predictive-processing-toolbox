# from ctypes import *
import numpy
from scipy.optimize import minimize, minimize_scalar, brute, basinhopping
from matplotlib.pyplot import plot, xlim, ylim, scatter, figure
from mpl_toolkits.mplot3d import Axes3D
import itertools


# PCTi=CDLL("/home/marvin/Coding/StudentAssistantship/bridepythonC/Predictive Coding Toolbox/LibPCTInference.so")
from lib_pct_inference import *
from lib_pct_read_network import *
from lib_pct_build_network import *
from lib_pct_tools import *

DefaultNetworkName="TestNetwork";


def BeliefRevision1(NetworkName=DefaultNetworkName,HypothesisNodes=["Node"], PredictionNodes=["Node"], Observations=[0.5,0.5], Method = 'Local Min'):
	if len(HypothesisNodes)>1: print "Only one Hypothesis Node."; return 0
	for Hyp in HypothesisNodes:
		if GetParents(NetworkName, Hyp)!=[]:
			print Hyp, " is not a hypothesis node."
			return 0
	H = HypothesisNodes[0];
	for Pred in PredictionNodes:
		if GetChildren(NetworkName, Pred)!=[]:
			print Pred, " is not a prediction node."
			return 0
	HOutcomes = GetOutcomes(NetworkName,H);
	dim = len(HOutcomes);
	x0 = numpy.ones(dim)/dim;
	bounds = tuple([(0,1) for i in range(dim)]);
	xplotx=[]; xploty=[]; xplotz=[];
	def Pminimize(x, disp=False, plotting=True):
		if any(x<numpy.zeros_like(x)): return 100;
		if sum(x) == 0: 
			x = 1.0/dim * numpy.ones_like(x);
		else:
			x = x/sum(x);
		SetProbabilities(NetworkName, H, list(x));
		Outcomes, Probs = P(NetworkName=NetworkName,TargetNodes=PredictionNodes, EvidenceNodes=[]);
		if plotting: xplotx.append(x[0]); xploty.append(x[1]); xplotz.append(x[2]);
		if disp: print "Hyp", x, sum(x); print "Pred", Probs[0]; print "Obs", Observations
		return KL(Probs[0], Observations)
	
	if Method=='Local Min' or Method == 0:
		res = minimize(Pminimize, x0, args=(False,True), method = 'SLSQP', constraints = ({'type':'eq','fun': lambda x: sum(x)-1}), bounds = bounds)
		xmin = numpy.asarray([xplotx[-1],xploty[-1],xplotz[-1]]);

	elif Method == 'Basinhopping' or Method == 1:
		minimizer_kwargs = dict(method = 'SLSQP', constraints = ({'type':'eq','fun': lambda x: sum(x)-1}), args=(False,True), bounds = bounds)
		res = basinhopping(Pminimize, x0, minimizer_kwargs=minimizer_kwargs, niter_success=10);
		xmin = numpy.asarray([xplotx[-1],xploty[-1],xplotz[-1]]);

	elif Method == 'Brute' or Method == 2:
		Ns = 10; step = 1.0/Ns; xdims = [];
		for i in range(dim): xdims.append(numpy.arange(0, 1, step));
		X = itertools.product(*xdims);
		Px = numpy.zeros(Ns**dim);
		Dmin = 100; xmin = []; i = 0;
		for x in X:
			if not(x): xmin=x;
			Px[i] = Pminimize(x, False, True);
			if Px[i] < Dmin:
				Dmin = Px[i];
				if sum(x) == 0: xmin = 1.0/dim * numpy.ones_like(xmin); 
				else: xmin = x/sum(x);
			i+=1;
	
	fig = figure()
	ax = fig.add_subplot(111, projection='3d')
	if Method != 'Brute' and Method != 2 :
		ax.plot(xplotx,xploty, xplotz,'-o')
	else:
		ax.scatter(xplotx,xploty,xplotz,c=Px, s=20)
	print xmin
	ax.scatter(xmin[0],xmin[1],xmin[2],c='k', marker='^', s=200)
	ax.set_xlim([0,1]);ax.set_ylim([0,1]); ax.set_zlim([0,1]);
	return xmin, Pminimize(numpy.asarray(xmin), disp=False, plotting=False)


def BeliefRevision(NetworkName=DefaultNetworkName,HypothesisNodes=["Node"], PredictionNodes=["Node"], Observations=[0.5,0.5], Method = 'Local Min', Searchgrid = 5, FullOutput = False, Ploting3D = False):
	dim = 0; HypOutcomeNumber = [];
	for Hyp in HypothesisNodes:
		if GetParents(NetworkName, Hyp)!=[]:
			print Hyp, " is not a hypothesis node."
			return 0
		OutcomeNumber = len(GetOutcomes(NetworkName,Hyp));
		dim += OutcomeNumber;
		HypOutcomeNumber.append(OutcomeNumber);
	
	for Pred in PredictionNodes:
		if GetChildren(NetworkName, Pred)!=[]:
			print Pred, " is not a prediction node."
			return 0
	# TODO also check number of outcomes in predictions TODO #
	# TODO check sum of observations=1 TODO #

	ih = 0; idim = 0;
	x0 = numpy.ones(dim)/dim;
	while True:
		node_dim = HypOutcomeNumber[ih];
		x0[idim : (idim + node_dim)] = numpy.ones(node_dim)/node_dim;
		ih+=1; idim+=node_dim;
		if idim == dim: break;
	bounds = tuple([(0,1) for i in range(dim)]);
	xplotx=[]; xploty=[]; xplotz=[];
	def Pminimize(x, disp=False, plotting=True):
		if any(x<numpy.zeros_like(x)): return 100;
		
		ih = 0; idim = 0;
		while True:
			node_dim = HypOutcomeNumber[ih];
			x_node = x[idim : (idim + node_dim)];
			if disp: print "Node sum", ih, sum(x_node)
			if sum(x_node) == 0: 
				x_node = 1.0/node_dim * numpy.ones_like(x_node);
			else:
				x_node = x_node/sum(x_node);
			SetProbabilities(NetworkName, HypothesisNodes[ih], list(x_node));
			if ih==0:
				if plotting: xplotx.append(x_node[0]); xploty.append(x_node[1]); xplotz.append(x_node[2]);
				if disp: print "Hyp", x_node, sum(x_node); print "Pred", Probs[0]; print "Obs", Observations
			ih+=1; idim+=node_dim;
			if idim == dim: break;
			
		Outcomes, Probs = P(NetworkName=NetworkName,TargetNodes=PredictionNodes, EvidenceNodes=[]);
		return KL(Probs[0], Observations)

	def constraints(x):
		ih = 0; idim = 0;
		totalsum = 0;
		while True:
			node_dim = HypOutcomeNumber[ih];
			x_node = x[idim : (idim + node_dim)];
			totalsum += sum(x_node);
			ih+=1; idim+=node_dim;
			if idim == dim: break;
		return totalsum - len(HypOutcomeNumber)
	
	mult_constraints = ();
	ih = 0; idim = 0;
	mult_constraints = {'type':'eq','fun': lambda x: constraints(x) } 
	if Method=='Local Min' or Method == 0:
		res = minimize(Pminimize, x0, args=(FullOutput, Ploting3D), method = 'SLSQP', constraints = mult_constraints, bounds = bounds)
		xmin = res.x;
		KLmin = res.fun;
		#print numpy.asarray([xplotx[-1],xploty[-1],xplotz[-1]]);

	elif Method == 'Basinhopping' or Method == 1:
		minimizer_kwargs = dict(method = 'SLSQP', constraints = mult_constraints, args=(FullOutput, Ploting3D), bounds = bounds)
		res = basinhopping(Pminimize, x0, minimizer_kwargs=minimizer_kwargs, niter_success=10);
		xmin = res.x;
		KLmin = res.fun;
		#print numpy.asarray([xplotx[-1],xploty[-1],xplotz[-1]]);

	elif Method == 'Brute' or Method == 2:
		Ns = Searchgrid; step = 1.0/Ns; xdims = [];
		for i in range(dim): xdims.append(numpy.arange(0, 1, step));
		X = itertools.product(*xdims);
		Px = numpy.zeros(Ns**dim);
		Dmin = 100; xmin = numpy.zeros(dim); i = 0;
		for x in X:
			# if not(x): xmin=numpy.asarray(x);
			Px[i] = Pminimize(x, FullOutput, Ploting3D);
			if Px[i] < Dmin:
				Dmin = Px[i];
				ih = 0; idim = 0;
				while True:			
					node_dim = HypOutcomeNumber[ih];
					#x_node = x[idim : (idim + node_dim)];
					if sum(x[idim : (idim + node_dim)]) == 0: 
						xmin[idim : (idim + node_dim)] = 1.0/node_dim * numpy.ones(node_dim);
					else:
						xmin[idim : (idim + node_dim)]= x[idim : (idim + node_dim)]/sum(x[idim : (idim + node_dim)]);
					ih+=1; idim+=node_dim;
					if idim == dim: break;
				#if sum(x) == 0: xmin = 1.0/dim * numpy.ones_like(xmin); 
				#else: xmin = x/sum(x);
			i+=1;
		KLmin = Dmin;
	
		
	ih = 0; idim = 0;
	while True:
		node_dim = HypOutcomeNumber[ih];
		xmin[idim : (idim + node_dim)]= xmin[idim : (idim + node_dim)]/sum(xmin[idim : (idim + node_dim)]);
		ih+=1; idim+=node_dim;
		if idim == dim: break;
	
	if Ploting3D:
		fig = figure()
		ax = fig.add_subplot(111, projection='3d')
		if Method != 'Brute' and Method != 2 :
			ax.plot(xplotx,xploty, xplotz,'-o') 
		else:
			ax.scatter(xplotx,xploty,xplotz,c=Px, s=20)
		ax.scatter(xmin[0],xmin[1],xmin[2],c='k', marker='^', s=200)
		ax.set_xlim([0,1]);ax.set_ylim([0,1]); ax.set_zlim([0,1]);
	
	return xmin, KLmin

def ModelRevision(NetworkName=DefaultNetworkName,HypothesisNodes=["Node"], PredictionNodes=["Node"], RevisionNodes=["Node"], Observations=[0.5,0.5], Method = 'Local Min', Searchgrid = 5):
	for Hyp in HypothesisNodes:
		if GetParents(NetworkName, Hyp)!=[]:
			print Hyp, " is not a hypothesis node."
			return 0
	for Pred in PredictionNodes:
		if GetChildren(NetworkName, Pred)!=[]:
			print Pred, " is not a prediction node."
			return 0
	# TODO also check number of outcomes in predictions TODO #
	# TODO check sum of observations=1 TODO #
	

	dim = 0;
	RevNodeNumber = len(RevisionNodes);
	ParentNumber = [];
	ParentOutcomeNumber = [];
	RevOutcomeNumber = [];
	for Rev in RevisionNodes:
		Parents=GetParents(NetworkName,Rev);
		ParentNumber.append(len(Parents));
		parentoutcomes = 1;
		for Par in Parents:
			parentoutcomes *= len(GetOutcomes(NetworkName,Par));
		ParentOutcomeNumber.append(parentoutcomes);
		OutcomeNumber = len(GetOutcomes(NetworkName,Rev));
		for ip in range(parentoutcomes):
			dim += OutcomeNumber;
			RevOutcomeNumber.append(OutcomeNumber);
	print RevNodeNumber, ParentNumber, ParentOutcomeNumber
	
	
	#for Rev in RevisionNodes:
		#Parents=GetParents(NetworkName,Rev);
		#ParentOutcomes=1;
		#for Par in Parents:
			#ParentOutcomes *= len(GetOutcomes(NetworkName,Par));
		#ParOutcomeNumber.append(ParentOutcomes);
		#OutcomeNumber = len(GetOutcomes(NetworkName,Rev));
		#for ip in range(ParentOutcomes):
			#dim += OutcomeNumber;
			#HypOutcomeNumber.append(OutcomeNumber);
	#print ParOutcomeNumber, HypOutcomeNumber

	ih = 0; idim = 0;
	x0 = numpy.ones(dim)/dim;
	while True:
		node_dim = RevOutcomeNumber[ih];
		x0[idim : (idim + node_dim)] = numpy.ones(node_dim)/node_dim;
		ih+=1; idim+=node_dim;
		if idim == dim: break;
	bounds = tuple([(0,1) for i in range(dim)]);
	xplotx=[]; xploty=[]; xplotz=[];
	def Pminimize(x, disp=False, plotting=True):
		if any(x<numpy.zeros_like(x)): return 100;
		
		pn = 0; po = 0; ron = 0; ir = 0; ipo = 0; iron = 0;
		newp = ParentOutcomeNumber[ipo] * RevOutcomeNumber[iron];
		newn = 1; 
		for ipn in range(ParentNumber[ir]): newn *= ParentOutcomeNumber[ipn];
		idim = 0; problist = [];
		while True:
			pn = ParentNumber[ir];
			po = ParentOutcomeNumber[ipo];
			ron = RevOutcomeNumber[iron];
			
			x_node = x[idim : (idim + ron)];
			if sum(x_node) == 0: 
				x_node = 1.0/ron * numpy.ones_like(x_node);
			else:
				x_node = x_node/sum(x_node);
			problist = problist + list(x_node);

			if iron==0:
				if plotting: xplotx.append(x_node[0]); xploty.append(x_node[1]); xplotz.append(x_node[2]);
				if disp: print "Hyp", x_node, sum(x_node); print "Pred", Probs[0]; print "Obs", Observations
			idim += ron;
			iron +=1;
			if idim == newp:
				# print "SetProb:", RevisionNodes[ih], problist
				SetProbabilities(NetworkName, RevisionNodes[ir], problist);
				ipo +=1;
				if idim == dim: break;
				newp += ParentOutcomeNumber[ipo] * RevOutcomeNumber[iron];
			if idim == newn:
				ir+=1;
				newn = 1; 
				for ipn in range(ParentNumber[ir]): newn *= ParentOutcomeNumber[ipn];
				newn += idim;
			if idim == dim: break;

		
		
		#ih = 0; idim = 0; ipar = 0; problist = []; ip = 0; next_par = 1;
		#while True:
			#node_dim = HypOutcomeNumber[ih];
			##if ip==0: next_par += ParOutcomeNumber[ip]*HypOutcomeNumber[ih];
			#x_node = x[idim : (idim + node_dim)];
			#if disp: print "Node sum", ih, sum(x_node)
			#if sum(x_node) == 0: 
				#x_node = 1.0/node_dim * numpy.ones_like(x_node);
			#else:
				#x_node = x_node/sum(x_node);
			#ipar += node_dim;
			#problist = problist + list(x_node);
			## print ip, ipar, next_par, problist, dim;
			#if ipar == next_par:
				#print "SetProb:", RevisionNodes[ih], problist
				#SetProbabilities(NetworkName, RevisionNodes[ih], problist);
				#problist = [];
				#if ip < len(ParOutcomeNumber)-1:
					#ip+=1;
					#next_par += ParOutcomeNumber[ip];
			#if ih==0:
				#if plotting: xplotx.append(x_node[0]); xploty.append(x_node[1]); xplotz.append(x_node[2]);
				#if disp: print "Hyp", x_node, sum(x_node); print "Pred", Probs[0]; print "Obs", Observations
			#ih+=1; idim+=node_dim;
			#if idim == dim: break;
			
		Outcomes, Probs = P(NetworkName=NetworkName,TargetNodes=PredictionNodes, EvidenceNodes=[]);
		return KL(Probs[0], Observations)

	def constraints(x):
		ih = 0; idim = 0;
		totalsum = 0;
		while True:
			node_dim = RevOutcomeNumber[ih];
			x_node = x[idim : (idim + node_dim)];
			totalsum += sum(x_node);
			ih+=1; idim+=node_dim;
			if idim == dim: break;
		return totalsum - len(RevOutcomeNumber)
	
	mult_constraints = ();
	ih = 0; idim = 0;
	mult_constraints = {'type':'eq','fun': lambda x: constraints(x) } 
	if Method=='Local Min' or Method == 0:
		res = minimize(Pminimize, x0, args=(False,True), method = 'SLSQP', constraints = mult_constraints, bounds = bounds)
		xmin = res.x;
		KLmin = res.fun;
		#print numpy.asarray([xplotx[-1],xploty[-1],xplotz[-1]]);

	elif Method == 'Basinhopping' or Method == 1:
		minimizer_kwargs = dict(method = 'SLSQP', constraints = mult_constraints, args=(False,True), bounds = bounds)
		res = basinhopping(Pminimize, x0, minimizer_kwargs=minimizer_kwargs, niter_success=10);
		xmin = res.x;
		KLmin = res.fun;
		#print numpy.asarray([xplotx[-1],xploty[-1],xplotz[-1]]);

	elif Method == 'Brute' or Method == 2:
		Ns = Searchgrid; step = 1.0/Ns; xdims = [];
		for i in range(dim): xdims.append(numpy.arange(0, 1, step));
		X = itertools.product(*xdims);
		Px = numpy.zeros(Ns**dim);
		Dmin = 100; xmin = numpy.zeros(dim); i = 0;
		for x in X:
			# if not(x): xmin=numpy.asarray(x);
			Px[i] = Pminimize(x, False, True);
			if Px[i] < Dmin:
				Dmin = Px[i];
				ih = 0; idim = 0;
				while True:			
					node_dim = RevOutcomeNumber[ih];
					#x_node = x[idim : (idim + node_dim)];
					if sum(x[idim : (idim + node_dim)]) == 0: 
						xmin[idim : (idim + node_dim)] = 1.0/node_dim * numpy.ones(node_dim);
					else:
						xmin[idim : (idim + node_dim)]= x[idim : (idim + node_dim)]/sum(x[idim : (idim + node_dim)]);
					ih+=1; idim+=node_dim;
					if idim == dim: break;
				#if sum(x) == 0: xmin = 1.0/dim * numpy.ones_like(xmin); 
				#else: xmin = x/sum(x);
			i+=1;
		KLmin = Dmin;
	
	fig = figure()
	ax = fig.add_subplot(111, projection='3d')
	if Method != 'Brute' and Method != 2 :
		ax.plot(xplotx,xploty, xplotz,'-o') 
	else:
		ax.scatter(xplotx,xploty,xplotz,c=Px, s=20)
	
	ih = 0; idim = 0;
	while True:
		node_dim = RevOutcomeNumber[ih];
		xmin[idim : (idim + node_dim)]= xmin[idim : (idim + node_dim)]/sum(xmin[idim : (idim + node_dim)]);
		ih+=1; idim+=node_dim;
		if idim == dim: break;
	
	ax.scatter(xmin[0],xmin[1],xmin[2],c='k', marker='^', s=200)
	ax.set_xlim([0,1]);ax.set_ylim([0,1]); ax.set_zlim([0,1]);
	return xmin, KLmin



def AddObservation(NetworkName=DefaultNetworkName,HypothesisNodes=["Node"], PredictionNodes=["Node"], ObservableNodes=["Node"], PredObservations=[0.5,0.5], FullOutput = False):
	dim = 0;
	HypOutcomeNumber = [];
	for Hyp in HypothesisNodes:
		if GetParents(NetworkName, Hyp)!=[]:
			print Hyp, " is not a hypothesis node."
			return 0
	for Pred in PredictionNodes:
		if GetChildren(NetworkName, Pred)!=[]:
			print Pred, " is not a prediction node."
			return 0
	
	ObsOutcomes=[];
	for ON in ObservableNodes:
		Outcomes = GetOutcomes(NetworkName,ON);
		ObsOutcomes.append(Outcomes);

	KLlist = [];
	Obslist = [];
	Comblist = [];
	
	for i in range(len(ObservableNodes)+1):
		X = itertools.combinations(ObservableNodes,i)
		for x in X:
			Outcomes, Probs = P(NetworkName=NetworkName,TargetNodes=PredictionNodes, EvidenceNodes=list(x));
			for probs,outs in zip(Probs,Outcomes):
				KLlist.append(KL(probs,PredObservations));
				Obslist.append(x);
				Comblist.append(outs);
			
	if FullOutput:
		for kls, combs, obs in zip(KLlist, Comblist, Obslist):
			print obs, combs, kls
	
	m = KLlist.index(min(KLlist));
	return Obslist[m], Comblist[m], KLlist[m]



def Intervention(NetworkName=DefaultNetworkName,HypothesisNodes=["Node"], PredictionNodes=["Node"], InterventionNodes=["Node"], PredObservations=[0.5,0.5], FullOutput = False):
	return AddObservation(NetworkName=NetworkName,HypothesisNodes=HypothesisNodes, PredictionNodes=PredictionNodes, ObservableNodes=InterventionNodes, PredObservations=PredObservations, FullOutput = FullOutput)




