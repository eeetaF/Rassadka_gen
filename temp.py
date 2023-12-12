import random
import numpy as np

def read_first_10_lines(file_path, M):
    """
    Reads the first 10 lines from the specified file and returns them as a list of strings.
    """
    lines = []
    try:
        with open(file_path, 'r', encoding="UTF-8") as file:
            for _ in range(M):
                line = file.readline()
                if not line:
                    break
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines

def init_dict(nicknames):
    return {nicknames[i]: [num for num in range(1, len(nicknames) + 1) if num != i + 1] for i in range(len(nicknames))}

if __name__ == '__main__':
    file_path = 'input.txt'
    M = 10
    nicknames = read_first_10_lines(file_path, M)
    random.shuffle(nicknames)
    places_dict = init_dict(nicknames)
    current_placement = np.array(M)
    print(current_placement[0])