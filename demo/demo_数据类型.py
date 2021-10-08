
'''
python中的五大标准数据类型
    -Number 数字型
    -String 字符串
    -List 列表
    -Tuple 元组，只读的List列表
    -Dictionary 字典
'''


''' Number数据类型 '''
counter = 100 #整型，python3x之后，移除了long,当int溢出后会自动转为为long
plural = 3 + 6j #复数
miles = 1000.0 #浮点型


'''String 字符串'''
name = 'John' #字符串 


#字符串下标正序从0开始，倒序从-1开始
#字符串下标取值 [first:last]   --> first~last-1 的字符串

s = 'abcde'
print(s[1:4])  # bcd 取下标 1 ~ 3 的字符，正序取值

'''
[start:end:step]

 [:] 提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串
 [start:] 从start 提取到结尾
 [:end] 从开头提取到end - 1
 [start:end] 从start 提取到end - 1
 [start:end:step] 从start 提取到end - 1，每step 个字符提取一个

 左侧第一个字符的位置/偏移量为0，右侧最后一个字符的位置/偏移量为-1
'''

print("逆序输出-->" + s[-1:-len(s)-1:-1]) #逆序输出



'''List 列表'''

# “+”： 拼接运算符
# “*”：重复操作
list = ['test', 789, 2.32, 2+3j]
tinyList = [123,'ruiqiang']

print(list)
print(list[0])
print(list[0:3])
print(list[0:])
print(tinyList *2)
print(list + tinyList)

'''Tuple 元组，只读的list列表'''

tuples = ('rrr', 'xxx', 'cccc')

print(tuples[0:])


'''dictionary 字典----------------*'''

dict = {}
dict['one'] = 'this is one'
dict[2] = 'this is two'

tinyDict = {'name': 'test', 'code': 6734, 'dept': 'sales'}

print(dict['one']) # 输出键为'one'的值
print(dict[2])     # 输出键为 2 的值
print(tinyDict)    # 输出完整的字典
print(tinyDict.keys())#输出所有键
print(tinyDict.values())#输出所有值






