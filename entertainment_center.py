import media
import fresh_tomatoes

# Initialize movies
the_godfather = media.Movie("The Godfather",
	"http://img.zanda.com/item/57040290000061/730xauto/The_Godfather.jpg",
	"https://www.youtube.com/watch?v=sY1S34973zA")

the_dark_knight = media.Movie("The Dark Knight",
 	"http://is4.mzstatic.com/image/thumb/Video18/v4/ec/95/94/ec959447-9c30-730b-75e7-8cbd160bc283/source/1200x630bb.jpg",
 	"https://www.youtube.com/watch?v=EXeTwQWrcwY")

inception = media.Movie("Inception",
 	"http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg",
 	"https://www.youtube.com/watch?v=YoHD9XEInc0")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
	"https://images-na.ssl-images-amazon.com/images/I/51SPVi-1rXL._SY450_.jpg",
	"https://www.youtube.com/watch?v=6hB3S9bIaco")

goodfellas = media.Movie("Goodfella",
	"https://static.rogerebert.com/uploads/movie/movie_poster/goodfellas-1990/large_pDTuWp3jRcGbfWn0Ic6XZ0M0DwP.jpg",
	"https://www.youtube.com/watch?v=qo5jJpHtI1Y")

logan = media.Movie("Logan",
	"https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
	"https://www.youtube.com/watch?v=gbug3zTm3Ws")

# Add movies to a list
movies = [the_godfather, the_dark_knight, inception,
          the_shawshank_redemption, goodfellas, logan]
#Open movies page
fresh_tomatoes.open_movies_page(movies)
