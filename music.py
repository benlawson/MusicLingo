import urllib2
from bs4 import BeautifulSoup

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def search(term, noun='song', adjective='genre'):
      
        genre_list = []
        #clean search term
        term = term.replace(" ","%20").lower()
        term_search = term.replace("_","%20").lower().replace(u'\u0024', 'S').replace(u'\u0026', 'and').replace(u'\u2300', 'o')

        search = "http://www.allmusic.com/search/all/" + term_search
        req = urllib2.Request(search, headers=hdr)
        x = urllib2.urlopen(req).read()
        #open first page (search)
        soup = BeautifulSoup(x)
        for link in soup.find_all('a'):
            a = link.get('href')
            if noun in a and "http" in a:
                target_page = a
                break
        
        if adjective == 'lyrics': 
           suffix = '/lyrics'
        else: suffix = None
        #navigate to main page
        req2 = urllib2.Request(target_page + suffix, headers=hdr)
        print target_page + suffix
        z = urllib2.urlopen(req2).read()
        soup = BeautifulSoup(z)

        #aquire information
        #set search terms
        no_link = False
        if adjective in ['styles', 'genre', 'genres']:
            tag = 'div'
            attr = 'class'
            query = adjective
        elif adjective == 'moods':
            tag = 'section'
            attr = 'class'
            query = adjective
        else:
            tag = 'p'
            attr = 'id'
            query = 'hidden_without_js' 
            no_link = True

        for genre in soup.find_all(tag, {attr : query}):
            if no_link:
                genre_list.append(genre.text)
            if not no_link:
                 for text in genre.find_all('a'):
                    genre_list.append( (text.string.replace(' ','_')))
        
        #except:
        #this is exception catches two known cases: when the 'artist' string is non-ascii and when the artist does not appear on the website
        #as it does in my collection
        #     return None 
        return genre_list
#eof
