packetStr = ''
with open('packet_example.txt', 'r') as f:
    packetStr = f.read()

charLenMacAddr = 12
charLenContentLength = 3
packetCharIndex = 0
minCharLength = charLenMacAddr + charLenContentLength + 1

packetList = []
while len(packetStr[packetCharIndex:]) >= minCharLength:
    packetMacAddr = []
    packetContentLengthStr = []
    packetContents = []
    for i in range(0, charLenMacAddr):
        packetMacAddr.append(packetStr[packetCharIndex+i])
    packetCharIndex += charLenMacAddr

    for i in range(0, charLenContentLength):
        packetContentLengthStr.append(packetStr[packetCharIndex+i])
    packetCharIndex += charLenContentLength

    packetContentLength = int(''.join(packetContentLengthStr), 16)
    for i in range(0, packetContentLength):
        if len(packetStr) <= packetCharIndex+i:
            break
        packetContents.append(packetStr[packetCharIndex+i])
    packetCharIndex += packetContentLength

    packetList.append((
        ''.join(packetMacAddr),
        ''.join(packetContentLengthStr),
        ''.join(packetContents)
    ))


for packet in packetList:
    print(packet)
