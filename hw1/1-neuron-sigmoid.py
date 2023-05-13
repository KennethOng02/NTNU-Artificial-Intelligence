import pandas as pd
import numpy as np

class NeuralNetwork:
    def __init__(self, input_no, output_no):
        self.input_no = input_no
        self.output_no = output_no
        self.weights = self.init_weight()

    def init_weight(self):
        return 2 * np.random.random((self.input_no, 1)) - 1

    # Activation Functions
    def sigmoid(self, Z):
        return 1/(1+np.exp(-Z)) #sigmoid

    def sigmoid_derivative(self, Z):
        return Z*(1-Z) #sigmoid

    def mean_squared_error(self, train_out, train_sol):
        return np.mean((train_out-train_sol)**2)

    def forward_propagation(self, Z):
        return self.sigmoid(np.dot(Z, self.weights))

    def train(self, train_in, train_sol):
        learning_rate = .1
        for i in range(100000):
            print("\n i = ", i, "weights=")
            print(self.weights)

            train_out = self.forward_propagation(train_in)

            print("train_out = ")
            print(train_out / scale)

            self.weights += learning_rate * np.dot(train_in.T, (train_sol-train_out) * self.sigmoid_derivative(train_out))  

if __name__ == '__main__':
    # dataset
    df = pd.read_csv('result.csv', encoding='utf-8')
    data = df.iloc[:]
    data_in = data.drop(columns='總成績').to_numpy()
    data_out = data['總成績'].to_numpy() 
    data_out = np.reshape(data_out, (data_out.size, 1))

    sep = 3
    scale = 0.01

    train_in = data_in[sep:] * scale
    train_sol = data_out[sep:] * scale

    test_in = data_in[:sep] * scale
    test_sol = data_out[:sep] * scale

    np.random.seed(1)

    nn = NeuralNetwork(10, 1)

    nn.train(train_in, train_sol)

    train_out = nn.forward_propagation(train_in)
    test_out  = nn.forward_propagation(test_in)
    train_out /= scale
    test_out /= scale

    print('\n MSE for training data: ', nn.mean_squared_error(train_out, train_sol/scale))
    print('\n MSE for testing data : ', nn.mean_squared_error(test_out, test_sol/scale))
    print('\nThe final prediction is \n', test_out)
