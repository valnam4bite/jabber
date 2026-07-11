class Catalog:

    def __init__(self):
        self.albums = []

    def add(self, album):
        self.albums.append(album)

    def all(self):
        return self.albums
