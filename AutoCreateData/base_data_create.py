import random


class BaseDataCreate(object):
    def __init__(self):
        pass

    # 生成基础电话号码
    @staticmethod
    def phone_create():
        arrow = ['139', '138', '137', '136', '135', '134', '178', '170', '188', '187',
                 '183', '182', '159', '158', '157', '152', '150', '147', '186',
                 '185', '156', '155', '130', '131', '132', '189', '180', '170', '153', '133']

        phone_header = random.choice(arrow)
        phone = list(phone_header)
        for i in range(11 - len(phone_header)):
            phone.append(str(random.randint(0, 9)))
        phone_str = ''.join(phone)
        return phone_str


if __name__ == '__main__':
    exp = BaseDataCreate()
    print(exp.phone_create())

