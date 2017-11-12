# 1 Remove HTML Tags

import HTMLParser

html_parser= HTMLParser.HTMLParser()

tweet=html_parser.unescape("original_tweet")

# 2 Remove appostophes

appostophes= {"'s" : " is", "'re": " are", "'t" : " not", "'d" : " had" , "'m":" am", "'ve":" have"}

test_string="It's a good thing that they're here"

slist=test_string.split()

newsen=[]

for word in slist:
    for candid in appostophes:
        if candid in word:
            word=word.replace(candid,appostophes[candid])
    newsen.append(word)

rfrm=" ".join(newsen)
print(rfrm)

#print(joined)

# 3 Split attached words

import re

ans=""

for a in re.findall('[A-Z][^A-Z]*',original_tweet):
	ans+=a.strip()+' '

print(ans)
# 4 Conversion of words like luv to love

#tweet=_slang_loopup(tweet)

# 5 Standardizing words like i am happpppyyy to i am happy

import itertools
tweet=" I am happpppy"
ans=''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))
print(ans)


# 6 Remove URL

import re
tweet="Hey there https://www.google.com"
final_tweet= re.sub(r"http\S+", "",tweet)
print(final_tweet)





