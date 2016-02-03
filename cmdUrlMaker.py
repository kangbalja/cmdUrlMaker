# -*- coding:utf-8 -*-

def cmdUrlMaker():
    
    rServer = "192.168.0.19"
    dServer = "192.168.0.70:7575"
    
    serverSelect = input('Choose the number of the server. (1)192.168.0.19 (2)192.168.0.70:7575 : ')
    if serverSelect == 1:
        server = rServer
    else:
        server = dServer

    cmd = raw_input('cmd : ')
    
    paramCnt = input('paramCnt : ')
    
    param = []
    for i in range(1, paramCnt+1):
        param.append(raw_input('param%s : ' % i))
        
    urlHead = "http://%s/Python/ServerRequest?cmd=%s" % (server, cmd)
    
    urlBody = ''
    for i in range(0, paramCnt):
        paramNum = i + 1
        urlBody += '&param%s=' % paramNum + param[i] 
    
    url = urlHead + urlBody
    
    print url
    
if __name__ == '__main__':
    cmdUrlMaker()
