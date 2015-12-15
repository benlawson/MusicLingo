import urllib2
try:
    import bs4  as bs
except:
    import BeautifulSoup as bs

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def firstpage(term, noun='song'):
      
        #clean search term
        term = term.replace(" ","%20").lower()
        term_search = term.replace("_","%20").lower().replace(u'\u0024', 'S').replace(u'\u0026', 'and').replace(u'\u2300', 'o')

        search = "http://www.allmusic.com/search/all/" + term_search
        print search
        req = urllib2.Request(search, headers=hdr)
        x = urllib2.urlopen(req).read()
        #open first page (search)
        soup = bs.BeautifulSoup(x)
        try:
            links = soup.find_all('a')
        except:
            links = soup.findAll('a')

        for link in links:
            a = link.get('href')
            if noun in a and "http" in a:
                target_page = a
                return target_page 

def bothpage(url, song):
        suffix =  '/songs/all/'
        nextpage = url + suffix if suffix not in url else url
        print nextpage
        req = urllib2.Request(nextpage, headers=hdr)
        x = urllib2.urlopen(req).read()

        soup = bs.BeautifulSoup(x)
        try:
            links = soup.find_all('a')
        except:
            links = soup.findAll('a')

        for link in links:
            a = str(link.get('href'))
            text = str(link.text)
            if song.split(' ')[0] in text and "http" in a:
                target_page = a
                return target_page 
        for link in soup.find_all('a'):
            if 'Next' in link.text: #need to page through all the songs
                 a = str(link.get('href'))
                 return bothpage(a, song)
    
def secondpage(target_page, adjective='genre'):        
        genre_list = []

        if adjective == 'lyrics': 
           suffix = '/lyrics'
        else: suffix = '' 
        #navigate to main page
        
        req = urllib2.Request(target_page + suffix, headers=hdr)
        print target_page + suffix
        x = urllib2.urlopen(req).read()
        soup = bs.BeautifulSoup(x)

        #aquire information
        #set search terms
        no_link = False
        if adjective in ['style', 'styles', 'genre', 'genres']:
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
        try:
            links = soup.find_all(tag, {attr : query})
        except:
            links = soup.findAll(tag, {attr : query})
            
        for genre in links:
            if no_link:
                return filter(lambda d: len(d) > 0, genre.text.split(' ')) #this should break in Python3 TODO fix this
            if not no_link:
                 print genre.find_all('a')
                 for text in genre.find_all('a'):
                    genre_list.append( (text.string.replace(' ','_')))
        return genre_list
#eof
