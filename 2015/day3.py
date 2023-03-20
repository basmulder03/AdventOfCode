def solve_part_1(input_data):
    steps = list(input_data)
    curr_coor = complex(0, 0)
    visited = set()
    visited.add(curr_coor)
    for step in steps:
        match step:
            case '^':
                curr_coor = complex(curr_coor.real, curr_coor.imag + 1)
            case 'v':
                curr_coor = complex(curr_coor.real, curr_coor.imag - 1)
            case '>':
                curr_coor = complex(curr_coor.real + 1, curr_coor.imag)
            case '<':
                curr_coor = complex(curr_coor.real - 1, curr_coor.imag)
            case _:
                print("How the hell did you get here? ", step)
        visited.add(curr_coor)
    return len(visited)
        

def solve_part_2(input_data):
    steps = list(input_data)
    curr_coor_santa = complex(0, 0)
    curr_coor_robot = complex(0, 0)
    visited = set()
    visited.add(curr_coor_santa)
    visited.add(curr_coor_robot)
    for i, step in enumerate(steps):
        santa_coor = curr_coor_santa
        robot_coor = curr_coor_robot
        match step:
            case '^':
                santa_coor = complex(santa_coor.real, santa_coor.imag + 1)
                robot_coor = complex(robot_coor.real, robot_coor.imag + 1)
            case 'v':
                santa_coor = complex(santa_coor.real, santa_coor.imag - 1)
                robot_coor = complex(robot_coor.real, robot_coor.imag - 1)
            case '>':
                santa_coor = complex(santa_coor.real + 1, santa_coor.imag)
                robot_coor = complex(robot_coor.real + 1, robot_coor.imag)
            case '<':
                santa_coor = complex(santa_coor.real - 1, santa_coor.imag)
                robot_coor = complex(robot_coor.real - 1, robot_coor.imag)
            case _:
                print("How the hell did you get here? ", step)
        if i % 2 == 0:
            curr_coor_santa = santa_coor
            visited.add(curr_coor_santa)
        else:
            curr_coor_robot = robot_coor
            visited.add(curr_coor_robot)
    return len(visited)