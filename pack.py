#coding:utf-8
#python 2.6

'''
s=字符串
b=字节
i=长整数
u=无符号整形
n=短整形
'''
datafmt ={ 
    '1001':'uuuuuuuu',
    #指定1001协议的数据格式，如果按如上指定，则表示该封包由
    #字符串 + 字符串 + 字节 + 长整型
    #构成
}
import struct
#对数据进行pack数据 comid(string)=协议号 data(list)=数据内容
def pack(comid,data):
    global datafmt
    if comid not in datafmt:
        print comid,'协议fmt格式读取错误'
    
    fmtStr = datafmt[comid]
    fmtStrRes = []
    idx = 0
    fixString ={}
    for k in fmtStr:
        if k=='n':
            fmtStrRes.append('h')
        elif k=='b':
            fmtStrRes.append('b')
        elif k=='u':
            fmtStrRes.append('I')
        elif k=='i':
            fmtStrRes.append('i')
        elif k=='s':
            _strLength = len(data[idx])
            fixString[idx] = _strLength #记录str的长度
            fmtStrRes.append('h'+ str(_strLength) +'s')
        idx = idx + 1
    
    fmt = '<'+''.join(fmtStrRes)
    #将字符串的长度值插入到data中
    if len(fixString)>0:
        idx = 0
        for k,v in fixString.items():
            data.insert(k+idx,v)
            idx = idx + 1
    
    #print 'data=',data
    print 'fmt=',fmt
    res = struct.pack(fmt,*data)
    #print 'pack=',res
    return res
#pack('1001',[32,2,3,2,13558871,2,'192.168.1.2',2])
