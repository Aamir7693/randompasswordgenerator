import random
#Program to generate random password
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
letter=[x for x in letters]
digits = '0123456789'
digit=[x for x in digits]
res=""
punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
punctuation=[x for x in punctuations]

Input=int(input("How many alphabets you want to enter"))
for i in range(Input):
    rand=random.randint(0,len(letter)-1)
    res+="".join(letter[rand])
Input=int(input("How many numbers you want"))
for i in range(Input):
    rand=random.randint(0,len(digit)-1)
    res+="".join(digit[rand])
Input = int(input("How many special characters you want"))
for i in range(Input):
    rand = random.randint(0, len(punctuation)-1)
    res += "".join(punctuation[rand])
res1=[x for x in res]
random.shuffle(res1)
res=""
for x in range(len(res1)):
    res+="".join(res1[x])
print(res)




