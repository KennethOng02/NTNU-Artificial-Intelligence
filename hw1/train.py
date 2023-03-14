from numpy import *

train_in = array([[0,2,0],[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
train_sol = array([[0,0,0,1,1]]).T

random.seed(1)
nn_weights = 2 * random.random((3,1)) - 1

for i in range(20):
    print("\n i = ", i, "nn_weight=")
    print(nn_weights)

    train_out = 1 / (1 + exp(-(dot(train_in, nn_weights))))
    print("train_out = ")
    print(train_out)

    nn_weights += dot(train_in.T, (train_sol-train_out) * train_out * (1 - train_out))

test_in = array([1,0,0])
print('\nThe final prediction is ', 1 / (1 + exp(-(dot(test_in, nn_weights)))))

# input_data = np.array([[11, 86   , 90  , 93.5, 93   , 90.63, 90 , 99 , 106, 98.33 ],
#                        [11, 85.5 , 70  , 86.5, 88.5 , 82.63, 91 , 88 , 90 , 89.67 ],
#                        [10, 77   , 63.5, 58.5, 78   , 69.25, 82 , 73 , 65 , 73.33 ],
#                        [8 , 82.5 , 75.5, 87.5, 82.5 , 82.00, 75 , 99 , 91 , 88.33 ],
#                        [11, 91   , 89  , 88.5, 89.75, 89.56, 105, 97 , 114, 105.33],
#                        [11, 94.5 , 89.5, 95.5, 90.5 , 92.50, 93 , 116, 112, 107.00],
#                        [6 , 78.25, 63.5, 62.5, 67.25, 67.88, 94 , 66 , 77 , 79.00 ],
#                        [5 , 86.5 , 90.5, 82.5, 0    , 64.88, 85 , 94 , 90 , 89.67 ],
#                        [11, 85   , 62  , 63  , 84.5 , 73.63, 96 , 95 , 74 , 88.33 ],
#                        [10, 89   , 77.5, 90  , 90.5 , 86.75, 95 , 105, 97 , 99.00 ],
#                        [8 , 91.25, 90.5, 88.5, 0    , 67.56, 83 , 83 , 60 , 75.33 ],
#                        [7 , 70.5 , 61.5, 59  , 52   , 60.75, 98 , 95 , 38 , 77.00 ],
#                        [7 , 84   , 0   , 0   , 0    , 21.00, 65 , 0  , 0  , 21.67 ],
#                        [11, 64   , 9   , 0   , 0    , 18.25, 85 , 48 , 71 , 68.00 ]])
#
# output_data = np.array([[94, 89, 79, 85, 95, 96, 75, 75, 85, 91, 76, 73, 44, 57]]).T
