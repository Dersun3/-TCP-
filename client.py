import socket
import os
import time

# 聊天窗口模块
def chat():
    # 创建一个客户端的socket对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置服务端的ip地址
    host = "192.168.80.136"
    # 设置端口
    port = 40006
    # 连接服务端
    client.connect((host, port))
    print("按q键结束连接服务器! 退出程序")
    # while循环是为了保证能持续进行对话
    while True:
        # 输入发送的消息
        sendmsg = input("请输入:")
        # 如果客户端输入的是q，则停止对话并且退出程序
        if sendmsg == 'q':
            break
        sendmsg = sendmsg

        # 发送数据，以二进制的形式发送数据，所以需要进行编码
        client.send(sendmsg.encode("utf-8"))
        msg = client.recv(1024)

        # 接收服务端返回的数据，需要解码
        print("收到:", msg.decode("utf-8"))

    # 关闭客户端
    client.close()

# 文件传输模块
def file():
    filename = input('请输入要传输的文件名:\n')
    filesize = str(os.path.getsize(filename))
    fname1, fname2 = os.path.split(filename)
    # 创建一个客户端的socket对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置服务端的ip地址
    host = "192.168.80.136"
    # 设置端口
    port = 40005
    # 连接服务端
    client.connect((host, port))
    f = open(filename, 'rb')
    count = 0
    flag = 1
    while True:
        if count == 0:
            client.send(filesize.encode())
            start = time.time()
            client.recv(1024)
            client.send(fname2.encode())
        for line in f:
            client.send(line)
            print('正在发送......')
            # client.send(b'end')
            client.send(b' ')


        break
        client.close
    #计算发送所用时间
    end = time.time()
    print('所用时间:' + str(round(end - start, 2)) + 's')

if __name__=="__main__":
    print("请输入相应功能实现:")
    print("1:打开聊天窗口")
    print("2:传输文件")
    print("q:退出程序")
    print("="*30)
    while True:
        res = str(input())
        if res == "1":
            chat()
        elif res == "2":
            file()
        if res == "q":
            break
        else:
            break






