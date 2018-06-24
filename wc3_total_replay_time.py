
import glob, os
#Example path. Replay should contain the w3g files.
os.chdir("C:/Users/Wc3addict/Desktop/Replay")
total_ms = 0
n = 0

for file in glob.glob("*.w3g"):
    n+= 1
    replay_file = open(file, 'rb')
    read_bytes = replay_file.read()
    replay_file.close()

    # Got the format from http://w3g.deepnode.de/files/w3g_format.txt
    gamelength_bytes = read_bytes[0x3C:0x3C + 4]

    # The bytes are stored with least significant bit first so we will reverse the bytes.
    gamelength_bytes_reversed = gamelength_bytes[::-1]

    # Make it into a hexadecimal number and then into an integer with base 10.
    # The game time is in milliseconds.
    ms = int(gamelength_bytes_reversed.hex(), 16)

    print('Rep nr', n)

    total_ms += ms

# Print the stuff
total_hours = total_ms / (1000 * 3600)
print()
print(n, "games.")
print('total', round(total_hours,2), "hours")
avg_mins_per_game = total_ms / (n*1000*60)
print("avg", round(avg_mins_per_game,1), "mins per game")

