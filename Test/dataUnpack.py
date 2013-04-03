#coding:utf-8
#基于python2.6



dataUnpackfmt = {
    '1001':'<IIIIIIh11sI',
     #fmt=<IIIIIIh11sI   I=unsigned int 占4位  h11s short 11位ip地址长度
}
import struct



def dataUnpack(cmdid,data):
    global dataUnpackfmt
    if cmdid not in dataUnpackfmt:
        print cmdid,'协议fmt格式读取错误'

    res = struct.unpack(dataUnpackfmt[cmdid],data)
    return res
