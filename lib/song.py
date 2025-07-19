class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
    
        self.name = name
        self.artist = artist
        self.genre = genre
        
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
    
    @classmethod
    def add_song_to_count(cls):
        """Increments the count of songs by one"""
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls):
        """Adds genres to the genres list, controlling for duplicates"""
       
    
    def add_to_genres(self):
        """Adds the current song's genre to the genres list"""
        Song.genres.append(self.genre)
        seen = set()
        unique_genres = []
        for genre in Song.genres:
            if genre not in seen:
                seen.add(genre)
                unique_genres.append(genre)
        Song.genres = unique_genres
    
    def add_to_artists(self):
        """Adds the current song's artist to the artists list"""
        Song.artists.append(self.artist)
        seen = set()
        unique_artists = []
        for artist in Song.artists:
            if artist not in seen:
                seen.add(artist)
                unique_artists.append(artist)
        Song.artists = unique_artists
    
    def add_to_genre_count(self):
        """Updates the genre_count histogram"""
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
    
    def add_to_artist_count(self):
        """Updates the artist_count histogram"""
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1