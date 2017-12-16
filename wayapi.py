import argparse as arg
import bs4
import urllib.request
def sumdef(user,passwd,mobile,text):
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)
    urllib.request.install_opener(opener)
    url = "http://site24.way2sms.com/content/Login1.action"
    payload = {
        'username': user,
        'password': passwd
    }
    data = urllib.parse.urlencode(payload).encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    contents = resp.read()
    token = ""
    soup = bs4.BeautifulSoup(contents, 'html.parser')
    for token in soup.find_all('input'):
        Token = token.get('id')
        if Token == "Token":
            break
    key = token.get('value')
    url = "http://site24.way2sms.com/smstoss.action"
    payload = {
        'Token': key,
        'mobile': mobile,
        'message': text
    }
    data = urllib.parse.urlencode(payload).encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    cont = resp.read()
    soup = bs4.BeautifulSoup(cont, 'html.parser')
    flg = 0
    for span in soup.find_all('span'):
        if span.text == "Message has been submitted successfully.":
            flg = 1
            break
        else:
            flg = 0
    if flg is 1:
        print("Message has been submitted successfully..")
    else:
        print("Something missing..")

parser = arg.ArgumentParser(description='Gopani Developers')

parser.add_argument('username',metavar="username", type=str,help="set username")
parser.add_argument('-u', dest='way2', action='store_const', const=sumdef, default=max,help='enter username')
parser.add_argument('password',metavar="password",help="set Your password")
parser.add_argument('-p',dest='way2', action='store_const',const=sumdef, help="Enter your password")
parser.add_argument('mobile',metavar="mobi", type=str,help="set reeciver mobile number")
parser.add_argument('-mo', dest='way2', action='store_const', const=sumdef, default=max,help='enter mobile number')
parser.add_argument('msg',metavar="msg",help="set Your text message")
parser.add_argument('-msg',dest='way2', action='store_const',const=sumdef, help="\"Enter your message\"")
args = parser.parse_args()
args.way2(args.username,args.password,args.mobile,args.msg)