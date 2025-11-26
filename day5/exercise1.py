lst = []
lst1 = [1, 2, 3, 4, 5, 6, 7]
print(len(lst1))
print(lst1[0], lst1[3], lst1[-1])
mixed_data_types = ['Renfred', 17, '178cm', 'single', 'Mississauga']
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])
it_companies[0] = 'Meta'
print(it_companies)
it_companies.append('Tesla')
it_companies.insert(5, 'Nvidia')
it_companies[3] = it_companies[3].upper()
print('#; '.join(it_companies))
print('Google' in it_companies)
print(it_companies[:3])
print(it_companies[len(it_companies)-3:])
print(it_companies[3:4])
del it_companies[0], it_companies[3], it_companies[-1]
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
