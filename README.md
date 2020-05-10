# DEV​PSU - SP2020

## Artificial Neural Network Script

The first step to creating some complex Artificial Intelligence programs is to first understand how to program a basic Artificial Neural Network (ANN)! ANN’s are brain-inspired systems which replicate the way in which humans learn. They do this by using a series of layers and functions that help the program get to the final predicted answer. For this project we will be using James Loy’s example of an ANN and predict the outcome of an AND logic gate.

## Installation

First make sure you have installed Python 3 or higher.
You will also need a text editor (ex. Sublime Text) or you can use the python shell. Download the boiler code (NeuralNetwork.py)


## Instructions

First, we must import our numpy library as np, so that we can use Numpy for calculations later in the program.
We now need to define our activation function that will be used to predict our output. 

In the sigmoid(x) ​function, you should return 1.0 / (1+ np.exp(-x)). Remember that np is just an alias -x​ for numpy, so np.exp(-x) is essentially just e​.

Our ​sigmoid_derivative ​function will be used to fix our predicted output to become more accurate. We will simply return the derivative of ​sigmoid(x)​ (x*(1.0-x))

We will now create our actual ​NeuralNetwork ​(class/object)

First, we must initialize some data in the ​__init__(self, x, y)​ constructor of the class: our input (x), our randomized weights, the expected output (y)

Time to see if our ANN will predict the correct output for an AND gate. Here’s a table that shows outputs given two inputs:

The variable y will be our expected outputs for the AND gate which are 0, 0, 0, and 1. You will HAVE​ to fill these in.

## Final Steps

Next, we will create a Neural Network (the class we just created) and run it for 1000 iterations. Finally, we print our final result! (this is done for you)

Your printed output should be close to the actual output of 0, 0, 0, 1, but it might not be ​exactly correct​.

Congratulations, you completed your first project and wrote a Neural Network that can predict the outputs of an AND gate!

## Additional Steps

1. See what happens when you increase the number of trials from 1000

2. Try using the same Network but for an OR gate and NAND gate

3. Try using the same Network for some custom state machine

