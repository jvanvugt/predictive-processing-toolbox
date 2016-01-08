# Predictive Processing Toolbox

Toolbox for predictive coding in python. Makes use of the [SMILE](https://dslpitt.org/genie/) library.

## Getting Started
Clone the repo:
```
$ git clone https://github.com/jvanvugt/predictive-processing-toolbox.git
```

Compile the C++ code
```
$ cd predictive-processing-toolbox/src
$ make
```

Now you can run the example
```
$ python example.py
```

Creating and manipulating a network is very easy:
```python
from pct_network import PCTNetwork

# Create a new network
net = PCTNetwork()

# Add nodes to the network
net.add_node('Fire', probabilities=[0.01, 0.99])
net.add_node('Tampering', probabilities=[0.02, 0.98])
net.add_node('Smoke')
net.add_node('Alarm')
net.add_node('Leaving')
net.add_node('Report')

# Add arcs between nodes
net.add_arc('Fire', 'Smoke')
net.add_arc('Tampering', 'Alarm')
net.add_arc('Fire', 'Alarm')
net.add_arc('Alarm', 'Leaving')
net.add_arc('Leaving', 'Report')

# Set the probabilities for some nodes
net.set_probabilities('Smoke', [0.9, 0.1, 0.01, 0.99])
net.set_probabilities('Alarm', [0.5,0.5,0.85,0.15,0.99,0.01,0.0001,0.9999])
net.set_probabilities('Leaving', [0.88, 0.12, 0.001, 0.999])
net.set_probabilities('Report', [0.75, 0.25, 0.01, 0.99])

print net.get_nodes()
# -> ['Fire', 'Tampering', 'Smoke', 'Alarm', 'Leaving', 'Report']

# Save the network to a file
net.write_to_file('Alarm')

```

## State of the Code
Most code was originally written by Marvin Uhlmann (Max Planck Institute).
I have made the code a lot faster and more according to Python styling conventions.
I haven't had the chance to test all code, so there might still be some minor typos.

The `model_revision` function is not done yet.
