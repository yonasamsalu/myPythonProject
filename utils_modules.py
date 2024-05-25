
'''
  1.import utils = access the whole module or importing the entire module.
  2.utils.find_max() = accessing individual function.
'''
from utils import find_max
numbers = [6, 2, 7, 43, 15]
largest = find_max(numbers)

print(largest)