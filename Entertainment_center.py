#Calling External Rendering Prog
import Fresh_tomatoes
#Calling movie related information
import media

Armageddon = media.Movie("Armageddon",
                        "https://images-na.ssl-images-amazon.com/images/I/51yk78NeNUL.jpg",
                        "https://www.youtube.com/watch?v=kg_jH47u480")

Batman_Begins = media.Movie("Batman Begins",
                        "http://vignette4.wikia.nocookie.net/batman/images/1/1e/Batman_Begins_poster6.jpg/revision/latest?cb=20111218145155" #noqa,
                        "https://www.youtube.com/watch?v=neY2xVmOfUM")

Fight_Club = media.Movie("Fight Club",
                         "http://ia.media-imdb.com/images/M/MV5BNGM2NjQxZTAtMmU5My00YTk5LWFmOWMtYjZlYzk4YzMwNjFlXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg" #noqa,
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

Star_Wars = media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                        "https://i.ytimg.com/vi/gPjJDdxQcfY/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=xESiohGGP7g")


Star_Trek = media.Movie("Star Trek (2009)",
                        "http://www.join4films.com/wp-content/uploads/2015/02/Star-Trek-2009.jpg",
                        "https://www.youtube.com/watch?v=FTzIaSQwxCU")


Ron_Burgundy = media.Movie("Anchorman: The Legend of Ron Burgundy",
                        "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",
                        "https://www.youtube.com/watch?v=1yWhVndYHGg")

#Opens webpage to view trailers
movies = [Armageddon, Batman_Begins, Fight_Club, Star_Wars, Star_Trek, Ron_Burgundy]
Fresh_tomatoes.open_movies_page(movies)



