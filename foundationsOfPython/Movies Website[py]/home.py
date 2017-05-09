
import fresh_tomatoes  #importing 'fresh_tomatoes.py' present in the same directory in which this program is placed

import ClassMovie      #importing 'ClassMovie.py' file from the same directory in which this program is placed

#first movie-Inception
story_inc="A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
inception=ClassMovie.Movie("Inception",
                           story_inc,
                           r"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                           r"https://www.youtube.com/watch?v=8hP9D6kZseM")

#second movie-Interstellar
story_int="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
interstellar=ClassMovie.Movie("Interstellar",
                              story_int,
                              r"https://goo.gl/ku21uc",
                              r"https://www.youtube.com/watch?v=zSWdZVtXT7E")


#Third movie-Storks
story_sto="Storks have moved on from delivering babies to packages. But when an order for a baby appears, the best delivery stork must scramble to fix the error by delivering the baby.",
storkes=ClassMovie.Movie("Storks",
                             story_sto,
                             r"https://goo.gl/l0OavG",
                             r"https://www.youtube.com/watch?v=WAY9RgVnONY")


#creating an array with all movies object created above //Pass as many as object you have(I am passing only 3) 
movies=[inception,interstellar,storkes]

#calling a function opne_movies_page from the 'fresh_tomatoes' pacakge which is placed in the same directory where our program is present.
fresh_tomatoes.open_movies_page(movies)
