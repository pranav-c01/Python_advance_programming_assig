# problem 2
def encrypt(word):
    temp = word
    word = word[::-1]
    trans = {"a":0,"e":1,"i":2,"o":3,"u":4}
    temp_word = ""
    for x in word:
        if x in trans.keys():
            temp_word += str(trans[x])
        else:
            temp_word += x
    temp_word += "aca"
    return temp_word
print(encrypt("alpaca"),encrypt("banana"))


# problem 5
from collections import Counter
def pluralize(list1):
  counts = Counter(list1)
  final_dict = set()
  for x in counts.keys():
     if counts[x] > 1:
        final_dict.add(f"{x}s")
     else:
        final_dict.add(x)
  return final_dict
print(pluralize(["cow","pig", "cow", "cow"]))  
       
        
