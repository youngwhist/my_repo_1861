import os,sys
def example_function():
    print('Это пример функции')
def Average( numbers ):
    if len(numbers)==0 : return 0
    return sum(numbers)/len(numbers)
example_function()
print(Average([4,5,3]))
