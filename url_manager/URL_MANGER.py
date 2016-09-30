import sys
reload(sys)
sys.setdefaultencoding('utf8')
class Url_manager(object):
    def __init__(self):
        self.new_url= set()
        self.old_url = set()

    def add_new_url(self,urls):
        if urls is None:
            return
        for url in urls:
            if url not in self.new_url and url not in self.old_url:
                self.new_url.add(url)

    def get_len_new_url(self):
        return len(self.new_url)

    def get_new_url(self):
        new_url = self.new_url.pop()
        self.old_url.add(new_url)
        # print 'new_nrl',self.new_url,'\n,old_url_set',self.old_url
        return new_url