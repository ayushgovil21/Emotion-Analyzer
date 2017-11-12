import pickle
from nltk.tokenize import word_tokenize as w
import numpy as np
from numpy.linalg import norm as no
n=5
f=open('/Users/aadharsachdeva/Desktop/GovilData/anger.txt','r')
a0=f.readlines()
f=open('/Users/aadharsachdeva/Desktop/GovilData/anticipation.txt','r')
a1=f.readlines()
f=open('/Users/aadharsachdeva/Desktop/GovilData/disgust.txt','r')
a2=f.readlines()
f=open('/Users/aadharsachdeva/Desktop/GovilData/fear.txt','r')
a3=f.readlines()
f=open('/Users/aadharsachdeva/Desktop/GovilData/joy.txt','r')
a4=f.readlines()
f=open('/Users/aadharsachdeva/Desktop/GovilData/sadness.txt','r')
a5=f.readlines()
f=open('/Users/aadharsachdeva/Desktop/GovilData/surprise.txt','r')
a6=f.readlines()
f=open('/Users/aadharsachdeva/Desktop/GovilData/trust.txt','r')
a7=f.readlines()
f=open('/Users/aadharsachdeva/Desktop/GovilData/tweets','rb')
a=pickle.load(f)
f=open('lol1','rb')
ques=pickle.load(f)
f=open('lol2','rb')
ans=pickle.load(f)
f=open('lol3','rb')
emo=pickle.load(f)
f.close()
tmp=[0,0,0,0,0,0,0,0]
tmp3=[]
tmp2=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
for k in a:
    t=w(str(a))
    for i in t:
        for j in range(8):
            if (i.lower()+'\n') in eval('a'+str(j)):
                tmp[j]=tmp[j]+1
    
    tmp1=[]
    for i in ques:
        tmp1.append(no(np.array(i)-np.array(tmp)))
    tmp1=sorted(range(len(tmp1)), key=lambda i:tmp1[i])[0:n]
    
    for i in tmp1:
        tmp2+=np.array(ans[i])
        tmp3.append(emo[i])

tmp2=tmp2/(n*len(a))

tmp4=set(tmp3)
tmp5={}
for i in tmp4:
    tmp5.update({i:tmp3.count(i)/(n*len(a))})
tmp6 = [ (v,k) for k,v in tmp5.items() ]
tmp6.sort(reverse=True)
for v,k in tmp6:
    print (str(k)+':'+str(v))
print(tmp2)
print("Enter y/Y to see the tweets")
if(input() in ['Y','y']):
    for i in a:
        print(i)
        print("\n")
