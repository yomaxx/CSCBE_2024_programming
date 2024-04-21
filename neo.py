import telnetlib
from colorama import Fore, Style
import re
import sys

# Define the Telnet parameters
HOST = "neo.challenges.cybersecuritychallenge.be"
PORT = 1338 
OUTPUT_FILE = "output.txt"

# Connect to the device
tn = telnetlib.Telnet(HOST, PORT)

ansi_escape = re.compile(r'\x1B\[[0-9;]*[A-Za-z]')

with open(OUTPUT_FILE, 'a') as f:
    while True:
        output = tn.read_some()
        if output:
            # Decode the output
            decoded_output = output.decode('ascii')
            # Remove the escape codes
            stripped_output = ansi_escape.sub('', decoded_output)
            # Write the stripped output to the file
            for letter in stripped_output:
                sys.stdout.write(letter)
        else:
            break

# Close the Telnet connection
tn.close()
