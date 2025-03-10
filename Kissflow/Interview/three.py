x = [1, 2, 3, 4, 5]
print(x)
_sum = sum(x)
print(_sum)

"""
>>> [1, 2, 3, 4, 5, 10]  -> total
>>> [15, 1, 2, 3, 4, 5, 10] -> total
>>> [15, 1, 3, 2, 4, 10] -> total
"""

x.append(10)
# x += [10]
print(x)
_sum += 10
print(_sum)

x.insert(0, 15)
# x[-x.__len__()] = 15
print(x)
_sum += 15
print(_sum)

x.remove(5)
print(x)
_sum -= 5
print(_sum)

n1 = 2
n2 = 5

x1 = x[:2] * 5
print(x1)
x.extend(x1)
print(x)
_sum += sum(x1)
print(_sum)
