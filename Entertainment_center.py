#Calling External Rendering Prog
import Fresh_tomatoes

import media

Armageddon = media.Movie("Armageddon",
                        "https://images-na.ssl-images-amazon.com/images/I/51yk78NeNUL.jpg",
                        "https://www.youtube.com/watch?v=kg_jH47u480")
#print(Armageddon.storyline)
#Armageddon.show_trailer()

Batman_Begins = media.Movie("Batman Begins",
                        "http://vignette4.wikia.nocookie.net/batman/images/1/1e/Batman_Begins_poster6.jpg/revision/latest?cb=20111218145155",
                        "https://www.youtube.com/watch?v=neY2xVmOfUM")
#print(Batman_Begins.storyline)
#Batman_Begins.show_trailer()

Fight_Club = media.Movie("Fight Club",
                         "http://ia.media-imdb.com/images/M/MV5BNGM2NjQxZTAtMmU5My00YTk5LWFmOWMtYjZlYzk4YzMwNjFlXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")
#print(Fight_Club.storyline)
#Fight_Club.show_trailer()

Star_Wars = media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                        "https://i.ytimg.com/vi/gPjJDdxQcfY/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=xESiohGGP7g")
#print(Star_Wars.storyline)
#Star_Wars.show_trailer()

Star_Trek = media.Movie("Star Trek (2009)",
                        "http://www.join4films.com/wp-content/uploads/2015/02/Star-Trek-2009.jpg",
                        "https://www.youtube.com/watch?v=FTzIaSQwxCU")
#print(Star_Trek.storyline)
#Star_Trek.show_trailer()

Ron_Burgundy = media.Movie("Anchorman: The Legend of Ron Burgundy",
                        "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",
                        "https://www.youtube.com/watch?v=1yWhVndYHGg")
#print(Star_Wars.storyline)
#Star_Wars.show_trailer()

movies = [Armageddon, Batman_Begins, Fight_Club, Star_Wars, Star_Trek, Ron_Burgundy]
Fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)


