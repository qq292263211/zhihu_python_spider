#_*_coding:utf-8_*_
import requests
import os
import json
import time
from bs4 import BeautifulSoup
class login_zhihu(object):
    def login(self):
        global proxies
        # proxies = {'http': 'http:/122.5.243.116'}
        url = 'http://www.zhihu.com'
        loginURL = 'https://www.zhihu.com/login/phone_num'
        global headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
            'Referer': 'https://www.zhihu.com/',
            'Host': 'www.zhihu.com'
        }
        data = {
            'phone_num': '13450483344',
            'password': '292263211',
            'rememberme': 'ture'
        }
        global s
        s = requests.session()
        global xsrf
        if os.path.exists('cookiefile'):
            with open('cookiefile') as f:
                cookie = json.load(f)
            s.cookies.update(cookie)
            req1 = s.get(url, headers=headers)
            soup = BeautifulSoup(req1.text, 'html.parser')
            xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
            with open('zhihu.html', 'w') as f:
                f.write(req1.content)
        else:
            req = s.get(url, headers=headers)
            print req
            soup = BeautifulSoup(req.text, 'html.parser')
            xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
            data['_xsrf'] = xsrf
            timestamp = int(time.time() * 1000)
            captchaURL = 'http://www.zhihu.com/captcha.gif?=' + str(timestamp)
            print captchaURL
            with open('zhihucaptcha.gif', 'w') as f:
                captchaREQ = s.get(captchaURL, headers=headers)
                f.write(captchaREQ.content)
            loginCaptcha = raw_input('input captcha:\n').strip()
            data['captcha'] = loginCaptcha
            print data
            loginREQ = s.post(loginURL, headers=headers, data=data)
            if not loginREQ.json()['r']:
                print s.cookies.get_dict()
                with open('cookiefile', 'wb') as f:
                    json.dump(s.cookies.get_dict(), f)
            else:
                print 'login fail'

    def request(self,url):
        content = s.get(url,headers=headers)
        return content
































