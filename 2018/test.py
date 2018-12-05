print([i for i in range(0, 101)])

# dict contains key and value alternating in the list
def create_dict_from_list(list):
    return dict(zip(list[::2], list[1::2]))

print(create_dict_from_list(['1',2,'3',4]))

print(type([*[1,2,3,4,5]]))

zipper_list = [(1, 'a'), (2, 'b'), (3, 'c')]
print(len([*zipper_list]))

list_a, list_b = zip(*zipper_list)
print( list_a )# (1, 2, 3)
print( list_b )# ('a', 'b', 'c')
