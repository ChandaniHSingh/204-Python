'''
Q.4. Write a Python program to overload:
 the ‘+’ operator for the string as under:
The 2 strings should be merged in such a way that the result will contain characters
one by one first from the 1st string and then from the 2nd string as shown in the
example given below.
Str1=’VNSGU’
Str2=’SURAT’
Then Str1+Str2 = ‘VSNUSRGAUT’ (i.e. here characters in Italics are from Str1 and
rest from Str2)
 the <, <=, >, >= and == operators for the strings as under:
Compare sum of ACII values of all the characters in both the strings and then
compare the results. Return True if the sum for the 1st string is more than that for the
2nd string for the ‘>’ operator and False otherwise. Similarly do for other operators.
'''

class String1:
    def __init__(self,word):
        self.word = word
        

    def __add__(self,other):
        l1 = len(self.word)
        l2 = len(other.word)
        ans = ""
        i=0
        j=0
        while(i<l1)and(j<l2):
            ans += self.word[i]
            ans += other.word[j]
            i+=1
            j+=1
        while(i<l1):
            ans += self.word[i]
            i+=1
        while(j<l2):
            ans += other.word[j]
            j+=1

        return ans

    def __lt__(self,other):
        if self.acount < other.acount:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.acount > other.acount:
            return True
        else:
            return False

    def __le__(self,other):
        if self.acount <= other.acount:
            return True
        else:
            return False

    def __ge__(self,other):
        if self.acount >= other.acount:
            return True
        else:
            return False

    def _eq__(self,other):
        if self.acount == other.acount:
            return True
        else:
            return False

    

s1 = String1("VNSGU")
s2 = String1("Surat")

s1.acount = 0
for i in s1.word:
    s1.acount += ord(i)


s2.acount = 0
for i in s2.word:
    s2.acount += ord(i)

print("Sum : ",s1 + s2)
print("Greater Than : ",s1 > s2)
print("Less Than : ",s1 < s2)
print("Greater Than Or Equal To : ",s1 >= s2)
print("Less Than Or Equal To : ",s1 <= s2)
print("Equal To : ",s1 == s2)

