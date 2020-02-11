"""
时间：2020年2月5日
描述：爬取优词网站的四级单词
"""

import requests
from bs4 import BeautifulSoup


class YouDictSpider:
    def __init__(self):
        # 单词首页url
        self.start_url = 'https://www.youdict.com/ciku/id_1_0_0_0_0.html'
        self.start_sub_url = self.start_url[:-6]
        self.end_url = 'https://www.youdict.com/ciku/id_1_0_0_0_291.html'
        self.url_list = list()
        self.word_dict = dict()
        pass

    # 获取所有四级单词的页面
    def get_url_list(self):
        # 一共192个页面

        for i in range(292):
            url = self.start_sub_url + str(i) + self.start_url[-5:]
            self.url_list.append(url)
            # r = requests.get(url)
        return self.url_list

    # 获取每一页的单词以字典的方式
    def get_words(self):
        for i in self.url_list:
            r = requests.get(i)
            # 开始解析
            soup = BeautifulSoup(r.text, 'lxml')
            # 获取div标签
            caption_list = soup.find_all('div', attrs={'class': 'caption'})
            for caption in caption_list:
                # 1、获取单词
                word = caption.a.text
                # 2、获取中文意思
                chinese = caption.p.text
                print(word,chinese)
                self.word_dict[word] = chinese
        return self.word_dict

    # 保存文件到本地
    def save_words(self):
        # self.get_words()
        with open('res/cet4.text', 'w', encoding='utf8') as f:
            f.write(str(self.word_dict))


if __name__ == '__main__':
    s = YouDictSpider()
    # print(s.start_sub_url)
    print(s.get_url_list())
    print(s.get_words())
    s.save_words()
