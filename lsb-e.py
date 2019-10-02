
filePath = "YOUR FILE PATH HERE"

# open file to hide data in
vesselFile = open(filePath, "rb+")

# create a list containing all the bytes in the file
print("Reading Vessel File...")
byte_list = bytearray()
byte = vesselFile.read(1)
while byte:
    byte_list += bytes(byte)
    byte = vesselFile.read(1)

# message to hide
secret = "Hello ChampDFA!"

print("Translating message...")
# split secret data into bits
secretStr = ""
for char in secret:
    secretStr += ("00000000" + bin(ord(char)).replace('0b', ''))[-8:]

bit_list = list()
for bit in secretStr:
    bit_list.append(int(bit))

# write the LSB into the file
print("Encoding Data...")

# this is in bytes
padding = 200

vesselFile = open(filePath, "wb")
count = -1
bitNum = 0
for byte in byte_list:
    count+=1
    if count >= padding and count < padding + count:
        if bitNum < len(bit_list):
            if bit_list[bitNum] == 1:
                if byte % 2 == 0:
                    byte += 1
            else:
                if byte % 2 == 1:
                    byte += 1
                    if byte > 255:
                        byte -= 2
            bitNum += 1
    vesselFile.write(bytes([byte]))
