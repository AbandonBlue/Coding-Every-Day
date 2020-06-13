# LinkedList

class Node():
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList():
	def __init__(self, head):
		self.head = head
		temp = self.head
		while temp.next:
			temp = temp.next
		self.last = temp
	
	
	def insert_first(self, node):
		node.next = self.head
		self.head = node
	
	
	def insert_last(self, node):
		self.last.next = node
		self.last = node
	
	
	def del_first(self):
		self.head = self.head.next
		
	
	def del_last(self):
		pass
		
	
	def to_list(self):
		result = []
		temp = self.head
		while temp:
			result.append(temp.val)
			temp = temp.next
		return result


linkedlist = LinkedList(Node(1))

linkedlist.insert_last(Node(2))
print(linkedlist.to_list())     # [1, 2]

linkedlist.insert_first(Node(0))
print(linkedlist.to_list())     # [0, 1, 2]

linkedlist.del_first()
print(linkedlist.to_list())     # [1, 2]
	