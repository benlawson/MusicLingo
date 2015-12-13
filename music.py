import urllib2
from bs4 import BeautifulSoup
def genre(term, type_='song'):
        genre_list = []
        #name_search = song.replace(" ","%20").lower()
        #name_inline = song.replace(" ","-").lower()
        #artist_inline = row.artists.replace("_","-").lower().replace('.','').replace(',','').replace('The-','').replace('the-','')[:-1]
        term_search = term.replace("_","%20").lower().replace(u'\u0024', 'S').replace(u'\u0026', 'and').replace(u'\u2300', 'o')
        search = "http://www.allmusic.com/search/all/" + term_search
        x = urllib2.urlopen(search).read()
        soup = BeautifulSoup(x)
        for link in soup.find_all('a'):
            a = link.get('href')
            if type_ in a and "http" in a:
                target_page = a
                break

        z = urllib2.urlopen(target_page).read()
        soup = BeautifulSoup(z)
        #find the genre
        for genre in soup.find_all('div', {"class" : "genre"}):
            for text in genre.find_all('a'):
                #print len(genre.find_all('a'))
                genre_list.append( (text.string.replace(' ','_')))
        '''   
        #find the styles
        for style in soup.find_all('div', {"class" : "styles"}):
            for text in style.find_all('a'):
                print >> f, (text.string.replace(' ','_')),
        for x in range(20-len(style.find_all('a'))):
                print f >> ("bbbb"),
        
        #find the moods
        for link in soup.find_all('section', { "class" : "moods" }):
            for text in link.find_all('a'):
                print >> f, (text.string.replace(' ','_'))
                '''
        #except:
        #this is exception catches two known cases: when the 'artist' string is non-ascii and when the artist does not appear on the website
        #as it does in my collection
        #     return None 
        return genre_list

#eof
