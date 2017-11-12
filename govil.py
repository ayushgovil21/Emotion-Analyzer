from nltk.tokenize import word_tokenize as w
import pickle
f=open(r'C:/Users/ayush/Desktop/Minor 2/sample.dataset.csv','r',encoding='utf-8')
tmp=f.readlines()
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
lol1=[]
lol2=[]
lol3=[]
for i in range(1,len(tmp)):
    tmp1=tmp[i].split(',')
    lol3.append(tmp1[3])
    tmp2=tmp1[5].split()
    tmp3=[float(tmp2[0][1:])]
    for j in range(1,7):
        tmp3.append(float(tmp2[j]))
    tmp3.append(float(tmp2[7][:-1]))
    lol2.append(tmp3)
    tmp4=[0,0,0,0,0,0,0,0]
    tmp5=w(tmp1[4])
    for k in tmp5:
        for l in range(8):
            if (k.lower()+'\n') in eval('a'+str(l)):
                tmp4[l]=tmp4[l]+1

    lol1.append(tmp4)
f=open("lol1","wb")
pickle.dump(lol1,f)
f=open("lol2","wb")
pickle.dump(lol2,f)
f=open("lol3","wb")
pickle.dump(lol3,f)
f.close()
