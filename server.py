import socket
import time


# 存储信息模块
def save_txt(strData,msg):
    with open("./save.txt", "a") as fp:
        try:
            if strData:
                # 打开save.txt,对服务器收到的信息进行存储
                fp.write("客户端信息："+ strData+"\n")
        except:
            pass

        # 打开save.txt,对服务器发送的信息进行存储
        try:
            if msg:
                fp.write("服务器信息："+msg+"\n")
        except:
            pass


# 查看信息模块
def read_txt():
    fp = open('save.txt','r')
    print("=="*30)
    # print("上一次聊天记录如下:"+"\n")
    for i in fp:
        print(i)

# 接收文件模块
def file_send():
    socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketserver.bind(('192.168.80.136',40005))
    socketserver.listen(5)
    print('等待客户端的连接......')
    count = 0
    while True:
        sock, addr = socketserver.accept()
        print('接收一个新的客户端来自:%s:%s...' % addr)
        if count == 0:
            # 接收数据
            data1 = sock.recv(1024)
            print(str(data1))
            # 文件大小
            file_total_size = int(data1.decode())
            received_size = 0
            sock.send('received'.encode())
            data = sock.recv(1024)
            filepath = str(data.decode())
            f = open(filepath, 'wb')
        while received_size < file_total_size:
            data = sock.recv(1024)
            f.write(data)
            received_size += len(data)
            print('已接收 ', received_size, ' Byte')
        data = sock.recv(1024)
        if data == b' ':
             break

    f.close()
    socketserver.close()


# 聊天窗口模块
def user_link():
    print("等待客户端的连接......")
    # 创建服务端的socket对象socketserver
    socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.80.136"
    port = 40006
    # 绑定地址（包括ip地址会端口号）
    socketserver.bind((host, port))
    # 设置监听
    socketserver.listen(5)
    # 注意：accept()函数会返回一个元组,即(ip地址，端口号)
    clientsocket, addr = socketserver.accept()
    # 用于区分每次不同的聊天记录
    with open("./save.txt", "a") as fp:
        fp.write('=='*30+"\n"+"上一次聊天记录"+"\n")

    # while循环是为了能让对话一直进行，直到客户端输入q
    while True:
        # 接收客户端的请求
        recvmsg = clientsocket.recv(1024)

        # 把接收到的数据进行解码
        strData = recvmsg.decode("utf-8")

        # 判断客户端是否发送q，是就退出此次对话
        if strData == 'q':
            break
        else:
            print("收到:" + strData)
            msg = input("回复:")
            # 对要发送的数据进行编码
            clientsocket.send(msg.encode("utf-8"))
            save_txt(strData, msg)

    socketserver.close()



if __name__=='__main__':
    # 请输入对应功能：1:打开服务器连接 2；查看聊天记录
    print("请输入对应功能: ")
    print("1:打开聊天窗口")
    print("2:查看聊天记录")
    print("3:进行文件传输")
    res =str(input())
    if res == '1':
        print("正在打开服务器的连接...")
        user_link()
    elif res == '2':
        read_txt()
    elif res == '3':
        file_send()
    else:
        print("输入有误！请重新输入")
        res = print(input("请输入对应功能:1:打开聊天窗口 2:查看聊天记录 3:进行文件传输"+"\n"))
