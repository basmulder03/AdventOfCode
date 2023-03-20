def solve_part_1(input_data):
    lines = input_data.split("\n")
    total_sqr_ft = 0
    for line in lines:
        if line == '':
            break
        l, w, h = [int(d) for d in line.split('x')]
        sides = [2*l*w, 2*w*h, 2*h*l]
        min_side = min(sides)
        packet_sqr_ft = sum(sides) + (min_side / 2)
        total_sqr_ft += packet_sqr_ft
    return total_sqr_ft

from math import prod

def solve_part_2(input_data):
    lines = input_data.split("\n")
    total_feet = 0
    for line in lines:
        if line == '':
            break
        sides = [int(d) for d in line.split('x')]
        sides.sort()
        length = 2*sides[0]+2*sides[1]
        volume = prod(sides)
        total_length = length + volume
        total_feet += total_length
    return total_feet
        