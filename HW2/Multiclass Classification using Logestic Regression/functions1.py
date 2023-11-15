#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt  # Import matplotlib for plotting

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_loss(y, h):
    return -np.mean(y * np.log(h) + (1 - y) * np.log(1 - h))

def logistic_regression(X, y, iterations, learning_rate):
    m, n = X.shape
    weights = np.zeros(n)
    bias = 1
    cost_history = []  # List to store cost at each iteration

    for _ in range(iterations):
        z = np.dot(X, weights) + bias
        h = sigmoid(z)
        gradient_weights = np.dot(X.T, (h - y)) / m
        gradient_bias = np.mean(h - y)
        weights -= learning_rate * gradient_weights
        bias -= learning_rate * gradient_bias

        # Calculate and store the cost at each iteration
        cost = logistic_loss(y, h)
        cost_history.append(cost)

    return weights, bias, cost_history

def predict(X, weights, bias):
    z = np.dot(X, weights) + bias
    return sigmoid(z) >= 0.5

def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

# Add any additional required functions here
