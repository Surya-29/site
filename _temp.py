import numpy as np

X1 = np.array([0, 0, 1, 1])

X2 = np.array([0, 1, 0, 1])

Y = np.array([0, 1, 1, 0])

np.random.seed(42)

# Weight Initialization

W11 = np.random.randn()

W21 = np.random.randn()

B1 = np.random.randn()

W12 = np.random.randn()

W22 = np.random.randn()

B2 = np.random.randn()

W1_out = np.random.randn()

W2_out = np.random.randn()

B_out = np.random.randn()

learning_rate = 0.5

def sigmoid(x):

    return 1 / (1 + np.exp(-x))

def forward_propagation(X1, X2):





    H1_input = (X1 * W11) + (X2 * W21) + B1

    H1_output = sigmoid(H1_input)

    H2_input = (X1 * W12) + (X2 * W22) + B2

    H2_output = sigmoid(H2_input)

    Y_pred_input = (H1_output * W1_out) + (H2_output * W2_out) + B_out

    Y_pred = sigmoid(Y_pred_input)

    return Y_pred, H1_output, H2_output

def error_func(Y, Y_pred):

    return (1/2) * np.sum((Y - Y_pred) ** 2)

def back_propagation(X1, X2, Y_pred, Y, H1_output, H2_output):

    global W11, W21, B1, W12, W22, B2, W1_out, W2_out, B_out

    dY_pred = (Y_pred - Y) * Y_pred * (1 - Y_pred)

    dW1_out = np.sum(H1_output * dY_pred)

    dW2_out = np.sum(H2_output * dY_pred)

    dB_out = np.sum(dY_pred)

    dH2_output = dY_pred * W2_out

    dH2_input = dH2_output * H2_output * (1 - H2_output)

    dW12 = np.sum(X1 * dH2_input)

    dW22 = np.sum(X2 * dH2_input)

    dB2 = np.sum(dH2_input)

    dH1_output = dY_pred * W1_out

    dH1_input = dH1_output * H1_output * (1 - H1_output)

    dW11 = np.sum(X1 * dH1_input)

    dW21 = np.sum(X2 * dH1_input)

    dB1 = np.sum(dH1_input)

    W11 -= learning_rate * dW11

    W21 -= learning_rate * dW21

    B1 -= learning_rate * dB1

    W12 -= learning_rate * dW12

    W22 -= learning_rate * dW22

    B2 -= learning_rate * dB2

    W1_out -= learning_rate * dW1_out





    W2_out -= learning_rate * dW2_out

    B_out -= learning_rate * dB_out

for epoch in range(2000):

    Y_pred, H1_output, H2_output = forward_propagation(X1, X2)

    if np.all(np.round(Y_pred) == Y):

        print("Weights are:\n")

        print("Hidden Layer 1: W11 =", W11, " W21 =", W21, " B1 =", B1)

        print("Hidden Layer 2: W12 =", W12, " W22 =", W22, " B2 =", B2)

        print("Output Layer: W1_out =", W1_out, " W2_out =", W2_out, " B_out =", B_out)

