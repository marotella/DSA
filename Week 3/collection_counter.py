n = int(input())
shoe_sizes = list(map(int, input().split()))

shoe_inventory = {}

for size in shoe_sizes:
    if size in shoe_inventory:
        shoe_inventory[size] += 1
    else:
        shoe_inventory[size] = 1
        
m = int(input())
total_earnings = 0

for _ in range(m):
    size, price = map(int, input().split())
    if size in shoe_inventory and shoe_inventory[size] > 0:
        total_earnings += price
        shoe_inventory[size] -= 1

print(total_earnings)        

