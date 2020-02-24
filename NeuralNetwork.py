# DevPSU Project 1
# Artificial Neural Network
# NeuralNetwork.py

# Author: Shashwat Shekhar
# Date: February 23, 2020

# Import numpy library as np here
import numpy as np


# Functions used for Propagation
def sigmoid(x):
    # function goes here
    return (1.0 / (1+ np.exp(-x))) 
    
    

def sigmoid_derivative(x):
    # function goes here
    return (sigmoid(x))*((x*(1.0-x)))
    


# Here is the logic of the Neural Network
class NeuralNetwork:
    def __init__(self, x, y):
        # Input, weights1, weights2, y, output go here
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1],4)
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np.zeros(self.y.shape)
    	

    def feedforward(self):
    	self.layer1 = sigmoid(np.dot(self.input, self.weights1))  # Calculates hidden layer 1
    	self.output = sigmoid(np.dot(self.layer1, self.weights2)) # Calculates hidden layer 2
    	
    def backprop(self):
        # Application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # Update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


# Test Cases
if __name__ == "__main__":
    X = np.array([[0,0],
                  [0,1],
                  [1,0],
                  [1,1]])

    y = np.array([[0],[0],[0],[1]])

    nn = NeuralNetwork(X,y)

    for i in range(1000):
        nn.feedforward()
        nn.backprop()

    print(nn.output)
    print("\n")