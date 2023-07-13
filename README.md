#### 文件内容介绍
```
│  10205501403_刘佳凡_实验二.pdf	  # 实验报告
│  README.md											# 本文件
│  requirements.txt								# 环境配置文件
│  A.py								            # 题目一解题代码
│  B.py							              # 题目二解题代码
```

#### 环境配置

环境依赖已经列在 requirements.txt 中了，使用

```py
pip install -r requirements.txt
```

#### 实验一

##### 运行方法

因为是py文件，直接run code就好了（注意这里的环境是：**anaconda3（Python 3.8.8）**）

状态类涉及到四种计算h值的方法，若想用不同的距离方式来计算h值，先注释掉当前的`def count_h(self):`，然后去掉注释了的另一种`def count_h(self):`

#### 实验一

##### 运行方法

因为是py文件，直接run code就好了（注意这里的环境是：**anaconda3（Python 3.8.8）**）

这里涉及到两种计算h值的方法，若想切换方法，先注释掉当前的`def count_h(self):`，然后去掉注释了的另一种`def count_h(self):`，并且在Pyramid_A_Start主函数的while循环中修改：

```py
#next_room.count_h()
next_room.count_h(N,M,rooms)
```

变为：

```py
next_room.count_h()
#next_room.count_h(N,M,rooms)
```

