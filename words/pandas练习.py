"""
日期：2020年2月10日
简单的练习
"""
import pandas as pd
from pandas import Series
from pandas import DataFrame

# 1、创建excel文件
# id = [1, 2, 3, 4]
# name = 'tom clan lucy marry'.split()
# stu = {'id': id, 'name': name}
# df = DataFrame(stu)
# df.to_excel('students.xlsx')
# 2、读取excel文件
stu = pd.read_excel('students.xlsx',usecols='B:C',index_col='id')
# stu.set_index('id')
print(stu)
#
