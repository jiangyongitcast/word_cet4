"""
2020年2月5日
英语词根分类
"""

with open("res/words.txt", 'r', encoding='utf8') as f:
    # print(f.read())
    s = f.read()
    # print(s)
    roots = s.split('巩固词汇：')
    with open('res/词根.txt', 'w', encoding='utf8') as f:
        i =0
        for root in roots:
            print(i)
            print(root)
            print("------------")
            f.write(str(i))
            f.write(root)
            f.write('-------------\n')
            i+=1