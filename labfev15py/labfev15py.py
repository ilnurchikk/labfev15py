##########################################
# class Fib:
#     def __init__(self, nn):
#         print("__init__")
#         self.__n = nn #########приватные изменение
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#     def __iter__(self):
#         print("__iter__")
#         return self
#     def __next__(self):
#         print("__next__")
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret переменные
#         return ret
# for i in Fib(10):
#     print(i)
###########################################
# class Fib:
#     def __init__(self, nn):
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#     def __iter__(self):
#         print("Fib iter")
#         return self
#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 +self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
# class Class:
#     def __init__(self, n):
#         self.__iter =Fib(n)
#     def __iter__(self):
#         print("Class iter")
#         return  self.__iter;
# object = Class(20)
# for i in object:
#     print(i)

#########################9стр
def fun(n):
    for i in range(n): ##итый элемент
        return i
print(fun(5))

####################################
def powersOf2(n):
    pow = 1
    for i in range(n):
        yield pow ########генератор
        pow *= 2
t = [x for x in powersOf2(10)] ####список выражении list
print(t)
########################################

def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)

##############################################

def powersOf2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2
t = list(powersOf2(3))
print(t)


#####################################стр 11

def powersOf2 (n):
    pow = 1 ###1
    for i in range(n):
        yield pow ###генератор
        pow *= 2 ## *  в квадрате
for v in powersOf2(8):
    print(v)

#############################стр13

def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n
fibs = list(Fib(10))
print(fibs)
#######################
lst = []
for x in range(10):
    lst.append(1 if x % 2 == 0 else 0)
print(lst)

#############################
lstt = [1 if x % 2 == 0 else 0 for x in range(10)]

print(lstt)

############################### функция

two = lambda: 2
sqr = lambda x: x * x ######параметр
pwr = lambda x, y: x ** y
for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

divid_two = lambda x: x / 2
divid_two(10)
def divid(x):
    return x / 2
print(divid(10))
################################## map список
list1 = [x for x in range(5)]
list2 = list(map(lambda x: 2 ** x, list1))
print(list2)
for x in map(lambda x: x * x, list2):
    print(x, end="  ")
###############################################
ls = [1, 2, 3, 4]
lss = list(map(lambda x: x * 2, ls))
print(ls)
print(lss)

##################################filter true список

lsss = [1, 2, 3, 4]
lssss = list(filter(lambda x: x > 0 and x % 2 != 0, lsss))
print(lsss)
print(lssss)

####################################замыкание closure0702


def outer(par):
    loc = par
    print(loc)
var = 1
outer(var)
print(var)
###############################################
for i in range(4):
    print(i)
print(i)
############################
def outer(par):
    loc = par
    def inner():
        return loc
    return inner
var = 1
fun = outer(var)
print(fun())
######################################

def makeclosure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

fsqr = makeclosure(2)
fcub = makeclosure(3)
fromq = makeclosure(4)
for i in range(6):
    print(i, fsqr(i), fcub(i), fromq(i))