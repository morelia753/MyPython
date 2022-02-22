import pygame
import time
def puton_music():
    file = r'C:\CloudMusic\房东的猫 - 所念皆星河.mp3'  # 音乐路径
    pygame.mixer.init()  # 初始化
    track = pygame.mixer.music.load(file)  # 加载音乐文件
    pygame.mixer.music.play(start=0.0)  # 开始播放音乐
    time.sleep(300)
    pygame.mixer.music.stop()
puton_music()