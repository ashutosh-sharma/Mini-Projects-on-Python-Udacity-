import webbrowser  #importing 'webbrowser' package which is in-built in python

#Defining a class Movie
class Movie():
    #Class Movie, having members:
                    #1.Movie Title
                    #2.Movie storyline
                    #3.Moive poster_url
                    #4.Movie youtube trailer_url
    #Constructor of the class passing arguments to constructor to initilize the object
    def __init__(self,title,story,poster,trailer):
        self.title=title
        self.storyline=story
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer
        
    #Member Funciton of the class movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url) #calling function open() from webbrowser pacakge
        
