# Mini-project report
Members: Ali Kathem  
Program: Network Security
Course: 1DV501 or 1DT901  
Date of submission: 2020-12-04
## Introduction
Projektet handlar om att arbeta med och analysera stora texter och utveckla två datastrukturer hash och binärt träd. Det första avsnittet förklarar vad som är definitionen av ett ord i vårt projekt. Andra avsnittet handlar om hur hash och binärt träd datastrukturer utvecklad.
## Part 1: Divide text into words
Ordet beskrivas som när bokstäver kopplas ihop och ge en mening medan när man vill identifiera ordet i programring den kallas String. String kan erkänna ord där har mellanslag både innan och efter ordet oberoende om det var ett riktigt ord eller inte. På grund av denna anledning används bibliotek som kan identifiera vilket språk den är och det finns metoder där kan också identifiera om text, tecken, eller tal. I den här projektet användas tre typ av metoder för identifiera ord. Metoden `isascii()` användes för identifiera ifall den typ av string och andre metod är `isalpha() `används för identifiera engelska bokstäver. För att kunna identifiera en hel maning must man kunna lösa problemet med taken tex (. Och , osv) så man fix det genom att använda `repleas()` metod som kopplat till string variabel där kan man tar bort de takan som kopplad till ordet. därefter, användas metoden `split()` dela varje ord enskilt.

I filen readtext.py, finns en metod kalls för read_file som lämna tillbaka en lista som innehåller bra ord. Ord är specificerade med ovan förklarade metoder. då resultat av `holy_grail.txt` och `eng_news_100K-sentences` är följande:

```
Words Number in holy_grail.txt:  6315
Words Number in eng_news_100K-sentences.txt:  1596247
```


## Part 2: Implementing data structures
`Hash`
Hash är en metod för data strukturer där för lätta och påskynda sökning genom att dela data till mindre  bucket och ta reda på resultat snabbare jämfört med vänligt list sökning.
En typ av dela data är genom att använda ascii table Unicode och sedan ta moduler på summen av ordet Unicode därefter lagras ordet på bucket som är lika moduler resultat.
`Hashoword` metod räkna hash av viss ord genom att använda `ord()` metoden som lämna tillbaka the Uncode av varja bokstav. Andra steg är att ta moduler av summa på närvarande antal bucket i listan.
Koden av hash:
```python
def Hashoword(word_set, word):
    sumWOrd = 0
    Hashoword = 0
    for i in word:
        sumWOrd += ord(i)
    Hashoword = sumWOrd % bucket_list_size(word_set)
    sumWOrd = 0
    return Hashoword
```
`add(word_set, word)` funktionen kommer att ta emot värja string/ord och ligga den i bucket lista om den finns inte redan och störa de med hash metoden som förklarade ovan. I projekten bestämmas att börja med 10 buckets och när den har 10 ord som är lika mycket som antal buckets, då antal buckets fördubblas och den process kalls för `rehash`. I processen av `rehash`, första kopias  resultat till en `templist`. Därefter fördubblas antal buckets i `original list`, efter fördubblings sker must ta bort gammal data i `original list` aftersom den distribueras med gammal hash räkning. Nästa steg kommer att kopira data från `templist` till `original list` fast distribueras med nya hash som räkna moduler med den nya antal av buckets i `original list`.
```python
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
```
Resultat som kommer från den här försök genom att använda den typen av `hash `och `rehash` visar att en del av resultaten skilja sig från den givna resultat i `word_set_main`. De resultatet som skilja sig är `to_string` metoden där ordning av ord är inte samma och `max_bucket` är 12 istället för 2 och denna beroende på använd hash typ ör inte lika.
```python
To_string(): { Ella Zoe Ola Fred Albin Ceve Jonas David Owen Amer Adam Fredrik Måns Morgan Simon  }
Count: 15
Contains(Fred): True
Contains(Bob): False
Max bucket: 12
Bucket list size: 20
Count: 11
```
Resultat av `holy_grail.txt`  max bucket är 533, och `eng_news_100K-sentences`  max bucket är


`BST based table`
Binär träd är en metod för datastrukture där för lätta och snabba upp sökning genom att dela data I pyramidal set. pyramidal delning genomföra att lägga mindre värde i vänster sida och största i höger sida.
`add(root, key, value)` funktion kommer att ta tree inmatning och root lista börja med bestämt struktur `[ None, None, None, None ]` där `key` lagras i första position, `value` i andra position, nya vänster node lista i tredje position och nya högre node lista i fjärde position.
1. root: är listan för att lagra data.
2. key: som skulle vara ord och lista sortera after.
3. value: är tal som kopplas till varja ord.
Första steg är att kolla upp om rooten är tomt och läga in rot `key och value `. Andra steg är att kolla upp nästa inmatning läger after på alfabetisk sortering inom att använda `compare(newChild, parentNode)`. `compare(newChild, parentNode)` jämföra den nya `key` med förälder `key` after vem som lägger först i alfabetisk order. tredje steg är att kolla om den närvarande förälder har en tömma väster sida, om det är sann då ett nytt node skapas för att lagra data på den nya barn, annars återkallelse den nästa nod i vänstra sidan. Ifall inmatning `key` är större än föräldra `key` då samma prossen jämföras men vi lägge noden i höger sida.
```python
def add(root, key, value):
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
```
`max_depth(node)` Först, skapas två variable ena för att räkna längsta rot-till-lövbanan i vänster sida och andra för höger sida. Sedan vi kolla vi kolla up om noden är inte tomt, och öka antal i båda vänster och höger sida. Därafter, användas rekursion funktion antigen om det finns nästa nod i vänster eller höger sida och genom att använda `countItem += max_depth(node[2]) `eller `countItem2 += max_depth(node[3]) ` då antal ökas beroende på vilken sida som återkallelse. Tillsist, den största värde lämnas tillbaka.
```python
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
```
Resultat som kommer från den här försök visar att den är lika med givna resultat i `table_main.py`.
```python
To_string:   (Adam, 27) (Ceve, 37) (Ella, 39) (Fred, 44) (Owen, 40) (Zoe, 41)
Get(Owen): 40
Get(Jonas): None
Size: 6
Max depth: 3
All pairs:  [('Adam', 27), ('Ceve', 37), ('Ella', 39), ('Fred', 44), ('Owen', 40), ('Zoe', 41)]
Size: 10
Max depth: 6
To_string:   (AA, 1) (AAA, 2) (AAAA, 3) (AAAAA, 4) (Adam, 27) (Ceve, 37) (Ella, 39) (Fred, 44) (Owen, 40) (Zoe, 41)
```
Resultat av `holy_grail.txt`  max depth är 294, och `eng_news_100K-sentences`  max bucket är
## Project conclusions and lessons learned

### Technical issues
Stora tekniska utmaningar var i BST när det gäller rekursion funktion och Global variabels. Det var svårt att hitta startpunkten och slutpunkten eftersom global variablers måste sätt igen till noll/None för den nästa återkalla. Ett andra problem var i word set var med rehash, där gick tillbaka till första listan och ta inte emot ändring.om projektet har mer tid då skulle försätta med uppgift 3 och 4, till och med förbättra hash.
### Project issues
I början var väldig svårt att har bra kommunikation p.g.a. all har inte lika erfarenhet med programmering samt hur man använda gitlab och koppla sitt arbete till web side. Distance kommunikation spelade en roll också för att man kund har rätt bestämmt tide för träffa. Till slut var att nårga som har redan börjat medan andre inte har kommit igång. Ett till problem att det var svårt att hitta all information från ett ställe, istället information var sprids på olike platser.