ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0], ages[-1])
# ages.append(ages[0]).append(ages[-1])
median_age = (ages[4]+ages[5])/2
total_age = 0
for age in ages:
    total_age += age
avg = total_age/len(ages)
range = ages[-1] - ages[0]
print(avg)
print(abs(ages[0] - avg) == abs(ages[-1] - avg))
