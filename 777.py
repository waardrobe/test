numbers = set([1, 1, 2, 4, 2])
print(numbers)

numbers = {1, 2, 3, 4, 5, 6, 7}
print(3 in numbers)
numbers.pop()
numbers.discard(66)
numbers.remove(2)
numbers.clear()

numbers = {1, 2, 3, 4, 5, 6, 7}
numbers2 = {2, 6, 54, 43, 31}
ALL = numbers.union(numbers2)
print(ALL)
ALL = numbers & numbers2
numbers = frozenset({1, 2, 3, 4, 5, 6, 7})
numbers.add(8)