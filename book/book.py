class Book:
    """A book"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author

