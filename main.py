from game_brain import GameBrain

brain = GameBrain()
count = 1
u_input = brain.get_input(count)

while u_input != 'q':

    if u_input == 'r':
        brain.reset_board()
        brain.reset_score()
        count = 1
        u_input = brain.get_input(count)

    else:
        if (u_input.isnumeric()) and (0 < int(u_input) < 10):
            brain.place_marker(u_input, brain.check_player(count))

            result = brain.detect_end()
            if result != None:
                if result == "X":
                    brain.winner(1)
                elif result == 'O':
                    brain.winner(2)
                count = 1
                
            else:
                count += 1

            u_input = brain.get_input(count)
        else:
            print('\nincorrect entry, ensure the entry is a number from 1 to 9! (or "q" to quit)')
            u_input = brain.get_input(count)
            continue

brain.reset_board()