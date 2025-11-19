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

# initiating a getter method so that one can access attributes in the class
    @property
    def name (self):
        return self._name

    # def articles(self):
    # here i am creating a string that is returning all article instances where the author is the author.
    # by doinging this i am coming up with a list comprehension (like shortening it)
        # return[article for article in Article.all if article.author == self]
     # the Article.all assumes that there is a list in the Article 
    # then the if article.author == self checks if the author of the article is the same as the {self} author

    def articles(self):
     # create an empty list to store matching articles
        result = []
        for article in Article.all:
        # go through every article
            if article.author == self:
            # check if this article was written by this author
                result.append(article)  
              # add it to the result list
        return result  
        # return the list of articles


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