n = 32
print(bin(n))
print(n.bit_length())

# print(n.bit_count())
print(dir(n))

print((1024).to_bytes(4, byteorder='big'))
print((65).to_bytes(2, byteorder='big'))

def bit_length(self):
    s = bin(self)
    s = s.lstrip('-0b')
    return len(s)

# 'in' and 'not in' operations used as subsequence testing
print('app' in 'apple')

# items in the sequence s are not copied; they are referenced multiple times
# Wow, amazing reference instead of copy examples for the sequence.
lists = [] * 3
print(lists)

listss = [[]] * 3
print(listss)
print(listss[0])
listss[0].append(3)
print(listss)

#Common Sequence operations
l1 = ['apple', 'orange', 'banbana']
l2 = ['berry', 'cherry', 'merry']

l3 = l1 + l2
print(l3)



l3 = l1[0:1:2]
print(l3)

l3 = l1 * 3
print(l3)

print(min(l1), max(l1))
print(l3.count('apple'))

# mutable sequence types operations
s = []
# s[0] = 'peach' list assignment index out of range
s.append('love')
s[0] = 'peach'
s[1:4] = l2
s.append('hary')
print(s)

s2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s2[0:10:2] = s
print(s2)

s3 = s2.copy()
print(s3)

del s3[0:10:2]
print(s2, s3)

s3.clear()
print(s3)
s3 = ['morning lina']
s3 *= 3
print(s3)

s3[0] = 'good morning, Lina'
s3.insert(0, 'Hello')
print(s3)

# QUESTIONS: why [[]] * n and [] * n follows the different rule? tricky and funny.
listss = [[]] * 3
listss[0].append(3)
listss[1].append(5)
print(listss)

s4 = [] * 3
s4.append('test')
print(s4)

s4 *= 10
print(s4)
n1 = [1, 2, 3, 4, 5]
s4[0:10:2] = n1
print(s4)
s4.pop()
print(s4)
s4.pop(0)
print(s4)
s4.remove('test')  #remove the first item from s.
print(s4)
s4.reverse()
print(s4)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  #show that duplicates have been removed

b = basket.copy()
print(b)
b.clear()
print(b)

l = ['a'], ['a', 'b', 'c']
print(l)

l = [i for i in range(0, 20)]
print(l)

l = list(range(1, 10, 2))
print(l)

l = sorted('aecba')
print(l)

l.sort(reverse=True)
print(l)

l = list(range(10))
print(l)

l = list(range(0,-11,3))
print(l)

l = list(range(0,-11,-3))
print(l)


s = '''this triple quote test
        span multi lines'''
print(s)

# only whitespace between them will be implicitly converted to a single string literal
s = "boiled" " eggs"
print(s)

s = str('abc')
print(s)

s = str('this morning I will eat\t toast and yogurt!')
print(s.capitalize())
print(s.casefold())
print(s.center(len(s) + 10, '*')) # original strsing is returned if width is less than or equal to len(s)


print(s.count('i'))
print(s.count('and'))

print(s.endswith("!"))

print(s.expandtabs(tabsize=16)) # default tabsize is 8, giving tab positions at colums 0, 8, 16

print('01\t012\t0123\t01234'.expandtabs())
print('01\t012\t0123\t01234'.expandtabs(4))
print('01\t012\t0123\t01234'.expandtabs(16))


print(s.find('!'))
print('the sum of 1 + 2 is {0}'.format(1+2))

print(s.index('I'))

print(s.isdigit())
print(s.islower())
print('     test lstrip funciton'.lstrip())
print('www.linaliu.com'.lstrip('xyz'))
print('www.linaliu.com'.lstrip('xyz.'))
print('www.linaliu.com'.lstrip('xyw.'))
print(' test rstrip  '.rstrip())
print('linaliu'.rstrip('liu'))

print('MyNameisNa na na na na'.removeprefix('My'))
print('MyNameisNa na na na'.removesuffix('na na na'))



print('1,2,3'.split(','))
print('1,2,3,4'.split(',',maxsplit=2))
print('1 2 3'.split())

print('ab c\n de fg \r kl\r\n'.splitlines())
print('ab c\n de fg \r kl\r\n'.splitlines(keepends=True))

print('#........Book title #32........'.strip('.#!  '))

print('this is book is dangerous'.title())

print('33'.zfill(5))
print('-33'.zfill(5))

s = {c for c in 'magic words abra-ca-da-bra' if c not in 'abc'}
print(s)

s = {'rainny', 'dayff'}
print(s)

s = set(['a', 'b', 'c'])
print(s)

# s = set('a', 'b', 'c')  # TypeError: set expected at most 1 argument, got 3
s = set('abcdefghijklmn')
print(s)

print(len(s))
print('x' in s)
print(s.isdisjoint('lmn'))
print(s.isdisjoint('xyz'))
print(s.issubset('abc'))

s1 = set('lina')
s2 = set('linaliu')
print(s1 <= s2)
print(s2 - s1)

s1 = set('morning')
print(s1 | s2)

print(s1.copy())
s1.add('!!!')
print(s1)
s1.remove('!!!')
print(s1)
s1.clear()
print(s1)

d = dict([('car', 6), ('bar', 3), ('tar', 4)])
print(d)

d = {x: x ** 2 for x in range(10)}
print(d)

d = {'my': 2, 'name': 4, 'is': 6, 'sker':8}
print(d)

s = str('abc')
k = list()
k.append(1)
k *= 3

d = dict(zip(s, k))
print(d)

d1 = dict(one=1, two=2, three=3)
d2 = {'one': 1, 'two': 2, 'three': 3}
d3 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(d3)
print(d1 == d2 == d3)

#dictionary operations
print('dictionary operations here:')
print(list(d1))

print(len(d1))
print(d1['one'])
print(d1.get('one'))

d1['two'] = 2
d1['three'] = 3
print(d1)

print('four' in d1)
print('Dictionary View Objects Examples:')
print(d1.values())
print(d1.keys())
print(list(d1.values()))
print(list(d1.keys()))
print(list(d1.items()))
i = iter(d1)
print(i)  #how to print iterator values?
print(list(i))
ri = reversed(d1)
print(list(ri))

i2 = d1.items()
print(i2)
print(list(reversed(i2)))

pairs = zip(d1.values(), d1.keys())
print(pairs)
print(list(pairs))

pairs = [(v, k) for (k, v) in d1.items()]
print(list(pairs))

# Other built-in Types
class test:
    value = 0

t = test()
print(dir(t))
print(t.__dict__)

# length limitations
import sys
### sys.set_int_max_str_digits(4300)  #no this function anymore

# derive(excs) returns an exception group with the sam message, but which wraps the exceptions in excs
class MyGroup(Exception):
    def derive(self, exc):
        return MyGroup(self.message, exec)

e = MyGroup('eg', [ValueError(1), TypeError(2)])

try:
    raise e
except Exception as e:
    exc = e

print(dir(exc))

# difference between del and pop in list
l = [i for i in range(0, 20)]
print(l)
del l[-1]
print(l)

l = [i for i in range(0, 20)]
print(l)
l.pop()
print(l)

print(list(reversed(l)))

s = """
# What is CSV(Comma Separated Values)?
# Comma Separated Values format is the most common import and export format for spreadsheets and databases.
# The CSV module implements classes to read and write tabular data in CSV format.
# Coder like say: write this data in the format preferred by Excel.
# Coder like say: read data from this file which was generated by Excel, without knowing the precise details of the CSV
# format used by EXCEL.

# The csv module's reader and writer objects read and write sequences.
# 4000 个测试工作，400个完成。
# 提交好之后，会有300多个测试工作，check CI编译选项没有enable，cmake
# CI哪些会做testing。代码问题。
# high level 分所有GRPC， 外界各种不同格式，CSV，JSON格式，PRotocol BUff, native format 支持，framework转为内部格式，到streamstore，就是个log
# append过来kayaklog一一昂，进入stream做processing， 给sequence number integer 64 number， stream store ： 两种模式native，kayaklog，
# streamprocessing， 还有一个 background processing， historical http / S3支持， post processing 的格式样子，点查，secondary index，
# 字符串差一个error message historical processing 支持的多一些，支持compressing 高效一些。flow string，目前手动制定primary and secondary index, 提高效率
# 会在restAPI有各种不同的background 定时的去run，按照大时间戳做sorting，很快完成， ： rest-API/ddl-service.yaml, primary index 多个key 放一起sorting，merging ，差起来效率搞，
# ttl expression SECONDARY EXPRESSION, secondary index 针对column的，skipping——index就是secondary-index
# RESTAPI是SQL子集，

#historical 复杂，merge，compression，merge越来越大，会很高效，mergerlevel每merge一次效率搞一次。
# 文件系统压力很大，对CPU压力大，merge同时rebuild 复杂。

# post-processing 可以配置，可以有时间delay，默认2秒，内存hold住，以块方式放入，量大也会flush，每5秒刷一次，每record刷一次。
# data collection , reinjection 的过程，基本没有format process，
# 数据进来后，sequence number commit到historical store ， 如果程序crash，会回溯
# 后面在文件系统看一下，sequence number很重要，数据会不会丢失，重叠，
# pure historical data 块，没有依赖，
# 如果是一个小时前数据到现在数据，到history store 捞，效率更高，
# stream 是一个append only的log，优势很快，
# historical 查1000条数据，要mapping， sequence number会起作用。
# query processing pipeline 最复杂，是一个粘合的实现，combine stream和historical query。
# stateful 的差别。融合代价很大的话会separate实现。
# aggregator 什么时候separate什么时候不separate

# stream store mana data, provoke 一个string，还没有convert一起。
# native log rependa
# native log play一个什么样的role，先进native log， fresh data buffer。
# 快速的buffer，enable stream processing。0 - 1000 到historical sorting，enablestream processing
# data native log historical data所有东西。
# stream first 平台，

# stream data query 还有一个不同的模式，我可以又一个option，整个 turn off掉
# 用户可以turn off stream 和historical，直接进memory，pure data processing，storeage mode 立刻查询，出结果，performance 高效
# 大部分用户不会turn off

# processing stream 可以是multi shards =3 三个在同一个机器里面
# 一个系统中有多少个，文件系统的结构长什么样的。
# Create stream test（int , string) 3
# insert into test(i,3)
#insert 3 times, run robin 做的
# 文件系统中有个data目录，所有的数据都在里面，
#symoblink data he metadata: 容易查询，其实两个混在一起的。
#每个stream user ID， 其实symolink store 里面
# 最终用户是 data 目录 default cd test
# commit_sn.txt 很重要 用年月日做pre index, sequence number 有特殊含义。
# 2个insert生成两个folder，historical 对小文件data 不友好，你会发现很多小文件里面，这就是 stream store存在的意义。
# data 有没有corruption，有多少column在里面，Count有多少数据，

# sequence number  3部分， version； 0-1；
# partition 有不同的 commit——SN perally lazy mode 和sequence——sn 不同。系统重启的时候recollection

# 2个问题，每个folder都有column文件是因为支持stream改变的，background processing 大量塞文件，结尾后者0，或者是1， 或者是2是指merge的次数。
# data要做merge，2的merge，是两个sequencenumber merge到一起，merge之后，之前目录删掉。

# 目录结构： 所有代码在src mulu, function he arregfunction 代码量最大，是容易理解的。
# native log 卡法卡 log 容易理解
# parsing 数据进来先做
# server： 暴露不同TCP/HTTP/GRPC/TCP都在server下面。
# Server parser 语法树，create 不同最重要的是，一一对应的interpreter，最主要的interpretselectsql, day to day job bug 在里面，
# QUery pipeline 调用哪个函数，执行这个sql, query plan 最终到 Excutor,
# stream processing 里面，transform call哪个function，把所有
# format 支持超多。

# testing 比较 core data structure. storage 容易理解
# sql 定义， data ，各种不同的继承的类，每个强相关 column一一对应，存在文件系统的都是column
# serialism， column， block 文件系统下面，

# column 组合，Idata column name
"""

s = s.replace('#', '')
print(s)

