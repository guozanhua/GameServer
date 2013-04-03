#!/usr/bin/python
# _*_ coding: UTF-8 _*_
#file name:gameSocket
#Email:13558871@qq.com

try:
    import twisted
except	ImportError:
	print "Need requires The Twisted framework."
	raise SystemExit

from twisted.internet import epollreactor
epollreactor.install()
from twisted.internet.protocol import Factory,Protocol
from twisted.internet import reactor
from datetime import datetime
import sys
if not "./protobuf" in sys.path:
	sys.path.append('./protobuf')
from py_mysql import *
import struct
#导入protoc解析类
import DiceFighter_LoginRequest_pb2
import DiceFighter_CreateRequest_pb2
import DiceFighter_CreateResponse_pb2
import DiceFighter_LoginResponse_pb2
import DiceFighter_PlayerInfo_pb2
import DiceFighter_RetInfo_pb2



class gameSocket(Protocol):
	#新客户端连接
    interval = 1.0 # 客户端链接到server后，server往客户端发送时间的间隔 
    timeout = 20  #客户端链接到server后多少时间不操作就断开链接的timeout 
    #datafmt = {
    #        '1001':'<IIIIIIh11sI',
                 #fmt=<IIIIIIh11sI   I=unsigned int 占4位  h11s short 11位ip地址长度
    #}
    _buffer=''
    HEADERSIZE=4
    
    def __init__(self):
        self.started = False
	
    def connectionMade(self):
        #如果服务器连接数超过最大连接数，拒绝新链接建立 
        if self.factory.number_of_connections >= self.factory.max_connections:
            self.transport.write('Too many connections,try again later')
            self.transport.loseConnection()
            return
        #总连接数+1
        self._buffer=''
        self.factory.number_of_connections += 1
        print 'New Client,ID: ', self.factory.number_of_connections

    #关闭客户端连接
    def connectionLost(self,reason):
        Protocol.connectionLost(self,reason)
        #客户端没断开一个链接，总连接数-1 
        print 'Lost Client:',reason.getErrorMessage()
        self.factory.number_of_connections -= 1
        print "Number_of_connections:",self.factory.number_of_connections

    #Received from Client
    def dataReceived(self,data):
        print '收到字节：', repr(data)
        print '*************dataReceived*******'
        self._buffer += data
        self.dataAnalysis()
	
	#self.transport.write(sendTemp+CRPobjStr)
    
    #dataAnalysis from Client
    def dataAnalysis(self):
        datafmt={'1001':'>IIIIIIII',}
        fmtLen = struct.calcsize(datafmt['1001'])
        while len(self._buffer) >= fmtLen:
            print "Buffer Length:%s" % len(self._buffer)
            (protocLength,) = \
                struct.unpack('>I',self._buffer[:self.HEADERSIZE])
            print protocLength
            if len(self._buffer) == fmtLen+protocLength:
                HeadStr=self._buffer[:fmtLen]
                ProtocStr=self._buffer[fmtLen:fmtLen+protocLength]
                srcStr = struct.unpack(datafmt['1001'],HeadStr)
                toIP = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])
		toINT = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])
                print '原始序列:', srcStr

                #CreateRequest
		if  srcStr[1] == 1:
			CRobj = DiceFighter_CreateRequest_pb2.CreateRequest()
			CRobj.ParseFromString(ProtocStr)
			#print CRobj.uin
			#print CRobj.role_id
			CRPobj = DiceFighter_CreateResponse_pb2.CreateResponse()
			CRPobj.result=1
			CRPobj.player.uin=CRobj.uin
			CRPobj.player.role_id=CRobj.role_id
			CRPobj.player.name='test'
			CRPobj.ret.error=0
			CRPobj.ret.errorStr='OK!'
			CRPobjStr = CRPobj.SerializeToString()
			
			sendTemp = struct.pack(datafmt['1001'],len(CRPobjStr),1,0,1,srcStr[4],srcStr[5],1,toINT('113.106.90.136'))
			
			self.transport.write(sendTemp+CRPobjStr)
			

                self._buffer = self._buffer[fmtLen+protocLength:]
            elif len(self._buffer) < fmtLen+protocLength:
                print "Continue Received"
                return
            else:
                print "Error"
                self.transport.loseConnection()
                return

		

class TimerFactory(Factory):
    protocol = gameSocket
    max_connections = 1000

    def __init__(self):
        self.number_of_connections = 0

class SocketPolicyProtocol(Protocol):
    """
    Server strict policy file for Flash Player >= 9,0,124.
    
    @see: U{http://adobe.com/go/strict_policy_files}
    """
    def connectionMade(self):
        self.buffer = ''

    def dataReceived(self,data):
        self.buffer += data
        self.buffer += '\0'
        print "请求获取策略文件",self.transport.getPeer().host,':',self.transport.getPeer().port
        if self.buffer.startswith('<policy-file-request/>\0'):
            self.transport.write(self.factory.getPolicyFile(self)+"\0")
            print '策略文件被发送!'
            self.transport.loseConnection()

class SocketPolicyFactory(Factory):
    protocol = SocketPolicyProtocol

    def __init__(self,policy_file):
        """
        @param policy_file: Path to the policy file definition
        """
        self.policy_file = policy_file

    def getPolicyFile(self,protocol):
        return open(self.policy_file,'rt').read()
	 
#定义服务器域名，端口。
host = '127.0.0.1'
appPort = 5200
defaultPolicyPort=843
policyPort = 7000
policyFile = 'crossdomain.xml'


if __name__ == '__main__':
    from optparse import OptionParser

	#设置server启动选项
    parser = OptionParser()
    parser.add_option("--host",default=host,
        dest="host",help="host address [default: %default]")
    parser.add_option("-a","--app-port",default=appPort,
        dest="app_port",help="Application port number [default: %default]")
    parser.add_option("-d","--defaultPolicy-Port",default=defaultPolicyPort,
        dest="defaultPolicy_port",help="Socket default policy port number [default: %default]")
    parser.add_option("-p","--policy-port",default=policyPort,
        dest="policy_port",help="Socket policy port number [default: %default]")
    parser.add_option("-f","--policy-file",default=policyFile,
        dest="policy_file",help="Location of socket policy file [default: %default]")

    (opt,args) = parser.parse_args()

    print "Running Socket Server on %s:%s" % (opt.host,opt.app_port)
    print "Running Policy file server on %s:%s" % (opt.host,opt.policy_port)	 
    print "Running DefaultPolicy file server on %s:%s" % (opt.host,opt.defaultPolicy_port)	

    reactor.listenTCP(int(opt.app_port),TimerFactory(),interface=opt.host)
    reactor.listenTCP(int(opt.policy_port),SocketPolicyFactory(opt.policy_file),interface=opt.host)
    reactor.listenTCP(int(opt.defaultPolicy_port),SocketPolicyFactory(opt.policy_file),interface=opt.host)


    reactor.run()


#if __name__=='__main__':
#	f = Factory()
#	f.protocol = gameSocket
#	reactor.listenTCP(5200,f)
#	print 'server started...'
#	reactor.run() 
