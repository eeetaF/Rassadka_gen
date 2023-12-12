import random
import time

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

def choose_random_nickname(nicknames, occupied_nicknames):
    for occupied_nickname in occupied_nicknames:
        try:
            nicknames.remove(occupied_nickname)
        except:
            pass
    return random.choice(nicknames)

def shuffle_nicknames_without_rep(nicknames, games, M):
    while True:
        try:
            new_games = []
            occupied_nicknames = []
            for i in range(M):
                occupied_nicknames_temp = []
                for game in games:
                    occupied_nicknames_temp.append(game[i])
                nickname = choose_random_nickname(nicknames.copy(), occupied_nicknames + occupied_nicknames_temp)
                occupied_nicknames.append(nickname)
                new_games.append(nickname)
            return new_games
        except:
            pass

if __name__ == '__main__':
    file_path = 'input.txt'
    M = 10
    nicknames = read_first_10_lines(file_path, M)
    games = []
    N_GAMES = int(input("How many games will be played? - "))
    
    start_time = time.time()
    
    for _ in range((N_GAMES - 1) // M + 1):
        games_temp = []
        random.shuffle(nicknames)
        for i in range(M):
            nicknames = shuffle_nicknames_without_rep(nicknames, games_temp, M)
            games_temp.append(nicknames.copy())
        games += games_temp
        
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