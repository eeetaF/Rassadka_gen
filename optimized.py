import random
import numpy as np
import copy
import time

def read_first_M_lines(file_path, M):
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

def find_lowest_remaining(places_dict):
    best_player = next(iter(places_dict.items()))
    for player, places in places_dict.items():
        if len(best_player[1]) > len(places):
            best_player = player, places
    return best_player

def init_dict(nicknames):
    return {nicknames[i]: [num for num in range(1, len(nicknames) + 1) if num != i + 1] for i in range(len(nicknames))}

if __name__ == '__main__':
    file_path = 'input.txt'
    M = 10
    nicknames = read_first_M_lines(file_path, M)
    games = []
    N_GAMES = int(input("How many games will be played? - "))
    
    start_time = time.time()
    
    i = 0
    while i < ((N_GAMES - 1) // M + 1):
        try:
            games_temp = []
            random.shuffle(nicknames)
            places_dict = init_dict(nicknames)
            games_temp.append(nicknames.copy())
            
            for _ in range(M - 1):
                places_dict_temp = copy.deepcopy(places_dict)
                current_placement = np.empty(M, dtype='U' + str(40))
                for _ in range(M):
                    pair = find_lowest_remaining(places_dict_temp)
                    sit = random.choice(pair[1])
                    current_placement[sit - 1] = pair[0]
                    places_dict[pair[0]].remove(sit)
                    del places_dict_temp[pair[0]]
                    for player, places in places_dict_temp.items():
                        if sit in places:
                            places.remove(sit)
                games_temp.append(current_placement)
                
            games += games_temp
            i += 1
        except:
            pass
        
    end_time = time.time()
    duration = end_time - start_time
    print(f"The function took {duration} seconds to complete.")

    with open('output.txt', 'w', encoding="UTF-8") as file:
        for i in range(N_GAMES):
            file.write("Игра " + str(i + 1) + ":\n")
            game = games[i]
            for j in range(len(game)):
                file.write("\t" + str(j + 1) + ": " + game[j] + "\n")
            file.write("\n")