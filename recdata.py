import socket
import time
import csv
import xlwt

book= xlwt.Workbook(encoding= 'utf-8')

sheet1=book.add_sheet("sheet 1", cell_overwrite_ok=True)

 try :

    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

except socket.error, msg :

    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]

    sys.exit()

try:

    s1.bind(('192.168.0.107', 3333))

except socket.error , msg:

    print 'Bind failed. Error: ' + str(msg[0]) + ': ' + msg[1]

    sys.exit()

j=1 #data number
i=0 #row value
print ("I am here")

t1= time.time()
while (time.time()-t1 < 5):
    data1= s1.recvfrom(1024)
    idc1, idc2, comp1, comp2 = data1.split()
    comp1=float(comp1)
    comp2=float(comp2)

    sheet1.write(i,0,comp1)
    sheet1.write(i,1,comp2)
    i=i+1
    print (i)

book.save('d%d.xls'%(j))

print " "
print "Data No-%d" %(j)
print (time.time()-t1)
