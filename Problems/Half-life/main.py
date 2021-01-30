initial_quantity = int(input())
final_quantity = int(input())

i = 0

while initial_quantity >= final_quantity:
    initial_quantity //= 2
    i += 12

print(i)
