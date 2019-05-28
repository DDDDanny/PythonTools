import random


# 选择困难症解决方案
class DifficultyOfChoice(object):
    def __init__(self):
        pass

    # 去哪吃饭？
    @staticmethod
    def foods_select():
        foods = [
            '全家', '兰州拉面', '老麻抄手', '冒菜', '点外卖', '点菜', '负一楼', '贼贵的面', '方便面', '修仙', 'C区食堂'
        ]
        food = random.choice(foods)
        print(food)

    # 怎么办？
    @staticmethod
    def general_choice():
        options = ['搞他！', '算了吧', '再来一次']
        option = random.choice(options)
        print(option)


if __name__ == '__main__':
    DifficultyOfChoice.foods_select()
    DifficultyOfChoice.general_choice()
