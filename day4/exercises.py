""" 30 Days of Python: Day 4 """

print('Thirty ' + 'Days ' + 'Of ' + 'Python')
print('Coding ' + 'for ' + 'all')
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
print('Python for Everyone'.replace("Everyone", "All"))
print(company.split(" "))
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(", "))
print(company[0])
print(company[-1])
print(company[10])
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))
print(company.find(
    'You cannot end a sentence with because because because is a conjunction'))
print(company.rfind(
    'You cannot end a sentence with because because because is a conjunction'))
print(
    'You cannot end a sentence with because because because is a conjunction'[32:53])
print(company.startswith("Coding"))
print(company.endswith("Coding"))
print('    Coding For All   '.strip())
# thirty_days_of_python
print(' # '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print('I am enjoying this challenge\nI just wonder what is next')
print('Name\tAge\tCountry\tCity\nRenfred\t17\tCanada\tMississauga')

radius = 10
area = 3.14 * radius**2
print("The area of a circle wiht radius {} is {} meters".format(
    radius, area))

a, b = 8, 6
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {}'.format(a, b, a/b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a//b))
print('{} ** {} = {}'.format(a, b, a**b))
