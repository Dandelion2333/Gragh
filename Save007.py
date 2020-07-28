# 项目目的：加深对图遍历方式的理解，如使用DFS或者BFS的理解与运用
# 题目介绍：007站在水池的中央，周围有很多鳄鱼，他要通过踩在鳄鱼的头上的方式最终跳到岸上。
#            已知007的跳跃半径为Jump，鳄鱼坐标存在list中，问题为，007是否能够跳到岸上？输出yes or no

def Save007_DFS(list, start, jump):
    answer = False
    # 循环遍历list中所有的顶点
    for cnt in range(len(list)):
        # 获取以顶点为圆心，跳跃距离为半径，落在圆内的点
        if IsJump(start, list[cnt]) == True :
            answer = Save007_DFS(list, list[cnt], jump)
            if answer == True:
                break
    if answer == True:
        print("yes")
    else:
        print("no")

def Dfs(start, list):


def IsJump(start, list):

    return True


if __name__ == "__main__":
    list = [[1,2],[3,4],[9,5],[6,4],[7,7],[2,5],[1,4]]
    start = [5,5]
    jump = 3


    answer_dfs = Save007_DFS(list, start, jump)
