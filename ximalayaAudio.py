import requests
import re
import time
import os
# 获取目标网页的html
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
html = requests.get('https://www.ximalaya.com/waiyu/23797888/',headers=header)
# 获取节目标题并创建文件夹
reg2 = r'<h1 class="title lO_">(.*?)<'
title = re.search(reg2,html.text).group(1)
folder = os.path.exists(title)
if not folder:
    os.makedirs(title)
    print("已创建新文件夹")
else:
    print("There is this folder!")
# 获取每个音频id
reg = r'<a title="(.*?)" href="/waiyu/23797888/(\w*)"'
name_url = re.findall(reg,html.text)
# 获取音频地址并下载
count = 0
for lessonName,lessonid in name_url:
    audioId = "https://www.ximalaya.com/revision/play/v1/audio?id={}".format(str(lessonid)+"&ptype=1")
    html1 = requests.get(audioId,headers=header)
    reg1 = 'src":"(https:.*?m4a)'
    audioUrl = re.findall(reg1,html1.text) 
    ## 定位下载地址
    path = title+"/"+lessonName+'.m4a'
    ## 下载文件
    audioData = requests.get(audioUrl[0],headers=header)
    with open(path,'wb') as f:
        f.write(audioData.content)
        count = count + 1
        print('\r当前速度:{:.2f}%'.format(count*30/len(lessonid)),end=" ")
        time.sleep(1)
print('\n'+"全部下载完成,音频文件路径为在{}".format(os.getcwd()))