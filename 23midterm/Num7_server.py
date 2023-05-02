from socket import *
from random import randint
import struct
import binascii

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen(1)

class random_pack:
    def __init__(self, sender_ID, recv_ID, Lumi, Humi, Temp, Air, Seq):
        self.send_ID = sender_ID    #송신자
        self.recv_ID = recv_ID    #수신자
        self.Lumi = Lumi    #조도
        self.Humi = Humi    #습도
        self.Temp = Temp    #온도
        self.Air = Air  #기압
        self.Seq = Seq #순서번호

    def pack_random_pack(self):
        self.send_ID, self.recv_ID = randint(1, 50000)
        # self.recv_ID = randint(1, 50000)
        self.Lumi, self.Humi, self.Temp, self.Air = randint(1, 100)
        self.Seq = randint(1, 100000)
        packed = struct.pack('!hhbbbbi', self.send_ID, self.recv_ID, self.Lumi, self.Humi, self.Temp, self.Air, self.Seq)
        return packed

    def unpack_random_pack(self, buffer):
        unpacked = struct.unpack('!hhbbbi', buffer[:12])
        return unpacked

    def getsend_ID(self, unpack_random_pack):
        return unpack_random_pack[0]
    
    def getrecv_ID(self, unpack_random_pack):
        return unpack_random_pack[1]

    def getLumi(self, unpack_random_pack):
        return unpack_random_pack[2]

    def getHumi(self, unpack_random_pack):
        return unpack_random_pack[3]
    
    def getTemp(self, unpack_random_pack):
        return unpack_random_pack[4]

    def getAir(self, unpack_random_pack):
        return unpack_random_pack[5]

    def getSeq(self, unpack_random_pack):
        return unpack_random_pack[6]



RP = random_pack(1234, 80, 1000, 2000, 5, 0, 0b00001010, 4096, 0, 0)
packed_tcphdr = tcp.pack_TcpHdr()
print(binascii.b2a_hex(packed_tcphdr))
print(struct.unpack('!HHLLBBHHL', packed_tcphdr))
unpacked_random_pack = tcp.unpack_TcpHdr(packed_tcphdr)
print('Source Port:{} Destination Port:{} Sequence Number:{} Acknowledgment Number:{} Data Offset:{} Reserved:{} Control Bits:{} Window Size:{} Checksum:{} Urgent Pointer:{}'.format(
        tcp.getSrcPort(unpacked_tcphdr), tcp.getDstPort(unpacked_tcphdr), tcp.getSeqNum(unpacked_tcphdr), tcp.getAckNum(unpacked_tcphdr), 
        tcp.getDataOffset(unpacked_tcphdr), tcp.getReserved(unpacked_tcphdr), tcp.getControlBits(unpacked_tcphdr), tcp.getWindowSize(unpacked_tcphdr), tcp.getChecksum(unpacked_tcphdr), tcp.getUrgentPointer(unpacked_tcphdr)))

while True:
    conn, addr = s.accept()
    print('connected by', addr)
    
    while True:
        data = conn.recv(1024).decode()

        
