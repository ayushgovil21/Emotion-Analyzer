from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP
import pickle
#from mechanize import Browser

def main(emotion):


    #emotion=input("Enter the emotion: ")
    qw={'Sad':'comedy.txt','Disgust':'romance.txt','Anger':'fantasy.txt','Anticipation':'mystry.txt','Fear':'Animation','Enjoyment':'western.txt','Trust':'music.txt','Surprise':'horror.txt'}
    for k,v in qw.items():
      #print("##########");
      #print(k+"->"+v);
      if k == emotion:
        #myfile = open('comedy.txt','r')
        #q = myfile.readline();
        i = 1;
        #movies = list([q])
        #print(q);
        i = 0;
        #print("->"+v);
        print("\nRecommended Movies:")
        for line in open(v,'r').readlines():
            print(line);
            if(i>3):
                break;
            i = i + 1;    
        #myfile.close();
        #line.close();
        #for qw in q: 
         # pass
          #print("***"+qw);
          #print(i);
    if(emotion=="Sad"):

                      urlhere='http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter,asc'

    elif(emotion=="Disgust"):
                      
                      urlhere='http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter,asc'

    elif(emotion=="Anger"):

                      urlhere='http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter,asc'

    elif(emotion=="Anticipation"):

                      urlhere='http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter,asc'

    elif(emotion=="Fear"):

                      urlhere='http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter,asc'

    elif(emotion=="Enjoyment"):

                      urlhere='http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter,asc'

    elif(emotion=="Trust"):

                      urlhere='http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter,asc'

    elif(emotion=="Surprise"):

                      urlhere='http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter,asc'

    response=HTTP.get(urlhere)

    data=response.text
    
    #br = Browser()

    #br.open(urlhere)

    #link = br.find_link(url_regex = re.compile(r'/title/tt.*'))

    #res = br.follow_link(link)
    
    #soup = SOUP(res.read())

    soup=SOUP(data,"lxml")

    title=soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    
    ''' for i in title:
        if(i.get('title')!="None\n" and i.get('title')!="Delete\n"):
            print (i.get('title'))
    '''
    return title

if __name__ == '__main__':
    
    emotion=input("Enter the emotion: ")
    
    a=main(emotion)
    
   #import pickle

    count=0

    if(emotion=="Disgust" or emotion=="Anger" or emotion=="Surprise"):
        for i in a:
            tmp=str(i).split('>')
            if(len(tmp)==3):
                print(tmp[1][:-3])
            if(count>13):
                break
            count+=1
    else:
        for i in a:
            tmp=str(i).split('>')
            if(len(tmp)==3):
                print(tmp[1][:-3])
                print("\n")
            if(count>11):
                break
            count+=1                            
