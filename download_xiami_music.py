#! python3

import subprocess
import os

# 切换到工作目录
os.chdir('/Users/test/Documents/myproject/music/')
# 读保存在本地的歌曲信息
with open('test', encoding='utf-8') as f:
    text = f.read()
# 将读取的内容转换成字典格式时，如果提示“false”、“true”没定义，就申明全局变量
globals = {'false': 0, 'true': 0}

# 提取歌曲信息，列表格式，列表元素为字典
songs = eval(text, globals)['data']['data']['songs']

# 循环列表，下载歌曲
for i in range(0, len(songs)):
    try:
        # 下载品质，默认下载无损品质，如果没有无损，则下载高清品质
        quality = songs[i]['listenFiles'][0]['quality']
        if quality != 's':
            quality = songs[i]['listenFiles'][3]['quality']
            listenFile = songs[i]['listenFiles'][3]['listenFile']
            fileSize = songs[i]['listenFiles'][3]['fileSize']
            format = songs[i]['listenFiles'][3]['format']
        else:
            # 下载地址
            listenFile = songs[i]['listenFiles'][0]['listenFile']
            fileSize = songs[i]['listenFiles'][0]['fileSize']
            format = songs[i]['listenFiles'][0]['format']

        # 歌曲名称
        songName = songs[i]['songName'] + '.' + format

        # 执行命令
        cmd = 'ffmpeg -i ' + '"' + listenFile + '"' + ' "' + songName + '"'

        # 调用ffmpeg下载歌曲到本地
        subprocess.call(cmd, shell=True)
        
        print(songName)
        print(quality)
        print(listenFile)
        print(fileSize)
    except:
        continue

     
