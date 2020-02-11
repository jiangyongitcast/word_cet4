"""
2020年2月6日
英语四级单词的处理
写入excel文件
"""
import xlwt

# 1、创建工作本类似数据库
# 2、创建工作表

workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet('英语单词四级')


def write_xls():
    with open('./res/cet4.text', encoding='utf8') as f:
        dict_ = eval(f.read())
        print(len(dict_))
        length = len(dict_)
        i = 0
        for word in dict_:
            # for i in range(length):
            worksheet.write(i, 0, word)
            worksheet.write(i, 2, dict_[word])
            print(i)
            i += 1
            print(word)
            # if i>=10:
            #     break

    workbook.save('./cet4.xls')


# 2、词性分类

def classify():
    with open('./res/cet4.text', encoding='utf8') as f:
        dict_ = eval(f.read())
        i = 0

        for word in dict_:
            chinese = dict_[word]
            if 'v' in chinese:
                print(i)
                print(word)
                print(dict_[word])
                i += 1


if __name__ == '__main__':
    classify()
