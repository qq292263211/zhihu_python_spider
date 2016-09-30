#_*_coding:utf-8_*_
from spi_loginer import spider_login
from parser_file import html_parser_file
from url_manager import  URL_MANGER
import sys
reload(sys)
sys.setdefaultencoding('utf8')
'''爬虫总调度程序'''
class spider_main(object):
    def __init__(self):
        self.sl=spider_login.login_zhihu()
        self.Parsers = html_parser_file.Html_parser()
        self.manager = URL_MANGER.Url_manager()
    '''爬虫总调度函数'''
    def craw(self,url):
        self.sl.login()#登录知乎
        content = self.sl.request(url)#访问网页
        question_urls = self.Parsers.parse(url,content)#提取知乎主页问题url
        self.manager.add_new_url(question_urls)
        print question_urls
        while self.manager.get_len_new_url() !=0: #判断待爬取的URL集合中 URL的个数
            self.manager.add_new_url(question_urls)#将知乎主页问题URL添加到待爬取集合
            content1=self.sl.request(self.manager.get_new_url())#从待爬取URL集合中拿出一个url去访问
            question_urls =self.Parsers.get_new_url(content1)
            self.Parsers.get_new_text(content1)
            self.manager.add_new_url(question_urls)
if __name__=='__main__':
    url='https://www.zhihu.com/question/26198612'
    go = spider_main()
    go.craw(url)








