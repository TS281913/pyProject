'''
    List列表的数据结构
'''

arr = [1, 2, 3, 4, 5, 6, 7]
# 作为堆栈，后入先出
arr.append(123)   # 将参数添加到list末尾，相当于堆栈顶
arr.pop() # 弹出list末尾的最后一位，后入先出


#列表推导式
vec = [1, 2, 3, 4, 5, 6, 7]
newVec = [3*x for x in vec] # 通过简单的运算生成新list,[3, 6, 9, 12, 15, 18, 21]
newVec = [[x, x**2] for x in vec] # [[2, 4], [4, 16], [6, 36]]
print(newVec[0:])

#列表推导式同样适用于,字符串list
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit] #['banana', 'loganberry', 'passion fruit']

#列表推导式还能用if作为条件
[3*x for x in vec if x > 3] #[12, 18]

# del语句，使用 del 语句可以从一个列表中依索引而不是值来删除一个元素
del arr[0] #删除单个数据
del arr[:] #删除全部数据



