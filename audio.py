
#尝试获取单词返回页面
import requests
import re
import os
from user_agent import generate_user_agent
things = input()
url = "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/word:{}".format(things)
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
r = requests.get(url,headers=headers,timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding
#尝试获取音频的url
try:
    wordRegex = re.compile(r'(\d*)_1_1_')
    wordNumber = wordRegex.search(r.text).group(1)
    maleAudioUrl = "http://www.gavo.t.u-tokyo.ac.jp/ojad/sound4/mp3/male/{:0>3d}/{}_1_1_male.mp3?20121005".format(int(wordNumber)//100,int(wordNumber))
    femaleAudioUrl = "http://www.gavo.t.u-tokyo.ac.jp/ojad/sound4/mp3/female/{:0>3d}/{}_1_1_female.mp3?20121005".format(int(wordNumber)//100,int(wordNumber))
    print("downloading...")
except:
    print("すみません")
#尝试下载音频并改名
root = "/Users/zhugeshuai/Desktop/"
male_path = "/Users/zhugeshuai/Desktop/{}_male.mp3".format(things)
female_path = "/Users/zhugeshuai/Desktop/{}_female.mp3".format(things)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(male_path):
        male = requests.get(maleAudioUrl)
        female = requests.get(femaleAudioUrl)
        with open(male_path,'wb') as b:
            b.write(male.content)
            print("男声音频保存成功")
        with open(female_path,'wb') as g:
            g.write(female.content)
            print("女声音频保存成功")
        
except:
    print("オーディオがない")
