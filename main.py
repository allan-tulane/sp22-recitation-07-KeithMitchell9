import math, queue
from collections import Counter

class TreeNode(object):
  def __init__(self, left=None, right=None, data=None):
    self.left = left
    self.right = right
    self.data = data
  def __lt__(self, other):
    return(self.data < other.data)
  def children(self):
    return((self.left, self.right))

    
def get_frequencies(fname):
  f=open(fname, 'r')
  C = Counter()
  for l in f.readlines():
    C.update(Counter(l))
  return(dict(C.most_common()))


def make_huffman_tree(f):
  p = queue.PriorityQueue()

  for c in f.keys():
    p.put(TreeNode(None,None,(f[c], c)))

  while (p.qsize() > 1):
    x = p.get()
    y = p.get()
    z = x.data[0] + y.data[0]
    p.put(TreeNode(x, y, (z, "")))
        
  return p.get()


def get_code(node, prefix="", code={}):
  if (node.left!= None):
    get_code(node.left, prefix + '0', code)

  if (node.right !=None):
    get_code(node.right, prefix + '1', code)

  if (node.left==None and node.right ==None):
    code[node.data[1]] = prefix
  return code


def fixed_length_cost(f):
  n = len(f.keys())
  cost = math.ceil(math.log2(n))
  fixed = 0
  for i in f.values():
    fixed += cost * int(i)
  return fixed


def huffman_cost(C, f):
  huff = 0
  for i in f:
    huff += len(C[i]) * f[i]
  return huff

f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))