from multiprocessing import Process
import time

def func1():
  print 'func1: starting'
  for i in range(10,0,-1):
  	time.sleep(1)
  	print("1 : "+str(i))
  print 'func1: finishing'

def func2():
  print 'func2: starting'
  for i in range(10,0,-1):
  	time.sleep(1)
  	print("2 : "+str(i))
  print 'func2: finishing'

def func3(p1):
  time.sleep(5)
  p1.terminate()

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p3 = Process(target=func3,args=[p1])
  p3.start()
  p1.join()
  p2.join()
  p3.join()
