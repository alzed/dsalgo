def linear_search(array, element):
    try:
        return array.index(element)
    except ValueError:
        return None
        