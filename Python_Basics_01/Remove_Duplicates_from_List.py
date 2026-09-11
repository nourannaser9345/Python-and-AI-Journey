List = [1, 4, 6, 9, 10, 9, 5, 4]
uniques = []
for item in List:
    if item not in uniques:
        uniques.append(item)
print(uniques)
