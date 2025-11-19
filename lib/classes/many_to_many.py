class Article:
    # i want to include all article instances by creating an empty list first
    all = []
    def __init__(self, author, magazine, title):
        # here i want to validate the author first 
        if isinstance(author, Author):
            self.author = author
        else:
            self.author = None

    # validating instances in the magazine
        if isinstance(magazine, Magazine):
            self.magazine = magazine
        else:
            self.magazine = None

    # validating instances in the title
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            title = "Untitled"
        self._title = title

    # Wanting to add an article to the list --implement the .append formart.
        Article.all.append(self)
        
    # adding of the property 
    @property
    def title(self):
        # Title is immutable
        return self._title

    @title.setter
    def title(self, value):

        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value    
        
class Author:
    def __init__(self, name):
        # Name must be a string with a length of not long than 0
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            self._name = "Anonymous"

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass