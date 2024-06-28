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
	
	p4[0] = 0
	start = time.time()
	ret = monteCarloPi(int(TOTAL_POINTS), p4)

	end = time.time()

	print("single:" + str(end - start))

	
	p4[0] = 0
	t1 = threading.Thread(target = monteCarloPi, args = (int(TOTAL_POINTS/4), p1,))
	t2 = threading.Thread(target = monteCarloPi, args = (int(TOTAL_POINTS/4), p2,))
	t3 = threading.Thread(target = monteCarloPi, args = (int(TOTAL_POINTS/4), p3,))
	start = time.time()
	
	
	t1.start()
	t2.start()
	t3.start()
	

	ret = monteCarloPi(int(TOTAL_POINTS/4), p4)
	
	t1.join()
	t2.join()
	t3.join()
	
	monteCarloPI = float(p1[0] + p2[0] + p3[0] + p4[0])/TOTAL_POINTS * 4.0
	print("pi: " + str(monteCarloPI))
    
	end = time.time()
	print("multi:" + str(end - start))

if __name__ == '__main__':
    main()  # next section explains the use of sys.exit