import pickle
from nltk.tokenize import word_tokenize as w
import numpy as np
from numpy.linalg import norm as no
print("Enter text to evaluate")
a=input()
print("Enter the number of neighbours")
n=int(input())
f=open('C:/Users/ayush/Desktop/Minor 2/GovilData/GovilData/anger.txt','r')
a0=f.readlines()
f=open('C:/Users/ayush/Desktop/Minor 2/GovilData/GovilData/anticipation.txt','r')
a1=f.readlines()
f=open('C:/Users/ayush/Desktop/Minor 2/GovilData/GovilData/disgust.txt','r')
a2=f.readlines()
f=open('C:/Users/ayush/Desktop/Minor 2/GovilData/GovilData/fear.txt','r')
a3=f.readlines()
f=open('C:/Users/ayush/Desktop/Minor 2/GovilData/GovilData/joy.txt','r')
a4=f.readlines()
f=open('C:/Users/ayush/Desktop/Minor 2/GovilData/GovilData/sadness.txt','r')
a5=f.readlines()
f=open('C:/Users/ayush/Desktop/Minor 2/GovilData/GovilData/surprise.txt','r')
a6=f.readlines()
f=open('C:/Users/ayush/Desktop/Minor 2/GovilData/GovilData/trust.txt','r')
a7=f.readlines()
f.close()
tmp=[0,0,0,0,0,0,0,0]
t=w(str(a))
for i in t:
    for j in range(8):
        if (i.lower()+'\n') in eval('a'+str(j)):
            tmp[j]=tmp[j]+1
f=open('lol1','rb') #vectors khud banaye he of the database
ques=pickle.load(f)
f=open('lol2','rb')# correspnding asli ans from the database(real emotion vector)
ans=pickle.load(f)
f=open('lol3','rb')# corresponifing emotion from the database
emo=pickle.load(f)
f.close()
tmp1=[]
for i in ques:
    tmp1.append(no(np.array(i)-np.array(tmp)))
tmp1=sorted(range(len(tmp1)), key=lambda i:tmp1[i])[0:n]#return tweet index 
tmp2=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
tmp3=[]
for i in tmp1:
    tmp2+=np.array(ans[i])#database wala ans add kardiye
    tmp3.append(emo[i]) # database emotion main
tmp2=tmp2/n

tmp4=set(tmp3)
tmp5={}
for i in tmp4:
    tmp5.update({i:tmp3.count(i)/n})
tmp6 = [ (v,k) for k,v in tmp5.items() ]
tmp6.sort(reverse=True)
for v,k in tmp6:
    print (str(k)+':'+str(v))
#ano=max(str(v))
#print(ano)
#for ano in tmp6:
 #   print(str(k))
#max=0
#for v in tmp6:
#    if (max<int(v)):
#        max=int(v)

#for v,k in tmp6:
#    if(max==int(v)):
#        print("Highest emotion is :")
#        print(k)
    
#print(tmp2)
