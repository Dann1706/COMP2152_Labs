point_1 = (3,5)
point_2 = (7,2)
x1, y1 = point_1
x2, y2 = point_2
print(f"X1 = {x1}, Y1 = {y1}")
print(f"X2 = {x2}, Y2 = {y2}")

distance = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
print(f"Distance between points: {distance}")

characters = ('P', 'Y', 'T', 'H', 'O', 'N')
print(tuple(characters))

for x in characters:
    print(x)