
def check_dict(word):
    dictionaries = open("dict.txt", "r")
    #查找单词
    for line in dictionaries:
        #提取单词和解释
        tmp=line.split(" ",1)
        #如果
        if word in line:
            if word ==tmp[0]:
                return  tmp[1].strip()


print(check_dict("a"))

    # while True:
    #     data=dictionaries.readline()
    #     if not data:
    #         break
    #     return data



