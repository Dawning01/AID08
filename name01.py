# print("22").sleep(2)
# print("djnmds")
# print("jkdfkd")
#
# print("jkj").sleep(3)
# print("jfkj")
#打开文件
# file=open("file.txt", "w")
# file=open("file.txt","rb")
# file=open("file.txt", "a")
# file=open("69c6dbd16b02aaa4e09766ed1d78389f.jpeg", "rb")
file=open("file.txt", "r")

#读文件
# # print(file)
# data=file.read(5)
# print(data)
# #不重新打开接着读
# data=file.read()
# print(data)

# while True:
#     data=file.read(2)
#     if not data:
#         break
#     print(data,end="")
# readline:每次读一行
# data=file.readline(2)
# print(data)
# readlines; 每次读取多`行 字符串读到那一行就把 这“一行跟之前的"全读完
# data=file.readlines(15)
# print(data)

# 循环读取，将每行内容，
for line in file:
    print(line)


#关闭文件
file.close()