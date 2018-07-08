
import glob, os
# Example absolute path.
# Relative paths work too.
os.chdir("C:/Users/Wc3addict/Documents/Warcraft III/Replay/Autosaved/Multiplayer")

total_ms = 0
nr_games = 0

# The glob module finds all files matching a specified pattern.
for file in glob.glob("*.w3g"):
    nr_games+= 1
    print('Reading rep', nr_games)

    replay_file = open(file, 'rb')
    read_bytes = replay_file.read()
    replay_file.close()

    # Got the format from http://w3g.deepnode.de/files/w3g_format.txt 
    # (replays from before wc3 1.07 have different offset)
    gamelength_bytes = read_bytes[0x3C:0x3C+4]

    # The bytes are stored with least significant bit first so we will reverse the bytes.
    gamelength_bytes_reversed = gamelength_bytes[::-1]

    # Make it into a hexadecimal number and then into an integer with base 10.
    # The game time is in milliseconds.
    ms = int(gamelength_bytes_reversed.hex(), 16)
    total_ms += ms


total_mins = total_ms / (1000 * 60)
total_hours = total_mins / 60

print()
print(nr_games, "games.")
print('total', round(total_hours,2), "hours")
avg_mins_per_game = total_mins / nr_games
print("avg", round(avg_mins_per_game,1), "mins per game")

