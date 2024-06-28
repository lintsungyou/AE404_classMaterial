import random
import threading
import time

TOTAL_POINTS = 50000000
RADIUS = 100000


def monteCarloPi(tatalPoints, pt):
	xs = []
	ys = []

	for i in range(tatalPoints):
		xs.append(random.randint(0, RADIUS))
		ys.append(random.randint(0, RADIUS))

	#print("addPt: " + str(xs[i]) + ", " + str(ys[i]))

	for i in range(tatalPoints):
		if(xs[i]*xs[i] + ys[i]*ys[i]) < RADIUS*RADIUS:
		#print("Pt: " + str(xs[i]) + ", " + str(ys[i]))
		#print(str(xs[i]*xs[i] + ys[i]*ys[i]))
			pt[0] = pt[0] + 1

	return pt


def main():

	p1 = [0]
	p2 = [0]
	p3 = [0]
	p4 = [0]
	
	start = time.time()
	ret = monteCarloPi(int(TOTAL_POINTS), p4)
	end = time.time()
	print("single:" + str(end - start))
	p4[0] = 0

	#Step 3: 創建另外三個thread(t1, t2, t3), 並將 MonteCarloPi 函式當作target, 並將int(TOTAL_POINTS/4), p1~p3當作arguments.
	
	start = time.time()
	
	#Step4: t1~t3 start thread.
	
	
	#Step5: main thread 計算剩下的部分
	
	
	#Step6: t1~t3 join
	
	#Step7: 利用main thread 和 t1~t3 所計算出的扇形內的點代表扇形面積，全部的點代表正方形面積，並計算出PI 的估計值
	
	print("pi: " + str(monteCarloPI))
    
	end = time.time()
	print("multi:" + str(end - start))

if __name__ == '__main__':
    main()  # next section explains the use of sys.exit


   monteCarloPi(int(TOTAL_POINTS/4), p1)