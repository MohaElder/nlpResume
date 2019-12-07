# encoding:utf-8
import requests 
from aip import AipNlp
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '17925688'
API_KEY = 'Ra8Mg2MLx2a8E9hs6BKrBp3D'
SECRET_KEY = 'VPeAIciWGBEqQcXs1lDNdY5rdubRoBaG'

clientOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
clientNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1575441285116&di=54ac097a7c11ff5c211ad13d788211a4&imgtype=0&src=http%3A%2F%2Fphotocdn.sohu.com%2F20131025%2FImg388882088.jpg"
""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """
text = clientOcr.basicGeneralUrl(url, options)
print(text)

""" 调用词法分析 """


#print(clientNlp.lexer(text))
