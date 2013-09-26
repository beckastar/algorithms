class Node():
	def __init__(self,data):

		self.data = data
		self.next = None
	def __repr__(self):
		return "Node(%r, %r)" %(self.data, self.next)

class LinkedList():
	def __init__(self):
		self.head = None

	def __repr__(self):
		return "List(%r)"%(self.head)

	def AddNodes(self, new_node):
		if self.head == None:
			self.head = new_node
		elif self.head.next is None:
			self.head.next = new_node
		else:
			node = self.head
			print node.next

			while node.next:
				# node = node.next
				if not node.next:
					print "adding new_node %d" % new_node.data 
					node.next = new_node
				else:
					node = node.next
	def printall(self):
		print "this is head %r" %(self.head)
		node = self.head
		while node.next:				
			print "this is node %r" %(node)
			node = node.next


	# def MakeCircle(self):
	# 	if node.next == None:
	# 		node.next = head



#node has no concept that it's in a list
# node only knows itself and the next node. 

 
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
 








