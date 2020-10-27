# import time
# def copy_tu(filename):
#     learing_fr = open(filename, 'rb')
#     new_learing = "%s-%s-%s.jpg" % time.localtime()[:3]
#     fw = open(new_learing, "wb")
#     while True:
#         data = learing_fr.read(1024)
#         if not data:
#             break
#         fw.write(data)
#     learing_fr.close()
#     fw.close()
# copy_tu("linux.jpg")
import  time
def copy(name):
    fr=open(name,"rb")
    new_fr="%s-%s-%s.jpg "%time.localtime()[:3]
    fw=open(new_fr,"wb")
    while True:
        data=fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()
copy("linux.jpg")