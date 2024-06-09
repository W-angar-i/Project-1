# #lambda functions
# #map
# #reduce
# c=lambda w: w*20
# print(c(10))

# pro=lambda x,y: (x*y)/(x+y)
# print(pro(10,20))

# import time
# timestapper=lambda: time.localtime()

# print(timestapper())

# def get_num(m):
#     return lambda x: x*m

# myfunction=get_num(3)
# myfunction1=get_num(4)
# print(myfunction(20))
# print(myfunction1(22))

# #Using lambda with map
# numbers = [1, 2, 3, 4,39,20,56]
# squares = map(lambda x: x**3, numbers)# x is the variable used to represent numbers 
# print(list(squares))  # Output: [1, 4, 9, 16]
# names=['jack','jill','john','jane']
# uppercase=list(map(lambda s: s.upper(),names))
# print(uppercase)
# capitalized=tuple(map(lambda d: d.capitalize(),names))
# print(capitalized)

# # Using lambda with filter
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))  # Output: [2, 4]
# fruits=['apple','banana','cherry','orange','kiwi','melon','mango','pineapple','papaya','grapes','watermelon']
# filtered=tuple(filter(lambda fruit: fruit.startswith('m'), fruits))
# print(filtered)

# # Using lambda with reduce
# # reduce function is in functools module. Functools module should be imported first
# from functools import reduce
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Output: 24
# maximum_num=reduce(lambda a,b: a if a>b else b, numbers)
# print(maximum_num)

# # Using lambda with sorted
# numbers = [5, 2, 8, 1, 9]
# sorted_numbers = sorted(numbers, key=lambda x: x)
# print(sorted_numbers)  # Output: [1, 2, 5, 8, 9]
# people_choice=[
#     ('Victor', 9),
#     ('Jack', 20),
#     ('Jill', 21),
#     ('John', 22),
#     ('Jane', 23)
#     ]
# age=sorted(people_choice, key=lambda w: w[1])
# print(age)
# stock=[{'name': 'Product B', 'price': 5.99},
#  {'name': 'Product D', 'price': 8.99},
#  {'name': 'Product A', 'price': 10.99},
#  {'name': 'Product C', 'price': 15.99}]
# stock_sort=sorted(stock, key=lambda value: value['price'])
# print(stock_sort)

list=[1,2,3,4]*3
print(list)
