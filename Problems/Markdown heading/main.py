def heading(text, n=1):
    if n < 1:
        n = 1
    if n >= 6:
        n = 6
    return "#" * n + " " + text