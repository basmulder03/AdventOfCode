def solve_part_1(input_data):
    map = {}
    instructions = []
    
    lines = input_data.split("\n")
    instructions = [c for c in lines[0]]
    
    for line in lines[2:]:
        key, values = line.strip().split(" = ")
        values = values.replace("(", "").replace(")", "")
        left, right = values.split(", ")
        
        map[key] = (left, right)
    current_instruction = 'AAA'
    current_index = 0
    while True:
        instruction = instructions[current_index % len(instructions)]        
        current_index += 1
        if instruction == 'L':
            current_instruction = map[current_instruction][0]
        elif instruction == 'R':
            current_instruction = map[current_instruction][1]
        
        if current_instruction == 'ZZZ':
            break
    
    return current_index
         
from math import lcm    

def solve_part_2(input_data):  
    map = {}
    instructions = []
    
    lines = input_data.split("\n")
    instructions = [c for c in lines[0]]
    
    for line in lines[2:]:
        key, values = line.strip().split(" = ")
        values = values.replace("(", "").replace(")", "")
        left, right = values.split(", ")
        
        map[key] = (left, right)
    
    current_instructions = [key for key in map.keys() if key.endswith("A")]
    current_index = 0
    
    cycles = []
    while True:
        instruction = instructions[current_index % len(instructions)]        
        current_index += 1
        temp_arr = []
        
        instruction_index = 0 if instruction == 'L' else 1
        for current_instruction in current_instructions:
            temp_arr.append(map[current_instruction][instruction_index])
            if temp_arr[-1].endswith("Z"):
                cycles.append(current_index)
        current_instructions = temp_arr
        
        if len(cycles) == len(current_instructions):
            break
    
    return lcm(*cycles)