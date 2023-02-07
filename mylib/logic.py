import wikipedia


def wiki(name="Harvard University", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search wikipedia for names"""
    return wikipedia.search(name)
