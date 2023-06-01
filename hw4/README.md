資工系 41047041S 王關平

a. ![](./a.png)

for features $X_1^{2}$ and $X_2^{2}$, at least 1 neuron needed to classify the dataset.
Explanation
These squared features allow the neural network to capture non-linear relationships between the input features and the target variable. By including the squared features, you effectively introduce additional dimensions to the input space. This can be beneficial in cases where the relationship between the input features and the target variable is not purely linear. The squared features enable the neural network to learn and model non-linear patterns in the data. in the Circle dataset, the original features $X_1$ and $X_2$ represent the x and y coordinates of points on a 2D plane. By including the squared features $X_1^2$ and $X_2^2$, the neural network can learn to capture the circular pattern in the data, as the equation of a circle involves the squared terms of the coordinates.

b. Yes.
As the learning rate increases, the data loss also increases. For example, when the learning rate is increased from 0.03 to 0.3, the data loss barely get less than 0.1, and for learning rate of 3, the data loss get aroung 0.5 and cannot reach below 0.1 at all.

Explanation
Difficulty in Converging: A very high learning rate can make it challenging for the optimization algorithm to find the global or local minima. The large steps taken during parameter updates can cause the algorithm to keep "jumping" across the optimal solution, preventing convergence and leading to an increase in data loss.

Another network architecture that gives test loss of less than 0.1 
![](./b.png)

c. For Gaussian data set using only the raw inputs, only 1 neuron needed to get test loss less than 0.1. In the case of the Gaussian dataset, the points from two different classes are distributed in a way that they can be separated by a linear boundary. Linear separability means that a straight line can effectively classify the data points into their respective classes. Since the input features $X_1$ and $X_2$ represent the x and y coordinates of the points on a 2D plane, a linear boundary (a line) can effectively separate the two classes. Thus a single neuron is sufficient to obtain a test loss less than 0.1.

Using $X_1^2$ and $X_2^2$ instead of $X_1$ and $X_2$. I cannot obtain test loss of less than 0.1. Again due to the linearity of Gaussian data set, when you use the squared features $X_1^2$ and $X_2^2$, you introduce non-linearity into the model. The relationship between the squared features and the target variable becomes more complex, as the decision boundary is no longer linear.

d. 
![](./c-1.png)
![](./c-2.png)

e. L1 regularization specifically encourages sparse weights by adding the absolute values of the weights to the loss function of the model. The L1 regularization term is calculated as the sum of the absolute values of the weights multiplied by a regularization parameter, also known as the regularization strength or lambda.

f. L2 regularization specifically encourages small weights by adding the squared values of the weights to the loss function of the model. The L2 regularization term is calculated as the sum of the squared values of the weights multiplied by a regularization parameter, also known as the regularization strength or lambda.

g. hyperparameter that controls the strength or intensity of regularization in a neural network model. Regularization is used to prevent overfitting and improve the model's generalization ability by adding a penalty term to the loss function.

h. refers to the amount of random noise added to the input data during training. It is used to simulate noisy or imperfect data and test the model's ability to handle and generalize from such data. 

i. refers to the number of training examples that are processed together in a single forward and backward pass during training. It represents the number of samples from the training dataset that are used to update the model's weights in each iteration.