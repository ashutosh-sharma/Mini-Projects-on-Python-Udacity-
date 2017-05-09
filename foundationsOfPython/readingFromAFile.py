import urllib

def read_file():
    quotes=open(r"C:\Python27\programs\movie_quotes.txt")
    text=quotes.read()
    print(text)
    print("\n")
    curse_finder(text)
    quotes.close()

def curse_finder(text):
    con=urllib.urlopen("http://www.wdylike.appspot.com/?q=shot"+text)
    op=con.read()
    print(op)
    con.close()
    
read_file()
