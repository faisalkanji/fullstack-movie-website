import webbrowser

#create Movie class to hold title, storyline, image and youtube URL
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	#define function to ope youtube url in browser
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)