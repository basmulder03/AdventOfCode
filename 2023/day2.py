from math import prod

def solve_part_1(input_data):
    total = 0
    
    amount_of_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    
    lines = input_data.split("\n")
    for line in lines:
        game, values = line.strip().split(": ")
        game_possible = True
        for draw in values.split("; "):
            for color_amount in draw.split(", "):
                amount, color = color_amount.split(" ")
                if int(amount) > amount_of_cubes[color]:
                    game_possible = False
                    break
            if not game_possible:
                break
        if game_possible:
            total += int(game.split(" ")[1])
    return total
                    
                
        
    
def solve_part_2(input_data):
    total = 0
    lines = input_data.split("\n")
    for line in lines:
        amount_of_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        game, values = line.strip().split(": ")
        game_possible = True
        for draw in values.split("; "):
            for color_amount in draw.split(", "):
                amount, color = color_amount.split(" ")
                if int(amount) > amount_of_cubes[color]:
                    amount_of_cubes[color] = int(amount)
        total += prod(amount_of_cubes.values())
                    
    return total