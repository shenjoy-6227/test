def add(*args):
    result = 0.0
    for item in args:
        if not isinstance(item, (int, float)):
            raise TypeError('add() only accepts numbers')
        result += item
    return result

print(add(1,2,3.1))
print(add(1,2,3.1, 'a'))