class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
 #the use of ._ is to show that the attribute should not be accessed 
class Author:
    def __init__(self, name):
        self.name = name
        self._articles = [] #array of articles that author has written

    def articles(self):
        return self._articles #returns a list of articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles)) # a unique list of magazines for which the author has contributed to

    def add_article(self, magazine, title):
        article = Article(self, magazine, title) #creation of an article instance
        self._articles.append(article) #adds the magazine and title to the article list
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles)) #unique list of categories of magazines for which the author has written articles.

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        self._contributors = set()

    def articles(self):
        return self._articles #a list of all the articles the magazine has published

    def contributors(self):
        return list(self._contributors) #a unique list of authors who have written for this magazine

    def article_titles(self):
        return [article.title for article in self._articles] #returns a list of titles of all articles

    def contributing_authors(self):
        authors=[article.author for article in self._articles]
        return [author for author in set(authors) if authors.counts() > 2]
