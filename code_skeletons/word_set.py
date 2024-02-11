# A list based hash table implementation for strings.
# Initial bucket size is 10, we the double the bucket size
# when nElements = bucketSize.

size = 0      # global variable, current number of elements

# Returns a new empty set
# The complete function is given and should not be changed.
def new_empty_set():
    global size
    size = 0
    buckets = []
    for i in range(10):
        buckets.append([])
    return buckets


# Adds word to word set if not already added
def add(word_set, word):
    countNum = 0
    if (contains(word_set, word) != True):
        Hasho = Hashoword(word_set, word)
        word_set[Hasho].append(word)
    if count(word_set) == bucket_list_size(word_set):
        old_list = []
        for i in word_set:
            old_list.append([])
            for n in i:
                old_list[countNum].append(n)
            countNum += 1
        for expend in range(bucket_list_size(word_set)*2-bucket_list_size(word_set)):
            word_set.append([])
        for i in old_list:
            for n in i:
                try:
                    oldhash = Hashoword(old_list, n)
                    word_set[oldhash].remove(n)
                except:
                    pass
                add(word_set, n)
        


def Hashoword(word_set, word):
    sumWOrd = 0
    Hashoword = 0
    for i in word:
        sumWOrd += ord(i)
    Hashoword = sumWOrd % bucket_list_size(word_set)
    sumWOrd = 0
    
    return Hashoword

# Returns current number of elements in set
def count(word_set):
    count = 0
    for i in word_set:
        for n in i:
            count += 1
    return count
# Returns current size of bucket list
def bucket_list_size(word_set):
    global size
    size = len(word_set)
    return len(word_set)

# Returns a string representation of the set content
def to_string(word_set):
    str1=""
    for i in word_set:
        for inner in i :
            str1 += inner+" "
    return "{"+str1+"}"
# Returns True if word in set, otherwise False    
def contains(word_set, word):
    NumHasg = Hashoword(word_set, word)
    try:
        word_set[NumHasg].index(word)
        return True
    except:
        return False

# Removes word from set if there, does nothing 
# if word not in set
def remove(word_set, word):
    if contains(word_set, word)== True:
        getHash= Hashoword(word_set,word)
        word_set[getHash].remove(word)
    else:
        pass
# Returns the size of the bucket with most elements
def max_bucket_size(word_set):
    count = 0
    mxNum = 0
    mxbucket = 0
    for i in word_set:
        print(i)
        mxbucket += 1
        if len(i) > count:
            count = len(i)
            mxNum = len(i)
    return mxNum




    


