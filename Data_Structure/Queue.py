# Queue, First In First Out(FIFO)

class Queue():
	def __init__(self):
		self._queue = []	# implement with list
	def __str__(self):
		string = ['head: ']
		for e in self._queue:
			string.append(f'{e} <- ')
		string.append(' tail')
		return ''.join(string)
	
	def enqueue(self, val):
		self._queue.append(val)
	
	def dequeue(self):
		if self._queue:
			return self._queue.pop(0)
		else:
			print('There is no element in the queue')


queue = Queue()

queue.enqueue(10)
queue.enqueue(100)

print(queue)

queue.dequeue()

print(queue)
