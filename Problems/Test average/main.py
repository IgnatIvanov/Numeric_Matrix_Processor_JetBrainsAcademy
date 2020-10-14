def average_mark(*args):
    average = 0
    for n in args:
        average += n
    average /= len(args)
    return round(average, 1)

