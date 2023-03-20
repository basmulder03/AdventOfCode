import hashlib

def solve_part_1(input_data):
    cleaned = input_data.strip()
    counter = 0
    while True:
        to_encode = cleaned + str(counter)
        encoded = hashlib.md5(to_encode.encode())
        first_five_chars = list(encoded.hexdigest())[:5]
        try:
            first_five_as_numbers = [int(c) for c in first_five_chars]
            if sum(first_five_as_numbers) == 0:
                break
        except Exception:
            pass
        counter += 1
    return counter


def solve_part_2(input_data):
    cleaned = input_data.strip()
    counter = 0
    while True:
        to_encode = cleaned + str(counter)
        encoded = hashlib.md5(to_encode.encode())
        first_six_chars = list(encoded.hexdigest())[:6]
        try:
            first_six_as_numbers = [int(c) for c in first_six_chars]
            if sum(first_six_as_numbers) == 0:
                break
        except Exception:
            pass
        counter += 1
    return counter