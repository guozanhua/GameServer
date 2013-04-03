#coding:utf-8
#基于python2.6
import struct
import pack
import dataUnpack
import PlayerInfo_pb2


test=PlayerInfo_pb2.PlayerInfo()

test.uin=13558871
test.role_id=2
test.name='FUCK'

test_str = test.SerializeToString()


print len(test_str)


k=pack.pack('1001',[len(test_str),2,3,2,13558871,2,'192.168.1.2',2])
print repr(k+test_str)

print len(k+test_str)

print dataUnpack.dataUnpack('1001',k)

print struct.calcsize('<IIIIIIh11sI')

