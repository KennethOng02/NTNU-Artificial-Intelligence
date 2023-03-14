import pandas as pd
import numpy as np

# Input Layer          Hidden Layer         Output Layer
# (10 neurons)          (1 neuron)           (1 neuron)
#
#   X1   __                __              __
#       /  \              /  \            /  \
#   X2-| N1 |---- w1 ----| N2 |--- w2 ---| N3 |---- Output
#       \__/              \__/            \__/
#   X3                  Bias              Bias

class NeuronLayer():
    def __init__(self, number_of_neurons, inputs_per_neuron):
        self.weights = np.random.rand(inputs_per_neuron, number_of_neurons)
        self.bias    = np.random.rand(1, number_of_neurons)

class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    def sigmoid(self, Z):
        return 1/(1 + np.exp(-Z)) #sigmoid
 
    def sigmoid_derivative(self, Z):
        return Z*(1-Z) #sigmoid

    def mean_squared_error(self, train_out, train_sol):
        return np.mean((train_out-train_sol)**2)

    def forward_propagation(self, Z):
        layer1_out = self.sigmoid(np.dot(Z, self.layer1.weights) + self.layer1.bias)
        layer2_out = self.sigmoid(np.dot(layer1_out, self.layer2.weights) + self.layer2.bias)
        return layer1_out, layer2_out

    def train(self, train_in, train_sol):
        learning_rate = .1
        mse = np.iinfo(np.int32(10)).max
        for i in range(100000):
            print("\n i = ", i, "nn_weight=")
            print(self.layer1.weights)
            print(self.layer2.weights)

            layer1_out, layer2_out = self.forward_propagation(train_in)

            print("train_out = ")
            print(layer2_out)

            layer2_error = train_sol - layer2_out
            layer2_delta = layer2_error * self.sigmoid_derivative(layer2_out)

            layer1_error = layer2_delta.dot(self.layer2.weights.T)
            layer1_delta = layer1_error * self.sigmoid_derivative(layer1_out)

            self.layer2.weights += learning_rate * layer1_out.T.dot(layer2_delta)
            self.layer2.bias    += learning_rate * np.sum(layer2_delta, axis=0, keepdims=True)
            self.layer1.weights += learning_rate * train_in.T.dot(layer1_delta)
            self.layer1.bias    += learning_rate * np.sum(layer1_delta, axis=0, keepdims=True)

if __name__ == '__main__':
    # dataset
    df = pd.read_csv('result.csv', encoding='utf-8')
    data = df.iloc[:]
    data_in = data.drop(columns='總成績').to_numpy()
    data_out = data['總成績'].to_numpy() 
    data_out = np.reshape(data_out, (data_out.size, 1))

    sep = 3
    scale = .01

    train_in = data_in[sep:] * scale
    train_sol = data_out[sep:] * scale

    test_in = data_in[:sep] * scale
    test_sol = data_out[:sep] * scale

    np.random.seed(1)

    layer1 = NeuronLayer(2, 10)
    layer2 = NeuronLayer(1, 2)

    nn = NeuralNetwork(layer1, layer2)

    nn.train(train_in, train_sol)

    _, train_out = nn.forward_propagation(train_in)
    _, test_out = nn.forward_propagation(test_in)

    train_out /= scale
    test_out /= scale

    print('\n MSE for training data: ', nn.mean_squared_error(train_out, train_sol/scale))
    print('\n MSE for testing data : ', nn.mean_squared_error(test_out, test_sol/scale))
    print('\nThe final prediction is \n', test_out)
