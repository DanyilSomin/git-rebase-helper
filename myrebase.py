import os
import subprocess
import sys

# Get the command line arguments
args = sys.argv[1:]

# env
my_env = os.environ.copy()
my_env["GIT_EDITOR"] = "true"

# Build the git rebase command
cmd = ["git", "rebase"] + args

# Run the git rebase command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=my_env)

# Capture stdout
while True:
    # Read a line from the git output
    line = process.stdout.readline()
    
    # Print the line to the console
    print(line, end="")    

    # If there are no more lines, break out of the loop
    if not line:
        break

    # Check if the line contains a merge conflict
    if "Merge conflict in " in line:
        # Extract the filename from the line
        filename_start = line.find("Merge conflict in ") + len("Merge conflict in ")
        filename_end = line.find("\n", filename_start)
        filename = line[filename_start:filename_end]
        
        # Call the code command to open the file in Visual Studio Code
        os.system(f"code \"{filename}\"")

# Capture stdin
while True:
    # Read a line from the git output
    line = process.stderr.readline()
    
    # Print the line to the console
    print(line, end="")    

    # If there are no more lines, break out of the loop
    if not line:
        break
