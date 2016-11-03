from Student import Student
from Node import Node

class BST:
  def __init__(self):
    self._root = None
    self.count = 0

  def insert(self, item):
    if self._root is None:
      self._root = Node(item)
      return True
    if self.exists(item):
      print("exists")
      return False
    n = Node(item)
    self._root = self.insertR(n, self._root)
    return True

  def insertR(self, n, current):
    if current is None:
      current = n
    elif n.item < current.item:
      current.left = self.insertR(n, current.left)
    else:
      current.right = self.insertR(n, current.right)
    return current

  def exists(self, item, current=False):
    if current == False:
      current = self._root
    if current is None:
      return False
    elif item == current.item:
      return True
    elif item < current.item:
      return self.exists(item, current.left)
    elif item > current.item:
      return self.exists(item, current.right)
    # return self.retrieve(item)

  def traverse(self, cb, current=False):
    if current == False:
     current = self._root 
    if current is None:
      return
    self.traverse(cb, current.left)
    cb(current.item)
    self.traverse(cb, current.right)

  def size(self, count=0, current=False):
    if current == False:
      current = self._root
    if current is None:
      return count
    count = self.size(count, current.right)
    count = self.size(count, current.left)
    count += 1
    return count
  
  def retrieve(self, item, current=False):
    if current == False:
      current = self._root
    if current is None:
      return False
    elif item == current.item:
      return current.item
    elif item < current.item:
      return self.retrieve(item, current.left)
    elif item > current.item:
      return self.retrieve(item, current.right)

  def delete(self, item):
    if not self.exists(item):
      return False
    self._root = self.deleteR(item, self._root)
    return True

  def deleteR(self, item, current):
    if item < current.item:
      current.left = self.deleteR(item, current.left)
    elif item > current.item:
      current.right = self.deleteR(item, current.right)
    else:
      if not current.left and not current.right: # No children - Point parent to null
        current = None
      elif not current.left: # One right child - Point parent to child
        current = current.right
      elif not current.right: # One left child - Point parent to child
        current = current.left
      else: # Two children - Swap the values of parent and least successor, then delete least successor
        # Find in-order successor
        s = current.right
        while s.left:
          s = s.left
        current.item = s.item
        current.right = self.deleteR(s.item, current.right)
    return current
  
  def printTree(self):
    def printf(item):
      print(item.ssn)
    self.traverse(printf)
    print("")

def main():
  t = BST()
  t.insert(Student("George", "Anthony", 435287, "pategeorge12@gmail.com", 16))
  t.insert(Student("George", "Bradley", 835287, "pategeorge12@gmail.com", 32))
  t.insert(Student("igfvbtfv", "rtyujfd", 736234, "adkfj", 56))
  t.insert(Student("George", "Wesley", 903234, "pategeorge12@gmail.com", 17))
  t.insert(Student("George", "Dick", 234565, "pategeorge12@gmail.com", 15))

  t.printTree()

  print(t.retrieve(835287))
  t.delete(835287)

  t.printTree()

main()

