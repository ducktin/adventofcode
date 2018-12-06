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

import string
print([(a+b, b+a) for a in string.ascii_lowercase for b in string.ascii_uppercase])

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.show()


import numpy as np
import matplotlib.pyplot as plt

plt.ioff()

list = [i%10 for i in range(50)]
plt.plot(list)
plt.axis('tight')
plt.show()