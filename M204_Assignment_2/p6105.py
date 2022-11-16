'''
Q.6. Consider a list of characters (characters may be alphabets, special characters, digits). Write
a Python program to do the following:
1) Count total number of elements in the list
2) Count total number of vowels in the list (vowels are ‘a’, ‘e’, ‘i’, ‘o’, ‘u’)
3) Count total number of consonants in the list (a consonant is an alphabet other
than vowel)
4) Count total number of characters other than vowels and consonants
Display all the values with appropriate titles.
'''

def count(charList):
    print("Count : ",len(charList))

def countVowel(charList,vowels):
    count = 0
    for i in charList:
        if(i.isalpha()):
            if i in vowels:
                count += 1
    print("Count of Vowels : ",count)

def countConsonant(charList,vowels):
    count = 0
    for i in charList:
        if(i.isalpha()):
            if i not in vowels:
                count += 1
    print("Count of Consonants : ",count)

def countOther(charList):
    count = 0
    for i in charList:
        if(i.isalpha() == False):
            count += 1
    print("Count of Character other than vowels & Consonants : ",count)

vowels = ['A','a','E','e','I','i','O','o','U','u']          
charList = ['A','$','*','a','s','1','3','U','k']
count(charList)
countVowel(charList,vowels)
countConsonant(charList,vowels)
countOther(charList)
