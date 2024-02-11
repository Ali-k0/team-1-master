# A binary search based dictionary imlementation 
# only using list of length 4.

# Each node is a list of length four where positions
# 0 = key, 1 = value, 2 = left-child, 3 = right-child

 
# Creates and returns the root to a new empty table.
# The complete function is given and should not be changed.
def new_empty_root():
    return [None,None,None,None]


# Add a new key-value pair to table if the key doean't already exist.
# Update value if already key exists in the table.
def add(root, key, value):
    if root != [None, None, None, None]:
        if get(root, key) != None:
            return False
    if root == [None, None, None, None]:
        root[0] = key
        root[1] = value
    elif compare(key, root[0]) == True:
        if root[2] is None:
            node1 = new_empty_root()
            node1[0] = key
            node1[1] = value
            root[2] = node1
            # add(root[2], key, value)
        else:
            add(root[2], key, value)
    elif compare(key, root[0]) == False:
        if root[3] is None:
            node = new_empty_root()
            node[0] = key
            node[1] = value
            root[3] = node
        else:
            add(root[3], key, value)

def compare(newChild, parentNode):
    lista = []
    lista.append(newChild)
    lista.append(parentNode)
    lista.sort()
    if newChild == lista[0]:
        return True
    else:
        return False
# Returns a string representation of the table content.
# That is, all key-value pairs
strTree = ""
c1 = 0
def to_string(node):
    global strTree
    global c1
    if count(node) >= c1 or count(node) == 0:
        c1 = count(node)
        strTree = ""
    if (node[2] != None):
        to_string(node[2])
    strTree += " (" + node[0] + ", "+str(node[1])+")"
    if (node[3] != None):
        to_string(node[3])
    return strTree
# Returns the value for the given key. Returns None if key doesn't exists.
def get(node,key):
    if (key < node[0]):
        if(node[2] == None):
            return None
        else:
            return get(node[2], key)
    elif (key > node[0]):
        if (node[3] == None):
            return None
        else:
            return get(node[3], key)
    return node[1]

# Returns the maximum depth (an integer) of the tree.
# That is, the length of longest root-to-leaf path.
def max_depth(node):
    countItem = 0
    countItem2 = 0
    if(node[0] != None):
        countItem += 1
        countItem2 += 1
    if(node[2] != None):
        countItem += max_depth(node[2])
    if(node[3] != None):
        countItem2 += max_depth(node[3])
    if(countItem > countItem2):
        return countItem
    else:
        return countItem2
            

# Returns the number og key-value pairs currently stored in the table
def count(node):
    countItem = 0
    if(node[0] != None):
        countItem += 1
    if(node[2] != None):
        countItem += count(node[2])
    if(node[3] != None):
        countItem += count(node[3])
    return countItem

# Returns a list of all key-value pairs as tuples 
# sorted as left-to-right, in-order
listAllPairs = []
c2 = 0
def get_all_pairs(node):
    global listAllPairs
    global c2
    if count(node) >= c2 or count(node) == 0:
        c2 = count(node)
        listAllPairs = []
    if (node[2] != None):
        get_all_pairs(node[2])
    listAllPairs += (str(node[0]), node[1]),
    if (node[3] != None):
        get_all_pairs(node[3])
    return listAllPairs


