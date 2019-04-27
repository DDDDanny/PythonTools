### AutoCreateData
---

* 运行环境
  Python 3.7

* 依赖包
    pip install xlrd
    pip install xlutils
    pip install openpyxl

* 如何使用
> 批量生成新增字段数据
```python
class BaseDataCreate(object):
	...
	def create_新增字段名(self):
        # 如果有两个list，会在两个list中各取一个值做拼接
        新增字段_list1 = [字段数据]
        新增字段_list2 = [字段数据]
        新增字段_str_list = []
        self.create_list(新增字段_list1, 新增字段_list2, 新增字段_str_list)
        return 新增字段_str_list
    ...
```
> Excel新增字段
```python
class DataInput(object):
	...
	def data_save(self):
		...
		ExcelSave().write_excel(数据, self.Excel, 列数)
		...
```
> 运行

1. 输入导出数据的用户类型（输入666，则会导出以9开头的11位字符串；输入其他，则会导出正常的电话号码。）
2. 输入需要导出的数据数量
3. 输入需要从第几行开始生成数据
4. 输入Excel文件地址

* 存在缺陷
  无法对自动添加的数据进行清空，以至于第一次生成50条数据后，第二次生成20条数据，Excel表中任然有50条数据，新生成的20条数据覆盖了第一次生成50条的前20条数据。

* 后期优化
  当没有找到匹配的文件时，可以自动生成文件

