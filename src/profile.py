class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []

    def add_favourite(self, film):
        self.favourites.append(film)

    def remove_favourite(self, film):
        if film in self.favourites:
            self.favourites.remove(film)

    def get_favourites(self):
        return self.favourites
