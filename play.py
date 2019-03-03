import time
import pygame
import os,sys
import eyed3


print (os.path.abspath('music'))
lu = os.path.abspath('music')
###加r换成普通的字符串
file = lu + r'/a.mp3'
print (file)

xx = eyed3.load(file)
a = xx.info.time_secs 
print(u'时长为：{}秒'.format(xx.info.time_secs))
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)
#
pygame.mixer.music.play()
time.sleep(a)
pygame.mixer.music.stop()
