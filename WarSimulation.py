import pygame
import random
import numpy as np

size = 30
WIN_WIDTH = 900
WIN_HEIGHT = 600

# 输出二维数组
def printArray2D(list):
    for i in range(worldRow):
        for j in range(worldCol):
            print(list[i][j], end=" ")
        print("")

# =================世界地图=================
# 世界的行数
worldRow = int(WIN_HEIGHT/size)
# 世界的列数
worldCol = int(WIN_WIDTH/size)
# 世界地图
world = []
# 世界地图基础颜色
worldBaseColor = []

# 生成世界地图，目前只有空地
for i in range(worldRow):
    worldTemp = []
    for j in range(worldCol):
        worldTemp.append("空地")
        # 0代表基础颜色
        worldBaseColor.append(0)
    world.append(worldTemp)





# 基础资源生长值
print("地区基础资源生长值:")
resource = np.random.random((worldRow, worldCol))
# 基础资源倍数
resourceRate = 10
resource = resource * resourceRate
printArray2D(resource)

class State:
    # 国家金钱初始值是100
    money = 100.0

    # 国家的科技水平
    science = 0

    # 国家的军队数量
    army = 0

    # 国家的领域是个二维数组，记录国家占领的地盘
    def __init__(self, field, name, year):
        '''
        :param field: 国家的占领的地盘
        :param name:  国家的名称
        :param year:  当前年份
        '''
        self.field = field
        self.name = name
        self.year = year
        world[field[0][0]][field[0][1]] = self.name

    # 和平扩展
    def extendField(self):
        # 保存最大资源点
        maxResource = 0.0
        maxField = [-1, -1]

        # 找到领土周围最大资源点
        for i in range(len(self.field)):
            X = self.field[i][0]
            Y = self.field[i][1]
            # 上
            if (X - 1 >= 0 and world[X - 1][Y] == "空地"):
                if (resource[X - 1][Y] > maxResource):
                    maxResource = resource[X - 1][Y]
                    maxField[0] = X - 1
                    maxField[1] = Y
            # 下
            if (X + 1 < worldRow and world[X + 1][Y] == "空地"):
                if (resource[X + 1][Y] > maxResource):
                    maxResource = resource[X + 1][Y]
                    maxField[0] = X + 1
                    maxField[1] = Y
            # 做
            if (Y - 1 >= 0 and world[X][Y - 1] == "空地"):
                if (resource[X][Y - 1] > maxResource):
                    maxResource = resource[X][Y - 1]
                    maxField[0] = X
                    maxField[1] = Y - 1

            if (Y + 1 < worldCol and world[X][Y + 1] == "空地"):
                if (resource[X][Y + 1] > maxResource):
                    maxResource = resource[X][Y + 1]
                    maxField[0] = X
                    maxField[1] = Y + 1
        buyRate = 1
        if(maxField[0]==-1):
            print("    " + self.name + "无法扩张[无钱或者没有空地]")
        elif (world[maxField[0]][maxField[1]] == "空地" and self.money >= resource[maxField[0]][maxField[1]] * buyRate):
            self.field.append([maxField[0], maxField[1]])
            self.money -= resource[maxField[0]][maxField[1]] * buyRate
            print("    " + self.name + "扩张了第" + str(maxField[0]) + "||" + str(maxField[1]) + "空地" + "||" + "支出" + str(
                resource[maxField[0]][maxField[1]] * buyRate))
            world[maxField[0]][maxField[1]] = self.name
            print("    " + self.name + "总地盘数:" + str(len(self.field)) + " " + self.name + "日渐昌盛")
        else:
            print("    " + self.name + "无法扩张[无钱或者没有空地]")

    # 国家一年的收入
    def addMoney(self):
        for i in range(len(self.field)):
            self.money += resource[self.field[i][0]][self.field[i][1]]

    # 输出国家的经济总值
    def printMoney(self):
        print(str(self.name) + str(self.year) + "的经济总值是:" + str(self.money))

    # 国家的军队投入
    def investmentArmy(self):
        Army = random.randint(0, int(self.money / 3))
        self.army += Army
        print("    " + self.year + "投资军队" + str(Army))
        print("    全国军队总数量" + str(self.army))
        self.money -= Army

    # 国家的科技投入
    def investmentScience(self):
        Science = random.randint(0, int(self.money / 3))
        self.money -= Science
        self.science += Science
        print("    " + self.year + "投资科技" + str(Science))
        print("    科技水平" + str(self.science))

    def yearAction(self, year):
        self.year = year
        self.addMoney()
        self.printMoney()
        self.investmentArmy()
        self.investmentScience()
        self.extendField()
        print("###############################################")




countryPositon = []
for i in range(7):
    temp = [0,0]
    temp[0] = int(random.random()*20)
    temp[1] = int(random.random()*30)
    countryPositon.append(temp)

print(countryPositon)

yearStr = "公元0年"
countryName = ["秦国","楚国","齐国","燕国","赵国","魏国","韩国"]
country = [
    State([countryPositon[0]],countryName[0],yearStr),
    State([countryPositon[1]],countryName[1],yearStr),
    State([countryPositon[2]],countryName[2],yearStr),
    State([countryPositon[3]],countryName[3],yearStr),
    State([countryPositon[4]],countryName[4],yearStr),
    State([countryPositon[5]],countryName[5],yearStr),
    State([countryPositon[6]],countryName[6],yearStr),
         ]

######################################################################
#                   游戏可视化模块                                      #
#                                                                    #
######################################################################
# 1.初始化操作
pygame.init()


# 2.创建游戏窗口
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# 设置游戏标题
pygame.display.set_caption("战国模拟器")
# 设置背景颜色
window.fill((0, 0, 0))

# 第一次刷新页面
pygame.display.flip()

# 游戏启动页面的静态图
# 显示图片
year = 0
color = (255,255,255)
# 3.让游戏保持一直运行的状态
# game loop


fcclock = pygame.time.Clock()

while True:
    for i in range(7):
            country[i].yearAction("公元"+str(year)+"年")
    year+=1
    # 游戏帧刷新

    for i in range(worldRow):
        fcclock.tick(60)
        for j in range(worldCol):
            X = j*size
            Y = i*size
            if world[i][j] == "空地":
                color = (255,255,255)
            elif world[i][j] == "秦国":
                color = (220,20,60)
            elif world[i][j] == "楚国":
                color = (128,0,128)
            elif world[i][j] == "齐国":
                color = (0,0,255)
            elif world[i][j] == "燕国":
                color = (212,242,231)
            elif world[i][j] == "赵国":
                color = (0,250,154)
            elif world[i][j] == "魏国":
                color = (34,139,34)
            elif world[i][j] == "韩国":
                color = (255,255,0)
            pygame.draw.rect(window,color,(X,Y,size,size),0)
    pygame.display.update()
    # 4.检测事件
    for event in pygame.event.get():
        # 检测关闭按钮
        if event.type == pygame.QUIT:
            # 退出
            exit()


