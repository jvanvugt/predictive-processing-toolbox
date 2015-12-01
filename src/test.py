from pct_network import PCTNetwork

net = PCTNetwork()
net.load_from_file("Alarm")
print net.get_nodes()