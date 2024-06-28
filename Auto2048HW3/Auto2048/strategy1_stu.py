import sys
import math
import random

MAP_FILE_NAME = "MAPFILE.txt"
STEPS_FILE_NAME = "steps.txt"
UP_DOWN_SCORE_HIGHER = True
LEFT_RIGHT_SCORE_HIGHER = False

def readMap():
	
	currentMap = []
	
	# TODO: 請撰寫從MAPFILE.txt 讀取 2048地圖與分數，並存進currentMap.
	# currentMap 是二維陣列
	# 第一行到第四行為 2048地圖，第五行為分數
	# 第一行到第四行每行有四個數字，每個數字之間用tab("\t")相隔


	#Step3-1: 開啟 MAP_FILE_NAME 這個名字的File, 模式為讀取模式，並且利用readlines() 將讀取的每列文字 存入lines中
	fReadMap = open(MAP_FILE_NAME, "r")
	lines = fReadMap.readlines()

	#Step3-2: 將lines中的每列利用split(<delimiter>) 函數分開，並且存入currentMap 中，分割字符(delimeter)請使用'\t'
	for line in lines:
		currentMap.append(line.split('\t'))

	#TODO done
	#下方可以印出你讀到的currentMap, 要使用以下功能，請開啟DEBUG_RECORD_PYOUTPUT
	for line in currentMap:
		print('row=' + str(id))
		strTemp = ""
		for item in line:
			strTemp = strTemp + "\t" + item
		print(strTemp)
		id+=1
	return currentMap



def writeStep(_score_higher):
	f = open(STEPS_FILE_NAME, "a")
	res = random.randint(0, 1) #隨機產生0或1並存入變數res中

	#TODO: 如果 _score_higher == UP_DOWN_SCORE_HIGHER, 代表上下移動會增加比較多的分數，
	#      就利用res 決定向上或向下移動。 else, 就代表左右移動會增加比較多的分數，
	#      就利用res 決定向左或向又移動


	f.close()
	return


def sum_up_down(_currentMap):
	score_add = 0
	# _currentMap 為現在2048的地圖，是個二為陣列有四個行和四個列, 存許方式_currentMap[i][j], 0<=i, j <=3
	# TODO 請計算向上向下移動可以增加的分數並存在score_add裡面

	return score_add


def sum_left_right(_currentMap):
	score_add = 0
	# _currentMap 為現在2048的地圖，是個二為陣列有四個行和四個列, 存許方式_currentMap[i][j], 0<=i, j <=3
	# TODO 請計算向左向右移動可以增加的分數並存在score_add裡面

	return score_add

def main():
	#print("debug here")
	currentMap = readMap()
	if sum_up_down(currentMap) > sum_left_right(currentMap):
		writeStep(UP_DOWN_SCORE_HIGHER)
	else:
		writeStep(LEFT_RIGHT_SCORE_HIGHER)


if __name__ == '__main__':
    main()
