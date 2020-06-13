from collections import defaultdict

def radix_sort(array):
    place = 1
    maxx = max(array)
    while int(maxx):
        array = counting_sort(array, place)
        place *= 10
        maxx /= 10
    return array

def counting_sort(arr, place):
    count_dict = defaultdict(list)
    for i in arr:
        place_digit = (i//place)%10
        count_dict[place_digit].append(i)
    array = []
    for i in range(10):
        if i in count_dict:
            array.extend(count_dict[i])
    return array
