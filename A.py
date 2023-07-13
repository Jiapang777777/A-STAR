#135702684目标状态
#150732684 - 2 过程：5先移到空位105732684 3再移到空位135732684
#1 5 0
#7 3 2
#6 8 4

# put() 插入元素
# get()取队首元素的值并将其弹出.
# full() 判断是否为满.
# empty() 判断是否为空

from queue import PriorityQueue
import math
import numpy as np

#先设定最终需要达到的目标状态
target_state = np.array([[1, 3, 5], [7, 0, 2], [6, 8, 4]], dtype=int)


class Forest:
    #先初始化
    def __init__(self, state_matrix, g):
        self.state_matrix = state_matrix  # 每个时刻的状态矩阵
        self.g = g                        # 真实代价 —— 与上个状态相比 就是多走一步的代价 即+1             
        self.h = self.count_h()       # 启发式函数
        self.f = self.g + self.h          # F值

    #计算曼哈顿距离
    def count_h(self):
        h = 0
        for i in self.state_matrix.flatten():
            dx = abs(np.where(self.state_matrix == i)[0][0] - np.where(target_state == i)[0][0])
            dy = abs(np.where(self.state_matrix == i)[1][0] - np.where(target_state == i)[1][0])
            h += dx + dy
        return h

    # #用对角线距离来计算启发式
    # def count_h(self):
    #     h = 0
    #     for i in self.state_matrix.flatten():
    #         dx = abs(np.where(self.state_matrix == i)[0][0] - np.where(target_state == i)[0][0])
    #         dy = abs(np.where(self.state_matrix == i)[1][0] - np.where(target_state == i)[1][0])
    #         h += math.sqrt(2)*max(dx,dy)
    #     return h
    
    
    # #换一个方式更复杂精确的方式来计算启发式
    # def count_h(self):
    #     h = 0
    #     for i in self.state_matrix.flatten():
    #         dx = abs(np.where(self.state_matrix == i)[0][0] - np.where(target_state == i)[0][0])
    #         dy = abs(np.where(self.state_matrix == i)[1][0] - np.where(target_state == i)[1][0])
    #         h += (dx+dy)+(math.sqrt(2)-2)*min(dx,dy)
    #     return h

    # #用欧几里得距离来计算启发式
    # def count_h(self):
    #     h = 0
    #     for i in self.state_matrix.flatten():
    #         #分别获取每个点的i和j
    #         dx = abs(np.where(self.state_matrix == i)[0][0] - np.where(target_state == i)[0][0])
    #         dy = abs(np.where(self.state_matrix == i)[1][0] - np.where(target_state == i)[1][0])
    #         h += math.sqrt(dx^2 + dy^2)
    #     #print(h)
    #     return h


    def find_next(self):
        next_states = []
        #相当于就是把0空格上下左右移动
        #上：i-1，j不变
        #下：i+1，j不变
        #左：i不变，j-1
        #右：i不变，j+1

        #先获取空格坐标
        i = np.where(self.state_matrix == 0)[0][0]
        j = np.where(self.state_matrix == 0)[1][0]

        # 空格上移
        if i-1 >= 0:
            next_state = self.state_matrix.copy()
            next_state[i][j] = next_state[i - 1][j]
            next_state[i - 1][j] = 0
            next_states.append(next_state)

        # 空格下移
        if i+1 <= 2:
            next_state = self.state_matrix.copy()
            next_state[i][j] = next_state[i + 1][j]
            next_state[i + 1][j] = 0
            next_states.append(next_state)

        # 左移
        if j-1 >= 0:
            next_state = self.state_matrix.copy()
            #这里相当于交换空格与周围的点
            next_state[i][j] = next_state[i][j - 1]
            next_state[i][j - 1] = 0
            next_states.append(next_state)

        # 右移
        if j+1 <= 2:
            next_state = self.state_matrix.copy()
            next_state[i][j] = next_state[i][j + 1]
            next_state[i][j + 1] = 0
            next_states.append(next_state)
        
        return next_states
    
    
    #重定义_lt_比较方法，使得类实例能够相互比较
    def __lt__(self, other):
        #定义< 比较符号，根据f值大小从小到大排序
        return self.f < other.f


def Forest_A_start(start_state):
    priority_q = PriorityQueue()
    expanded_state_set = []  # 已经访问过的状态
    state = Forest(start_state, 0)
    priority_q.put(state)
  
    #取出f值最小的状态,取队首元素的值并将其弹出
    present_state = priority_q.get()
    #n = 0  # 统计步数
    real_cost = 0
    while present_state.count_h() != 0: #设置中止条件为当h启发式函数为0
        
        #每循环一次步数➕1
        #n += 1
        #flatten为了将矩阵拉平放在list列表里面，这样在后面好做对比
        #这里必须要str为了后面in来比较
        expanded_state_set.append(str(present_state.state_matrix.flatten()))

        # 寻找下一步的可行状态
        next_states = present_state.find_next()
        for i in range(len(next_states)):
            #print(next_states[i].flatten().all())
            if str(next_states[i].flatten()) in expanded_state_set:  #跳过已经扩展过的路径
                continue
            #这里由于每一步代价均相同，真实代价为1即可，最终的真实代价即可代表步数
            real_cost = present_state.g + 1
            #将下一个可行状态都放入priority中
            state_next = Forest(next_states[i], real_cost)
            priority_q.put(state_next)
        #为下一轮迭代做准备
        present_state = priority_q.get() #获取f值最小的开始
    print(real_cost)


if __name__ == "__main__":
    #a = np.array([[1, 3, 5], [7, 0, 2], [6, 8, 4]], dtype=int)
    #print(a.flatten())
    #首先第一步,将输入的一串数字转换为array
    array = np.array(list(input()), dtype=int)
    array = array.reshape(3, 3)
    #print(array)
    Forest_A_start(array)