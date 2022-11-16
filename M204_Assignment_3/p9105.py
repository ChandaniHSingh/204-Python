'''
Q.9. Consider a very small dictionary that contains the translations of English words to Dutch as shown below:
english_dutch = {"last" : "laatst", "week" : "week", "the" : "de", "royal" : "koninklijk", "festival" : "feest", "hall" : "hal", "saw" : "zaag", "first" : "eerst", "performance" : "optreden", "of" : "van", "a" : "een", "new" : "nieuw", "symphony" : "symphonie", "by" : "bij", "one" : "een", "world" : "wereld", "leading" : "leidend", "modern" : "modern", "composer" : "componist", "composers" : "componisten", "two" : "twee", "shed" : "schuur", "sheds" : "schuren" }
Write a program that uses this dictionary to create a word-for-word translation of a sentence to be taken as an input from the user. A word for which you cannot find a translation, you can leave “as is.” The dictionary is supposed to be used case-insensitively, but your translation may consist of all lower-case words. It is nice if you leave punctuation in the translation, but if you take it out, that is acceptable (as leaving punctuation in is quite a bit of work and does not really have anything to do with dictionaries – besides, leaving punctuation in is much easier to do once you have learned about regular expressions).
'''
import re
str1 = input("Enter String : ")
str2 = ""
english_dutch = {"last" : "laatst", "week" : "week", "the" : "de", "royal" : "koninklijk",
"festival" : "feest", "hall" : "hal", "saw" : "zaag", "first" : "eerst", "performance" : "optreden",
"of" : "van", "a" : "een", "new" : "nieuw", "symphony" : "symphonie", "by" : "bij", "one" : "een",
"world" : "wereld", "leading" : "leidend", "modern" : "modern", "composer" : "componist",
"composers" : "componisten", "two" : "twee", "shed" : "schuur", "sheds" : "schuren" }


list1 = str1.lower().split(" ")

for i in list1:
    if(re.match('^[a-z]*[?,.!]$',i) is not None):
        temp = i[0:len(i)-1]
        if temp in english_dutch.keys():
            str2 += english_dutch[temp] + i[len(i)-1:len(i)] + " "
        else:
            str2 += temp + " "
    else:
        if i in english_dutch.keys():
            str2 += english_dutch[i] + " "
        else:
            str2 += i + " "
        

print("Input : ",str1)
print("Output : ",str2)


