# -----------------------------
# 创建客户端
# -----------------------------
from socket import *
# 1.创建套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 2.准备连接服务器，建立连接
serve_ip = "服务器端（主机B）的IP"
serve_port = 8000  #端口，比如8000
tcp_socket.connect((serve_ip,serve_port))  # 连接服务器，建立连接,参数是元组形式
#准备需要传送的数据
send_data = "今天是2021年08月29日，Kolbey给服务器端发送数据了"
tcp_socket.send(send_data.encode("gbk")) 
#从服务器接收数据
#注意这个1024byte，大小根据需求自己设置
from_server_msg = tcp_socket.recv(1024)
#加上.decode("gbk")可以解决乱码
print(from_server_msg.decode("gbk"))  
#关闭连接
tcp_socket.close()


# -----------------------------
# 创建服务器
# -----------------------------
from socket import  *
#创建套接字
tcp_server = socket(AF_INET,SOCK_STREAM)
#绑定ip，port
#这里ip默认本机
address = ('',8000)
tcp_server.bind(address)
# 启动被动连接
#多少个客户端可以连接
tcp_server.listen(128)  
#使用socket创建的套接字默认的属性是主动的
#使用listen将其变为被动的，这样就可以接收别人的链接了
# 创建接收
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
client_socket, clientAddr = tcp_server.accept()
# client_socket用来为这个客户端服务，相当于的tcp_server套接字的代理
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
# 这里clientAddr存放的就是连接服务器的客户端地址
#接收对方发送过来的数据
from_client_msg = client_socket.recv(1024)#接收1024给字节,这里recv接收的不再是元组，区别UDP
print("接收的数据：",from_client_msg.encode("gbk"))
#发送数据给客户端
send_data = client_socket.send("客户端你好，服务器端收到！".encode("gbk"))
#关闭套接字
#关闭为这个客户端服务的套接字，就意味着为不能再为这个客户端服务了
#如果还需要服务，只能再次重新连
client_socket.close()


# -----------------------------
# 创建客户端，实现持续通信
# -----------------------------
from socket import *
# 1.创建套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 2.准备连接服务器，建立连接
serve_ip = "服务器端（主机B）的IP"
serve_port = 8000  #端口，比如8000
tcp_socket.connect((serve_ip,serve_port))  # 连接服务器，建立连接,参数是元组形式
while True:
    send_data = input("请输入内容：")
    #send_data = "今天是2021年08月29日，Kolbey给服务器端发送数据了"
    tcp_socket.send(send_data.encode("gbk"))
    if send_data == "exit":
         break
    #从服务器接收数据
    #注意这个1024byte，大小根据需求自己设置
    from_server_msg = tcp_socket.recv(1024)
    #加上.decode("gbk")可以解决乱码
    print(from_server_msg.decode("gbk"))
#关闭连接
tcp_socket.close()



# -----------------------------
# 创建服务器，实现持续通信
# -----------------------------
from socket import  *
import time
#创建套接字
tcp_server = socket(AF_INET,SOCK_STREAM)
#绑定ip，port
#这里ip默认本机
address = ('',8000)
tcp_server.bind(address)
# 启动被动连接
#多少个客户端可以连接
tcp_server.listen(128)  
#使用socket创建的套接字默认的属性是主动的
#使用listen将其变为被动的，这样就可以接收别人的链接了
# 创建接收
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
client_socket, clientAddr = tcp_server.accept()
# client_socket用来为这个客户端服务，相当于的tcp_server套接字的代理
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
# 这里clientAddr存放的就是连接服务器的客户端地址

while True:
    #接收对方发送过来的数据
    from_client_msg = client_socket.recv(1024)#接收1024给字节,这里recv接收的不再是元组，区别UDP
    if(from_client_msg=="exit"):
        break
    print("接收的数据：",from_client_msg.decode("gbk"))
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #发送数据给客户端
    send_data = client_socket.send((str(now_time)+" 服务端：客户端你好，服务器端收到！").encode("gbk"))
    #关闭套接字
    #关闭为这个客户端服务的套接字，就意味着为不能再为这个客户端服务了
    #如果还需要服务，只能再次重新连
client_socket.close()
