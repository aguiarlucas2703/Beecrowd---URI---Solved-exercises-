k = int(input())

if k <= 1:
    category = 1
elif k <= 3:
    category = 3
elif k <= 5:
    category = 5
elif k <= 10:
    category = 10
elif k <= 25:
    category = 25
elif k <= 50:
    category = 50
else:
    category = 100

print(f"Top {category}")
