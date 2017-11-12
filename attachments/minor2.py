import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import pickle as pp
import numpy as np

i = 1;
ter = None;
class abc:
 def __init__(self):
  self.i = 0
  self.A = []
  self.row = 0
  self.col = 0
  self.te = ""; 
 def fetchInfo(abc,url):
  #print(self.i)
  #if abc.i == 5:
  # return
  body = requests.get(url)
  soup = BeautifulSoup(body.text)
  
  #page = urllib2.urlopen(url).read()
  #soup = BeautifulSoup(page)
  
  #counter1 = counter1 + 1
  #nextUrl = soup.find('a',attrs={'href':re.compile("ref_=gnr_mn_ac_mp")})
  ans = soup.find_all('a',attrs={'href':re.compile(r"/title/.*adv_li_tt")});
  print(ans);
  for i in ans:
    tmp=str(i).split('>')
    if(len(tmp)==3):
      #print(tmp[1][:-3])
      qww = tmp[1][:-3]
      abc.te ="%s\n%s"%(abc.te,qww);
  for a in ans:
  	pass
    #print(str(a));
  	#xglobal te;
  	#abc.te ="%s\n%s"%(abc.te,str(a));
  	#print(abc.te);
  #global i;
  abc.i = abc.i + 1;
  if abc.i == 4:
    print(abc.i)
    return abc.te	
  #nextUrl = "http://www.imdb.com/search/title?genres="+str(var)+"&title_type=feature&sort=moviemeter,asc"	;
  #qw= abc();
  #global te;
  #abc.te = abc.fetchInfo(nextUrl);
  abc.i = 1;
  #print(abc.te);
  global ter;		
  ter = "";
  print(abc.te);
  ter = abc.te;
  abc.te=""
  return ter;
#class final():

def fin():
 za =abc()
 myfile = open('comedy.txt', 'w')
 wr = csv.writer(myfile, dialect='excel')
 te = za.fetchInfo("http://www.imdb.com/search/title?genres=comedy&title_type=feature&sort=moviemeter,asc")
 #wr.writerow([te]);
 #pp.dump(te,myfile);
 myfile.write(te);
 myfile.close();
 myfile = open('comedy.txt', 'r')
 #q = pp.load(myfile);
 #print(q);
 myfile.close();

 myfile1 = open('western.txt', 'w')
 wr = csv.writer(myfile1, dialect='excel')
 te5 = za.fetchInfo("http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter,asc")
 #pp.dump(te5,myfile);
 myfile1.write(te5);
 #wr.writerow([te]);
 myfile1.close();
 #print(te)
 
 myfile = open('romance.txt', 'w')
 wr = csv.writer(myfile, dialect='excel')
 te1 = za.fetchInfo("http://www.imdb.com/search/title?genres=romance&title_type=feature&sort=moviemeter,asc")
 #wr.writerow([te]);
 #pp.dump(te1,myfile);
 myfile.write(te1);
 myfile.close();

 myfile = open('mystry.txt', 'w')
 wr = csv.writer(myfile, dialect='excel')
 te3 = za.fetchInfo("http://www.imdb.com/search/title?genres=mystry&title_type=feature&sort=moviemeter,asc")
 #wr.writerow([te]);
 #pp.dump(te3,myfile);
 myfile.write(te3);
 myfile.close(); 
 
 myfile = open('fantasy.txt', 'w')
 wr = csv.writer(myfile, dialect='excel')
 te2 = za.fetchInfo("http://www.imdb.com/search/title?genres=fantasy&title_type=feature&sort=moviemeter,asc")
 #wr.writerow([te]);
 #pp.dump(te2,myfile);
 myfile.write(te2);
 myfile.close();
 
 myfile = open('animation.txt', 'w')
 wr = csv.writer(myfile, dialect='excel')
 te4 = za.fetchInfo("http://www.imdb.com/search/title?genres=animation&title_type=feature&sort=moviemeter,asc")
 #wr.writerow([te]);
 #pp.dump(te4,myfile);
 myfile.write(te4);
 myfile.close();
 
 myfile = open('music.txt', 'w')
 wr = csv.writer(myfile, dialect='excel')
 te6 = za.fetchInfo("http://www.imdb.com/search/title?genres=music&title_type=feature&sort=moviemeter,asc")
 #pp.dump(te6,myfile);
 myfile.write(te6);
 #wr.writerow([te]);
 myfile.close();
 
 myfile = open('horror.txt', 'w')
 wr = csv.writer(myfile, dialect='excel')
 te7 = za.fetchInfo("http://www.imdb.com/search/title?genres=horror&title_type=feature&sort=moviemeter,asc")
 #pp.dump(te7,myfile);
 #wr.writerow([te]);
 myfile.write(te7);
 myfile.close();
#qe = za.fetchInfo(