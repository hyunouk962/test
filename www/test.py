#!/usr/bin/python
#from asyncio.windows_events import NULL
#from curses.ascii import isupper
def print_r(str,ttt,sum = ''):
    return print(ttt(str),'===',str,sum)
import keyword
print(keyword.kwlist)
#separator 옵션
print('P','Y','T','H','O','N',sep='')
print('010','1234','1234',sep='')
print('Welcom to',end=' ')
print('IT News',end=' ')
print('Web Site')
#file 옵션
import sys
print('Learn Python',file=sys.stdout)

print('==format==')
# format 사용(d,s,f)
# d = 정수(3) ,s = 문자('python') , f = 실수(3.145123654)
print('%s %s' % ( 'one','two') )
print('{} {}'.format('one1','tow2'))
print('{1} {0}'.format('one','two'))
#%s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))
print('{:_>10}'.format('nice'))
print('%.5s' % format('nice'))
print('%.5s' % format('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))
#%d
print('%d %d' %(1,2))
print('{} {}'.format(1,2))
print('%4d' % (423))
print('{:4d}'.format(423))
#%f
print('%f' % (3.144896153563))
print('{:f}'.format(3.144896153563))
#익스 프레션
print('%06.2f' % (3.154653463763))
print('{:06.2f}'.format(3.154653463763))
print('==format==')

print('==변수==')
#변수
#변수 할당 설명
#object Identity
#예약어

n=700
print(n)
print(type(n))
x = y= z= 500
print(x,y,z)
var = 75
var ='change'
print(var)
print(type(var))
#object References
#변수 값 할당 상태 
# 예1)
print(300)
print(int(300))
# 예2)
n = 777
print(n,type(n))
m = n

#id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print()
#인터프리터 파이썬 엔진
m = 800
n = 800
print(id(m))
print(id(n))
print()
#다양한 변수 선언
#CameL Case     numberOfCollegeGraduates ->Method
#Pascal Case    NumberOfCollegeGraduates ->Class
#Snake Case     number_of_college_graduates ->변수 네임

#예약어는 변수 명으로 불가능
#for,class는 예약어 이미 지정된 명령어므로 변수 지정이 불가능하다.

print('==변수==')
print('==숫자형==')
#숫자형
#파이썬 지원 자료형
"""
int 정수
float 실수
complex 복소수
bool 불린
str 문자열(시퀀스)
list 리스트(시퀀스)  배열
tuple 튜플(시퀀스) 
set 집합
dict 사전 = 딕셔너리(key:value)방식
complex  복소수
"""
#데이터 타입ll
str11 = "python"
boo1l = True
str22 = 'Anaconda'
float11 = 10.0 # 10 == 10.0
int11 = 7
list11 = [str11,str22]
dict11 = {
    "name":"Machine Learing",
    "version":2.0
}
tuple1 = (7,8,9)
set1 = {7,8,9}
#숫자형
"""
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) x ** y -> 2 ** 3
"""
#정수 선언
i = 77
ii = -15
big_int = 154534534345343243243243243
#실수
f = 0.999
f2 = 3.154541
f3 = -3.945
f4 = 3/9
print(f)
print(f2)
print(f3)
print(f4)
#연산 실습
i1 = 39
i2 = 939
big_int1 = 5135564156132432432432
big_int2 = 5135564156132432432432
f1 = 1.234
f2 = 3.954
print(">>>>>>+")
print("i1 * i2",i1*i2)
print("f1 * f2",f1*f2)
print("big_int1 * big_int2",big_int1*big_int2)
#형변환 실습
a = 3.
b = 6
c = .7
d = 12.7
print_r(a,type)
print_r(b,type)
print_r(c,type)
print_r(d,type)

print_r(b,float)
print_r(c,int)
print_r(d,int)
print_r(True,int)
print_r(False,float)
print_r(3,complex)
print_r('3',complex)

#수치 연산 함수
print(abs(-7))
x,y = divmod(100,8)#나누기
print(x,y)
print(pow(5,3),5 ** 3)# 5의 3승
#외부 모듈
import math
print(math.ceil(5.1))#x 이상의 수중에서 가장 작은 정수(올림)
print(math.pi)
print('==변수==')
print('==문자형==')
#문자형
#문자열 생성
text3 = "I am Python"
text3_1 = 'Python'
text3_2 = """"How are you?"""
text3_3 = '''Thank you'''
print_r(text3,type)
print_r(text3_1,type)
print_r(text3_2,type)
print_r(text3_3,type)
print_r(text3,len)
print_r(text3_1,len)
print_r(text3_2,len)
print_r(text3_3,len)

#빈문자열
text3_t1 = ''
text3_t2 = str()#고급표현 좀더 명확하게 선언
print_r(text3_t1,type)
print_r(text3_t1,len)
print_r(text3_t2,type)
print_r(text3_t2,len)
#이스케이프 문자 사용
#I'm
"""
\n : 줄바꿈
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : Null 문자
"""
print('I\'m Boy')
print('I\\m Boy')
print('a \t b')
print('a \n b')
print('a \"\" b')
print('a\\b')
#Raw String
text3_s1 = r'D:\python\test'
print(text3_s1)
#멀티라인 입력
#역슬러시 \ 넣으면  파이썬은 \뒤에 값이 있다라고 인식해서 종료 시키지 않고 읽어옴
multi_str = \
"""
문자열
멀티라인 입력
테스트
"""
print(multi_str)
#문자열 연산 시퀀스란?
text3_o1 = "python"
text3_o2 = "Apple"
text3_o3 = "HOW are you doing"
text3_o4 = "Seoul Deajeon Busan"
print(text3_o1*3)
print(text3_o1 + text3_o2)
print('y' in text3_o1)
print('z' in text3_o1)
print('P' not in text3_o2 )
#문자열 형 변환 
print_r(str(66),type)
print_r(str(True),type)

#문자열 함수 (upper,isalumn,startswith,count,endswith,isalpha 등등)
print("Capitalize : ",text3_o1.capitalize())
print("endswith : ",text3_o1.endswith("s"))
print("endswith : ",text3_o3.replace("HOW","test"))
print("sorted : ",sorted(text3_o1))
#반복(시퀀스)
im_text3 = "Good Boy!"
print(dir(im_text3))#__iter__
#출력
for i in im_text3:
    print(i)

#슬라이싱 연습
str_sl = "Nice Python"
print(str_sl[0:3])
print(str_sl[5:])
print(str_sl[:len(str_sl)])
print(str_sl[1:4:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])
#아스키 코드
a='z'
print(ord(a))
print(chr(122))
print('==문자형==')
print('==리스트,튜플==')
#파이썬 리스트(배열)

#리스트 자료형(순서,중복,수정,삭제)
#선언[리스트](튜플){딕셔너리}
a = []
b = list()
c = [70,75,80,85]
d = [1000,10000,'apple','base']
e = [1000,10000,['apple','base']]
f = [21.42,'footer',3,4,False,3.149]
print(d[2])
#슬라이싱
print(d[0:3])
#값 비교
print(c == c[:3] + c[3:])
#identity(id)
temp = c
print(temp,c)
print(id(temp))
#리스트 수정삭제
c[0] = 4
print(c)
c[1:2] = ['a','b','c']
#c[1:2] = [['a','b','c']]
print(c)
c[1] = ['a','b','c']
print(c)
c[1:3] = ''
del c[2] #삭제
#리스트 함수
aaaa = [5,2,3,1,4]
print(aaaa)
aaaa.append(10)
print(aaaa)
aaaa.sort()
aaaa.reverse()
print(aaaa)
print(aaaa.index(3),aaaa[3])
aaaa.insert(2,7)
print(aaaa)
aaaa.reverse()
print(aaaa)
aaaa.remove(4)
print(aaaa)
print(aaaa.pop())
print(aaaa)
print(aaaa.pop())
print(aaaa)
print(aaaa.count(4))
ex = [8,9]
aaaa.extend(ex)
print(aaaa)
#반복문
while aaaa:
    data = aaaa.pop()
    print(data)

# 튜플
#선언[리스트](튜플){딕셔너리}
#튜플자료형(순서 중복 수정X ,삭제X) 불변
a = ()
b = (1,)
c = (11,12,13,14)
d = (100,1000,'Ace','Base')
e = (100,1000,('Ace','Base','tets'))

#인덱싱
print(d[1])
print(d[1]+d[1]+d[1])
print(e[-1])
print(e[-1][1])
print(list(e[-1][1]))
#수정X
#슬라이싱
print(d[0:3])
print(d[2:])
print(e[2][1:3])
print('==리스트,튜플==')
print('==팩킹 & 언팩킹==')
#팩킹 & 언팩킹
#팩킹
t = ('foo','bar','baz','qux')
print(t)
#언팩킹 ()괄호 없어도 됨
(x1,x2,x3,x4) = t
print_r(x1,type)
print_r(x2,type)
print_r(x3,type)
print_r(x4,type)
print('==팩킹 & 언팩킹==')
print('==딕셔너리==')
#파이썬 딕셔너리
#딕셔너리 자료형(순서X,키 중복X ,수정 삭제)
#선언[리스트](튜플){딕셔너리}
dic1 = {
    'Name':'kim',
    'City' : 'Seoul'
    }
dic2 = dict([
    ('Name','kim'),
    ('City' , 'Seoul')
])
dic3 = dict(
    Name ='kim',
    City = 'Seoul'
)
#dic1,dic3 이 주로 쓰임
#자바 는 map,웹에서는 json ,php 연관배열(associative array, hash, dictionary)
print(dic1)
print(dic2)
print(dic3)
print_r(dic1,type)
print_r(dic2,type)
print_r(dic3,type)
#출력
print(dic2)
print(dic2['Name'])
print(dic2.get('Name1'))
#딕셔너리 추가
dic3['asdasdasd'] = 'sesese'
print(dic3)
#키값 확인
print(dic1.keys())
print(list(dic1.keys()))
print(dic1.values())
print(list(dic1.values()))
print(dic1.items())
print(list(dic1.items()))
print(dic1.popitem())
print(dic1)
print('City' in dic3)
#수정
dic3['City'] = 'none'
print(dic3)
dic3.update(City='non2')
print(dic3)
tmp2 = {'City':'non3'}
dic3.update(tmp2)
print(dic3)
print('==딕셔너리==')
print('==집합==')
#집합(set)
#집합(set) 자료형(순서X ,중복X)

a = set()
b = set([1,2,3,4,4,4,])
c = set([1,8,5,4])
d = set([1,8,'zoo','pia'])
e = {'zoo','to','pia','good'}
f = {42,'to',(1,2,3),3.145}
print_r(a,type,2 in a)
print_r(b,type)
print_r(c,type)
print_r(d,type)
print_r(e,type)
print_r(f,type)
#튜플 변환 set -> tuple
t = tuple(b)
print_r(t,type)
print_r(t,type,t[1:3])
#리스트 변환set -> list
l = list(b)
print_r(l,type)
#집합 자료형 활용
s1 = set([1,2,3,4,5,6,7])
s2 = set([1,9,34,5,8,7])
#교집합
print(s1 & s2)
print(s1.intersection(s2))
#합집합
print(s1|s2)
print(s1.union(s2))
#차집합
print(s1 - s2)
print(s1.difference(s2))
#중복원소 확인
print(s1.isdisjoint(s2))
#부분집합
print(s1.issubset(s2))
print(s1.issuperset(s2))
#추가 제거
s1 = set([1,2,3,4])
#리스트 index,append
s1.add(5)
print(s1)
s1.remove(2)
#s1.remove(20)
print(s1)
s1.discard(3)
#s1.discard(20) 오류 리턴 하지않음
print(s1)
s1.clear()
print(s1)
print('==집합==')
print('==IF문==')
if True:
    print('good')

if False:
    print('bad')

sss=2
if sss == 1:
    print('false')
elif sss == 2:
    print('??')
else:
    print('good')

#관계 연산자
#>,>=,<,<=,==,!= 
e = {"name":"kim"}
f = {"con":"test"}
print("name" in e)
print("test" in f.values())

print('==IF문==')
print('==for문==')
#for문

#for in <collection>
#   <Loop body>
for v1 in range(10):
    print(v1)
    print()
for v2 in range(1,11):
    print(v2)
    print()
for v3 in range(1,11,2):
    print(v3)
sum1=0
for v4 in range(1,1001):
    sum1 += v4
print(sum1)
print(sum(range(1,1001)))
#자료형 반복
#문자열 리스트 튜플 집합 사전(딕셔너리)
#iterable 리턴함수 : range, reversed enumerate, filter , map,zip
names=['kim','pack','cho','Lee','Choi','Yoo']
for name in names:
    print(name)

lotto_number = [11,19,21,28,36,37]
for n in lotto_number:
    print(n)

word = "Beautigul"
for s in word:
    print(s)

my_info = {
    "name":"kim",
    "Age":33
}
for key in my_info:
    print(my_info[key])

for v in my_info.values():
    print(v)

name1 = 'FineApple'
for n in name1:
    if n.isupper():
        print(n)
    else :
        print(n.upper())
#break
number = [14,3,4,7,10,24,17,2,33,15,34,36,38]
for num in number:
    if num ==34:
        print('found : 34')
        break
    else:
        print('not found')

#continue
text = ["1",2,5,True,4.3,complex(4)]
for v in text:
    if type(v) is bool:
        continue
    print_r(v,type)

      
number = [14,3,4,7,10,24,17,2,33,15,34,36,38]
for num in number:
    if num ==24:
        print(num)
        break
else:
    print('not found')

#구구단
for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i * j), end ='')
    print()
#변환 예제

name2 = 'Aceman'
print('Reversed', reversed(name2) )
print( list(reversed(name2)))
print( tuple(reversed(name2)))
print( set(reversed(name2)))
print('==for문==')
print('==while문==')
#while 과 if 의 양식은 같다
#whild <expr>:
#    <statement(s)>
n=5
while n > 0:
    print(n)
    n = n - 1


a = ['foo','bar','baz']
while a:
    print(a.pop())

#brake,continue
n = 5
while n > 0:
    n -=1
    if n == 2:
        break
    print(n)
print('loop end 2')
m = 5
while m > 0:
    m -=1
    if m == 2:
        continue
    print(m)

i = 1
while i <= 10:
    print(i)
    if i ==6: 
        break
    i +=1
print('loop end 3')

#whil else
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')

a = ['foo','bar','baz','qux']
s = 'qux'
i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s,'not found in list')

a = ['foo','bar','baz']
while True:
    if not a:
        break
    print(a.pop())


print('==while문==')
print('==fontion문==')
#파이썬 함수식 및 람다(Lambda)
#함수 의 정의
#def functio_name(parameter):
#   code
xv= 10
def fun1(x):
    y1 = x*10
    y2 = x*20
    y3 = x*20
    return {'v1':y1,'v2':y2,'v3':y3}

xx = fun1(x)
print(type(xx),xx,xx.get('v1'),xx.items(),xx.keys())
#중요
#*args,**kwargs
#*args(언팩킹) 튜플
def args_func(*args): #매개변수 명 자유
    for i,v in enumerate(args):
        print('result : {}'.format(i),v)
    print('------')
args_func('Lee')
args_func('Lee','pack')


#**kwargs(언팩킹)딕셔너리
def kwargs_func(**kwargs): #매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('=====')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee',name2='pack',name3='cho')

#전체 혼합
def example(args_1,args_2,*args,**kwargs):
    print(args_1,args_2,args,kwargs)

example(10,20,'Lee','kim','Park' ,'cho',age1=10,age2=20,age3=30)

#중첩함수 클로저
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('in func')
    func_in_func(num + 100)
nested_func(100)

#람다(Lambda) 개념
#메모리 절약,가독성 향상,코드 간결
#함수는 객체 생성 -> 리소스(메모리) 할당
#람다는 즉시ㅣ 실행 함수 (Heap 초기화) -> 메모리 초기화
#너무 남발시  가독성이 감소
#def mul_func(x,y):
#    return x * y
#lambda x,y : x*y
#일반적 함수 -> 할당
def mul_func(x,y):
    return x * y
q = mul_func(10,50)
print(q)

mul_func_var = mul_func
print(mul_func_var(20,50))

#람다 함수 -> 할당
lambda_mul_func = lambda x,y:x*y
print(lambda_mul_func(20,60))

def func_final(x,y,func):
    print(x * y * func(200,100))

func_final(10,20,lambda x,y:x*y) 

print('==fontion문==')
print('==input==')
#input사용법
#기본타입(srt) => 형변환을 해준다

#name=input('enter name : ')
#grade=input('enter grade : ')
#company=input('enter company : ')
#print(name,grade,company)

#number = input('enter number : ')
#name = input('enter name : ')
#print_r(number,type,number*5)
#print_r(name,type)

#first_number = int(input('enter number1 : '))
#second_number = int(input('enter number2 : '))
#total = first_number*second_number
#print(total)

#float_number = float(input('enter a float number1 : '))
#print_r(float_number,type)

#print('firstName  - {0},LastName - {1}'.format(input("enter first name : "),input("enter last name : ")))

print('==input==')
print('==Class==')
#객체지향
#클래스 개념
#OOP (객체 지향 프로그래밍),클래스 인스턴스,SElf  인스턴스 메소드 ,클래스 인스턴스 변수
#네임스페이스 객체를 인스턴스화 할 때 저장된 공간
#클래스 변수 직접 접근 가능
#인스턴스 변수 객체마다 별도 존제
class Dog:#object 상속 Dog: ,Dog():, Dog(object)
    #클래스 속성
    species = 'firstdog'
    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
print(Dog)
#인스턴스화
a = Dog("mikky",2)
b = Dog("baby",3)
#비교
print(a == b, id(a) , id(b))
#네임스페이스
print(a.__dict__)
print(b.__dict__)
#인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name,a.age,b.name,b.age))
if a.species == 'firstdog' :
    print('{0} is a {1}'.format(a.name,a.species))

#self의 이해
class selfTest:
    def func1():
        print('func1 called')
    def func2(self):
        print(id(self))
        print('func2 called')
f = selfTest()
#print(dir(f))
print(id(f))
#f.func1() 예외
#selfTest.func1()

f.func2()
#클래스 변수 , 인스턴스 변수
class warehouse:
    #클래스 변수 
    stock_num  = 0 
    def __init__(self,name):
        self.name = name
        warehouse.stock_num +=1
    def __del__(self):
        warehouse.stock_num -=1
user1 = warehouse('Lee')
user2 = warehouse('cho')
print(warehouse.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(warehouse.__dict__)
del user1
print(warehouse.__dict__)

class Dogs:#object 상속 Dog: ,Dog():, Dog(object)
    #클래스 속성
    species = 'firstdog'
    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info (self):
        return '{} is {} years old'.format(self.name,self.age)
    def speak(self,sound):
        return '{} says {}!'.format(self.name, sound)
C = Dogs('july',4)
print(C.info())
print(C.speak('wal wal'))
print('==Class==')
print('==Module==')
#Module : 함수 변수 클래스 등 파이썬 구성요소 등을 모아놓은 파일
"""
/class/
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def power(x,y):
    return x ** y
print(add(5,5))"""
#모듈의 패키지 작성시 빈 __init__.py 를 디렉토리마다 만들어 넣어야한다.( python3.3 부터는 없어도  패키지로 인식을 하나 이전 버전은 인식못함. 하위호환을 위해 생성)
#class 의 test_mo.py 기본 module 추가 방법
#동일경로 import *,파일명
#지정 경로 from sub.sub1 import *
#지정 경로 (절대 경로,상대 경로)
"""
Absolute Path(절대 경로)
www > sub > sub1 > module1.py 라는 경로에 module이 위치하고 있다면
from sub.sub1 import module1

Relative Path(상대 경로)
sub1의 module1에서 sub1의 class1을 import (module1,class1 같은 위치)
from . import class1
dot(.)은 import가 선언된 파일의 현재 위치
될수있으면 절대 경로를 사용하기를 권장
"""

print('==Module==')