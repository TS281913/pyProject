######################### open返回一个文件对象

'''
    a: 追加模式打开文件，指针在文件末尾，
'''
appendfile = open("e:/test.txt", "a")
appendfile.write("This is a test file. append")
appendfile.close()


'''
    w: 写入模式打开文件，指针在文件开头，会删除原有内容
'''
writefile = open("e:/test.txt", "w")
writefile.write("This is a test file. write")
writefile.close()

'''
    r：只读模式打开文件，指针在文件开头，这是open的默认打开模式
'''
readfile = open("e:/test.txt", "r")
str = readfile.read()
print(str)
readfile.close()


###################### pickle 模块,实现对象序列化，反序列化
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]

output = open('d:\data.pkl', 'wb')
'''
    有3种协议，索引0为ASCII，1为旧式二进制，2为新式二进制协议，不同之处在于2要更高效一些
        默认为0
        当为负数或者HIGHEST_PROTOCOL时，则为最高协议
'''
pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)
output.close()


inObj = open('d:\data.pkl', 'rb')
obj = pickle.load(inObj)
print(obj)
obj = pickle.load(inObj)
print(obj)
# obj = pickle.load(inObj)
# print(obj)
#解决index问题，在最后加一个字典参数，代表有多少个对象，或者在最前面加
inObj.close()
