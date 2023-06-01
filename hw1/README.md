姓名: 王關平Kenneth Ong Kuan Phing 學號: 41047041S

1. 對於這次成績計算的dataset，我選擇用所有10欄資料作為輸入，而訓練出來的輸出為一個數字，即預測的總成績。作為訓練資料，我使用了dataset中第 4 行到最后一行共11筆，而dataset中第 1 行到第 3 行則用于测试训练的正确性。
軟硬體規格:
- 2020 Macbook Air M1
- python3 3.11.2
- 套件和環境管理： poetry, 
安裝需要的dependencies
```bash
pip install -r requirements.txt
```
執行檔案方式為
```bash
python <filename>.py
```

使用原因:
- 我只有這台筆電
- python語法簡單明瞭

2. 我使用 sigmoid 作为这道题的激活函数。
对数据集进行 100000 次训练后，均方误差如下：
訓練資料之均方误差: 7.116795912741762
測試資料之均方误差: 8.875497889352898
執行方法: 
```bash
python3 1-neuron-sigmoid.py 
```

3. 我选择 tanh 作为替代激活函数，训练和测试数据集与上面的问题相同。執行100000 次训练后，结果是：
訓練資料之均方误差: 7.9758120854022225
測試資料之均方误差: 7.801875923718417
執行方法: 
```bash
python3 1-neuron-tanh.py
```
因此，这个激活函数比上一个问题中使用的 sigmoid函数稍微好一些。


4. 两个神经元的架構為
![](https://i.imgur.com/WkYSSbd.png)
其中其后向传播函数backward propagation function可以写成
```python!
def backward_propagation(X, y, hidden_layer_output, output_layer_output, weights1, weights2, bias1, bias2):
    # Calculate the error between the predicted output and the actual output
    error = y - output_layer_output
    
    # Calculate the derivative of the output layer activation function
    d_output = error * sigmoid_derivative(output_layer_output)
    
    # Calculate the error for the hidden layer
    error_hidden = d_output.dot(weights2.T)
    
    # Calculate the derivative of the hidden layer activation function
    d_hidden = error_hidden * sigmoid_derivative(hidden_layer_output)
    
    # Calculate the gradients for the weights and biases
    d_weights2 = hidden_layer_output.T.dot(d_output)
    d_bias2 = np.sum(d_output, axis=0, keepdims=True)
    d_weights1 = X.T.dot(d_hidden)
    d_bias1 = np.sum(d_hidden, axis=0, keepdims=True)
    
    return d_weights1, d_weights2, d_bias1, d_bias2
```

5. 使用以上結論訓練資料，執行100000 次训练后，得出
訓練資料之均方误差: 0.9086389625047453
測試資料之均方误差: 6.869907068097764
執行方法: 
```bash
python3 2-neurons-sigmoid.py
```

6. 這次使用leaky relu的activation function訓練資料，執行100000 次训练后，得出
訓練資料之均方误差: 1.5856206188302047
測試資料之均方误差: 5.5879409676101615
執行方法:
```bash
python3 2-neurons-leaky-relu.py
```
照輸出的均方误差數據，leaky relu activation function有比原本sigmoid好


7. 若使用三個神經元，神經元架構如下
![](https://i.imgur.com/UShaVZN.png)
因跟前一題一樣為二層的神經元架構，因此backward propagation的函數皆一樣。不同的是weights權重的矩陣大小（第一層weights為10x2，第二層為2x1），因此三層神經元架構一樣為
```python!
def backward_propagation(X, y, hidden_layer_output, output_layer_output, weights1, weights2, bias1, bias2):
    # Calculate the error between the predicted output and the actual output
    error = y - output_layer_output
    
    # Calculate the derivative of the output layer activation function
    d_output = error * sigmoid_derivative(output_layer_output)
    
    # Calculate the error for the hidden layer
    error_hidden = d_output.dot(weights2.T)
    
    # Calculate the derivative of the hidden layer activation function
    d_hidden = error_hidden * sigmoid_derivative(hidden_layer_output)
    
    # Calculate the gradients for the weights and biases
    d_weights2 = hidden_layer_output.T.dot(d_output)
    d_bias2 = np.sum(d_output, axis=0, keepdims=True)
    d_weights1 = X.T.dot(d_hidden)
    d_bias1 = np.sum(d_hidden, axis=0, keepdims=True)
    
    return d_weights1, d_weights2, d_bias1, d_bias2
```

8. 我使用 sigmoid 作为这次三層神經元的激活函数。
对数据集进行100000次训练后，均方误差如下：
訓練資料之均方误差: 0.2708460023481153
測試資料之均方误差: 2.851957170946919
執行方法: 
```bash
python3 3-neurons-sigmoid.py
```
    
9. 
A. 問ChatGPT十個問題，大約有二到三個問題是令我滿意的。
B. 有
C. 會
> Q：台灣最近covid-19是不是升溫了？
> A：我作為一個語言模型，我的知識截止到2021年9月，因此我不能提供最新的關於台灣covid-19疫情的信息。但是，從截至2021年9月的信息來看，台灣的covid-19疫情曾經出現過一些反覆的情況，但在政府和民眾的共同努力下，疫情得到了控制。
> 
> 台灣政府採取了多項措施來控制疫情，例如：加強邊境管控、實行居家檢疫、限制大型聚會、加強社交距離等。台灣民眾也非常配合，積極遵守防疫規定，這些都是控制疫情的重要因素。
>
> 如果您需要最新的台灣covid-19疫情信息，建議您關注台灣政府官方公告或可信的新聞媒體。

若再問多一次，則會回答

> Ａ：從2021年底至今，台灣確實經歷了一波COVID-19疫情爆發。最初的病例是由於一位境外入境的船員帶回台灣，並在社區中感染其他人。此後，疫情迅速擴散，並在2022年初達到高峰。截至2023年3月12日，台灣共報告了約34萬例COVID-19確診病例和約3,800人死亡。
>
>近期，台灣政府已加強了疫情防控措施，包括加強邊境管制、加強社區篩檢、推動疫苗接種等，疫情呈現趨緩的趨勢。然而，由於新冠病毒的高度傳染性和變異性，疫情仍需密切關注和應對。

這兩個回答很矛盾，第一個因尚未更新最新消息而沒直接回答題目。第二次回答則可以給出最新（更新至當天）的數據。再一次刷新的話會得到
> Ａ：截至我回答这个问题的时间（2023年3月12日），我无法回答这个问题，因为我的知识截止到2021年9月，而且我不是一个实时的新闻平台。建议您查看台湾当地的新闻和卫生部门发布的最新信息以获取最准确的答案。

E. 作为一名语言模型，ChatGPT可以对各种数学问题进行计算和推理，包括复杂的数学问题。但能力是基于已知的数学知识和算法，並沒有自己的创造力或独立思考能力。因此，在处理某些非常复杂的问题时可能會出錯。ChatGPT可以解決的困難的題目有	
微积分和微分方程(求解导数、积分和微分方程等)
线性代数(高斯消元法、矩阵分解等)
统计学(方差分析、回归分析等)

10. 這次作業中我遇到的問題有
- 無法確定ChatGPT是否給出正確的解釋或解法。因在不斷的提問中可以發現它有時候不完全照著我給的條件下給出解答。因此不斷的刷新ChatGPT答覆，但自己不能再判斷哪一個是可以相信的答覆。
- 對於feed forward和backward propagation沒有充分的暸解，在課堂上沒足夠暸解內容。導致寫作業在做更多變化的時候的沒有很多的想法與頭緒。

11. 
- https://towardsdatascience.com/how-to-build-a-simple-neural-network-from-scratch-with-python-9f011896d2f3 (參考code的構造，把feedforward函式分出來，並瞭解backward propagation的原理)
- https://towardsdatascience.com/math-neural-network-from-scratch-in-python-d6da9f29ce65 (暸解backward propagation的函數推倒方式)
- https://www.youtube.com/watch?v=0e0z28wAWfg&t=661s (參考2層神經元的backward propagation推倒原理)
- https://gist.github.com/miloharper (參考簡潔的coding style)
    
12. 我使用了尋找三角形面積的公式，訓練資料為自己產生的，一共50筆。每一筆資料擁有三角形底部長度和高度。而測試資料有3筆，一樣為隨機產生。這次的神經元結構為二層神經元，其中第一層有4個神經元。
```python!
from numpy import np
    
train_in = np.array([[0.19832373 0.3791779],
                     [0.12645244 0.21835166],
                     [0.28745333 0.25592968]])
    
train_sol = np.array([[0.03759999, 0.01380555, 0.03678392]).T
```
![](https://i.imgur.com/2COlZt4.png)
程式碼可以參考area.py檔案，其中訓練出來的數據如下
訓練資料之均方误差: 3.4337707008928074e-05
測試資料之均方误差: 3.990658418017117e-05
執行方法: 
```bash
python3 area.py
```