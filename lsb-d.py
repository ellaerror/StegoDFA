# file open
filePath = "YOUR FILE PATH HERE"

print("Reading File...")
file = open(filePath, "rb")

# parse data
byte_list = bytearray()
byte = file.read(1)
while byte:
    byte_list += bytes(byte)
    byte = file.read(1)

# change this if you only want to look at certain portions of the file
# This is in BITS not BYTES
start = 0
end = len(byte_list)

outputString = ""

# Save the LSB into a string
for i in range(start, end):
    outputString += str(byte_list[i] % 2)

print("Saving Data...")

# output that string into a file
outputFile = open("output.txt", "wb+")
count = 0

for num in range(int(len(outputString)/8)):
    outputFile.write(bytes([int(outputString[count:count+8],2)]))
    count += 8
