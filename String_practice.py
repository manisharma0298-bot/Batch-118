
#waf to remove last word from string
str1 = "This is python code in VS"
str2 = str1.split()
str3 = str2[:-1]
str4 = " ".join(str3)
print(str4)

#waf to count the vowels in a string
str1 = "This is python code in VS"
vowels = "aeiouAEIOU"
count = 0
for char in str1:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)

#waf to remove word if vowel is present in the word
str1="This is python code in VS"
str2=str1.split()
vowels="aeiouAEIOU"
str3=[]
for word in str2:
    if not any(char in vowels for char in word):
        str3.append(word)
str4=" ".join(str3)
print(str4)

#waf to counttotal whitespace in a string
str1="This is python code in VS"
count=0
for char in str1:
    if char.isspace():
        count +=1
print("Number of whitespace in the string:",count)


#waf to extract only number for string
str1="This is python code123 in VS version-35 adress noida-11096"
numbers=""
for char in str1:
    if char.isdigit():
        numbers +=char
print("Numbers in the string:",numbers)

#waf to remove all whitespace from string
str1 = "This is python code123 in VS version-35 adress noida-11096"
str2=str1.replace(",","")
str3=str2.replace(" ","")
print("String without whitespace:",str3)

#waf to print all special symbols
str1 = "This is python code@123 in VS version-35 add$ress noida-11096"
special_symbols=""
for char in str1:
    if not char.isalnum() and not char.isspace():
        special_symbols +=char
print("Special symbols in the string:",special_symbols) 

#7.Waf to reverse all words of string
str1 = "This is python code@123 in VS version-35 add$ress noida-11096"
str2 = str1.split()
str3 = str2[::-1]
str4 = " ".join(str3)
print("String with reversed words:",str4)



