import urllib2
from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import re

def getunicode(soup):
	body=''
	if isinstance(soup, unicode):
		soup = soup.replace('&#39;',"'")
		soup = soup.replace('&quot;','"')
		soup = soup.replace('&nbsp;',' ')
		body = body + soup
	else:
		if not soup.contents:
			return ''
		con_list = soup.contents
		for con in con_list:
			body = body + getunicode(con)
	return body


def main():
	
        urlhere='http://www.imdb.com/genre/action/?ref_=gnr_mn_ac_mp'
        title_search = re.compile('/title/tt\d+')
    
        br = Browser()
        br.open(urlhere)

        #titlemovie=[]
        #titlemovie_soup=soup.findAll('a'.itemprop='title')
        #for i in range(len(titlemovie_soup)):
         #   titlemovie.append(getunicode(titlemovie_soup[i]))

        #print(', '.join(titlemovie))
            

        link = br.find_link(url_regex = re.compile(r'/title/tt.*'))
        res = br.follow_link(link)
    
        
        soup = BeautifulSoup(res.read())
        movie_title = getunicode(soup.find('title'))
        print(movie_title)

        #for div in soup.findAll('div',attrs={'class':'image'}):
        #    print div.find('a')['href']
        #    print div.find('a').contents[0]

        
if __name__ == '__main__':
    main()
