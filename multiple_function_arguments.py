def my_function(first, second, *third):
    print("First : ", first)
    print("Second : ", second)
    print("Third : ", list(third))

my_function(1, 2, 3, 4, 5)

# First :  1
# Second :  2
# Third :  [3, 4, 5]
print('\n--------------------------------\n')


def bar(first, second, third, **options):
    if options['action'] == 'sum':
        print('The sum is : ', first + second + third)

    if options['number'] == 'second':
        return second

result = bar(1, 2, 3, action='sum', number='second')
print('Result : ', result)

# The sum is :  6
# Result :  2
# [Finished in 0.0s]