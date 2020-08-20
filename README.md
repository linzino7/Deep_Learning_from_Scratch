# Deep_Learning_from_Scratch
Deep Learning：用Python進行深度學習的基礎理論實作。

本Rep 為看書筆記。

## 第二章 感知器
AND OR NAND 都可以被感知器實作。
皆可以由人工設定"參數"+階梯函數(step function)實作。

但XOR 就需要多層感知器材可以實做出來。
所以把多個感知器堆疊就可以實作非線性結構。

```
# XOR 實作
NAND---|
       | ---OR 
OR  ---|
```
> 這也是為什麼機器學習總是要不斷更新 "參數" 的原因。


## 第三章 神經網路
### 3.5.2 Softmax Function
當exp(x) 中的x 超過1000 時，會回傳代表無限大的Inf 導致無法計算。

避免電腦溢位所以才需要取 log C 讓電腦可以計算執行。

### 3.2.6 非線性函數

如果當Activate Function 都是線性時，堆疊感知器將會沒有意義。

當h(x) = cx ， y(x) = h(h(h(x)))。 就只是 y= c^3 * X ，所以就會直接傳遞過去(無隱藏層) 。

使用線性函數時，無法發揮多層結構的優點

# Reference
https://github.com/oreilly-japan/deep-learning-from-scratch
