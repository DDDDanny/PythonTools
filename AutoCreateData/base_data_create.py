# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 1:42
# @Author  : DannyDong
# @File    : base_data_create.py
# @describe: 基础数据生成类

import random


class BaseDataCreate(object):
    """
        新字段生成数据逻辑写在这里
    """
    def __init__(self, cnt=1):
        self.cnt = cnt

    # 处理生成多条数据(生成字符串类型的list)
    def create_list(self, demo_list1=None, demo_list2=None, res_list=None):
        if demo_list1 is None and demo_list2 is None or demo_list1 is None:
            raise Exception('demo_list参数错误')

        if demo_list2 is None:
            for i in range(self.cnt):
                res = random.choice(demo_list1)
                res_list_str = ''.join(res)
                res_list.append(res_list_str)
        else:
            for i in range(self.cnt):
                res = random.choice(demo_list1) + random.choice(demo_list2)
                res_list_str = ''.join(res)  # list转字符串
                res_list.append(res_list_str)
        return res_list

    # 处理生成多条数据(生成数字类型的list)
    def create_num_list(self, demo_list=None, res_list=None):
        if demo_list is None:
            raise Exception('demo_list参数错误')

        for i in range(self.cnt):
            res = random.choice(demo_list)
            res_list.append(res)
        return res_list

    # 处理生成多条电话
    def phone_nums(self, demo_list=None, res_list=None):
        if demo_list is None:
            raise Exception('demo_list参数错误')

        for i in range(self.cnt):
            phone_header = random.choice(demo_list)
            phone = list(phone_header)
            cnt = len(phone)
            for j in range(11 - cnt):
                phone.append(str(random.randint(0, 9)))
            phone_str = ''.join(phone)
            res_list.append(phone_str)
        return res_list

    # 生成基础姓名
    def create_name(self):
        # 姓氏
        list1 = ['赵', '钱', '孙', '李', '韩', '陈', '程', '周', '吴', '郑', '王', '冯', '卫', '蒋', '沈', '杨', '朱', '秦',
                 '许', '何', '吕', '张', '孔', '曹', '严', '金', '魏', '陶', '姜', '谢', '章', '云', '苏', '窦', '潘', '刘',
                 '袁', '任', '贺', '胡', '彭', '汤', '唐', '柳', '伍', '齐', '康', '黄', '汪', '萧', '宋', '屈', '毛', '卢',
                 '樊', '田', '钟', '徐', '邱', '万', '林', '丁', '邓', '高', '江', '段', '曲', '叶', '赖', '谭', '宁', '燕',
                 '庄', '易', '古', '容', '阎', '温', '欧阳', '公孙', '阳', '轩辕', '司徒', '诸葛', '宇文', '慕容', '上官']
        # 名字
        list2 = ['婧文', '立民', '卫国', '依萱', '坤', '伟', '萌', '一唯', '丽红', '成祥', '辉煌', '展翔', '展翅',
                 '泽西', '韵澄', '文贤', '丽清', '静', '学豪', '博文', '琳', '宇', '涛', '轩海', '雪凡', '春燕',
                 '泉', '玉萍', '若兰', '慧丽', '腾', '本山', '馨', '希远', '玉芝', '琳琳', '梦琪', '杰', '馨怡',
                 '紫萱', '智雅', '忠泽', '亚', '莹', '浩', '华生', '天云', '金波', '烨', '策', '萌', '娟', '超',
                 '亮', '怀文', '可', '哲', '逸轩', '克', '心云', '然', '洁', '丽娜', '云鹏', '鑫', '平', '晶', '威',
                 '铭', '宁', '令江', '国平', '炎', '子文', '陨', '茜', '峥', '祥颖', '倾', '岳', '延军', '帆', '晨',
                 '均', '锦', '升宇', '度', '瑞', '若男', '阳']

        full_name_str_list = []
        self.create_list(list1, list2, full_name_str_list)
        return full_name_str_list

    # 生成性别
    def create_sex(self):
        sex_list = ['男生', '女生', '待确认']
        sex_str_list = []
        self.create_list(sex_list, None, sex_str_list)
        return sex_str_list

    # 生成基础电话号码
    def create_phone(self, user_type=0):
        list1 = ['139', '138', '137', '136', '135', '134', '178', '170', '188', '187',
                 '183', '182', '159', '158', '157', '152', '150', '147', '186', '199',
                 '185', '156', '155', '130', '131', '132', '189', '180', '170', '153', '133']
        list2 = ['9']

        phone_str_list = []
        if user_type == 666:
            self.phone_nums(list2, phone_str_list)
        else:
            self.phone_nums(list1, phone_str_list)
        return phone_str_list

    # 生成课程信息
    def create_course(self):
        course_list = ['语文', '数学', '英语', '物理', '化学']
        course_str_list = []
        self.create_list(course_list, None, course_str_list)
        return course_str_list


# 测试数据
if __name__ == '__main__':
    exp = BaseDataCreate(5)
    print(exp.create_phone(666))
    print(exp.create_name())
    print(exp.create_sex())
    print(exp.create_course())
