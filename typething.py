import random
import time
import keyboard


def main():
    keys = ['a', 'r', 's', 't', 'g', 'm', 'n', 'e', 'i', 'o', 'p', 'l', 'f',
            'u', 'w', 'y', 'q', 'd', 'h', 'v', 'k', 'x', 'z']

    print("Time to type!")
    difficulty = 10
    current_round = 1
    play_game = True
    score = 0

    while play_game is True:
        start_time = time.time()
        print("--NEW  GAME--")
        print(f"  ROUND: {current_round}")
        for i in range(0, 100):
            index = random.randint(0, difficulty)
            this_letter = keys[index]
            print(f"\n  {this_letter}")
            key = keyboard.read_key()
            print(f"  {key}")
            if key == this_letter:
                score += 1
        end_time = time.time()
        game_time = end_time - start_time

        print("--GAME COMPLETE--")
        print(f"  TIME: {game_time}")
        print(f"  SCORE: {score}")
        if score > 99:
            print("\n  Nice Score!")
            if difficulty < (len(keys) - 1):
                print("Increaring Difficulty...")
                difficulty += 1
            derp = True
            while derp is True:
                print("Press ENTER to keep going or ESC to exit...")
                key = keyboard.read_key()
                if key == 'esc':
                    derp = False
                    play_game = False
                elif key == 'enter':
                    derp = False


main()
