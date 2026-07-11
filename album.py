class Album:

    def __init__(self, title, artist, source, rating):
        self.title = title
        self.artist = artist
        self.source = source
        self.rating = rating

    def __str__(self):
        return (
            f"{self.title}\n"
            f"{self.artist}\n"
            f"Source: {self.source}\n"
            f"Rating: {self.rating}/5"
        )
