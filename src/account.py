class Account:
    def __init__(self, first_name, last_name, email_address, profiles=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        if profiles is None:
            self.profiles = []

    def add_profile(self, profile):
        self.profiles.append(profile)

    def remove_profile(self, profile):
        if profile in self.profiles:
            self.profiles.remove(profile)

    def get_profiles(self):
        return self.profiles
