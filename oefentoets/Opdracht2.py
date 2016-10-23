packets_str = ''
with open('packet_example.txt', 'r') as f:
    packets_str = f.read()

packet_length=''
mac_address =''
packet_content=''
packetstart = 0
packetend = -1

packet_list=[]

for pointer in range(0, len(packets_str)):
    if pointer < (packetstart+12):
        mac_address+=packets_str[pointer]

    if pointer>packetstart+11 and pointer<packetstart+15:
        packet_length += (packets_str[pointer])

    if pointer>=packetstart+15 and \
                    pointer<(int(packet_length, 16)+packetstart+15):
        packet_content+=packets_str[pointer]

    if pointer>packetstart+15 and packetend<pointer:
        packetend=(int(packet_length,16)+packetstart+15)

    if pointer == (packetend):
        #print(mac_address, packet_length, packet_content)
        packet_list.append((mac_address, packet_length, packet_content))
        packetstart=pointer
        mac_address= packets_str[pointer]
        packet_content=''
        packet_length=''
#place last packet in list
packet_list.append((mac_address, packet_length, packet_content))

#packet_list.sort(key=lambda packet: packet[1])
for packet in packet_list:
    print(packet)


