
import re
s = "His name is Harry and his phone game num is videogames 9848022338"
# print(len(re.findall(r'a',s)))
# print(re.findall(r'[hH]is',s))
print(re.search(r'is',s))
print(re.match(r'is',s))
print(re.search(r'phone',s))
print(re.match(r'phone',s))

print(re.split(r'is',s))
print(re.split(r'phone',s))
print(re.split(r' ',s))
print(len(re.split(r' ',s)))
new_s = re.sub(r'e',"a", s)

print(s)
print(new_s)

# print(re.search(r'phone',s))
# print(re.search(r'8$',s))

l  = ["Orange", "Grape","Papaya", "Pink", "Apple", "Spark"]

# for i in l:
#   print(i)
words_ending_with_e = [] # Orange, GRape. Apple
words_ending_with_k = [] # Spark
words_starting_with_P = [] # Papaya, Pink
for i in l:
  if re.search(r'e$',i):
    words_ending_with_e.append(i)
  elif re.search(r'^P',i):
    words_starting_with_P.append(i)
  elif re.search(r'k$',i):
    words_ending_with_k.append(i)
  
print(words_ending_with_e)
print(words_ending_with_k)
print(words_starting_with_P)

l  = ["Orange", "Grape","Papaya9", "Pink", "Apple8", "Spark"]
for i in l:
  print(re.search(r'\d\Z',i))

