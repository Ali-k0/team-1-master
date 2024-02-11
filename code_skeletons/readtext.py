
import collections
import os


def read_file(file_path):
    wordlist = []
    x = []
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            for line in file:
                x = line.replace(', ', ' ').replace('. ', ' ').replace(
                    '] ', ' ').replace('[', ' ').replace(': ', ' ').replace('! ', ' ').replace('? ', ' ').replace('\'', '').split(" ")
                for i in x:  # iterera över all karaktär
                    if i.isalpha() and i.isascii():  # kontrollera om det är en engelska bokstav
                        # omvandla all till små bokstav
                        wordlist.append(i)
    except IOError as e:  # koden är hämtad från förläsningar
        print(type(e), "==>", e)
        print("No such file: ", file_path)
    return wordlist


newAdd = read_file(
    os.getcwd()+"/code_skeletons/large_texts.txt/holy_grail.txt")
newAdd2 = read_file(
    os.getcwd()+"/code_skeletons/large_texts.txt/eng_news_100K-sentences.txt")

# newAdd = readtext.read_file(os.getcwd()+"/code_skeletons/large_texts.txt/eng_news_100K-sentences.

count = 0
for i in newAdd:
    count += 1
print("Words Number in holy_grail.txt: ", count)

count2 = 0
for i in newAdd2:
    count += 1
print("Words Number in eng_news_100K-sentences.txt: ", count)
print("== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ===")
