from lib.Grid import Grid, Moves
from lib.AI import AI
import sys
import math
import random
import time


MAP_FILE_NAME = "MAPFILE.txt"
STEPS_FILE_NAME = "steps.txt"
UP_DOWN_SCORE_HIGHER = True
LEFT_RIGHT_SCORE_HIGHER = False
N_GAMES = 500

DEBUG=False


def readMap():

	currentMap = []
	
	fReadMap = open(MAP_FILE_NAME, "r")
	lines = fReadMap.readlines()
	

	for line in lines:
		currentMap.append(line.split('\t'))
	id = 0
	for line in currentMap:
		print('row=' + str(id))
		strTemp = ""
		for item in line:
			strTemp = strTemp + "\t" + item
		print(strTemp)
		id+=1


	return [[int(num) for num in row] for row in currentMap]

def moveMonteCarlo(_currentMap):
	if DEBUG:
		print(str(_currentMap))
	game = Grid(template=_currentMap)
	Ai = AI(multi_core=True)

	choice = Ai.next_move(game, N_GAMES)
	print("monteChoice" + str(choice))
	game.move(choice)

	print(game)	

	return choice


def writeStep(_monteCarloMove):
	f = open(STEPS_FILE_NAME, "a")
	
	if _monteCarloMove == Moves.UP:
		f.write('w')
	elif _monteCarloMove == Moves.DOWN:
		f.write('s')
	
	if _monteCarloMove == Moves.LEFT:
		f.write('a')
	elif _monteCarloMove == Moves.RIGHT:
		f.write('d')
	f.close()
	return


def sum_up_down(_currentMap):
	score_add = 0 
	for j in range(4):
		last_num = int(_currentMap[0][j])
		for i in range(1, 4):
			if last_num != 0 and int(_currentMap[i][j]) == last_num:
				score_add += last_num * 2
				last_num = -1 # prevent next comparison
			else:
				if int(_currentMap[i][j]) != 0:
					last_num = int(_currentMap[i][j])
	print("score add up_down:" + str(score_add))
	return score_add


def sum_left_right(_currentMap):
	score_add = 0 
	for i in range(4):
		last_num = int(_currentMap[i][0])
		for j in range(1, 4):
			if last_num != 0 and int(_currentMap[i][j]) == last_num:
				score_add += last_num * 2
				last_num = -1 # prevent next comparison
			else:
				if int(_currentMap[i][j]) != 0:
					last_num = int(_currentMap[i][j])
	print("score add left_right:" + str(score_add))
	return score_add



def main():
	#print("debug here")
	currentMap = readMap()
	start = time.time()
	choice = moveMonteCarlo(currentMap)
	end = time.time()
	print("MonteCarlo duration: " + str(end - start))
	writeStep(choice)


if __name__ == '__main__':
    main()
