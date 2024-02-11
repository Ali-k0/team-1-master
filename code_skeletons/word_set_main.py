import word_set as ws
import readtext
import os
# Program starts    

names = ["Ella", "Owen", "Fred", "Zoe", "Adam", "Ceve", "Adam", "Ceve", "Jonas", "Ola", "Morgan", "Fredrik", "Simon", "Albin", "Måns", "Amer", "David"]

word_set = ws.new_empty_set()
for s in names:
    ws.add(word_set,s)

print("To_string():", ws.to_string(word_set) )  # { Owen Fred Amer Albin Måns Ola Ceve Jonas Fredrik Adam Simon Zoe David Ella Morgan }
print("Count:", ws.count(word_set))             # 15
print("Contains(Fred):", ws.contains(word_set,"Fred"))   # True
print("Contains(Bob):", ws.contains(word_set,"Bob"))     # False

# Hash specific data
mx = ws.max_bucket_size(word_set)
print("Max bucket:", mx)               # 2
buckets = ws.bucket_list_size(word_set) 
print("Bucket list size:", buckets)     # 20

# Remove elements
delete = ["Ceve", "Adam", "Ceve", "Jonas", "Ola"]
for s in delete:
    ws.remove(word_set,s)
print("\nCount:", ws.count(word_set))   # 11
print("To_string():", ws.to_string(word_set) ) # { Owen Fred Amer Albin Måns Fredrik Simon Zoe David Ella Morgan }


word_set2 = ws.new_empty_set()

newAdd =  readtext.read_file(os.getcwd()+"/code_skeletons/large_texts.txt/holy_grail.txt")
for i in newAdd:
    ws.add(word_set2, i)
print("\nCount holy_grail.txt:", ws.count(word_set2))
mx2 = ws.max_bucket_size(word_set2)
print("Max bucket:", mx2)               
newAdd2 =  readtext.read_file(os.getcwd()+"/code_skeletons/large_texts.txt/eng_news_100K-sentences.txt")

word_set3 = ws.new_empty_set()
for i in newAdd2:
    print(i)
    ws.add(word_set3, i)
print("\nCount eng_news_100K-sentences:", ws.count(word_set3))
mx3 = ws.max_bucket_size(word_set3)
print("Max bucket:", mx3)  
             