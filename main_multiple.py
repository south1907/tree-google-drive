# not use

from threading import Thread
import time

def runrequest(threadname, test):
	time.sleep(3)
	print(threadname + str(test))

	return test * 4

class ThreadWithReturnValue(Thread):
	def __init__(self, group=None, target=None, name=None,
				 args=(), kwargs={}, Verbose=None):
		Thread.__init__(self, group, target, name, args, kwargs)
		self._return = None
	def run(self):
		if self._target is not None:
			self._return = self._target(*self._args,
												**self._kwargs)
	def join(self, *args):
		Thread.join(self, *args)

	def getResult(self):
		return self._return


if __name__ == "__main__":

	list_thread = []
	number_thread = 10

	for i in range(number_thread):
		temp = ThreadWithReturnValue(target=runrequest, args=("Thread", i))
		temp.start()

		list_thread.append(temp)

	for mythread in list_thread:
		mythread.join()
		print(mythread.getResult())