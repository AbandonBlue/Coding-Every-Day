# First In Last Out(FILO)

class Stack():
	def __init__(self):
		self._stack = [] # implement with list
	def push(self, val):
		self._stack.append(val)
		return val

	def pop(self):
		if self._stack:
			return self._stack.pop()
		return None
	
	def peep(self):
		if self._stack:
			return self._stack[-1]
		
	def __str__(self):
		string = ['|']
		for e in self._stack:
			string.append(str(e))
			string.append('|')
		string.pop()
		return ''.join(string)
	
	def __len__(self):
		return len(self._stack)
	
	
stack = Stack()
stack.push(10)
stack.push(12)
stack.push(14)

print(stack)

stack.pop()

print(stack)
print(len(stack))