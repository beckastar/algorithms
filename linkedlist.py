class Node():
	def __init__(self,data):

		self.data = data
		self.next = None
"""
	def __repr__(self):
		return "Node(%r, %r)" %(self.data, self.next)
"""

class LinkedList():
	def __init__(self):
		self.head = None
	"""
	def __repr__(self):
		return "List(%r)"%(self.head)
	"""
	def AddNodes(self, new_node):
		if self.head == None:
			self.head = new_node
		# elif self.head.next is None:
		#	self.head.next = new_node
		else:
			node = self.head
			while node.next:
				node = node.next
			node.next = new_node
	def RemoveNodes(self, node):
		if node.next == node:
			return
		if node.next.next:
			node.next = node.next.next

	def printall(self):
		print "this is head %r" %(self.head.data)
		node = self.head
		while node.next.data != self.head.data:	
			print node.next.data , self.head.data		
			print "this is node %s" %(node.data)
			node = node.next

	def MakeCircle(self):
		node = self.head
		while node.next != None:
			node = node.next
		node.next = self.head





chaircircle = LinkedList()
for i in range(101):
	node = Node(i)
	chaircircle.AddNodes(node)
chaircircle.MakeCircle()
#chaircircle.printall()


node = chaircircle.head

while node.next != node:
	chaircircle.RemoveNodes(node.next)
	node = node.next

chaircircle.head = node
chaircircle.printall()






"""
 
ll = LinkedList()
three = Node(3)
two = Node(2)
one = Node(1)

print one 

ll.AddNodes(three)
ll.AddNodes(two)
ll.AddNodes(one)

ll.printall()
#repr method for ll doesn't seem to work 
 
"""







