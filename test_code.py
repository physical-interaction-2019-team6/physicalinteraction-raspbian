
#coding: utf-8
import wave
import sys, os
import numpy as np
import matplotlib.pyplot as plt
import glob
from tqdm import tqdm

CROP_MS     = 1000  #クロップする範囲(ms)
OVERRAP_MS  = 500   #クロップ時に重ねる範囲(ms)
DIVISION    = 150   #ペリオドグラムの時間分割数
PERIODOGRAM_SIZE = [28,28]  #ペリオドグラムのプーリング後サイズ


"""
    waveファイルを読み込む
"""
def _read_wave(file_name):
    try:
        wave_file = wave.open(file_name,"r") #Open
    except IOError as e:
        print("[ERROR] "+file_name+" is not found.")
        exit()
    return wave_file

def read(file_name):
    """読み込み作業"""
    wave_file = _read_wave(file_name)

    print("-----------------------------------------------------")
    print("FILE NAME            : ", file_name)
    #print("NONOLAL(1)/STEREO(2) : ", wave_file.getnchannels())  #モノラルorステレオ
    #print("BYTE 2(16bit)3(24bit): ", wave_file.getsampwidth())  #１サンプルあたりのバイト数
    #print("SAMPLING RATE(khz)   : ", wave_file.getframerate())  #サンプリング周波数
    #print("FLAME NUMBER         : ", wave_file.getnframes())    #フレームの総数

    """numpy形式に変換"""
    wave_flames  = wave_file.readframes(wave_file.getnframes())  #waveファイルのframeを読み込み
    wave_buffers = np.frombuffer(wave_flames, dtype= "int16")    #waveファイルをnumpy.arrayに変換
    print("WAVE BUFFER SIZE      : ", wave_buffers.shape)

    """一次元のnumpy形式で出力"""
    if wave_file.getnchannels() == 2:
        #サラウンド（2チャンネル）の場合
        l_buffers = wave_buffers[::wave_file.getnchannels()]
        r_buffers = wave_buffers[1::wave_file.getnchannels()]
        #DEBUG: 読み込んだwaveの全体波形
        #plt.plot(l_buffers)
        #plt.show()
        return l_buffers, wave_file.getframerate()
    return buffers, wave_file.getframerate()
