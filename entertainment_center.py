import media
import fresh_tomatoes

#create instance of movie class
beauty = media.Movie("Beauty and the Beast",
                      "2017 American musical romantic fantasy film",
                      "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                      "https://www.youtube.com/watch?v=e3Nl_TCQXuw")

despicable = media.Movie("Despicable Me 3",
                      "Gru teams up with his long lost twin brother Dru",
                      "https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg",
                      "https://www.youtube.com/watch?v=6DBi41reeF0")

furious = media.Movie("The Fate of the Furious",
                       "The Fate of the Furious follows Dominic Toretto (Diesel), who has settled down with his wife Letty (Rodriguez), until cyberterrorist Cipher (Theron) coerces him into working for her and turns him against his team, forcing them to find Dom and take down Cipher.",
                       "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                       "https://www.youtube.com/watch?v=J_k1yGJtHgw")

gardians = media.Movie("Guardians of the Galaxy Vol. 2",
                     "2017 American superhero film based on the Marvel Comics superhero team Guardians of the Galaxy",
                     "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                     "https://www.youtube.com/watch?v=duGqrYw4usE")

wonder = media.Movie("Wonder Woman",
                       "2017 American superhero film based on the DC Comics character of the same name",
                       "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                       "https://www.youtube.com/watch?v=VSB4wGIdDwo")

pirates = media.Movie("Pirates of the Caribbean: Dead Men Tell No Tales",
                      "2017 American fantasy swashbuckler film, the fifth installment in the Pirates of the Caribbean film series and the sequel to On Stranger Tides (2011)",
                      "https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
                      "https://www.youtube.com/watch?v=Hgeu5rhoxxY")

# Store the Movie objects in a list.
movies = [beauty, despicable, furious, gardians, wonder, pirates]

# Open the movie website in the user's browser, featuring the movies above.
fresh_tomatoes.open_movies_page(movies)
