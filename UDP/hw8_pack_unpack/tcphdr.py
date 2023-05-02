import struct
import binascii

class TcpHdr:
    def __init__(self, src_port, dst_port, seq_num, ack_num, data_offset, reserved, control_bits, window_size, checksum, urg_pointer):
        self.src_port = src_port
        self.dst_port = dst_port
        self.seq_num = seq_num
        self.ack_num = ack_num
        self.data_offset = data_offset
        self.reserved = reserved
        self.control_bits = control_bits
        self.window_size = window_size
        self.checksum = checksum
        self.urg_pointer = urg_pointer

    def pack_TcpHdr(self):
        packed = struct.pack('!HHLLBBHHL', self.src_port, self.dst_port, self.seq_num, self.ack_num, 
                             (self.data_offset << 4) + self.reserved, self.control_bits, self.window_size, self.checksum, self.urg_pointer)
        return packed

    def unpack_TcpHdr(self, buffer):
        unpacked = struct.unpack('!HHLLBBHHL', buffer[:20])
        return unpacked

    def getSrcPort(self, unpacked_tcphdr):
        return unpacked_tcphdr[0]
    
    def getDstPort(self, unpacked_tcphdr):
        return unpacked_tcphdr[1]

    def getSeqNum(self, unpacked_tcphdr):
        return unpacked_tcphdr[2]

    def getAckNum(self, unpacked_tcphdr):
        return unpacked_tcphdr[3]

    def getDataOffset(self, unpacked_tcphdr):
        return unpacked_tcphdr[4] >> 4

    def getReserved(self, unpacked_tcphdr):
        return unpacked_tcphdr[4] & 0x0f

    def getControlBits(self, unpacked_tcphdr):
        return unpacked_tcphdr[5]

    def getWindowSize(self, unpacked_tcphdr):
        return unpacked_tcphdr[6]

    def getChecksum(self, unpacked_tcphdr):
        return unpacked_tcphdr[7]

    def getUrgPointer(self, unpacked_tcphdr):
        return unpacked_tcphdr[8]

tcp = TcpHdr(1234, 80, 1000, 2000, 5, 0, 0b00001010, 4096, 0, 0)
packed_tcphdr = tcp.pack_TcpHdr()
print(binascii.b2a_hex(packed_tcphdr))
print(struct.unpack('!HHLLBBHHL', packed_tcphdr))
unpacked_tcphdr = tcp.unpack_TcpHdr(packed_tcphdr)
print('Source Port:{} Destination Port:{} Sequence Number:{} Acknowledgment Number:{} Data Offset:{} Reserved:{} Control Bits:{} Window Size:{} Checksum:{} Urgent Pointer:{}'.format(
        tcp.getSrcPort(unpacked_tcphdr), tcp.getDstPort(unpacked_tcphdr), tcp.getSeqNum(unpacked_tcphdr), tcp.getAckNum(unpacked_tcphdr), 
        tcp.getDataOffset(unpacked_tcphdr), tcp.getReserved(unpacked_tcphdr), tcp.getControlBits(unpacked_tcphdr), tcp.getWindowSize(unpacked_tcphdr), tcp.getChecksum(unpacked_tcphdr), tcp.getUrgentPointer(unpacked_tcphdr)))