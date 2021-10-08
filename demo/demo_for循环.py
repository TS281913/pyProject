
arr = ['banana', 'apple', 'mango']

# 循环list
for item in arr:
    print(item)
    
# 循环字符串中的字符char
for c in arr[0]:
    print(c)

print('end')

# 通过序列索引迭代
for index in range(len(arr)):
    print('当前item --> %s' %arr[index])