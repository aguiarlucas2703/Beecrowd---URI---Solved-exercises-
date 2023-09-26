while True:
    inputs = input().split()
    if inputs == ['0']:
        break
    side_a, side_b, percent = inputs
    side_a, side_b, percent = int(side_a), int(side_b), int(percent)
    area = side_a * side_b
    min_side = int((area * 100 / percent) ** 0.5)
    print(min_side)
