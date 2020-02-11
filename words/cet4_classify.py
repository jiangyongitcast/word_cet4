"""
2020年2月10日
英语单词的分类
1、所有单词 排两次正序和逆序
2、名词 动词 形容词 副词
"""
import pandas as pd
import xlwt


def words():
    with open('./res/cet4.text', encoding='utf8') as f:
        words = eval(f.read())
        words_sorted = sorted(words, key=lambda x: x[::-1])
        # flags = 'n v adj adv'.split()
        # name = 'words_'
        # exec_str = ''
        # for flag in flags:
        #     exec_str += name + flag + ' = ' + 'dict()\n'
        # exec(exec_str)
        words_n = {}
        words_v = {}
        words_adj = {}
        words_adv = {}
        for word in words:
            # 开始筛选
            if 'n.' in words[word]:
                words_n[word] = words[word]
                # print(word,words[word])
            if 'v.' in words[word]:
                words_v[word] = words[word]
            if 'adj' in words[word]:
                words_adj[word] = words[word]
            if 'adv' in words[word]:
                words_adv[word] = words[word]
    return words, words_n, words_v, words_adj, words_adv
    # print(word)


# 2、写入excel文件
def write_excel(words, name):
    table = xlwt.Workbook(encoding='utf8')
    # for name in names_list:
    #     s1 = table.add_sheet(name)
    # # sheet1 = table.add_sheet()
    # s1 = table.get_sheet('所有单词正序')
    sheet = table.add_sheet(name)
    # sheet = table.get_sheet(name)
    # for word in words:
    sheet.write(0, 0, 'English')
    sheet.write(0, 1, 'Know?')
    sheet.write(0, 2, 'Chinese')
    i = 1
    for word in words:
        print(word)
        sheet.write(i, 0, word)
        # sheet.write(i, 1)
        sheet.write(i, 2, words[word])
        i += 1
    # s1.write(0, 0, 'ok?')
    # s1.wirte(0,0,'test')

    table.save('cet4_classify.xlsx')


if __name__ == '__main__':
    # print(words())
    names_list = '所有单词正序 所有单词逆序 名词正序 名词逆序 动词正序 动词逆序 形容词正序 形容词逆序 副词正序 副词逆序'.split()

    # write_excel(words()[0],'所有单词正序')
    # words_sorted = sorted(words, key=lambda x: x[::-1])
    # i = 0
    # for name in names_list:
    #     write_excel(words()[i], name)
    #     write_excel(sorted(words()[i], key=lambda x: x[::-1]),name)
    #     i += 1
    d = words()[0]
    v = sorted(d, key=lambda x: x[::-1])
    v1 = dict()
    for i in v:
        # print(i)
        v1[i] = d[i]
    # print(v1)
    write_excel(v1,'名词逆序')