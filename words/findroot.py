"""
2020年2月7日
寻找单词词根
"""


def find_word():
    with open('./res/词根.txt', encoding='utf8') as f:
        list1 = f.read().split('-------------')
        print(len(list1))
        new_list = list()
        for word_area in list1[:10]:
            word_list = word_area.split(' ')
            i = 0
            root_list = list()
            for word in word_list:
                if word.strip().encode('utf8').isalpha():
                    print(i)
                    print(word.strip())
                    root_list.append(word.strip())
                    i += 1
            new_list.append(root_list)
            # if not word.strip().isalpha():
            #     word_list.remove(word.strip())
            # print(word.strip())
    return new_list


def find_root(list1):
    list1 = ['Abuse', 'Abduct', 'Aberrant']
    i = 0
    j = 2
    root = list1[0][i:j].lower()
    # 下面开始找最大词根，先找最小的词根，分两种情况
    # 1、找到了
    # 2、没找到
    count = 0
    for word in list1[1:]:
        if root in word:
            count +=1
    if count== len(list1)-1:
        print('找的词根')
    else:
        print('j-1')
        # return root


if __name__ == '__main__':
    print(find_word())
