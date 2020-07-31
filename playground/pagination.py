def get_available_pages(page_number, pages, window_size):
    return [1,2,3,4,5]


def assert_thing(expected, received):
    if expected != received:
        print(f"expected {expected} but received {received}")
    else:
        print(f"Good: {expected}")


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
