import socket
import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)
        return packed

    def unpack_Udphdr(self, buffer):
        unpacked = struct.unpack('!HHHH', buffer[:8])
        return unpacked

    def getSrcPort(self, unpacked_udphdr):
        return unpacked_udphdr[0]
    
    def getDstPort(self, unpacked_udphdr):
        return unpacked_udphdr[1]

    def getLength(self, unpacked_udphdr):
        return unpacked_udphdr[2]

    def getChecksum(self, unpacked_udphdr):
        return unpacked_udphdr[3]

udp = Udphdr(5000, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))
print(struct.unpack('!HHHH', packed_udphdr))
unpacked_udphdr = udp.unpack_Udphdr(packed_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(udp.getSrcPort(unpacked_udphdr), udp.getDstPort(unpacked_udphdr), 
                    udp.getLength(unpacked_udphdr), udp.getChecksum(unpacked_udphdr)))