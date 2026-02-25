# PYTHON SET:

# 1...Find common element between two lists using set.
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
common=set(list1) & set(list2)
print(common)

# #2...Remove duplicate words from a sentence using set
sentence = "this is a test sentence with duplicate words"
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Words:", words)

#3...check if two strings are anagrams using sets and logic 
a=input("Enter first string: ")
b=input("Enter second string: ")
if sorted(a) == sorted(b):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


#4...find elements present in first list but not in second list
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
diff=set(list1)-set(list2)
print("Elements present in first list but not in second:", diff)

#5...check if all character in a string are unique using set
s = input("Enter a string: ")
if len(s) == len(set(s)):
    print("All characters in the string are unique.")
else:
    print("Some characters in the string are repeated.")


# 6...count number of distinct elements in a list using set
list1=[1,2,3,3,2,1]
distinct=len(set(list1))
print("Number of distinct elements:",distinct)


#7...find symetric difference between two sets without built in methods.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
sym = set()
for item in set1:
    if item not in set2:
        sym.add(item)
for item in set2:
    if item not in set1:
        sym.add(item)
print("Symmetric difference:", sym)


#8...remove common characters from two string using set
s1 = input("Enter first string: ") 
s2 = input("Enter second string: ")
common = set(s1) & set(s2)
result = ""
for ch in s1:
    if ch not in common:
        result += ch
print("String after removing common characters:", result)


#9... check if one set is a subset of another without buit in function
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

subset = True

for element in set1:
    if element not in set2:
        subset = False
        break

if subset:
    print("Set1 is a subset of Set2")
else:
    print("Set1 is NOT a subset of Set2")

# 10...find repeated elements in a list useing set
numbers = [1, 2, 3, 2, 4]
seen = set()
repeated = set()
for num in numbers:
    if num in seen:
        repeated.add(num)
    else:
        seen.add(num)
print("Repeated elements:", repeated)