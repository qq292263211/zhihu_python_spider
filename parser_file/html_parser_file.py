#_*_coding:utf-8_*_
from bs4 import BeautifulSoup
import urlparse
import sys
import os
import re
reload(sys)
sys.setdefaultencoding('utf8')
'''进入知乎主页后爬取知乎主页的所有的问题URL'''
class Html_parser():
    def parse(self,url,content):
        global question_urls
        question_urls = set()
        if url is None and content is None:
            return
        soup=BeautifulSoup(content.text,"html.parser")
        links= soup.find_all('a',class_='question_link')
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url,new_url)
            question_urls.add(new_full_url)
            # question_urls['name'] = link['title']
            # question_urls['url'] = urlparse.urljoin(url,new_url)
        return question_urls

    '''再次获取问题页面相关的问题URL'''
    def get_new_url(self,content):

        '''问题页面URL提取器'''
        if content is None:
            return
        soup = BeautifulSoup(content.text, "html.parser")
        links = soup.find_all('a', class_='question_link')
        for link in links:
            new_url = link['href']
            new_full_url = 'https://www.zhihu.com'+new_url
            question_urls.add(new_full_url)
            return question_urls
    def get_new_text(self,content):
        '''问题页面内容提取器'''
        if content is None:
            return
        soup = BeautifulSoup(content.text,"html.parser")
        title = soup.title.string.split('\n')[2] #找出问题标题
        text = soup.find_all('div',tabindex="-1")
        print title
        num =1
        error=0
        again=0
        for content in range(len(text)):
            try:
                answer_name = text[content].find('a',class_="author-link")
                answer_file_namename = answer_name.text
            except:
                print '该问题暂时无人回答'
                error+=1
                answer_file_namename = '匿名用户'
            try:
                answer_text=text[content].find('div',class_="zm-editable-content clearfix")
                answer_content = answer_text.text
            except:
                error += 1
                answer_content='作者修改内容通过后，回答会重新显示。如果一周内未得到有效修改，回答会自动折叠。'
            path = title
            if  os.path.isdir(path) ==None: #判断当前目录有没有此文件.没有的话就新建一个
                os.mkdir(path)
            else:
                again += 1
                print '重复文件%s'%str(again)
            answer_file_name=path+'/'+answer_file_namename+'.txt'
            fr=open(re.sub('[\/:*?"<>|]', '-', answer_file_name),'w')
            fr.write(str(answer_content))
            fr.close()
            print "当前已经爬取了%s个问题,成功了%s个" % (str(num),str(num - error))
            num+=1










