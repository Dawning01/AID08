#写方式打开文件
# file01=open("file01.txt","w")
# file01=open("file01.txt","a")

file01=open("file01.txt","w")

#写入内容
# n=file01.write("国庆,七天，庆佳节快乐\n".encode())
# print("写入了%d个字符"%n)
# n=file01.write(b"hello")
# print("写入了%d个字符"%n)

#将列表逐个写入
data=["嗯哼，你好棒棒哦","那各么里"]# \n \n
file01.writelines(data)
print(file01)

#关闭
file01.close()