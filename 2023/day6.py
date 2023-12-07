def solve_part_1(input_data):
    f = input_data.splitlines()
    times = [int(numbs) for numbs in f[0].split()[1::]]
    distances = [int(numbs) for numbs in f[1].split()[1::]]

    total = 1
    for i in range(len(times)):
        time = times[i]
        dist = distances[i]
        valid_method = 0
        for push_time in range(time):
            if push_time*(time-push_time) > dist:
                valid_method += 1
        total *= valid_method
    return total

def solve_part_2(input_data):
    f = input_data.splitlines()
    time = int(''.join(f[0].split()[1::]))
    distance =  int(''.join(f[1].split()[1::]))

    lover_time=0
    upper_time = 0
    curr_time = 0
    while(True):
        curr_time += 1
        if(curr_time*(time-curr_time) > distance):
            lover_time = curr_time
            break
    curr_time = time
    while(True):
        curr_time -= 1
        if(curr_time*(time-curr_time) > distance):
            upper_time = curr_time
            break
    return upper_time - lover_time + 1