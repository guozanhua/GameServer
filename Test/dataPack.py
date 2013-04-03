#coding:utf-8
#基于python2.6
import struct
import pack
import PlayerInfo_pb2
from socket import *

sock = socket(AF_INET,SOCK_STREAM)
sock.connect(('113.106.90.136',5200))



test=PlayerInfo_pb2.PlayerInfo()

test.uin=13558871
test.role_id=2
test.name='FUChhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhKkkklkljljlkjljlk'

test_str = test.SerializeToString()


print len(test_str)

toIP = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])

toINT =  lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])

k=pack.pack('1001',[len(test_str),1,3,2,13558871,2,toINT('192.168.0.2'),2])
print repr(k+test_str)

print len(k+test_str)

j=struct.unpack('<IIIIIIII',k)
print '包头大小',struct.calcsize('<IIIIIIII')

print j

sock.send(k+test_str)

test22= sock.recv(1024)
sock.close()

print struct.unpack('>I',test22)
