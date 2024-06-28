from multiprocessing import Process
from multiprocessing.managers import SharedMemoryManager
from multiprocessing import shared_memory
import random
import threading
import time


TOTAL_POINTS = 50000000
RADIUS = 100000


def monteCarloPi(tatalPoints, pilId, pilName):
	xs = []
	ys = []

	pt = 0

	for i in range(tatalPoints):
		xs.append(random.randint(0, RADIUS))
		ys.append(random.randint(0, RADIUS))

	#print("addPt: " + str(xs[i]) + ", " + str(ys[i]))

	for i in range(tatalPoints):
		if(xs[i]*xs[i] + ys[i]*ys[i]) < RADIUS*RADIUS:
		#print("Pt: " + str(xs[i]) + ", " + str(ys[i]))
		#print(str(xs[i]*xs[i] + ys[i]*ys[i]))
			pt = pt + 1
	if pilId >= 0:
		pil = shared_memory.ShareableList(name=pilName)
		pil[pilId] = pt
		pil.shm.close()
		pil.shm.unlink()

	return pt




def main():
	
	smm = SharedMemoryManager()
	smm.start()
	pil = smm.ShareableList([0, 0, 0, 0]) 


	
	start = time.time()
	ret = monteCarloPi(int(TOTAL_POINTS), -1, "none")

	end = time.time()

	print("single:" + str(end - start))
	
	
	
	p1 = Process(target = monteCarloPi, args = (int(TOTAL_POINTS/4), 1, pil.shm.name))
	p2 = Process(target = monteCarloPi, args = (int(TOTAL_POINTS/4), 2, pil.shm.name))
	p3 = Process(target = monteCarloPi, args = (int(TOTAL_POINTS/4), 3, pil.shm.name))
	start = time.time()
	
	
	p1.start()
	p2.start()
	p3.start()
	

	ret = monteCarloPi(int(TOTAL_POINTS/4), 0, pil.shm.name)
	
	p1.join()
	p2.join()
	p3.join()
	
	monteCarloPI = float(pil[0] + pil[1] + pil[2] + pil[3])/TOTAL_POINTS * 4.0
	print("pi: " + str(monteCarloPI))
	print("pi1~pi4:" + str(pil[0]) + "," + str(pil[0]) + "," + str(pil[0]) + "," + str(pil[0]))
    
	end = time.time()
	print("multi:" + str(end - start))

if __name__ == '__main__':
    main()  # next section explains the use of sys.exit