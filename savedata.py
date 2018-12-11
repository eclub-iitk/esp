import socket
import system
import xlwt
from xlwt import Workbook
import time
UDP_IP_ADDRESS="192.168.43.108"
UDP_PORT_NO=3333

serverSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS,UDP_PORT_NO))
#while True:
	#data,addr=serverSock.recvfrom(1024)
	#k = data.rstrip().split()	#print(k)
j=2
i=0
wb=Workbook(encoding='utf-8')
sheet=wb.add_sheet("data1",cell_overwrite_ok=True)
t=time.process_time()
while (time.process_time()-t)<=0.50:
	data,addr=serverSock.recvfrom(1024)
	comp1, comp2 = data.split()
	comp1=float(comp1)
	comp2=float(comp2)
	print(data)
	sheet.write(i,0,comp1)
	sheet.write(i,1,comp2)
	i=i+1
	s=time.process_time()-t
	print(s)
wb.save('d%d.xls'%(j))
exit()
serverSock.close()

