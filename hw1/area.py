import numpy as np

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

    def tanh(self, Z):
        return np.tanh(Z)

    def tanh_derivative(self, Z):
        return 1 - np.tanh(Z)**2

    def relu(self, Z):
        return np.maximum(0, Z)

    def relu_derivative(self, Z):
        Z[Z<=0] = 0
        Z[Z>0] = 1
        return Z

    def leaky_relu(self, x, alpha=0.01):
        return np.maximum(alpha * x, x)

    def leaky_relu_derivative(self, x, alpha=0.01):
        dx = np.ones_like(x)
        dx[x <= 0] = alpha
        return dx

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
            layer1_out, layer2_out = self.forward_propagation(train_in)

            layer2_error = train_sol - layer2_out
            layer2_delta = layer2_error * self.sigmoid_derivative(layer2_out)

            layer1_error = layer2_delta.dot(self.layer2.weights.T)
            layer1_delta = layer1_error * self.sigmoid_derivative(layer1_out)

            self.layer2.weights += learning_rate * layer1_out.T.dot(layer2_delta)
            self.layer2.bias    += learning_rate * np.sum(layer2_delta, axis=0, keepdims=True)
            self.layer1.weights += learning_rate * train_in.T.dot(layer1_delta)
            self.layer1.bias    += learning_rate * np.sum(layer1_delta, axis=0, keepdims=True)

            _, layer2_out = self.forward_propagation(train_in)
            temp = self.mean_squared_error(train_sol, layer2_out)
            if temp > mse:
                break
            else:
                mse = temp
        print(i)

def get_dataset(m, scale=.1):
    base = np.random.uniform(low=1, high=10, size=(m, 1))
    height = np.random.uniform(low=1, high=10, size=(m, 1))
    y = 0.5 * base * height * scale
    X = np.concatenate((base, height), axis=1)
    y *= scale
    X *= scale
    return X, y

if __name__ == '__main__':
    # dataset
    train_in, train_sol = get_dataset(50)

    layer1 = NeuronLayer(4, 2)
    layer2 = NeuronLayer(1, 4)
    #
    nn = NeuralNetwork(layer1, layer2)

    nn.train(train_in, train_sol)

    test_in, test_sol = get_dataset(3)

    _, train_out = nn.forward_propagation(train_in)
    _, test_out = nn.forward_propagation(test_in)

    print(nn.mean_squared_error(train_out, train_sol))
    print(nn.mean_squared_error(test_out, test_sol))

    print('\n MSE for training data: ', nn.mean_squared_error(train_out, train_sol))
    print('\n MSE for testing data : ', nn.mean_squared_error(test_out, test_sol))
    print('\nThe final prediction is \n', test_out)
