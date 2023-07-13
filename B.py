from queue import PriorityQueue
import numpy as np


class Pyramid:
    def __init__(self, input_state, g):
        self.state = input_state
        self.g = g
        self.h = 0
        self.f = self.g + self.h

    # #这里的启发式函数
    # def count_h(self):
    #     if Pyramid == N:  # 已经到山下了
    #         return
    #     self.h = 0.2  # 由于不知道每一条具体长度，所以这里值设为0即可，或者是小于1的值（因为可以看到最小的路径代价都是1）

    #这里启发式函数是以从该点出发的最短路径长度作为启发式函数的值，这一定是满足可容性的
    def count_h(self,N,M,rooms):  
        if Pyramid == N:  # 已经到山下了
            return
        mini = 0 
        #先找到一条存在的路径设为mini
        for i in range(M):
            if rooms[i][0] == self.state:
                mini = rooms[i][2]
                break
        #找到最小的
        for i in range(M):
            if rooms[i][0] == self.state:
                if rooms[i][2] < mini:
                    mini = rooms[i][2]
        self.h = mini

    #遍历一下找到下一个可走房间
    def find_next(self, M, rooms): 
        next_rooms = []
        #遍历一下我们的房间们
        for i in range(M):
            if rooms[i][0] == self.state:
                next_rooms.append(rooms[i][1])
        return next_rooms

    #与第一题写法都同理
    def __lt__(self, other):
        return self.f < other.f


def Pyramid_A_Start(N, M, K, rooms):
    #这里与第一题一样
    priority_q = PriorityQueue()
    cost_set = [] #记录下每条目标路径的代价
    State = Pyramid(1, 0) #从1号房间塔顶开始往下走，初始代价为0
    priority_q.put(State)

    #存下各个房间的路径关系
    #注意➕1是为了让后面所以的index都对应相应路标
    rooms_map = np.zeros((N + 1, N + 1), dtype=int)
    for i in range(M):
        #因为输入矩阵是这样的：[[1 2 1] [1 3 4] [2 4 3][3 4 2][3 5 1][4 5 2][5 1 5]]
        rooms_map[rooms[i][0], rooms[i][1]] = rooms[i][2]
    #print(rooms_map)

    #注意这里一共是找K条路
    while not priority_q.empty() and len(cost_set) < K:
        State = priority_q.get()
        #先看看到塔底没有
        if State.state == N:  # 到底了
            cost_set.append(State.g)
        #然后寻找下一个房间
        next_rooms = State.find_next(M, rooms)
        for i in range(len(next_rooms)):
            new_g = State.g + rooms_map[State.state, next_rooms[i]]  # 更新 g
            next_room = Pyramid(next_rooms[i], new_g)
            #next_room.count_h()
            next_room.count_h(N,M,rooms)
            priority_q.put(next_room)

    #查看是否一共找到了K条路径
    if len(cost_set) < K:
        for i in range(K - len(cost_set)):
            cost_set.append(-1)
    #然后全部打印出来
    for item in cost_set:
        print(item)


if __name__ == "__main__":
    #先处理第一行读取的字符串为字符串列表
    str = input().split()
    #接着用迭代器处理
    N, M, K = list(map(int, str))
    #接着来记录下每一条路径，存储在表中
    rooms = []
    for i in range(M):
        str = input().split()
        rooms.append(list(map(int, str)))
    # print(rooms[0])
    Pyramid_A_Start(N=N, M=M, K=K, rooms=rooms)