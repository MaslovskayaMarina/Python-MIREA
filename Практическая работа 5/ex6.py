from hypothesis import given, strategies as st
from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule, precondition
import random


def add(x, y):
    return x + y

# Для чисел
@given(x=st.integers(), y=st.integers(), z=st.integers())
def test_add_num(x, y, z):
    print(x, y, z);
    assert add(x, y) == add(y, x) # Трудно доказать, легко проверить.
    assert add(x, add(y, z)) == add(add(x, y), z) # Трудно доказать, легко проверить.

    
test_add_num()

# Для строк
@given(x=st.text(), y=st.text(), z=st.text())
def test_add_str(x, y, z):
    print (x, y, z)
    assert add(x, y) == add(x, y)

    
test_add_str()

# Для списков
# Для строки
# Вернуть наиболее часто встречающийся элемент
def mode(data):
    return max(data, key=data.count)

@given(data=st.lists(st.integers(), min_size=1))
def test_mode(data):
    print(data)
    res = mode(data)
    # Трудно доказать, легко проверить
    assert res in data
    assert all(data.count(res) >= data.count(x) for x in data)
    

test_mode()


# Для словарей
@given (data=st.dictionaries(st.booleans(), st.integers(), min_size=2))
def clean_dicts(data):
    print(data)
    assert len(data) != 0
    assert isinstance(data[True], int) # Сложно доказать легко проверить
    data.clear()
    assert (len(data) == 0)

clean_dicts()


# Деревья
class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None
        return 0

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

@given(q=st.integers(), w=st.integers(), e=st.integers(), r=st.integers(), t=st.integers(), y=st.integers())
def testing_tree(q, w, e, r, t, y):
    tree = Tree()
    assert tree is not None
    tree.add(q)
    tree.add(w)
    tree.add(e)
    tree.add(r)
    tree.add(t)
    tree.add(y)
    tree.printTree()
    assert tree.deleteTree() == 0 # Трудно доказать, легко проверить
 

testing_tree()

#Графы
class Node:
  
    def __init__(self, data, indexloc = None):
        self.data = data
        self.index = indexloc
        
       
class Graph:
 
    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)
 
  
    def __init__(self, row, col, nodes = None):
        self.adj_mat = [[0] * col for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i
    def connect_dir(self, node1, node2, weight = 1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = weight
    def connect(self, node1, node2, weight = 1):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)
    def connections_from(self, node):
        node = self.get_index_from_node(node)
        return [(self.nodes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node])) if self.adj_mat[node][col_num] != 0]
    
    def connections_to(self, node):
      node = self.get_index_from_node(node)
      column = [row[node] for row in self.adj_mat]
      return [(self.nodes[row_num], column[row_num]) for row_num in range(len(column)) if column[row_num] != 0]
     
    def print_adj_mat(self):
      for row in self.adj_mat:
          print(row)
    
    def node(self, index):
      return self.nodes[index]
    
  
    def remove_conn(self, node1, node2):
      self.remove_conn_dir(node1, node2)
      self.remove_conn_dir(node2, node1)
   

    def remove_conn_dir(self, node1, node2):
      node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
      self.adj_mat[node1][node2] = 0   
  

    def can_traverse_dir(self, node1, node2):
      node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
      return self.adj_mat[node1][node2] != 0  
  
    def has_conn(self, node1, node2):
      return self.can_traverse_dir(node1, node2) or self.can_traverse_dir(node2, node1)
  
    def add_node(self,node):
      self.nodes.append(node)
      node.index = len(self.nodes) - 1
      for row in self.adj_mat:
        row.append(0)     
      self.adj_mat.append([0] * (len(self.adj_mat) + 1))
 

    def get_weight(self, n1, n2):
        node1, node2 = self.get_index_from_node(n1), self.get_index_from_node(n2)
        return self.adj_mat[node1][node2]
   
    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index


@given(q=st.integers(min_value = 0, max_value=1000), w=st.integers(min_value = 0, max_value=1000), e=st.integers(min_value = 0, max_value=1000), r=st.integers(min_value = 0, max_value=1000), t=st.integers(min_value = 0, max_value=1000), y=st.integers(min_value = 0, max_value=1000))
def testing_graph(q, w, e, r, t, y):
    a = Node(q)
    b = Node(w)
    c = Node(e)
    d = Node(r)
    e = Node(t)
    f = Node(y)
    testlist = [a, b, c, d, e, f]
    graph = Graph.create_from_nodes([a, b, c, d, e, f])
    assert graph is not None #Трудно доказать, легко проверить
    for i in range (10):
        x = random.choice(testlist)
        g = random.choice(testlist)
        if x != y:
            assert x != y #Трудно доказать, легко проверить
            graph.connect(x, g)
    assert graph is not None # Некоторые вещи не меняются
    assert testlist is not None # Некоторые вещи не меняются
    graph.print_adj_mat()
    del graph

testing_graph()

# Тестирование на основе модели
import shutil
import tempfile
from collections import defaultdict

import hypothesis.strategies as st
from hypothesis.database import DirectoryBasedExampleDatabase
from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule


class DatabaseComparison(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.tempd = tempfile.mkdtemp()
        self.database = DirectoryBasedExampleDatabase(self.tempd)
        self.model = defaultdict(set)

    keys = Bundle("keys")
    values = Bundle("values")

    @rule(target=keys, k=st.binary())
    def add_key(self, k):
        return k

    @rule(target=values, v=st.binary())
    def add_value(self, v):
        return v

    @rule(k=keys, v=values)
    def save(self, k, v):
        self.model[k].add(v)
        self.database.save(k, v)

    @rule(k=keys, v=values)
    def delete(self, k, v):
        self.model[k].discard(v)
        self.database.delete(k, v)

    @rule(k=keys)
    def values_agree(self, k):
        assert set(self.database.fetch(k)) == self.model[k]

    def teardown(self):
        shutil.rmtree(self.tempd)


TestDBComparison = DatabaseComparison.TestCase
