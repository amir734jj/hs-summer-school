import math

def in_range(lower, upper, n):
    return n >= lower and n <= upper

def items_in_range(x, y):
    result = []
    while x <= y:
        result.append(x)
        x = x + 1
    return result

def get_available_pages(page_number, pages, window_size):
    # when we are too left
    if page_number <= window_size / 2:
        return items_in_range(1, window_size)
    
    # wehen we are too right
    if page_number >= pages - window_size / 2:
        return items_in_range(pages - window_size + 1, pages)
    
    # when its perfect place
    return items_in_range(page_number + 1 - math.ceil(window_size / 2), page_number + math.floor(window_size / 2))
   

def get_available_pages2(page_number, pages, window_size):

    result = [None] * window_size
    
    # page_number = 6
    # pages       = 10
    # window_size = 5
    # [ 0, 1, 2, 3, _ ]

    i = 0
    size = 0
    while size < window_size:
        lower_index_candidate = page_number - i - 1
        upper_index_candidate = page_number + i - 1
    
        if in_range(0, window_size - 1, lower_index_candidate) and result[lower_index_candidate] is None:
            result[lower_index_candidate] = page_number - i
            size = size + 1
        if in_range(0, window_size - 1, upper_index_candidate) and result[upper_index_candidate] is None:
            result[upper_index_candidate] = page_number + i
            size = size + 1

        print(f" {i} => {result}")

        i = i + 1

    return result


def assert_thing(received, expected):
    if expected != received:
        print(f"expected {expected} but received {received}\n")
    else:
        print(f"Good: {expected}\n")


# How should the algorithm behave:
#   At each page algorithm should try to have same number
#   of pages before and after. If before or after is missing
#   some number of pages then we need to make up for that in
#   the opposite side
#
#   [1,2,3,4,5,6,7,8,9,10]
    

assert_thing(get_available_pages(1,10,5), [1,2,3,4,5])
assert_thing(get_available_pages(2,10,5), [1,2,3,4,5])
assert_thing(get_available_pages(3,10,5), [1,2,3,4,5])
assert_thing(get_available_pages(4,10,5), [2,3,4,5,6])
assert_thing(get_available_pages(5,10,5), [3,4,5,6,7])
assert_thing(get_available_pages(6,10,5), [4,5,6,7,8])
assert_thing(get_available_pages(7,10,5), [5,6,7,8,9])
assert_thing(get_available_pages(8,10,5), [6,7,8,9,10])
assert_thing(get_available_pages(9,10,5), [6,7,8,9,10])
assert_thing(get_available_pages(10,10,5), [6,7,8,9,10])
