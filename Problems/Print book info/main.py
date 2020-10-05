def print_book_info(title, author=None, year=None):
    text = '"' + title + '"'
    if author is None and year is None:
        pass
    elif author is not None and year is not None:
        text += " was written by " + author + " in " + year
    elif year is not None and author is None:
        text += " was written in " + year
    elif author is not None and year is None:
        text += " was written by " + author
    print(text)
