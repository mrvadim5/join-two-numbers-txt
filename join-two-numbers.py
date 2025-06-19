# Open the original file for reading and a new file for writing
#Tale txt with two numbers per row and join with "-" and no space
# Example "100 1" becomes "100-1"
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        # Split the line into parts, strip any leading/trailing whitespace
        parts = line.strip().split()
        # Join with hyphen if exactly two parts are found
        if len(parts) == 2:
            new_line = f"{parts[0]}-{parts[1]}"
            outfile.write(new_line + "\n")
        else:
            # Handle unexpected formats gracefully
            outfile.write(line)
print("Done!")