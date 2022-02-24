import socket

target=input("Enter the target: ")
targetinfo=socket.getaddrinfo(target, "", proto=socket.IPPROTO_TCP)
infoTuple=targetinfo[0]
netInfoList=infoTuple[4]
print(netInfoList[0])
