f2=open("ayush_govil_tweets.csv",'w+')
for line in f2:
        f2.write(line.replace("\xe2\x80\x99","'"))

f2.close();
