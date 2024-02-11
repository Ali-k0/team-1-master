import table as tbl
import readtext
import operator
import os
d = {"Ella": 39, "Owen": 40, "Fred": 44, "Zoe": 41,
     "Adam": 27, "Ceve": 37,  "Adam": 27, "Ceve": 37}
root = tbl.new_empty_root()
for k, v in d.items():
    tbl.add(root, k, v)

# { (Adam,27) (Ceve,37) (Ella,39) (Fred,44) (Owen,40) (Zoe,41) }
print("To_string: ", tbl.to_string(root))
print("Get(Owen):", tbl.get(root, "Owen"))    # 40
print("Get(Jonas):", tbl.get(root, "Jonas"))  # None
print("Size:", tbl.count(root))               # 6
print("Max depth:", tbl.max_depth(root))     # 3
pairs = tbl.get_all_pairs(root)
# [('Adam', 27), ('Ceve', 37), ('Ella', 39), ('Fred', 44), ('Owen', 40), ('Zoe', 41)]
print("All pairs: ", pairs)
tbl.add(root, "AA", 1)
tbl.add(root, "AAA", 2)
tbl.add(root, "AAAA", 3)
tbl.add(root, "AAAAA", 4)
print("Size:", tbl.count(root))              # 10
print("Max depth:", tbl.max_depth(root))    # 6
# { (AA,1) (AAA,2) (AAAA,3) (AAAAA,4) (Adam,27) (Ceve,37) (Ella,39) (Fred,44) (Owen,40) (Zoe,41) }
print("To_string: ", tbl.to_string(root))
newAdd = readtext.read_file(
    os.getcwd()+"/code_skeletons/large_texts.txt/holy_grail.txt")
newAdd2 = readtext.read_file(
    os.getcwd()+"/code_skeletons/large_texts.txt/eng_news_100K-sentences.txt")
root2 = tbl.new_empty_root()
for i in newAdd:
    tbl.add(root2, i, 0)
print("Max depth holy_grail:", tbl.max_depth(root2))
root3 = tbl.new_empty_root()
for i in newAdd2:
    tbl.add(root3, i, 0)
print("Max depth eng_news_100K-sentences:", tbl.max_depth(root3))


# print(root2)
def getpairs(Words):
    for i in Words:
        tbl.add(root2, i, 0)
    p2 = tbl.get_all_pairs(root2)
    return p2
def task2(Wordstask2):
    p2 = getpairs(Wordstask2)
    count = 0
    for i, k in p2:
        if len(i) == 5:
            count+=1
    return count

print("== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ===")

print("task 3 part 2 holy_grail: ", task2(newAdd))
print("task 3 part 2 eng_news_100K-sentences: ", task2(newAdd2))
"""
def task3(Wordstask3):
    p2 = getpairs(Wordstask3)
    listdic = {}
    for i, k in p2:
        if len(i) > 4:
            listdic[i] = listdic.get(i, 0) + 1
    sortWords = sorted(listdic.items(), key=operator.itemgetter(1))
    print("task 3 part 3: ")
    count = 0
    for k, v in sortWords:  # itrerera över varja nyckle och värde
        count += 1
        if count > len(sortWords)-10:
            print(k, " | ", (int(v)*"*"), v, end="\n")
print("== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ===")
setlist = set(task2(newAdd))
print("task 3 part 2: ", len(setlist))
task3(newAdd)
print("== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ===")
setlist2 = set(task2(newAdd2))
print("task 3 part 2: ", len(setlist2))
task3(newAdd2)

"""



   
