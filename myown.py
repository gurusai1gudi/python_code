'''
def sum_addition(a,b):
    return a+b
num1=4
num2=5
print(sum_addition(num1,num2))
'''
#from anyio.pytest_plugin import free_tcp_port
from prometheus_client import values

'''
from django.contrib.sitemaps.views import index
from django.core.files import temp
from numpy._core.strings import upper
from scipy.signal import max_len_seq
from sklearn.covariance import ledoit_wolf
from streamlit import title
from sympy import false
from sympy.codegen.cnodes import sizeof
from tenacity import wait_exponential_jitter
'''
'''
def int_to_str(num):
    return str(num)
a=int(input("Enter a number: "))
print(int_to_str(a))
'''
# substring
'''
s = "my name is gurusai"
substring=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        substring.append(s[i:j+1])
print(substring)
'''
from pandas.core.methods.selectn import SelectNSeries

#palindrome
'''
s="markram"
n=len(s)
is_palindrome=True
for i in range(n//2):
     if s[i]!=s[n-i-1]:
         is_palindrome=False
         break
if is_palindrome:
    print("its an palindrome")
else:
    print("it is not a palindrome")
'''

# new
'''
s ="i am an software engineer"
print(s.replace("n","e"))
'''
'''
s=input()
print(s.count("$"))
'''

#sliding window problem
'''
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result=[]
max_val = arr[0]
for i in range(0, k):
    if arr[i] > max_val:
        max_val = arr[i]
print(max_val)
result.append(max_val)
max_val = arr[1]
for j in range(1, 1 + k):
    if arr[j] > max_val:
        max_val = arr[j]
print(max_val)
result.append(max_val)
max_val = arr[2]
for m in range(2, 2 + k):
    if arr[m] > max_val:
        max_val = arr[m]
print(max_val)
result.append(max_val)
for h in range(3, 3 + k):
    if arr[h] > max_val:
        max_val = arr[h]
print(max_val)
result.append(max_val)
for g in range(4, 4 + k):
    if arr[g] > max_val:
        max_val = arr[g]
print(max_val)
result.append(max_val)
for n in range(5, 5 + k):
    if arr[n] > max_val:
        max_val = arr[n]
print(max_val)
result.append(max_val)
print(result)
'''

#sum of unique_elements
'''
n = list(map(int, input().split()))
total = 0

for i in range(len(n)):
    count = 0
    for j in range(len(n)):
        if n[i] == n[j]:
            count += 1
    if count == 1:
        total = total + n[i]
print(total)
'''
'''
def printdict():
    d={}
    for i in range(1,21):
        d[i]=i**2
    for(k,v) in d.items():
        print(v)
printdict()
'''
#tcs
'''
v=int(input())
w=int(input())
fw = (w - 2*v) // 2
tw = v-fw
print(tw,fw)
'''
#push 0s to last
'''
n=list(map(int, input().split()))
zeros=[]
for i in range(len(n)):
    if n[i]<1:
        zeros.append(n[i])
        n.pop(i)
        break
n.extend(zeros)
print(n)
'''
#toggling of a numbers
'''
n=int(input())
binary=''
while n>0:
    binary = str(n % 2)+binary
    n = n // 2
reverse=binary[::-1]
decimal=0
for digit in reverse:
    decimal = decimal*2 + int(digit)
print(decimal)
'''
#international round table
'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
factorial = 2*fact(n-1)
print(factorial)
'''
#intelligence agency
'''
n=input()
r=int(input())
sum=0
n1,n2=map(int,n.split())
for i in range(r):
    sum = sum+n1+ n2
new=str(sum)
s1,s2=map(int,new)
print(s1+s2)
'''
'''
li=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x:x%2==0,li)
print(list(even))
'''
#jack sunday
'''
start = input().strip().lower()
n=int(input())
days=["sun","mon","tue","wed","thu","fri","sat"]
start_index=days.index(start)
sundays=0
for i in range(1,n+1):
    current_day=(start_index+i)%7
    if days[current_day]=="sun":
        sundays += 1
print(sundays)
'''
#risk sorting
'''
n=int(input())
risk=[]
for i in range(n):
    risk.append(int(input()))
risk.sort()
for i in range(n):
    print(risk[i],end=" ")
'''
# prior greater count
'''
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
result=arr[0]
count=1
for i in range(1,n):
    if arr[i] > result:
        result = arr[i]
        count += 1
print(count)
'''
'''
n=int(input())
product=1
for i in str(n):
    product=product*int(i)
print(product)
'''
#max curtains
'''
s=input()
l=int(input())
max_a=0
for i in range(len(s)-l+1):
    substring=s[i:i+l]
    count=substring.count("a")
    if count>max_a:
        max_a=count
print(max_a)
'''
#rank cut
'''
n=int(input())
rank=list(map(int,input().split()))
count=0
current_best=rank[0]
for i in range(1,n):
    if rank[i] < current_best:
        current_best = rank[i]
        count += 1
print(count)
'''
#reverse a string
'''
s="GEEKFORGEEKS"
reverse_string=s[::-1]
print(reverse_string)
'''
#string rotation by d
'''
s="GEEKFORGEEKS"
d=2
for i in range(d):
    new=s[1:]+s[0]
print(new)
'''
#sort the string
'''
s="geeksforgeeks"
char=list(s)
n=len(char)
for i in range(n):
    for j in range(n-1):
        if char[j]>char[j+1]:
            char[j],char[j+1]=char[j+1],char[j]
string =''.join(char)
print(string)
'''
#longest common prefix
'''
s=["flower","flow","flight"]
prefix=""
for i in range(len(s[0])):
    c=s[0][i]
    for word in s:
        if i>len(word) or word[i]!=c:
            print(prefix)
            exit()
    prefix+=c
print(prefix)
'''
#frequency
'''
s="aabccccddd"
char=list(s)
for i in range(len(char)):
    count=0
    for j in range(i+1):
        if char[i]==char[j]:
            count+=1
    print(char[i],count)
'''
#duplicate elements
'''
n=list(map(int,input().split()))
count=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            print(n[i])
'''
#distinct elements
'''
l=int(input())
arr=[]
unique=[]
for i in range(l):
    n=int(input())
    arr.append(n)
for i in range(len(arr)):
    if arr[i] not in unique:
        unique.append(arr[i])
        print(arr[i])
'''
# k index
'''
arr=list(map(int,input().split()))
k =int(input())
new=[]
found=False
for i in range(len(arr)):
    if arr[i]==k:
      print(i)
      found=True
      break
if not found:
        for j in range(len(arr)):
            if k<arr[j]:
                arr.insert(j,k)
                print(j)
                break
'''
#heyhey
'''
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(len(a))
res = []
while a:
    word = a[0]
    group = [word]
    a.remove(word)
    i = 0
    while i < len(a):
        if sorted(word) == sorted(a[i]):
            group.append(a[i])
            a.pop(i)
        else:
            i += 1
    res.append(group)
print(res)
'''
# longest common prefix
'''
s=["flower","flow","flight"]
prefix=s[0]
for i in range(1,len(s)):
    while not s[i].startswith(prefix):
        prefix=prefix[:-1]
        if not prefix:
           break
print(prefix)
'''
#duplicates

'''
for i in range(len(s)):
    count=s.count(s[i])
    if count>1:
        dup.append(s[i])
i = 0
while i < len(dup):
    if dup.count(dup[i]) > 1:
        dup.remove(dup[i])
        continue
    i += 1
    ans = []
for ch in dup:
    l = []
    l.append(ch)
    l.append(s.count(ch))
    ans.append(l)
print(ans)
'''
#duplicates another
'''
s = "geeksforgeeks"
dup = {}

for i in range(len(s)):
    count = s.count(s[i])
    if s[i] in dup:
        continue
    if count > 1:
        dup[s[i]] = count
c=list(dup.items())
print(c)
'''
# k power factorial
'''
n = int(input())
k = int(input())
def fact(n):
    if n==0 or n== 1:
        return 1
    return n * fact(n - 1)
factorial = fact(n)
count=0
for i in range(n):
    if factorial %k.__pow__(i) == 0:
        count += 1
print(count-1)
'''
#picking numbers
'''
n = int(input())
arr = list(map(int, input().split()))
all_subarrays = []
final=[]
max_length = 0
for i in range(n):
    for j in range(i, n):
        subarray = arr[i:j+1]
        all_subarrays.append(subarray)
        final.append(all_subarrays)
for sub in all_subarrays:
    if max(sub) - min(sub) <= 1:
        if len(sub) > max_length:
            max_length = len(sub)
print(max_length)
'''
#subarray
''''
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = float('-inf')

for i in range(len(nums)):
    for j in range(i, len(nums)):
        sub_arr = nums[i:j+1]
        current_sum = sum(sub_arr)
        if current_sum > max_sum:
            max_sum = current_sum
print(max_sum)
'''
#jump game
'''
nums=[3,2,1,0,4]
found = False
first_index = nums[0]
last_index = len(nums) - 1

for i in range(first_index):
    if i + nums[i] >= last_index:
        found = True
        break

print("true" if found else "false")
'''
'''

class Computer:
    def config(self):
        print(f"CPU: {self.CPU}, RAM: {self.RAM}")

    def __init__(self, CPU, RAM):
        self.CPU = CPU
        self.RAM = RAM
        print(f"Initial config: CPU: {self.CPU}, RAM: {self.RAM}")

    def update(self):
        self.CPU = "na"
        print("CPU updated to:", self.CPU)

com1 = Computer('i5', 16)
com1.config()
com1.update()
com1.config()
'''
#tcs
'''
arr=list(map(int, input().split()))
count=1
result=arr[0]
for i in range(1,len(arr)):
    if arr[i]>result:
        count=count+1
print(count)
'''
#khohko
'''
n=int(input())
c=[]
count=0
for i in range(n):
    a=int(input())
    c.append(a)
print(c)
for j in range(1,len(c)):
    if c[j]!=c[0]:
        count+=1
print(count)
'''
#reverse a string from index2
'''
s="Hello world this is python"
res=[]
word=s.split(" ")
for i in range(len(word)):
    if i%2==0:
        res.append(word[i])
    else:
        res.append(word[i][::-1])
new=" ".join(res)
print(new)
'''
#rotate a matrix
'''
s = "geeksforgeeks"
res = []
k = 3
reverse = True
while s:
    temp = []
    for i in range(min(k, len(s))):
        temp.append(s[i])
    if reverse:
        temp.reverse()
    for ch in temp:
        res.append(ch)

    s = s[k:]
    reverse = not reverse
out=''.join(res)
print(out)
'''
#equillibrium point
'''
arr=[1,-1,2,1,-2]
total=sum(arr)
left_sum=0
for i in range(len(arr)):
    right_sum=total-left_sum-arr[i]
    if left_sum==right_sum:
        print(i)
    left_sum+=arr[i]
    break
'''

'''
arr=[1,-1,2,1,-2]
for i in range(len(arr)):
    left=sum(arr[:i])
    right=sum(arr[i+1:])
    if left==right:
        print(i)
'''
'''
arr = [6, 1, 2, 3]
count=0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i]+arr[j]) % 2==0:
            count+=1
print(count)
'''
#divisible by 7 but are not divisible by 5
'''
begin=2000
end=3200
for i in range(begin, end):
    if (i%7==0) and (i%5!=0):
        print(i,end=",")
'''
#dictionary
'''
n=8
res={}
for i in range(1,n):
    res[i]=i*i
print(res)
'''
#list and
'''
n=input()
values=n.split(",")
t=tuple(values)
l=list(values)
print(t)
print(l)
'''
#two methods
'''
class Solution:
    def __init__(self):
        self.s=""
    def getstring(self):
        self.s=input()

    def printstring(self):
        print (self.s.upper())

    def stringtolist(self):
        new=list(self.s)
        print(new)

strobject=Solution()
strobject.getstring()
strobject.printstring()
strobject.stringtolist()
'''
'''
import math
input_values=[100,150,180]
c=50
h=30
for i in range(len(input_values)):
    q=math.sqrt((2*c*input_values[i])/h)
    if i==len(input_values)-1:
        print(round(q),end="")
    else:
        print(round(q),end=", ")
'''
'''
x=int(input())
y=int(input())
result=[]
for i in range(x):
    row=[]
    for j in range(y):
        row.append(i*j)
    result.append(row)
print(result)
'''
'''
lines=[]
while True:
    s=input()
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
    print(sentence)
'''
'''
s = input()
words = s.split(" ")
dup = []
result=""
for word in words:
    if word not in dup:
        dup.append(word)

dup.sort()
result=" ".join(dup)
print(result)
'''
'''
value=[]
s=input()
items=[word for word in s.split(",")]
for i in items:
    if int(i,2)%5==0:
        value.append(i)
print(''.join(value))
'''
'''
class Person:
    name="person"
    def __init__(self,name="default"):
        self.name=name
ram=Person("ram")
print(ram.name,Person.name)
nico=Person()
nico.name="Nico"
print(Person.name,nico.name)
'''
#tcs
'''
def multiply(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = multiply(result, i)
    return result

num = int(input())
print(factorial(num))
'''
'''
nums = [1, 3, 5, 6]
target = 2
if target in nums:
    for i in range(len(nums)):
        if nums[i] == target:
            print(i)
            break
else:
    nums.append(target)
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            print(i)
            break
'''
#good number
'''
k = int(input())
for i in range(k):
    n = int(input())
    num = n
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num //= 10
    if n % sum_num == 0:
        print("Good Number")
    else:
        print("Bad Number")
'''
'''
arr=[23,44,21,2,32]
max_index=0
for i in range(len(arr)):
    if arr[i] > arr[max_index]:
        max_index = i
        print(arr[max_index])
'''
'''
list_in =list(map(int, input().split()))
for i in range(len(list_in)):
    if list_in[i]%2==0:
        print("its an even number")
    else:
        print("its an odd number")
'''
#POPPING ZEROS AT LAST
#given an array we have to choose the zeros from the array and add it to the last of the array
'''
arr=[12,0,3,8,0,1]
final=[]
zeros=[]
for i in range(len(arr)):
    if arr[i]>=1:
        final.append(arr[i])
    else:
        zeros.append(arr[i])
combined=final+zeros
print(combined)
'''
#second_largest
'''
arr=[12,35,1,10,35,34,1]
count=1
while count<=2:
    max_element=0
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    arr.remove(max_element)
    if count==2:
        print(max_element)
    count+=1
'''
#oops
'''
class Tractor:
    def __init__(self):
        pass
    def move(self,function):
        self.function=function
        return self.function
start=Tractor()
print(start.move("move forward"))
t2=start.move("move down")
print(t2)
'''
'''
class Student:
    def __init__ (self,name,roll_no,age,marks):
        self.name=name
        self.roll_no=roll_no
        self.age=age
        self.marks=marks
    def average(self,marks):
        self.marks=marks
        avg=sum(marks)/len(marks)
        return avg
s1=Student(name="John",roll_no=1,age=20,marks=[10,20,40,11])
print(s1.average(s1.marks))
'''
# palindrome
'''
name="markram"
n=len(name)
if name==name[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
    '''
#max_subarray
'''
arr=[12,35,1,10,35,34,1]
sub=[]
sum_max=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        subarray = arr[i:j+1]
        sub.append(subarray)
        if sum(subarray)>sum_max:
            sum_max=sum(subarray)
print(sum_max)
'''
'''
arr=[1,2,3]
for i in range(len(arr)):
    new=arr[i],arr[i+1:i+2]
    print(new)
'''
'''
import math
class Solution(object):
    def myPow(self,x,n):
        if n==0:
            return 1
        else:
            return float(math.pow(x,n))
x=float(input())
n=int(input())
new=Solution()
s=new.myPow(x,n)
print("{:.5f}".format(s))
'''
#class method
'''
class Student:
    name = "telusko"
    def __init__(self,rollno,id):
        self.rollno=rollno
        self.id=id
    @classmethod
    def getschool(cls):
        return cls.name
print(Student.getschool())
'''
#static method
# it is the method which does not relate to class or object it can be directly called without creating an object
'''
class Vehicle:
    def __init__(self,make,year):
        self.make=make
        self.year=year
    @staticmethod
    def info():
        print("The motor vehicle is issued under the act of law")
c1=Vehicle('red',2000)
print(c1.make,c1.year,end=" \n")
print(Vehicle.info())
'''
#inheritence
#single and multilevel
'''
class Employee:    # super class
    def emp1(self):
        print("emp1 is working")
    def emp2(self):
        print("emp2 is working")
class B(Employee):    #sub class
    def emp3(self):
        print("emp3 is working")
    def emp4(self):
        print("emp4 is working")
class c(B):
    def emp5(self):
        print("emp5 is working")
b1=B()
b1.emp1()
c1=c()
c1.emp2()
'''
#multiple inheritance
'''
class Employee:    # super class
    def emp1(self):
        print("emp1 is working")
    def emp2(self):
        print("emp2 is working")
class B:
    def emp3(self):
        print("emp3 is working")
    def emp4(self):
        print("emp4 is working")
class c(Employee,B):
    def emp5(self):
        print("emp5 is working")
b1=B()
b1.emp3()
c1=c()
c1.emp2()
'''
#polymorphism duck typing
'''
class Pycharm:
    def execute(self):
        print("execute")
class Myeditor:
    def execute(self):
        print("compile and execute")
class Laptop:
    def code(self,ide):
        ide.execute()
ide=Myeditor()
lap1=Laptop()
lap1.code(ide)
'''
#Stack
'''
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def traverse(self):
        return self.items
def is_balanced(expr):
    s=Stack()
    for char in expr:
        if char=='(':
            s.push(char)
        elif char==')':
            if s.is_empty():
                return False
            s.pop()
    return s.is_empty()
def reverse_string(text):
    s=Stack()
    for char in text:
        s.push(char)
    reversed_text=""
    while not s.is_empty():
        reversed_text=reversed_text+s.pop()
    return reversed_text

print(reverse_string('abc'))
def simulate_editor(actions):
    undo_stack = Stack()
    redo_stack = Stack()
    for action in actions:
        if action == "UNDO":
            if not undo_stack.is_empty():
                last = undo_stack.pop()
                redo_stack.push(last)
        elif action == "REDO":
            if not redo_stack.is_empty():
                last = redo_stack.pop()
                undo_stack.push(last)
        else:
            undo_stack.push(action)
            redo_stack = Stack()  # clear redo stack
    return undo_stack.traverse()

c=simulate_editor(["A", "B", "C", "UNDO", "UNDO", "REDO", "D"])
print(c)
def next_greater(arr):
    s=Stack()
    result=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while not s.is_empty() and s.peek() <=arr[i]:
            s.pop()
        if not s.is_empty():
            result[i]=s.peek()
        s.push(arr[i])
    return result
def next_smaller(arr):
    s=Stack()
    result=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while not s.is_empty() and s.peek()>=arr[i]:
            s.pop()
        if not s.is_empty():
            result[i]=s.peek()
        s.push(arr[i])
    return result
print(next_smaller([4,5,2,10,8]))
def is_valid(expr):
    s=Stack()
    match={')':'(','{':'}','[':']'}
    for char in expr:
        if char in "({[":
            s.push(char)
        elif char in ")}]":
            if s.is_empty():
                return False
            top=s.pop()
            if match[char]!=top:
               return False

    return s.is_empty()
def adjacent_dup(expr):
    s=Stack()
    for char in expr:
        if not s.is_empty() and char==s.peek():
            s.pop()
        else:
            s.push(char)
    return "".join(s.traverse())
print(adjacent_dup("abbaca"))
def min_add_to_make_para_valid(expr):
    s=Stack()
    count=0
    for char in expr:
        if char=="(":
            s.push(char)
        else:
            if not s.is_empty():
                s.pop()
            else:
                count+=1
    return count + s.size()
print(min_add_to_make_para_valid("(())("))
'''
#next greater
'''
arr=[4,5,2,25]
res=[]
for i in range(len(arr)):
    found=-1
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            found=arr[j]
            break
    res.append(found)
print(res)
'''
#search in rotated sorted arr
'''
nums=list(map(int,input().split()))
target=int(input())
target_arr=[]
new_arr=[]
for i in range(target):
    for j in range(len(nums)):
        target_arr.append(nums[j])
        nums.pop(j)
        break
nums.extend(target_arr)
new_arr=nums
print(new_arr)
'''
#queues
'''
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def traverse(self):
        return self.items
q=Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.traverse())
def generate_binary(n):
    q=Queue()
    q.enqueue("1")
    for i in range(n):
        front=q.dequeue()
        print(front,end=" ")
        q.enqueue(front+"0")
        q.enqueue(front+"1")
print(generate_binary(10))
def tickets(my_dict):
    q=Queue()
    for key,value in my_dict.items():
        q.enqueue(key)
    result=[]
    while not q.is_empty():
        person=q.dequeue()
        result.append(person)
        my_dict[person]=my_dict[person]-1
        if my_dict[person]>0:
            q.enqueue(person)
    return result
#my_dict = {"charlie": 1, "david": 2, "eve": 3}
#print(tickets(my_dict))
def rotate_k(my_arr,k):
    q=Queue()
    i=0
    for item in my_arr:
        q.enqueue(item)
    for _ in range(k):
        temp=q.dequeue()
        q.enqueue(temp)
    return q.traverse()
def rotate_first_k(arr,k):
    q=Queue()
    new=[]
    for item in arr:
        q.enqueue(item)
    for _ in range(k):
        temp=q.dequeue()
        new.append(temp)
    new=new[::-1]
    new.extend(q.traverse())
    return new
print(rotate_first_k([10,20,30,40,50,60,70],4))
'''
#minimum size subarray
'''
nums=list(map(int,input().split()))
target=int(input())
sub_arr=[]
min_sub=None
min_len=float('inf')
for i in range(len(nums)):
    for j in range(i,len(nums)):
        sub_arr.append(nums[i:j+1])
for arr in sub_arr:
    if sum(arr)>=target:
        if len(arr)<min_len:
            min_len=len(arr)
            min_sub=arr
if min_sub:
    print(min_sub)
    print(min_len)
else:
    print("not found")
'''
#move negatives to end
'''
arr = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(arr)
i = 0
steps = 0

while steps < n:
    if arr[i] < 0:
        temp = arr.pop(i)
        arr.append(temp)
    else:
        i += 1
    steps += 1
print(arr)
'''
#linked list
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head1=None
        self.head2=None
    def append_at_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def print_ll(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
    def append_at_first(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def remove(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
    def get_length(self):
        count=0
        current=self.head
        while current:
            count=count+1
            current=current.next
        return count
    def search_value(self,data):
        current=self.head
        while current:
            if current.data==data:
                return 1
            current=current.next
        return 0
    def reverse(self):
        temp=[]
        current=self.head
        while current:
            temp.append(current.data)
            current=current.next
        current=self.head
        while current:
            current.data=temp.pop()
            current=current.next
    def sum_elem(self):
        if self.head is None:
            return
        sum=0
        current=self.head
        while current:
            sum=sum+current.data
            current=current.next
        return sum
    def max_elem(self):
        if self.head is None:
            return None
        max=0
        current=self.head
        while current:
            if current.data>max:
                max=current.data
            current=current.next
        return max
    def find_middle(self):
        if self.head is None:
            return None
        slow,fast=self.head,self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
l1=LinkedList()
l1.append_at_first(1)
l1.append_at_first(2)
l1.append_at_first(3)
l1.append_at_first(2)
l1.append_at_first(1)
print(l1.sum_elem())
print(l1.max_elem())
print(l1.find_middle())
'''

#coin change
''''
coins = [1, 2, 3]
target = 4
count = 0
def Ways(total, start):
    global count
    if total == target:
        count += 1
        return
    if total > target:
        return

    for i in range(start, len(coins)):
        Ways(total + coins[i], i)
Ways(0, 0)
print(count)
'''
'''
input="(()())(())"
match={'(':')'}
for i in range(len(input)-1):
    if input[i] in match and input[i+1] == match[input[i]]:
        print(f"{input[i]}{input[i+1]}",end="")
'''
#ocurrence of digit in range
'''
digit=1
count=0
for i in range(1,20):
    if (i%10==digit) or (i//10==digit):
        count+=1
print(count)
'''
#possible number of decodings
'''
n=int(input())
a=str(n)
substring=[]
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        substring.append(a[i:j+1])
        count=count+1
print(count)
'''
#jewels and stones
'''
jewels="aA"
stones="aAAbbbb"
count=0
for i in range(len(jewels)):
    for j in range(len(stones)):
        if stones[j]==jewels[i]:
            count+=1
print(count)
'''
#count the number of consistent strings
'''
allowed="ab"
words=["ad","bd","aaab","baa","badab"]
count=0
for word in words:
    flag=True
    for char in word:
        if char not in allowed:
            flag=False
            break
    if flag:
        count+=1
print(count)
'''
#remove adjacent duplicates in a string
'''
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def traverse(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def adjacent_dup(expr):
    s=Stack()
    for char in expr:
        if s.peek()==char:
            s.pop()
        else:
            s.push(char)
    return s.traverse()
print(*adjacent_dup("abbaca"))
'''
#maximum repeating string
'''
sequence="ababc"
word="ab"
count=0
print(len(word))
for i in range(len(sequence)):
    if sequence[i:i+len(word)] ==  word:
        print(sequence[i:i+len(word)])
        count+=1
print(count)
'''
#revrese the sentence
'''
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def traverse(self):
        return self.items
def reverse_sentence(expr):
    s=Stack()
    temp=[]
    for word in expr.split():
        s.push(word)
    while not s.is_empty():
        temp.append(s.pop())
    return temp
print(*reverse_sentence("the sky is blue"))
'''
'''
s=input()
vowels=['a', 'e', 'i', 'o', 'u']
count1=0
count2=0
mid=(len(s)//2)
first_one=s[:mid]
second_one=s[mid:]
for char in first_one:
    if char in vowels:
        count1+=1
for char in second_one:
    if char in vowels:
        count2+=1
if count1==count2:
    print("True")
else:
    print("False")
'''
#
'''
n=int(input())
fact=0
for i in range(n+1):
    fact=fact*i
print(fact)
'''
#
'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
'''
#armstrong number
'''
n=int(input())
origin=n
temp=0
while n>0:
    last_digit=n%10
    temp=temp+last_digit**len(str(origin))
    n=n//10
if temp==origin:
    print("armstrong")
else:
    print("not an armstrong")
'''
#decode nested encoded string
'''
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def traverse(self):
        return self.items
def decode_nested_string(string):
    s=Stack()
    for char in string:
'''
#anagrams
''''
a=input()
b=input()
count=0
for char in set(a+b):
    count+=abs(a.count(char)-b.count(char))
print(count)
'''
#balanced substrings
'''
a = "00110011"
substring = []

for i in range(len(a)):
    for j in range(i+1, len(a)):
        sub = a[i:j+1]
        if sub.count("0") == sub.count("1"):
            half = len(sub) // 2
            if sub[:half] == "0" * half and sub[half:] == "1" * half:
                substring.append(sub)
            elif sub[:half] == "1" * half and sub[half:] == "0" * half:
                substring.append(sub)

print(len(substring))
print(substring)
'''
# salutes exchanged by soldiers
'''
n=">><<"
count=0
for i in range(len(n)):
    if n[i]==">":
        for j in range(i+1, len(n)):
            if n[j]=="<":
                count+=1
print(count)
'''
#sort words by embedded numbers
'''
input=["is2","a3","Th1is"]
result=[]
while len(input)>0:
    min_word=input[0]
    for word in input:
        for i in word:
            if i.isdigit():
                if int(i) < int([ch for ch in min_word if ch.isdigit()][0]):
                    min_word=word
    result.append(min_word)
    input.remove(min_word)
print(*result)
'''
#happy numbers in range
'''
n1 = int(input())
n2 = int(input())
result = []
for num in range(n1, n2 + 1):
    temp = num
    while temp != 1 and temp!=4:
        sum_of_sq=0
        while temp>0:
            digit = temp%10
            sum_of_sq += digit**2
            temp = temp//10
        temp=sum_of_sq
    if temp == 1:
        result.append(num)
print(*result)
'''
#product of array excluding the current index
''''
arr=[1,2,3,4]
result=[]
for i in range(len(arr)):
    mul=1
    for j in range(len(arr)):
        if i!=j:
            mul*=arr[j]
    result.append(mul)
print(*result)
'''
#pyramid pattern
'''
n = int(input())
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
#check two strings are permutations
'''
a=input()
b=input()
mine=False
for char in set(a+b):
    if a.count(char)==b.count(char):
        mine=True
    else:
        mine=False
if mine:
    print("True")
else:
    print("False")
'''
#score of balanced paranthesis
'''
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def traverse(self):
        return self.items
def score_balanced(expr):
    count=0
    s=Stack()
    for char in expr:
        if char=='(':
            s.push(char)
        elif char==')':
            if not s.is_empty():
                s.pop()
                count+=2
    print(count)
print(score_balanced("(()"))
'''
#stick cutiing problem
'''
n=int(input())
final=[]
arr=list(map(int,input().split()))
final.append(n)
while arr:
    shortest=min(arr)
    temp=[]
    for i in range(len(arr)):
        new=arr[i]-shortest
        if new>0:
            temp.append(new)
    arr=temp
    if arr:
        final.append(len(arr))
print(*final)
'''
#Alice and Bob's Challenge Ratings
'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count_a=0
count_b=0
for i in range(len(a)):
    if a[i]>b[i]:
        count_a+=1
    elif a[i]<b[i]:
        count_b+=1
    elif a[i]==b[i]:
        continue
print([count_a,count_b])
'''
#page-turning problem
'''
n=int(input())
p=int(input())
page_turns_from_first=0
page_turns_from_last=0
#from first onwards
for i in range(1,n,2):#from 1-2,3-4.....
    if i+1>=p:
        break
    page_turns_from_first+=1
# from last onwards
if n%2==0:#if it is even
    start=n-1
else:#if odd
    start=n
for i in range(start,0,-2):
    if i-1<=p:
        break
    page_turns_from_last+=1
print(page_turns_from_first,page_turns_from_last)
s=min(page_turns_from_first,page_turns_from_last)
print(s)
'''
#minimun number of platforms required for a railway station
'''
arrivals=list(map(int,input().split()))
departures=list(map(int,input().split()))
max_platforms=0
for i in range(len(arrivals)):
    platforms_needed=1
    for j in range(len(arrivals)):
        if i!=j:
            if arrivals[i]<departures[j] and arrivals[j]<departures[i]:
                platforms_needed+=1
    if platforms_needed>max_platforms:
        max_platforms=platforms_needed
print(max_platforms)
'''
#group anagrams in a list of string
'''
arr = ["eat","tea","tan","ate","nat","bat"]
result = []

while arr:
    compare = arr[0]
    new = []

    for word in arr[1:]:
        if sorted(word) == sorted(compare):
            new.append(word)

    arr = [word for word in arr if word not in new and word != compare]
    group = [compare] + new
    result.append(group)
print(result)
'''
#Cognizant Genc
'''
litres=int(input())
distance=int(input())
if litres<=0:
    print(litres,"is a invalid input")
elif distance<=0:
    print(distance,"is an invalid input")
else:
    fuel_consumption=(litres/distance)*100
    miles=(distance*0.6214)
    gallons=(litres*0.2642)
    miles_per_gallon=miles/gallons
    print("Litres/100km:%.2f"%fuel_consumption)
    print("Miles/gallons:%.2f"%miles_per_gallon)
'''
#vohra amount
'''
pizza=int(input())
puffs=int(input())
cool_drinks=int(input())
total_sum=(100*pizza)+(20*puffs)+(10*cool_drinks)
print("BILL DETAILS")
print("No of pizzas:",pizza)
print("No of puffs:",puffs)
print("Cool drinks:",cool_drinks)
print("Total price=",total_sum)
print("Enjoy the show!!!!")
'''
# Ascii value
'''
n = int(input())
result = ""
for i in range(n):
    digits = int(input())
    form = chr(digits)
    result += str(digits) + " " + form + "\n"
print(result.strip())
'''
# Highest Placement
'''
CSE = int(input("Enter the no of students placed in CSE: "))
ECE = int(input("Enter the no of students placed in ECE: "))
MECH = int(input("Enter the no of students placed in MECH: "))

if CSE == ECE == MECH:
    print("All branches have the same placement:", CSE)

elif CSE >= ECE and CSE >= MECH:
    if CSE == ECE:
        print("Highest Placement in CSE and ECE:", CSE)
    elif CSE == MECH:
        print("Highest Placement in CSE and MECH:", CSE)
    else:
        print("Highest Placement in CSE:", CSE)

elif ECE >= CSE and ECE >= MECH:
    if ECE == MECH:
        print("Highest Placement in ECE and MECH:", ECE)
    else:
        print("Highest Placement in ECE:", ECE)

else:
    print("Highest Placement in MECH:", MECH)
'''
# Median of two sorted arrays same size
'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
c.sort()
mid=len(c)//2
median=(c[mid-1]+c[mid])//2
print(median)
'''
# sort the stack using recursion
'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def traverse(self):
        return self.items


# Insert element into sorted stack
def sorted_insert(stack, element):
    if stack.is_empty() or element > stack.peek():
        stack.push(element)
    else:
        temp = stack.pop()
        sorted_insert(stack, element)
        stack.push(temp)


# Recursively sort the stack
def sort_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, temp)


# Example usagex
s = Stack()
s.push(5)
s.push(2)
s.push(9)
s.push(1)
s.push(6)

print("Original stack:", s.traverse())
sort_stack(s)
print("Sorted stack:", s.traverse())
'''
#profit of a chef
'''
A,B,C=map(int,input().split())
total_cp_chef=B+C
selling_price=A
if selling_price>total_cp_chef:
    profit = selling_price-total_cp_chef
    print("Profit:",profit)
else:
    loss=selling_price-total_cp_chef
    print("Loss:",loss)
'''

#checking special characters
'''
str="welcome to python programming"
substring="pyt"
num=True
for char in substring:
    if char not in str:
        num=False
        break
if num:
    print("correct substring")
else:
    print("incorrect substring")
'''
#longest consecutive sequence
'''
input=[100,4,200,1,3,2]
new=sorted(input)
print(new)
count=1
max_count=1
for i in range(len(new)-1):
    if new[i+1] - new[i] ==1:
        count=count+1
    elif new[i+1] - new[i] >1:
        count=1
    max_count=max(max_count,count)
print(max_count)
'''
# weight of the string
'''
input1 = [15,16,1,2,-13,6,1,11,4,3,19,-4,17,-3,90,-65,67,12,0,13,2,3,4,3,21,-17]
input2 = "Wipro Limited"
alphabets_weight={}
for i in range(26):
    letter=chr(65+i)
    weight=input1[i]
    alphabets_weight[letter]=weight
all_words=[]
for word in input2.split():
    weight=[]
    for i,letter in enumerate(word):
        if letter.upper() in alphabets_weight:
            if(i==0 or i==len(word)-1) and alphabets_weight[letter.upper()]<0:
                alphabets_weight[letter.upper()]+=(ord(letter.upper())-(65)+1)
            weight.append(alphabets_weight[letter.upper()])
    sum_weight = 0
    for char_weight in weight:
        sum_weight += char_weight
    all_words.append(sum_weight)
mul=1
for char in all_words:
    mul=mul*char
print(mul)
'''
#Problem
'''
def is_prime(num):
    if num == 1:
        return False
    for j in range(2, num):
        if num % j == 0:
            return False
    return True
n = int(input())
arr = list(map(int,input().split()))[:n]
new=[]
for i in range(n):
    if is_prime(arr[i]):
        new.append(arr[i])
new1=max(new)
new.remove(new1)
sum=0
for value in new:
    sum=sum+value
print(sum)
'''
#minimum cost
'''
total_books_required=int(input())
x_bundle,x_cost=map(int,input().split())
y_bundle,y_cost=map(int,input().split())
min_cost=float('inf')
for i in range(total_books_required):
    for j in range(total_books_required):
        if i*x_bundle + j*y_bundle ==total_books_required:
            new = i*x_cost + j*y_cost
            min_cost=min(min_cost,new)
print(min_cost)
'''
#parity of a string
'''
string=input()
count=0
new=[]
for char in string:
    if char not in new:
        new.append(char)
        count=count+1
if count%2==0:
    print("it is an even string")
else:
    print("it is an odd string")
'''
#sum of diagonal of a matrix
'''
elements=list(map(int,input().split()))
row,col=elements[0],elements[1]
matrix=elements[2:]
new=[]
for i in range(row):
    for j in range(col):
        if i==j:
            new.append(matrix[i*col+j])
print(sum(new))
'''
#
'''
import string
String=input()
Key_value=int(input())
alphabet=string.ascii_lowercase
cipher=""
for char in String.lower():
  if char in alphabet:
    new_index=(alphabet.index(char)+Key_value)%26
    cipher+=alphabet[new_index]
  else:
    cipher+=char
print(cipher)
'''
#
'''
n,m=map(int,input().split())
new=[]
for i in range(1,m):
  if m%i==0 and n%i==0:
    new.append(i)
print(max(new))
'''
'''
n = int(input())
matrix = []
mid=n//2
for i in range(n + 1):
    row = []
    for j in range(n):
        if  0<i<n and j==mid:   
            row.append(str(i))
        else:
            row.append(str(n))
    matrix.append(row)

for r in matrix:
    print("".join(r))
'''
#longest substring
'''
s=input()
substring=[]
count=0
max=0
largest_substring=""
for i in range(len(s)):
    sub=""
    count=0
    for j in range(i,len(s)):
        if s[j] not in sub:
            sub+=s[j]
            substring.append(sub)
            count+=1
            if count>max:
                max=count
                longest_substring=sub
        else:
            break
print(substring)
print(longest_substring)
print(max)
'''
#level1
#basic array&strings
'''
a=input()
n=len(a)
d=list(a)
for i in range(n//2):
    temp=d[i]
    d[i]=d[n-i-1]
    d[n-i-1]=temp
print(*d,end="")
'''
#check if a string is palindrome
'''
a=input()
n=len(a)
mine=False
for i in range(n//2):
    if a[i]==a[n-i-1]:
        mine=True
    else:
        mine=False
if mine:
    print("it is a palindrome string")
else:
    print("it is not a palindrome string")
'''
#remove duplicates from the sorted array
'''
arr=[1,2,2,4]
new_arr=[]
for i in range(len(arr)):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])
print(*new_arr)
'''
#second largest in the array
'''
arr=[1,4,5,6,1]
for i in range(2):
    max=0
    max_index=0
    for j in range(len(arr)):
        if arr[j]>max:
            max=arr[j]
            max_index=j
    if i==1:
        print(max)
    arr.pop(max_index)
'''
#first non repeating character in a string
'''
a="swiss"
count=0
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if i!=j and a[i]==a[j]:
            count+=1
    if count==0:
        print(a[i])
        break
'''
#anagrams
'''
str1="listen"
str2="silent"
found=True
for i in range(len(str1)):
    match=False
    for j in range(len(str2)):
        if str1[i]==str2[j]:
            match=True
            break
    if not match:
        found=False
        break
if found==True:
    print("anagram")
else:
    print("not anagram")
'''
#linked list
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def print_list(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
        print("None")
    def reverse(self):
        temp=[]
        current=self.head
        while current:
            temp.append(current.data)
            current=current.next
        temp.reverse()
        print(temp)
ll=LinkedList()
ll.append(3)
ll.append(2)
ll.append(1)
ll.reverse()
'''
#majority element\
'''
n=list(map(int,input().split()))
same_element=[]
for i in range(len(n)):
    count=0
    if n[i] not in same_element:
        same_element.append(n[i])
        for j in range(len(n)):
            if n[i]==n[j]:
                count+=1
        if count>len(n)//2:
            print(n[i],count)
'''
#missing and repeated values
'''
grid = [[9,1,7],[8,9,2],[3,4,6]]
new = []
re = []
all_ele = []

for i in range(len(grid)):
    for j in range(len(grid)):
        all_ele.append(grid[i][j])
        if grid[i][j] in new:
            re.append(grid[i][j])  # repeated element
        else:
            new.append(grid[i][j])
   # only the number
new.sort()
missing = None
for i in range(len(new)-1):
    if new[i+1] - new[i] != 1:
        missing = new[i] + 1
        break
print("Missing:", missing)
if missing is None:
    missing=new[-1]+1
print([*re,missing])
'''
# Merge sorted array
'''
m=int(input())
n=int(input())
nums1=[]
nums2=[]
for i in range(m):
    nums1.append(int(input()))
nums1+=[0]*n
for j in range(n):
    nums2.append(int(input()))
for i in range(n):
    nums1[m+i]=nums2[i]
nums1.sort()
print(nums1)
'''
#Contains Duplicate
'''
nums=list(map(int,input().split()))
add_list=[]
boolean=False
for i in range(len(nums)):
    if nums[i] in add_list:
        boolean=True
    else:
        add_list.append(nums[i])
if boolean==True:
    print("true")
else:
    print("false")
'''
#chocolate distribution problem
'''
arr=list(map(int,input().split()))
m=int(input())
arr.sort()
new=[]
for i in range(len(arr)-m+1):
    group=arr[i:i+m]
    for j in range(len(group)-m+1):
        new.append(group[len(group)-1]-group[0])
print(min(*new))
'''
# maximum subarray
'''
nums=list(map(int,input().split()))
subarray=[]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        subarray.append(nums[i:j+1])
print(subarray)
max_sum=float('-inf')
max_arr=float('-inf')
for value in subarray:
    total=0
    for i in value:
        total+=i
    if total>max_sum:
        max_sum=total
        max_arr=value
print(max_sum,max_arr)
'''
#next permutation
'''
arr = [1, 2, 3]
pivot = -1
for i in range(len(arr)-2, -1, -1):
    if arr[i] < arr[i+1]:
        pivot = i
        break
if pivot != -1:
    next_bigger = float('inf')
    next_bigger_index = -1
    for j in range(pivot+1, len(arr)):
        if arr[pivot] < arr[j] < next_bigger:
            next_bigger=arr[j]
            next_bigger_index=j
    arr[pivot],arr[next_bigger_index]=arr[next_bigger_index],arr[pivot]
left=pivot+1
right=len(arr)-1
while left<=right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(*arr)
'''
#Best time to buy and sell stock
'''
arr=list(map(int,input().split()))
best_buy=min(arr)
buy_index = arr.index(best_buy)
best_sell=0
for i in range(buy_index+1,len(arr)):
    if arr[i]>best_sell:
        best_sell=arr[i]
profit=best_sell-best_buy
print(profit)
'''
#
'''
class Solution:
    def repeatedNumber(self, A):
        out=[]
        repeated=None
        for i in range(len(A)):
            if A[i] in out:
                repeated=A[i]
            else:
                out.append(A[i])
        out.sort()
        missing=None
        for j in range(len(out)-1):
            if out[j+1]-out[j]!=1:
                missing=out[j]+1
                break
        return [repeated,missing]
s=Solution()
print(s.repeatedNumber([3,1,2,5,3]))
'''
#kth largest element in the array
'''
nums=list(map(int,input().split()))
k=int(input())
for i in range(k):
    max_val=float('-inf')
    max_index=-1
    for j in range(len(nums)):
        if nums[j]>max_val:
            max_val=nums[j]
            max_index=j
    if i==k-1:
        print(max_val)
        break
    nums.pop(max_index)
'''
# product of array expect self
'''
nums=list(map(int,input().split()))
mul=1
new=[]
for i in range(len(nums)):
    mul=1
    for j in range(len(nums)):
        if j==i:
            continue
        mul=mul*nums[j]
    new.append(mul)
print(new)
'''
#maximum product subarray
'''
arr=list(map(int,input().split()))
max_product=float('-inf')
max_subarray=float('-inf')
for start in range(len(arr)):
    subarray=[]
    product=1
    for end in range(start,len(arr)):
        subarray.append(arr[end])
        print(subarray)
        product*=arr[end]
        if product>max_product:
            max_product=product
            max_subarray=arr[start:end+1]
print(max_product)
print(max_subarray)
'''
#contain with the most water
'''
height=list(map(int,input().split()))
max_area=0
for i in range(len(height)):
    stick1=height[i]
    for j in range(i+1,len(height)):
        stick2=height[j]
        h=min(stick1,stick2)
        width=j-i
        Area=h*width
        if Area>max_area:
            max_area=Area
print(max_area)
'''
#longest substring without repeating characters
'''
s="abcabcbb"
max_count=0
max_substring=""
for start in range(len(s)):
    substring=[]
    new=[]
    for end in range(start,len(s)):
       if s[end] in new:
           break
       new.append(s[end])
       substring.append(s[end])
    count=0
    for i in range(len(substring)):
        count+=1
        if count>max_count:
            max_count=count
            max_substring=substring
print(max_count)
print(max_substring)
'''
#longest repeating character replacement
'''
s=input()
k=int(input())
longest_count=float('-inf')
longest_length=float('-inf')
longest_char=""
count=0
for start in range(len(s)):
    substring=[]
    for end in range(start,len(s)):
        substring.append(s[end])
    for char in substring:
        count=substring.count(char)
        if count>longest_count:
            longest_count=count
            longest_char=char
    changes_needed=len(substring)-longest_count
    if changes_needed<=k:
        if len(substring)>longest_length:
            longest_length=len(substring)
print(longest_length)
'''
# group anagrams
'''
str=input().split()
i=0
while i<len(str):
    first_char=str[i]
    anagrams=[first_char]
    for j in range(i+1,len(str)):
        if sorted(str[j])==sorted(str[i]):
            anagrams.append(str[j])
    if anagrams:
        print(*anagrams)
        for word in anagrams[1:]:
            str.remove(word)
        i+=1
'''
#longest palindromic Substring
'''
s = input()
longest_substring=""
for start in range(len(s)):
    substring = ""
    for end in range(start, len(s)):
        substring+=s[end]
        if substring==substring[::-1]:
            if len(substring)>len(longest_substring):
                longest_substring=substring
print(longest_substring)
'''
#smallest window containing all characters
'''
s=input()
p=input()
answer=""
for start in range(len(s)):
    substring=""
    for end in range(start,len(s)):
        substring+=s[end]
        valid=True
        for i in p:
            if i not in substring:
                valid=False
                break
        if valid:
            if answer=="" or len(substring)<len(answer):
                answer=substring
print(answer)
'''
# Function to generate all permutations
'''
def permute(prefix, remaining):
    if len(remaining) == 0:
        length_of_prefix = len(prefix)
        numbers = range(length_of_prefix)
        numbers_as_strings = []
        for i in numbers:
            numbers_as_strings.append(str(i))
        indices = " ".join(numbers_as_strings)
        print(prefix, "(INDEX:", indices, ")")

    else:
        for i in range(len(remaining)):
            ch = remaining[i]
            new_remaining = remaining[:i] + remaining[i+1:]
            permute(prefix + ch, new_remaining)
s = "ABC"
s = ''.join(sorted(s))  
permute("", s)
'''
#dice problem
# Take D1, D2, Q as input
# Dice problem correct version
'''
D1, D2, Q = map(int, input().split())

d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))

for _ in range(Q):
    v = int(input())  # take new query each time
    count = 0
    for a in d1:
        for b in d2:
            if a + b == v:
                count += 1
    print(count)
'''
#Titans
'''
n=int(input())
values=""
for j in range(n):
    values=(int(input()))
for m in range(n):
    if  (n*n) - (m*m)== values:
        print(n,m)
    else:
        print(-1)
'''
#next permutation
'''
arr=list(map(int, input().split()))
pivot=-1
for i in range(len(arr)-2,-1,-1):
    if arr[i]<arr[i+1]:
        pivot=i
        break
if pivot !=-1:
    next_bigger=float('-inf')
    next_bigger_index=-1
    for j in range(pivot+1,len(arr)):
        if arr[pivot]<arr[j] and  arr[j]<arr[next_bigger]:
            next_bigger=arr[j]
            next_bigger_index=j
    arr[pivot],arr[next_bigger_index]=arr[next_bigger_index],arr[pivot]
left=pivot+1
right=len(arr)-1
while left<=right:
    arr[left],arr[right]=arr[right],arr[left]
'''
# camel case matching
'''
queries = list(map(str, input().strip().split()))
pattern = input()
for word in queries:
    i = 0
    match = True
    for char in word:
        if i < len(pattern) and char == pattern[i]:
            i += 1
        elif (char.isupper
             ()):
            match = False
            break
    if match and i == len(pattern):
        print("true")
    else:
        print("false")
'''
# wild string matching pattern
'''
def match(wild, pattern):
    if len(wild) == 0:
        if len(pattern) == 0:
            return True
        else:
            return False
    if wild[0] == '*':
        match_zero = match(wild[1:], pattern)
        match_one_or_more = False
        if len(pattern) > 0:
            match_one_or_more = match(wild, pattern[1:])
        return match_zero or match_one_or_more

    if len(pattern) > 0 and wild[0] == '?':
        return match(wild[1:], pattern[1:])

    if len(pattern) > 0 and wild[0] == pattern[0]:
        return match(wild[1:], pattern[1:])

    return False
w=input()
a=input()
print(match(w,a))
'''
# tranform one string to another using minimum number of given operations
'''
def convert(A, B):
    count = 0
    A = list(A)
    B = list(B)
    i = len(A) - 1
    j = len(B) - 1
    while i >= 0:
        if A[i] == B[j]:
            j -= 1
        else:
            count += 1
        i -= 1
    return count
string1 = input()
string2 = input()
print(convert(string1, string2))
'''
#count palindromic subsequences
'''
s=input()
substring=[]
list=[]
count=0
for i in range(len(s)):
    for j in range(i,len(s)):
        substring.append(s[i:j+1])
for sub in substring:
    if sub == sub[::-1]:
        list.append(sub)
        count += 1
print(*list)
print(count)
'''
#word wrap
'''
def min_cost(arr,k):
    dp=[0]*(len(arr)+1)
    for i in range(len(arr)-1,-1,-1):
        dp[i]=float('inf')
        total_len=0
        for j in range(i,len(arr)):
            total_len+=arr[j]
            if j>i:
                total_len+=1
            if total_len>k:
                break
            if j==len(arr)-1:
                cost=0
            else:
                cost=(k-total_len)**2
            dp[i]=min(dp[i],cost+dp[j+1])
    return dp[0]
a=list(map(int, input().split()))
s=int(input())
print(min_cost(a,s))
'''
# swap odd - eve
'''
arr=list(map(int, input().split()))
for i in range(len(arr)//2):
    if (arr[i]%2==0 and arr[len(arr)-1-i]%2!=0) or (arr[i]%2!=0 and arr[len(arr)-1-i]%2==0):
        arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
print(*arr)
'''
#minimum window substring
'''
s=input()
t=input()
substring=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        sub=s[i:j+1]
        if all(ch in sub for ch in t):
            substring.append(sub)
if substring:
    min_sub=min(substring,key=len)
    print(min_sub)
else:
    print("no substring")
'''
# half pyramid
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
'''
# inverted right half pyramid
'''
n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
'''
#inverted left half pyramid
'''
n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end="")
    print()
'''
#left half pyramid pattern
'''
n=int(input())
for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
'''
#pyramid pattern
'''
n=int(input())
for i in range(n+1):
    for j in range(n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
'''
# inverted full pyramid
'''
n=int(input())
for i in range(1,n):
    for j in range(i-1):
        print(" ",end="")
    for j in range(1,2*(n-i)):
        print("*",end="")
    print()
'''
# half diamond star pattern
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for j in range(n-1,0,-1):
    for k in range(j):
        print("*",end="")
    print()
'''
# diamond shape
'''
n=int(input())
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
for k in range(n):
    for j in range(k):
        print(" ",end="")
    for i in range(n-k):
        print("*",end=" ")
    print()
'''
#alphabet A using stars
'''
n = int(input("Number of lines: "))
for i in range(n):
    for j in range(n):
        if i == 0 and j > 0 and j < n - 1:
            print("*", end="")
        elif i == n // 2:
            print("*", end="")
        elif (j == 0 or j == n - 1) and i != 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''
# program to print solid and hollow sphere
'''
n=int(input())
print("Solid Square:")
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
print("Hollow Square:")
for i in range(n):
    for j in range(n):
        if i!=0 and i!=n-1 and j!=0 and j!=n-1:
            print(" ",end="")
        else:
            print("*",end="")
    print()
'''
#prime check or not
'''
n=int(input())
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("it is not a prime")
            break
    else:
        print("it is a prime")
else:
    print("no prime")
'''
# range of prime
'''
n=int(input())
for i in range(2,n):
    for j in range(2,int(i**0.5)+1):
        if i%j==0 and i!=j:
            break
    else:
        print(i)
'''
#top 50 code
## reverse a number
'''
n=int(input())
string="%s"%n
print(string[::-1])
'''
#fibonacci series upto nth term
'''
n=int(input())
a,b=0,1
print(a,b,end=" ")
for i in range(n):
    c = a + b
    print(c,end=" ")
    a,b=b,c
'''
#gcd
'''
n1 = int(input())
n2 = int(input())

n1divisors = []
n2divisors = []
common = []

for i in range(1, n1 + 1):
    if n1 % i == 0:
        n1divisors.append(i)

for j in range(1, n2 + 1):
    if n2 % j == 0:
        n2divisors.append(j)

for num in n1divisors:
    for num2 in n2divisors:
        if num == num2:
            print(num2, end=" ")
            
            common.append(num2)

print("\n",max(common))
'''
#perfect number
'''
n=int(input())
number=str(n)
sums=[]
sum=0
for i in range(1,len(number)):
    if n%i==0:
        sums.append(number[i])
for char in sums:
    sum+=int(char)
if sum==number:
    print("yes")
'''
#strings are anagram or not
'''
str1=input()
str2=input()
if all(char in str2 for char in str1):
    print("anagram")
else:
    print("no")
'''
#palindrome
'''
str=input()
if all(str[i] == str[len(str) - 1 - i] for i in range(len(str) // 2)):
    print("yes")
else:
    print("no")
'''
#frequency of char in string
'''
s = input("Enter string: ")
new = []

for char in s:
    if char not in new:      
        count = 0
        for c in s:          
            if c == char:
                count += 1
        new.append(char)
        print(char, count)
'''
# wildcard characters
'''
pattern=input()
string=input()
match=True
for i in range(len(pattern)):
    if i>len(string):
        match=False
    if pattern[i]=='?':
        continue
    elif pattern[i]=="*":
        break
    elif pattern[i]!=string[i]:
        match=False
for j in range(i,len(string)):
    if i < len(pattern) and pattern[i]=='*':
        match=True
        break
    else:
        match=False
if match and (len(string) == len(pattern) or '*' in pattern):
    print("Yes")
else:
    print("No")
'''
#bubble sort
'''
list=list(map(int, input().split()))
for i in range(len(list)):
    for j in range(0,len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(*list)
'''
#leap year
'''
n=int(input())
if n%4==0 and n%100!=0 or n%400==0:
    print("yes")
else:
    print("no")
'''
# non repeating in string
'''
n=input()
s=n
non_repeat=[]
for char in n:
    if char not in non_repeat:
        count=0
        for c in s:
            if c==char:
                count+=1
        non_repeat.append(char)
        if count==1:
            print(char)
'''
#replace a substring in a string
'''
str1=input()
str2=input()
str3=input()
result=str1.replace(str2,str3)
print(result)
'''
# code to replace each element in array
'''
arr=list(map(int, input().split()))
new=sorted(arr)
for i in range(len(arr)):
    for j in range(len(new)):
        if arr[i]==new[j]:
            arr[i]=j+1
            break
print(*arr)
'''
# circular rotation of array by k positions
'''
arr=list(map(int,input().split()))
k=int(input())
while k>=1:
    new = arr[-1]
    arr.pop(-1)
    arr.insert(0, new)
    k -= 1
print(*arr)
'''
# non repeating elemetns in array
'''
arr=list(map(int,input().split()))
s=arr
non_repeat=[]
char1=[]
for char in arr:
    if char not in non_repeat:
        count=0
        for c in s:
            if c==char:
                count+=1
        if count==1:
            char1.append(char)
print(*char1)
'''
#
'''
arr = input().split()  
max_count = 0
max_palindrome = ""

for char in arr:
    if char == char[::-1]:  # check if palindrome
        if len(char) > max_count:
            max_count = len(char)
            max_palindrome = char

print(max_palindrome)
'''
#factorial of a number
'''
n=int(input())
fact=1
for i in range(1,n+1):
    fact *= i
print(fact)
'''
# armstrong number
'''
n=int(input())
number=str(n)
power=len(number)
sum=0
for i in range(len(number)):
    sum+=int(number[i])**power
if n==sum:
    print("yes")
else:
    print("no")
'''
#sum of natural numbers using recursion
'''
def sum_of(n):
    if n==1:
        return 1
    return n+sum_of(n-1)
a=int(input())
print(sum_of(a))
'''
# add matrix
'''
rows=int(input())
cols=int(input())
matrix1=[]
matrix2=[]
for i in range(rows):
    row1=list(map(int,input().split()))
    matrix1.append(row1)
for j in range(rows):
    row2=list(map(int,input().split()))
    matrix2.append(row2)
sum_matrix=[]
for i in range(rows):
    row_sum=[]
    for j in range(cols):
        row_sum.append(matrix1[i][j]+matrix2[i][j])
    sum_matrix.append(row_sum)
for row in sum_matrix:
    print(*row)
'''
# binary to decimal conversion
'''
n=int(input())
new=str(n)
sum=0
for i in range(len(new)):
    digit=int(new[i])
    power=len(new)-1-i
    sum+=digit*(2**power)
print(sum)
'''
#Automorphic number
'''
n=int(input())
square= n**2
if square%(10**len(str(n)))==n:
    print("autophormic")
else:
    print("ben")
'''
# Ascii value of a char
'''
char=input()
ascii_val=ord(char)
print(ascii_val)
'''
# remove all from string except alphabets
'''
string=input()
string2=""
for char in string:
    if (ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122):
        string2+=char
print(string2)
'''
#smallest element in an array
'''
arr=list(map(int,input().split()))
min_ele=arr[0]
for i in range(len(arr)):
    if arr[i]<min_ele:
        min_ele=arr[i]
print(min_ele)
'''
#reverse the element of an array
'''
arr=list(map(int,input().split()))
n=len(arr)
for i in range(n//2):
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
print(*arr)
'''
#code to sort the elements in the array
'''
arr=list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)
'''
#Replace substring in a string
'''
input1=input()
input2=input()
input3=input()
result=input1.replace(input2,input3)
print(*result)
'''
#code to remove space in a string
'''
str=input()
new=""
for char in str:
    if char==" ":
        continue
    new+=char
print(new)
'''
#code to count inversion
'''
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j] < arr[i]:
            count += 1
            print(arr[i], arr[j])
print(count)
'''
#consecutive largest subsequence
'''
arr=list(map(int,input().split()))
new=sorted(arr)
max_count = 1
count=1
longest_sequence=[new[0]]
temp_seq=[new[0]]
for i in range(len(new)-1):
    if new[i+1]-new[i]==1:
        count+=1
        temp_seq.append(new[i+1])
    elif new[i+1]-new[i]!=1:
        count=1
        temp_seq=[new[i+1]]
    if count>max_count:
        max_count=count
        longest_sequence=temp_seq[:]
print(max_count)
print(longest_sequence)
'''
# add two fractions
'''
num1, den1 = map(int, input("Enter first fraction (numerator denominator): ").split())
num2, den2 = map(int, input("Enter second fraction (numerator denominator): ").split())
numerator = num1 * den2 + num2 * den1
denominator = den1 * den2
print(numerator,"/",denominator)
'''
# roots of quadratic equation
'''
import math
a,b,c=map(int,input().split())
if a==0:
    print("invalid")
d=b*b-4*a*c
sq=math.sqrt(abs(d))
if d>0:
    print("real")
    print((-b + sq) / (2 * a))
    print((-b - sq) / (2 * a))
elif d == 0:
    print("Roots are real and same")
    print(-b / (2*a))
else:
    print("complex")
    print(- b / (2 * a), " + i", sq)
    print(- b / (2 * a), " - i", sq)
'''
#prime factorials of a number
'''
n = int(input("Enter a number: "))
num = n
factors = []
while num % 2 == 0:
    factors.append(2)
    num //= 2
i = 3
while num != 1:
    while num % i == 0:
        factors.append(i)
        num //= i
    i += 2 

print(f"Prime factors of {n} are: {factors}")
'''
#convert digits into words
'''
from num2words import num2words
num=input()
for char in num:
    print(num2words(int(char)))
'''
#fibonacci using recursion
'''
def fibo(n):
    if n<0:
        print("Negative number")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
def fibo_series(n):
    if n<=0:
        print("Negative number")
    else:
        for i in range(n):
            print(fibo(i),end=" ")
n=int(input())
print(fibo(n))
print(fibo_series(n))
'''
# aremovable indices
'''
st1=input()
st2=input()
for i in range(min(len(st1), len(st2))):
    if st1[i] != st2[i]:
        char=st1[i]
        for j in range(len(st1)):
            if st1[j] == char:
                print(j, end=" ")
        break
'''
# merge sort
'''
def merge_sort(arr):
    mid=len(arr)//2
    left_half= arr[:mid]
    right_half=arr[mid:]
    merged=[]
    i=j=0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i+=1
        else:
            merged.append(right_half[j])
            j+=1

    merged.extend(left_half[i:])
    merged.extend(right_half[j:])
    print(merged)
print(merge_sort([223,5567,333,112,234,344]))
'''
#add two matrices
'''
row=int(input())
cols=int(input())
matrixA=[]
matrixB=[]
final=[]
for i in range(row):
    row1=list(map(int,input().split()))
    matrixA.append(row1)
for j in range(row):
    row2=list(map(int,input().split()))
    matrixB.append(row2)
total=[]
for i in range(row):
    for j in range(cols):
        total.append(matrixA[i][j]+matrixB[i][j])
print(total)
'''
#bigger is greater
'''
n=int(input())
for i in range(n):
    string=list(input())
    pivot=-1
    for i in range(len(string)-2,-1,-1):
        if string[i]<string[i+1]:
            pivot=i
            break
    if pivot!=-1:
        next_bigger=-1
        for j in range(pivot+1,len(string)):
            if string[j]>string[pivot]:
                if next_bigger==-1 or string[j]<string[next_bigger]:
                    next_bigger=j
        string[pivot],string[next_bigger]=string[next_bigger],string[pivot]
    left=pivot+1
    right=len(string)-1
    while left<right:
        string[left],string[right]=string[right],string[left]
        left+=1
        right-=1
    if pivot==-1:
        print("no answer")
    else:
        print("".join(string))
'''
#
import math
'''
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort(key=lambda x: x[0])

merged = []
for interval in intervals:
    # If merged list is empty OR current interval does not overlap, append it
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        # If they overlap, merge by updating the end value
        merged[-1][1] = max(merged[-1][1], interval[1])
print(merged)
'''
#minmaxriddle
'''
def window_size(arr):
    new=[]
    n=len(arr)
    for i in range(1,n+1):
        inner = []
        for j in range(n-i+1):
            inner.append(arr[j:j+i])
        new.append(inner)
    for size, windows in enumerate(new, start=1):
        if size==1:
            result=max(windows)
        else:
            mins = []
            for w in windows:
                mins.append(min(w))
            result=max(mins)
        print(result)


n=int(input())
arr = list(map(int, input().split()))
window_size(arr)
'''
# some problem
'''
def value(s,k):
    new={}
    for char in s:
        if char not in new:
            new[char]=1
        else:
            new[char]+=1
    ram=[]
    for key,val in new.items():
        if val not in ram:
            ram.append(val)
    ram.sort(reverse=True)
    if k>len(ram):
        return -1
    kthlargest=ram[k-1]
    for key,val in new.items():
        if val==kthlargest:
            return key
s=input()
k=int(input())
print(value(s,k))
'''
# permuation extension
'''
s = input()
rev = s[::-1]

for i in range(len(s)):
    if s[i:] == rev[:len(s)-i]:
        extension = rev[len(s)-i:]
        print(extension)
        break
'''
# deloittesh
'''
str="myprogram"
new=[]
for i in range(0,len(str)-1,2):
    new.append(str[i:i+2])
if len(str)%2!=0:
    new.append(str[-1])
print(*new)
'''
#
'''
str="myprogram"
substring=[]
for i in range(len(str)):
    for j in range(i,len(str)):
        substring.append(str[i:j+1])
new=[]
for sub in substring:
    if len(sub) == 2:
        start_index = str.index(sub)
        if start_index % 2 == 0:
            new.append(sub)
if len(str) % 2 != 0:
    new.append(str[-1])
print(*new)
'''
# encryption problem
'''
import math
text = "haveaniceday"
length = len(text)
sqrt = math.sqrt(length)
grid = []
encrypted = []

for i in range(length):
    if sqrt <= i + 1 and sqrt > i:
        row = i
        col = i + 1
        break
for r in range(row):
    start = r * col
    end = start + col
    grid.append(text[start:end])
for c in range(col):
    word = ""
    for r in range(row):
        if c < len(grid[r]):
            word += grid[r][c]
    encrypted.append(word)
print(" ".join(encrypted))
'''
#mincost to merge elements
'''
def min_cost(arr):
    while len(arr) > 1:
        min_cost = float('inf')
        min_index = -1
        for i in range(len(arr) - 1):
            cost = arr[i] + arr[i + 1]
            if cost < min_cost:
                min_cost = cost
                min_index = i
        arr[min_index] = min_cost
        arr.pop(min_index + 1)
    return arr[0]
print(min_cost([5,3,5,2]))
'''
#minoperations
'''
def get_min_op(arr):
    new=[]
    for char in arr:
        binary=bin(char)[2:].zfill(2)
        new.append(binary)
    op_count=0
    first=new[0]
    for b in new[1:]:
        for i in range(len(b)):
            if b[i]!=first[i]:
                op_count+=1
    return op_count
print(get_min_op([1,2]))
'''
#group anagrams
'''
arr=list(map(str,input().split()))
groups=[]
while len(arr)>0:
    new=arr[0]
    key=sorted(new)
    ram=[new]
    i=1
    while i<len(arr):
        if sorted(arr[i])==key:
            ram.append(arr[i])
            arr.pop(i)
            i-=1
        i+=1
    arr.pop(0)
    groups.append(ram)
print(groups)
'''
#maximum number of 2*2 squares that can be fit inside a right isocelous triangle
'''
length=int(input())
new=(length-2)//2
ram=0
for i in range(1,new+1):
    ram+=i
print(ram)
'''
#count elements greater than previous average
import math
'''
def avg(ele):
    average=sum(ele)/len(ele)
    return average
resp=list(map(int,input().split()))
count=0
for i in range(len(resp)):
    if i!=0:
        if resp[i]>avg(resp[:i]):
            count+=1
print(count)
'''
#merge and sort intervals
'''
intervals=[[1,3],[2,6],[8,10],[15,18]]
merged_interval=[]
merged_interval.append(intervals[0])
for i in range(1,len(intervals)):
    current=intervals[i]
    last=merged_interval[-1]
    if current[0]<=last[1]:
        last[1]=max(last[1],current[1])
    else:
        merged_interval.append(current)
print(merged_interval)
'''
# longest common prefix
'''
def longest_common_prefix(words):
    first = words[0]
    result = ""

    for i in range(len(first)):
        sub = first[:i+1]      
        for word in words:
            if not word.startswith(sub):
                return result
        result = sub

    return result


words = input().split()
print(longest_common_prefix(words))
'''
#### find first and last position of an index
'''
def searchRange(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            start_index = i
            for j in range(start_index, len(nums)):
                if nums[j] == target:
                    end_index = j
            return [start_index,end_index]
    return [-1,-1]
ram=searchRange([5,7,7,8,8,10],8)
print(ram)
'''
#count and say
'''
n=int(input())
first_count="1"
print(first_count)
for i in range(n-1):
    result=""
    c=1
    for j in range(1,len(first_count)):
        if first_count[j]==first_count[j-1]:
            c+=1
        else:
            result += str(c) + first_count[j - 1]
            c = 1
    result += str(c) + first_count[-1]
    first_count = result
    print(first_count)
'''
#combination sum
'''
def combinationSum(candidates, target):
    result = []
    def solve(start,path,total):
        if total==target:
            result.append(path)
            return
        if total>target:
            return
        for i in range(start,len(candidates)):
            solve(i,path+[candidates[i]],total-candidates[i])
'''
#jump game
'''
nums = [2, 3, 1, 1, 4]
count = 0
i = 0
while i < len(nums) - 1:
    count = count + 1
    best = i
    for j in range(i + 1, i + nums[i] + 1):
        if j < len(nums):
            if j + nums[j] > best + nums[best]:
                best = j
    i = best
print(count)
'''
#maximum subarray
'''
nums = [-2,1,-3,4,-1,2,1,-5,4]
subarray = []
max_sub=0
for i in range(len(nums)-1):
    for j in range(i + 1, len(nums)-1):
        subarray.append(nums[i:j+1])
for char in subarray:
    if sum(char)>max_sub:
        max_sub=sum(char)
print(max_sub)
'''
#rotate list
'''
head=[1,2,3,4,5]
k=2
i=0
while i<k:
    new=head.pop(-1)
    i+=1
    head.insert(0,new)
print(head)
'''
#
'''
nums = list(map(int, input().split()))
for i in range(1, len(nums) + 2):
    if i in nums:
        continue
    else:
        print(i)
        break
'''
#
'''
n = 4
k = 2
new=[]
def combinations(start, curr):
    if len(curr) == k:
        new.append(curr)
        return

    for i in range(start, n+1):
        combinations(i+1, curr + [i])

combinations(1, [])
print(new)
'''
#combination sum
'''
candidates=[10,1,2,7,6,1,5]
target=8
sub_array=[]

for i in range(len(candidates)):
    for j in range(i, len(candidates)):
        array = candidates[i:j+1]
        sub_array.append(array)

for char in sub_array:
    if sum(char)==target:
        print(char)
'''
'''
s = [[5,3,4],
     [1,5,8],
     [6,4,2]]

magic = [
    [[8,1,6],[3,5,7],[4,9,2]],
    [[6,1,8],[7,5,3],[2,9,4]],
    [[4,9,2],[3,5,7],[8,1,6]],
    [[2,9,4],[7,5,3],[6,1,8]],
    [[8,3,4],[1,5,9],[6,7,2]],
    [[4,3,8],[9,5,1],[2,7,6]],
    [[6,7,2],[1,5,9],[8,3,4]],
    [[2,7,6],[9,5,1],[4,3,8]]
]

min_cost = 1000   # big number

for m in magic:
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(s[i][j] - m[i][j])
    if cost < min_cost:
        min_cost = cost

print(min_cost)
'''
#coding question
'''
string=input()
space_count=string.count(" ")
if space_count==0:
    print(string+"%40")
elif space_count==1:
    new=""
    for ch in string:
        if ch==" ":
            new+="%20"
        else:
            new+=ch
    print(new)
elif space_count == 2:
    new = ""
    for ch in string:
        if ch == " ":
            new += "%30"
        else:
            new += ch
    print(new)
'''
#
'''
class InvalidPasswordException(Exception):
    pass
string=input()
try:
    if len(string)>=8 and any(char.isupper() for char in string) and any(char.islower() for char in string) and any(char.isnumeric() for char in string) and any(not char.isalnum() for char in string):
        print("password is valid")
    else:
        raise InvalidPasswordException
except:
    print("invalid password")
'''
#combination
'''
def combination(open, close):
    if open == close == n:
        print("".join(new))
        return
    if open < n:
        new.append("(")
        combination(open + 1, close)
        new.pop()

    if close < open:
        new.append(")")
        combination(open, close + 1)
        new.pop()

n = int(input())
new = []
combination(0, 0)
'''
# minimum path sum
'''
def min_cost(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == 0 and col != 0:
                grid[row][col] += grid[row][col-1]
            elif col == 0 and row != 0:
                grid[row][col] += grid[row-1][col]
            elif row != 0 and col != 0:
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])

    return grid[-1][-1]
grid=[[1,3,5],[2,3,6]]
print(min_cost(grid))
'''
#
'''
n=int(input())
ugly_numbers=[]
i=1
while len(ugly_numbers)<n:
    x=i
    while x%2==0:
        x//=2
    while x%3==0:
        x//=3
    while x%5==0:
        x//=5
    if x==1:
        ugly_numbers.append(i)
    i+=1
print(ugly_numbers[-1])
'''
#longest_substring with k unique characters
'''
s = "aabacbebebe"
k = 3
max_substring = ""
substring = []
for i in range(len(s)):
    for j in range(i, len(s)):
        substring.append(s[i:j+1])
for char in substring:
    new = []
    for c in char:
        if c not in new:
            new.append(c)
    if len(new) == k and len(char) > len(max_substring):
        max_substring = char
print(max_substring)
'''
#####
''''
nums = int(input())
digits = list(str(nums))
max_number = nums
for i in range(len(digits)):
    for j in range(i + 1, len(digits)):
        digits[i], digits[j] = digits[j], digits[i]
        current = int("".join(digits))
        if current > max_number:
            max_number = current
        digits[i], digits[j] = digits[j], digits[i]
print(max_number)
'''
#
'''
input2 = ["AAA00000", "CCC0003", "ABA0001"]
kar = []
def lexographical(min_plates):
    s1 = min_plates[0]
    s2 = min_plates[1]

    for i in range(len(s1)):
        if s1[i] < s2[i]:
            print("Lexicographically first:", s1)
            return
        elif s1[i] > s2[i]:
            print("Lexicographically first:", s2)
            return
    print("Lexicographically first:", s1)
for char in input2:
    alpha_sum = 0
    num_sum = 0

    for bar in char:
        if bar.isalpha():
            alpha_sum += (ord(bar.lower()) - 96)
        elif bar.isdigit():
            num_sum += int(bar)

    kar.append({char: abs(alpha_sum - num_sum)})
first_dict = kar[0]
min_value = list(first_dict.values())[0]
min_plates = []
count=0
for d in kar:
    for key, value in d.items():
        if value < min_value:
            min_value = value
for d in kar:
    for key, value in d.items():
        if value == min_value:
            min_plates.append(key)
            count += 1
print(min_value)
for plate in min_plates:
    print(plate)
print(count)
if count==2:
    lexographical(list(min_plates))
'''
#linked list
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
    def print_list(self):
        current = self.head
        while current != None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count
    def insert_at_middle(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        count = 0
        mid = self.length() // 2
        while count < mid - 1:
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node
added = LinkedList()
added.insert_at_begining(3)
added.insert_at_end(10)
added.insert_at_end(5)
added.insert_at_end(2)
added.insert_at_middle(8)
added.print_list()
print(added.length())
'''
# double_linked_list
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self, value):
        new_node = Node(value)
        new_node.prev=None
        new_node.next=self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def print_list(self):
        current=self.head
        while current != None:
            print(current.value, end=" -> ")
            current=current.next
    def insert_at_end(self, value):
        new_node = Node(value)
S=LinkedList()
S.insert_at_begining(3)
S.insert_at_begining(10)
S.print_list()
'''
#finding all anagrams in a string
'''
s = input()
p = input()
result = [i for i in range(len(s))
          for j in range(i, len(s))
          if sorted(s[i:j+1]) == sorted(p)]
print(result)
'''
#check for subsequence
'''
A = "gksrek"
B = "geeksforgeeks"
new = ""
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            new=new+A[i]
            B = B[j+1:]
            break
if new==A:
    print(1)
else:
    print(0)
'''

#linked_list_operations
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def search_single_linked_list(self,target):
        current=self.head
        while current is not None:
            if current.data==target:
                return True
            current = current.next
        return False
    def print_ll(self):
        current=self.head
        while current is not None:
            print(current.data, end=" -> ")
            current=current.next
    def insert_at_end(self,data):
        new_node = Node(data)
        current=self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def delete_at_first(self):
        self.head = self.head.next
    def delete_at_end(self):
        current = self.head
        while current.next.next is not None:
            current=current.next
        current.next=None
new=Linked_list()
new.insert_at_beginning(34)
new.insert_at_beginning(20)
new.insert_at_beginning(43)
new.insert_at_end(23)
new.delete_at_first()
new.delete_at_end()
print(new.search_single_linked_list(20))
new.print_ll()
'''
# Transpose matrix
'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transp=[]
for i in range(len(matrix)):
    new=[]
    for j in range(len(matrix)):
        new.append(matrix[j][i])
    transp.append(new)
print(transp)
'''
#toeplitz matrix
'''
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
is_toeplitz=True
ram=[]
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        if i!=0:
            if matrix[i][j]!=matrix[i-1][j-1]:
                is_toeplitz=False
                break
            else:
                ram.append(matrix[i][j])
        if not is_toeplitz:
            break
print(is_toeplitz)
print(ram)
'''
#camelcase matching
'''
queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FB"
final = []

for char in queries:
    capital = ""
    for word in char:
        if word == word.upper():
            capital += word

    if capital == pattern:
        final.append(True)
    else:
        final.append(False)

print(final)
'''
#maths
'''
a = 2
b = [1,0]
new=""
for char in b:
    new+=str(char)
power=a**int(new)
mod=power%1337
print(mod)
'''
#zigzag conversion
'''
s = "PAYPALISHIRING"
numRows = 3
rows = [""] * numRows
direction=1
current_row=0
for char in s:
    rows[current_row]+=char
    if current_row==numRows-1:
        direction=-1
    elif current_row==0:
        direction=1
    current_row+=direction
print("".join(rows))
'''
#letter combination of a phone number
'''
mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

digits = "23"
result=[""]
for char in digits:
    new = []
    if char in mapping:
        for prev in result:
            for letter in mapping[char]:
                new.append(prev+letter)
    result=new
print(result)
'''
# Swap Nodes in Pairs
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def swap(self):
        temp = self.head

        while temp and temp.next:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def Nth_node_from_end(self,n):
        slow = self.head
        fast = self.head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            self.head = self.head.next
            return self.head

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
# Input
values = list(map(int, input().split()))
ll = Linked_list()

for v in values:
    ll.insert_at_end(v)
ll.Nth_node_from_end(2)


ll.display()
'''

#tap academy
'''
n=5
k=4
heights=[1,6,3,5,2]
max_height=max(heights)
if max_height==k:
    print("yes")
else:
    print("NO")
    new=max_height-k
    print(new)
'''
# 3 Sum closest
'''
nums = [-1,2,1,-4]
sun = []
i = 0
while i < len(nums):
    j = i + 1
    while j < len(nums):
        k = j + 1
        while k < len(nums):
            temp = nums[i] + nums[j] + nums[k]
            sun.append(temp)
            k += 1
        j += 1
    i += 1
positive=[]
for sun in sun:
    if sun>0:
        positive.append(sun)
if positive:
    print(min(positive))
'''
# double_linked_list
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class double_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        new_node.prev = None
        self.head=new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node

    def delete_at_beginning(self):
        self.head=self.head.next
        self.head.prev=None
    def delete_at_end(self):
        self.tail=self.tail.prev
        self.tail.next=None
'''
#permutations
'''
nums = [1, 2, 3]
nums.sort()  # print first permutation
while True:
    pivot = -1   # reset every loop
    # Step 1: find pivot
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            pivot = i
            break
    # If no pivot → stop loop
    if pivot == -1:
        break
    # Step 2: find next greater from right
    for j in range(len(nums)-1, pivot, -1):
        if nums[j] > nums[pivot]:
            nums[j], nums[pivot] = nums[pivot], nums[j]
            break
    # Step 3: reverse right part
    left = pivot + 1
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    print(nums)
'''
# H-Index
'''
citations = [3,0,6,1,5]
ans=0
for i in range(len(citations)+1):
    count=0
    for j  in range(len(citations)):
        if citations[j]>=i:
            count+=1
    if count>=i:
        ans=i
print(ans)
'''
#validate email
'''
emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]
def validate(mail):
    local, domain = email.split("@")
    local=local.split("+")[0]
    local=local.replace(".","")
    clean_mail=local+"@"+domain
    return  clean_mail
unique=set()
for email in emails:
    clean=validate(email)
    unique.add(clean)
print(len(unique))
'''
#max_number of fruits can hold
'''
fruits = [0,0,2,1]
key_value = {}
left=0
right=len(fruits)-1
max_length=0
for fruit in fruits:
    if fruit not in key_value:
        key_value[fruit] = 1
    else:
        key_value[fruit] += 1

    while len(key_value) > 2:
        right_fruit=fruits[right]
        left_fruit = fruits[left]
        if key_value[right_fruit] < key_value[left_fruit]:
            key_value[right_fruit]-=1
        key_value[left_fruit] -= 1

        if key_value[left_fruit] == 0:
            del key_value[left_fruit]
        elif key_value[right_fruit] == 0:
            del key_value[right_fruit]

        left += 1
        right-=1
    current_length = sum(key_value.values())
    if current_length > max_length:
        max_length = current_length

print(max_length)
'''
#validate
''''
emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]

def validate(mail):
    local, domain = mail.split("@")
    name_part=domain.replace(".com","")
    if "." in name_part:
        return "invalid"
    return"valid"
for mail in emails:
    print(validate(mail))
'''
# tcs next step
'''
n=int(input())
arr=list(map(int,input().split()))
count=0
i=0
for j in range(i+1,len(arr)):
    if arr[i]!=arr[j]:
        count+=1
print(count)
'''
#tcs nextstep2
'''
N = int(input())
K = int(input())
prices = list(map(int, input().split()))
start = 0
sum_find = 0
max_length = 0

for end in range(N):
    sum_find += prices[end]

    while sum_find >= K:
        sum_find -= prices[start]
        start += 1

    length = end - start + 1
    if length > max_length:
        max_length = length

print(max_length)
'''
#tcs next step3
'''
N =int(input())
K = int(input())
list_new=[]
list_map=list(map(int,input().split()))
for i in range(len(list_map)):
    for j in range(i,len(list_map)):
        sub=list_map[i:j+1]
        if sum(sub)==K:
            print(i+1,j+1)
            print(sub)
            exit()
'''
# drum beat
'''
N = 5
board = [2, 3, 1, 5, 4]
board_dict = {}
for i in range(len(board)):
    board_dict[i + 1] = board[i]
original = board_dict.copy()
count = 0
print("Start:", board_dict)
while True:
    new_dict = {}
    for key in board_dict:
        new_dict[key] = original[board_dict[key]]
    board_dict = new_dict
    count += 1
    print("After beat", count, ":", board_dict)
    if board_dict == original:
        break
print("Total beats:", count)
'''
# subset
'''
A = "abcab"
B = "aabab"
count_moves = 0
A=list(A)
B=list(B)
n=len(A)
while True:
    new=[]
    target=[]
    for i in range(n):
        if A[i]!=B[i]:
            if A[i]<B[i]:
                print(-1)
                exit()
            new.append(A[i])
            target.append(B[i])
    if not new:
        break
    ram2=max(target)
    final_postions=[]
    for i in range(n):
        if A[i]!=B[i] and B[i]==ram2:
            final_postions.append(i)
    for i in final_postions:
        A[i]=ram2
    count_moves += 1
print(count_moves)
'''
#########################
'''
N=int(input())
new=str(N)
mul=1
for char in new:
    mul*=int(char)
print(mul)
'''
######################
'''
p = 10000
T = 20

rate1 = [
    {"year": 5, "rate": 9.5},
    {"year": 10, "rate": 9.6},
    {"year": 5, "rate": 8.5}
]

rate2 = [
    {"year": 10, "rate": 6.9},
    {"year": 5, "rate": 8.5},
    {"year": 5, "rate": 7.9},
]

def calculate_total_interest(p, rates):
    principal = p
    total_payment = 0

    for rate in rates:
        monthly_rate = rate["rate"] / (12 * 100)
        months = rate["year"] * 12

        EMI = (principal * monthly_rate) / (1 - (1 / (1 + monthly_rate) ** months))

        for _ in range(months):
            interest = principal * monthly_rate
            principal -= (EMI - interest)

        total_payment += EMI * months

    return total_payment - p


interest1 = calculate_total_interest(p, rate1)
interest2 = calculate_total_interest(p, rate2)

if interest1 < interest2:
    print("Bank A")
else:
    print("Bank B")
'''
#####################
'''
string=input()
T=20
new=[]
for char in string:
    position = ord(char.upper()) - ord('A') + 1
    new.append(position+T)
print(new)
'''
########primes checking
'''
N = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
count = 0

for num in range(2, N+1):
    if is_prime(num):
        sum += num
        if sum > N:
            break
        if sum>=3 and is_prime(sum):
            count += 1
print(count)
print(sum)
'''
#rock problem
'''
S, R = map(int, input().split())
arr = list(map(int, input().split()))
new=[]
ranges = []
for _ in range(R):
    low, high = map(int, input().split())
    ranges.append((low, high))

for low, high in ranges:
    count = 0
    for rock in arr:
        if low <= rock <= high:
            count += 1
    print(count)
'''
###########
'''
N, K = map(int, input().split(","))

factors = []
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        factors.append(i)
        if i != N // i:
            factors.append(N // i)
factors.sort()
if K > len(factors):
    print(1)
else:
    print(factors[len(factors) - K])
'''
#move zeros to end
'''
N = int(input())
arr = list(map(int, input().split()))
i=0
for j in range(len(arr)):
    if arr[j]==0:
        continue
    elif arr[j]>=0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    else:
        print("0")
print(arr)
'''
#########
'''
arr=list(map(int, input().split()))
target=int(input())
left=0
right=len(arr)-1
while left<=right:
    sum_target=arr[left]+arr[right]
    if sum_target==target:
        print(True)
        print((arr[left],arr[right]))
        break
    elif sum_target<target:
        left+=1
    else:
        right-=1
'''
#
'''
arr="abcabcbb"
substrings=[]
new_sub=[]
def duplicate(sub):
    new = []
    for char in sub:
        if char in new:
            return False
        new.append(char)
    return True

for i in range(len(arr)):
    for j in range(i,len(arr)):
        substrings.append(arr[i:j+1])
for sub in substrings:
    if duplicate(sub)==True:
        new_sub.append(sub)
max_len=0
longest=""
for sub in new_sub:
    if len(sub)>max_len:
        max_len = len(sub)
        longest = sub
print(max_len)
print(longest)
'''
#candies smallest
'''
arr = [1, 2, 3, 4]
total_sum = 0

while len(arr) > 1:
    arr.sort()
    first_min, second_min = arr[0], arr[1]
    sum_value = first_min + second_min
    arr.remove(first_min)
    arr.remove(second_min)
    arr.insert(0,sum_value)
    total_sum += sum_value

print(total_sum)
'''
#freesquares
'''
import math
N=int(input())
count=0
for i  in range(2,N+1):
    is_sq = True
    for j in range(2,int(math.sqrt(i)) + 1):
        if i % (j * j)==0:
            is_sq=False
            break
    if is_sq and N%i==0:
        count+=1
        print(i)
print(count)
'''
# sldiing window problem-dynamic
'''
def longest_subarray(arr,k):
    start=0
    window_sum=0
    max_length=0
    for end in range(len(arr)):
        window_sum+=arr[end]
        while window_sum>=k:
            window_sum-=arr[start]
            start+=1
        length=end-start+1
        if length>max_length:
            max_length=length
    return max_length
print(longest_subarray([30,40,50,20,20,10,90,10,10,10],100))
'''
#sliding window static
'''
def substring(arr,k):
    start=0
    end=k
    window_sum=0
    max_sum=0
    for end in range(len(arr)):
        window_sum+=arr[end]
        if end>k-1:
            window_sum-=arr[start]
            start+=1
            if window_sum>max_sum:
                max_sum=window_sum
    return max_sum
print(substring([2,1,5,1,3,2],3))
'''
#####
'''
str1=input()
str2=input()
for char in str1:
    if char in str2:
        str1=str1.replace(char,"")
print(str1)
'''
#################
'''
def convert_to_binary(n):
    binary_value=[]
    while n>0:
        remainder=n%2
        binary_value.append(remainder)
        n=n//2
    reversed=binary_value[::-1]
    return reversed
def count_iterations(n,k):
    count=0
    for i in range(len(n)):
        if n[i]==1 and k[i]==0:
            n[i]=0
            count+=1
    return count,n
N=int(input())
K=int(input())
n=convert_to_binary(N)
k=convert_to_binary(K)
print(count_iterations(n,k))
'''
######
'''
s=input()
start=0
window=""
max_window=0
seen=[]
for end in s:
    if end not in seen:
        seen.append(end)
        window += end
    else:
        while end in seen:
            removed=seen.pop(0)
            window=window[1:]
        seen.append(end)
        window+=end
    if len(window)>max_window:
        max_window=len(window)
print(max_window)
'''
#####
'''
nums=[2,3,1,1,4]
end=len(nums)-1
count=0
sum_length=nums[0]
length=0
for i in range(1,len(nums)):
    sum_length+=nums[i]
    if sum_length>nums[end]:
        sum_length-=nums[i]
        continue
    elif sum_length<nums[end]:
        count+=1
    elif sum_length==nums[end]:
        print(count)
'''
#############
'''
nums = [2,3,1,1,4]

n = len(nums)
i = 0
jump = 0

while i < n - 1:

    start = nums[i]
    best_reach = 0
    best_index = i

    for j in range(1, start + 1):

        new_position = i + j

        if new_position >= n - 1:
            jump += 1
            print(jump)
            exit()

        if new_position + nums[new_position] > best_reach:
            best_reach = new_position + nums[new_position]
            best_index = new_position

    i = best_index
    jump += 1
'''
#left decrease
'''
n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
'''
#right decrease triangle
'''
n=int(input())
for i in range(n):
    for s in range(i):
        print(" ",end="")
    for  j in range(n-i):
        print("*",end="")
    print()
'''
#leftindreasing
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
'''
#right increasing triangle
'''
n=int(input())
for i in range(n+1):
    for s in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
'''
####uphill
'''
n = int(input())
for i in range(n):
    for s  in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(n-1):
    for s in range(i+1):
        print(" ",end="")
    for j in range(2*(n-i-1)-1):
        print("*",end="")
    print()
'''
####sandtimer
'''
n=int(input())
for i in range(n):
    for s in range(i+1):
        print(" ",end="")
    for j in range(2*(n-i)-1):
        print("*",end="")
    print()
for i in range(n-1):
    for  s in range(n-i-1):
        print(" ",end="")
    for  j in range(2*(i+1)+1):
        print("*",end="")
    print()
'''
########rightpointed triangle
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end="")
    print()
'''
#leftpointed triangle
'''

'''
#butterflypatten
'''
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    for s in range(2*(n-i)):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end="")
    for s in range(2*(i+1)):
        print(" ",end="")
    for j in range(n-i-1):
        print("*",end="")
    print()
'''
#### merge_alternatively
'''
word1="abc"
word2="pqr"
merged_result=""
n1=len(word1)
n2=len(word2)
max_result=max(n1,n2)
for i in range(max_result):
    if i < n1:
        merged_result += word1[i]

    if i < n2:
        merged_result += word2[i]
print(merged_result)
'''
#buddy strings
'''
s = "ab"
goal = "ba"
s_list = list(s)
for i in range(len(s_list)):
    for j in range(len(s_list)):
        if i != j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            if "".join(s_list) == goal:
                print("true")
            else:
                print("false")

            s_list[i], s_list[j] = s_list[j], s_list[i]
'''
############
''''
def three_sum(nums):
    nums.sort()
    result=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left,right=i+1,len(nums)-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total<0:
                left+=1
            elif total>0:
                right-=1
            else:
                result.append([nums[i],nums[left],nums[right]])
                while left<right and nums[left]==nums[left]+1:
                    left+=1
                while left<right and nums[right]==nums[right]-1:
                    right-=1
                left+=1
                right-=1
    return result
print(three_sum([-1,0,1,2,-1,-4]))
'''
#minimum in rotated sorted_array
'''
def find_min(arr):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]>arr[right]:
            left=mid+1
        else:
            right=mid
    return arr[left]

print(find_min(arr=[4,5,6,7,0,1,2]))
'''
#trailing zeros
'''
n=int(input())
sum_val=0
multi=5
while multi<n:
    sum_val+=n//multi
    multi=multi*5
print(sum_val)
'''
#max_subarray
'''
arr=[-2,1,-3,4,-1,2,1,-5,4]
max_sub=0
for i in range(len(arr)):
    for j in range(len(arr)):
        sub=arr[i:j+1]
        if sum(sub)>max_sub:
            max_sub=sum(sub)
print(max_sub)
'''
# first non repeating in array
'''
arr=[-1,2,-1,3,0]
unique_ones={}
for i in range(len(arr)):
    unique_ones[arr[i]]=arr.count(arr[i])
for key,values in unique_ones.items():
    if values==1:
        print(key)
        break
'''
#rotate by d positions
''''
arr=[1,2,3,4,5,6]
d=2
for i in range(d):
    new=arr.pop(0)
    arr.append(new)
print(arr)
'''
'''
arr = [1, 2, 0, 3]
left = 0
right = len(arr) - 1
left_sum = arr[left]
right_sum = arr[right]

for end in range(1, len(arr)):
    if left_sum == right_sum and left + 1 == right - 1:
        print("Equilibrium index:", left + 1)
    elif left_sum < right_sum:
        left += 1
        left_sum += arr[left]
    else:
        right -= 1
        right_sum += arr[right]
'''
#clockwisektimesrotatw
'''
arr=[1,2,3,4,5,6]
k=2
for i in range(k):
    new=arr.pop(-1)
    arr.insert(0,new)
print(arr)
'''
#######
'''
a=[[1,2],[3,4]]
b=[[4,3],[2,1]]
c=[]
sum_val=0
for i in range(len(a)):
    row=[]
    for j in range(len(a[0])):
        sum_val=a[i][j]+b[i][j]
        row.append(sum_val)
    c.append(row)
print(c)
'''
#college problem
'''
def min_cost_hiring(q,w,k):
    accepted=[]
    for i in range(len(q)):
        ratio=w[i]/q[i]
        for  j in range(len(q)):
            if q[i]*ratio>=w[j]:
                accepted.append(q[j]*ratio)
        if len(accepted)>=k:
            accepted.sort()
            return sum(accepted[:k])
print(min_cost_hiring([3,1,10,10,1],[4,8,2,2,7],3))
'''
#########
'''
def kth_smallest(arr, k):
    pivot = arr[0]

    left = []
    right = []

    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    rank = len(left) + 1

    if k == rank:
        return pivot
    elif k < rank:
        return kth_smallest(left, k)
    else:
        return kth_smallest(right, k - rank)


arr = [20,14,12,1]
k = 2

print(kth_smallest(arr, k))
'''
#bitflips
'''
def bits_conversion(number):
    nam=[]
    while number>0:
        rem=number%2
        nam.append(rem)
        number=number//2
    nam.reverse()
    return nam
def flips_required(one,two):
    count=0
    for i in range(len(one)):
        if one[i]!=two[i]:
            count+=1
    return count
start=10
goal=7
madhava=bits_conversion(start)
kesava=bits_conversion(goal)
while len(madhava)<len(kesava):
    madhava.insert(0,0)
while len(kesava)<len(madhava):
    kesava.insert(0,0)
print(flips_required(madhava,kesava))
'''
#####max of each window
'''
arr=[1, 3, -1 ,-3 ,5 ,3 ,6 ,7]
k=3
list_new=[]
left=0
right=k
i=0
while right<=len(arr):
    window=arr[left:right]
    final=max(window)
    list_new.append(final)
    left+=1
    right+=1
print(list_new)
'''
#printing sliding window
'''
s="abcabcbb"
left=0
right=1
Max_len=0
ans=""
while right<=len(s):
    substring=s[left:right]
    if s[right-1] not in substring[:-1]:
        print(substring)
        if len(substring)>Max_len:
            Max_len=len(substring)
            ans=substring
        right+=1
    else:
        left+=1
print(ans)
'''
##### arranging with the rank
'''
arr=[100,5,70,2]
rank_arrangement={}
new=sorted(arr)
for i in range(len(new)):
    rank_arrangement[new[i]]=i+1
for i in range(len(arr)):
    if arr[i] in rank_arrangement:
        print(rank_arrangement[arr[i]])
'''
## highest_frequency_comes_first
''''
arr = [5, 5, 4, 6, 4]
freq_count={}
for char in arr:
    if char not in freq_count:
        freq_count[char]=1
    else:
        freq_count[char]+=1
final_keys = []
while len(freq_count)>=1:
    highest_freq=max(freq_count.values())
    keys_to_remove=[]
    smallest_key = float('inf')
    for key,values in freq_count.items():
        if values==highest_freq:
            if key<smallest_key:
                smallest_key = key
    for i in range(highest_freq):
        final_keys.append(smallest_key)
    keys_to_remove.append(smallest_key)
    for k in keys_to_remove:
        freq_count.pop(k)
print(final_keys)
'''
####
'''
arr1=[2,1,2,3,4]
arr2=[2,1,2]
final_arr2=[]
last_final=[]
for i in range(len(arr2)):
    if arr2[i] not  in final_arr2:
        final_arr2.append(arr2[i])
count_set={}
for i in range(len(arr1)):
    if arr1[i] not in count_set:
        count_set[arr1[i]]=1
    else:
        count_set[arr1[i]]+=1
for char in final_arr2:
    if char in count_set:
        for i in range(count_set[char]):
            last_final.append(char)
            arr1.remove(char)
last_final.extend(arr1)
print(last_final)
'''
#######maximum product subarray
'''
arr = [-2,6,-3,-10,0,2]
left=0
subarray=[]
while left<len(arr):
    right=left+1
    while right<=len(arr):
        subarray.append(arr[left:right])
        right+=1
    left+=1
highest_mul=1
for i in range(len(subarray)):
    multiple=1
    for j in range(len(subarray[i])):
        multiple*=subarray[i][j]
    if multiple>highest_mul:
        highest_mul=multiple
print(highest_mul)
'''
#profit hoga mere baat suno
'''
prices=[1,3,6,9,11]
max_profit=0
for i in range(len(prices)):
    buy=prices[i]
    for j in range(i+1,len(prices)):
        sell=prices[j]
        profit=sell-buy
        if profit > max_profit:
            max_profit=profit
print(max_profit)
'''
#consecutiveonesorzeros
'''
arr=[0,1,0,1,1,1,1]
one_count=0
zero_count=0
for i in range(len(arr)):
    if arr[i]==0:
        zero_count+=1
    else:
        zero_count=0
    if arr[i]==1:
        one_count+=1
    else:
        one_count=0
if zero_count>one_count:
    print(zero_count)
else:
    print(one_count)
'''
#min duration plans tcs given problem
'''
n=9
plans={3:5000,6:9000,9:12000,12:15000}
min_cost=float('inf')
for plan in plans:
    remaining_cost=n
    cost=0
    i=plan
    while remaining_cost>0:
        if remaining_cost>=i:
            remaining_cost-=i
            cost+=plans[i]
        else:
            break
    if remaining_cost==0:
        min_cost=min(min_cost,cost)
if n in plans:
    min_cost=min(min_cost,plans[n])
print(min_cost)
'''
###### small library management system
'''
library = []
def add():
    no_of_books = int(input("Enter number of books: "))
    for i in range(no_of_books):
        name = input("Enter book name: ")
        title = input("Enter book title: ")
        library.append({
            "name": name,
            "title": title,
            "issued": False
        })
    print("Books added successfully!")
def view():
    if not library:
        print("no books available")
        return
    print("\navailable books:")
    for book in library:
        if book["issued"]==True:
            status="Issued"
        else:
            status="available"
            print(f"{book['name']} ({book['title']}) - {status}")
def issue():
    issued_book_name=input("enter the book name to issue")
    for book_name in library:
        if book_name["name"]==issued_book_name:
            if book_name["issued"]==True:
                print("book already issued")
            else:
                book_name["issued"]=True
                print("book issued succesfully")
            return
    print("book not found")
def return_book():
    returned_book_name=input("enter the book name to return:")
    for book_name in library:
        if book_name["name"]==returned_book_name:
            if not book_name["issued"]:
                print("Book was not issued ")
            else:
                book_name["issued"]=False
                print("Book returned successfully")
            return
    print("book not found")
while True:
    print("\n1. Add Books")
    print("2. View Books")
    print("3. Issue Books")
    print("4. Return Books")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add()
    elif choice==2:
        view()
    elif choice==3:
        issue()
    elif choice==4:
        return_book()
    else:
        exit()
'''
#sorting the array
'''
arr=[1,3,2,4]
k=2
new=arr.sort()
for i in range(len(arr)):
    if i==k:
        print(arr[i])
'''
# something operation
'''
arr=[1,0,1,1,1]
flip_count=0
for i in range(len(arr)):
    if arr[i]==0:
        flip_count+=1
        for j in range(i,len(arr)):
            if arr[j]==0:
                arr[j]=1
            else:
                arr[j]=0
print(flip_count)
'''
#optimal way
'''
arr = [1, 0, 1, 1, 1]

flipped = False
count = 0

for i in range(len(arr)):
    value = arr[i]

    if flipped:
        if value == 0:
            value = 1
        else:
            value = 0

    if value == 0:
        count += 1
        flipped = not flipped

print(count)
'''
#minjumpsrequired
''''
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
count=0
i=0
n=len(arr)
while i<n-1:
    max_count=0
    next_index=i
    for j in range(i+1,min(i+arr[i]+1,n)):
        next_element=j+arr[j]
        if next_element>max_count:
            max_count=next_element
            next_index=j
    i=next_index
    count+=1
print(count)
'''
#selection sort
'''
arr=[4, 1, 3, 9, 7]
for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)
'''
#####patternlast
'''
n=5
for i in range(n):
    for j in range(i):
        print("*",end="")
    for k in range(2*(n-i-1)):
        print(" ",end="")
    for r in range(i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i-2):
        print("*",end="")
    for k in range(2*(i+1)):
        print(" ",end="")
    for r in range(n-i-2):
        print("*",end="")
    print()
'''
#check whether a string is palindrome
'''
string="madam"
palindrome=False
n=len(string)
for i in range(n):
    if string[i]==string[n-i-1]:
        palindrome=True
    else:
        palindrome=False
print(palindrome)
'''
## remove vowels  in a string
'''
vowels="what is your name ?"
new=vowels
for i in range(len(vowels)):
    if vowels[i] in "aeiou":
        new=new.replace(vowels[i]," ")
print(new)
'''
##remove spaces fromthe givenstrig
'''
s= "g  eeks   for ge  eeks  "
new=""
for char in s:
    if char!=" ":
        new+=char
print(new)
'''
#
'''
string1 = "computer"
string2 = "cat"
new=""
for char in string1:
    if char not in string2:
        new+=char
print(new)
'''
##
'''
S="$Gee*k;s..fo, r'Ge^eks?"
new=""
for char in S:
    if char.isalpha():
        new+=char
print(new)
'''
#
'''
s="skeeG"
n=len(s)
new_s=""
for i in range(n):
    new_s+=s[n-i-1]
print(new_s)
'''
##
'''
s="1abc23"
sum_num=0
for char in s:
    if char.isnumeric():
        sum_num+=int(char)
print(sum_num)
'''
#
'''
s = "geeksforgeeks"
dict_count={}
for char in s:
    if char not in dict_count:
        dict_count[char]=1
    else:
        dict_count[char]+=1
for char,values in dict_count.items():
    print(f"{char}{values}",end=" ")
'''
##########
'''
s = "geeksforgeeks"
new_dict={}
max_val=0
max_char=""
for char in s:
    if char not in new_dict:
        new_dict[char]=1
    else:
        new_dict[char]+=1
for char,values in new_dict.items():
    if values>max_val:
        max_val=values
        max_char=char
print(f'{max_char}{max_val}')
'''
#first non repeating characters in a string
'''
s = "geeksforgeeks"
boolean_dict={}
first_non_repeat=""
for char in s:
    if char not in boolean_dict:
        boolean_dict[char]=1
    else:
        boolean_dict[char]+=1
for char,values in boolean_dict.items():
    if values==1:
        first_non_repeat=char
        break
print(first_non_repeat)
'''
####
'''
s="This is a test string"
words = s.split()
min_length_word = float('inf')
max_length_word = 0
for word in words:
    length = len(word)
    if length > max_length_word:
        max_length_word = length
    if length < min_length_word:
        min_length_word = length
print(min_length_word, max_length_word)
'''
#### strings are anagrams of each other
'''
s1 ="geeks"
s2 ="kseeg"
anagrams=False
if len(s1)==len(s2):
    for char in s1:
        if char in s2:
            anagrams=True
        else:
            anagrams=False
print(anagrams)
'''
#######sort the string of characters
''''
s = "dcab"
s = list(s)
for i in range(len(s) - 1):
    for j in range(len(s)-1):
        if s[j]>s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
new="".join(s)
print(new)
'''
#convert into opposite case
'''
s = "geeksForgEeks"
for char in s:
    if char.isupper():
        s=s.replace(char,char.lower())
    else:
        s=s.replace(char,char.upper())
print(s)
'''
####
'''
s= "abc\\p\""
count=0
for i in range(len(s)):
    if s[i]!=' 'and s[i]!='\t' and s[i]!='\n':
        if i==0 or s[i-1]==" "or s[i-1] == '\t' or s[i-1] == '\n':
                count += 1
print(count)
'''
#remove duplicates in string
'''
s = "geeksforgeeks"
seen=[]
for char in s:
    if char not in seen:
        seen.append(char)
    else:
        s=s.replace(char,"")
print(*seen,end="")
'''
#######
'''
txt = "geeksforgeeks"
pat="eks"
left = 0
finded=False
while left < len(txt):
    right = left + 1

    while right < len(txt):

        if txt[left] == txt[right]:
            left += 1
            break  # restart with new left

        sub = txt[left:right + 1]
        if sub==pat:
            finded=True

        right += 1

    else:
        left += 1
print(finded)
'''
####revreser the word in a  string
'''
s = "i.like.this.program.very.much"
word=s.split(".")
ram=word[::-1]
new=".".join(ram)
print(new)
'''
####count common subsequencesin given string
'''
def substrings(s):
    sub = []
    left = 0
    while left < len(s):
        right = left + 1
        while right < len(s):
            if s[left] == s[right]:
                left += 1
                break
            sub.append(s[left:right+1])
            right += 1
        else:
            left += 1
    return sub
S = "ajblqcpdz"
T = "aefcnbtdi"
sub_S = substrings(S)
sub_T = substrings(T)
common = []
for i in range(len(sub_S)):
    for j in range(len(sub_T)):
        if sub_S[i] == sub_T[j]:
            common.append(sub_S[i])
print("Common substrings:", common)
'''
###selection sort job scheduling with priority=3
'''
n=int(input())
priority=3
jobs={}
new=[]
for i in range(n):
    a,b=map(int,input().split())
    jobs[a]=b
for key,values in jobs.items():
    if values==priority:
        new.append(key)
def selection_sort(value):
    for i in range(len(value)):
        min_index = i
        for j in range(i+1,len(value)):
            if value[j]<value[min_index]:
                min_index = j
        value[i],value[min_index] = value[min_index],value[i]
selection_sort(new)
print(*new)
'''
###
'''
n=int(input())
input_map=[]
for i in range(n):
    input_map.append(int(input()))
for j in range(len(input_map)):
    if input_map[j]<=0:
        input_map[j]=5
    print(input_map[j])
print(input_map)
'''
#gcd of two  numbers
'''
a = int(input())
b = int(input())

a_factors = []
b_factors = []
max_factor = 0
for i in range(1, a+1):
    if a % i == 0:
        a_factors.append(i)
for i in range(1, b+1):
    if b % i == 0:
        b_factors.append(i)
for i in a_factors:
    if i in b_factors and i > max_factor:
        max_factor = i

print( max_factor)
'''
##sales_data_by_month
'''
data=[{"month":"Jan","sales":100},{"month":"Feb","sales":150},{"month":"Mar","sales":120},{"month":"Apr","sales":180}]
prev_month=None
prev_sales=None
for item in data:
    current_month=item["month"]
    current_sales=item["sales"]
    if prev_sales is not None and current_sales > prev_sales:
        print(f"{current_month}->{prev_month}:{current_sales}>{prev_sales}")
    prev_month=current_month
    prev_sales=current_sales
'''
######lcm of two numbers
'''
a = int(input())
b = int(input())
a_factors = []
b_factors = []
for i in range(1, a + 1):
    if a % i == 0:
        a_factors.append(i)
for j in range(1, b + 1):
    if b % j == 0:
        b_factors.append(j)
common = []
for x in a_factors:
    if x in b_factors:
        common.append(x)
gcd = max(common)
lcm = (a * b) // gcd
print(a_factors)
print(b_factors)
print("LCM:", lcm)
'''
####
'''
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
a=int(input())
print(fibonacci(a))
'''
###### minimum rotations needed to convert arr1 to arr2
'''
arr1=[1,2,3,4,5]
arr2=[3,4,5,1,2]
count=0
while arr1!=arr2:
    first=arr2.pop(0)
    arr2.append(first)
    count+=1
if arr1==arr2:
    print(count)
else:
    print(-1)
'''
#####maximum product of contigous subarray
'''
arr = [2, 3, -2, 4]
max_product=float('-inf')
max_product_subarray=[]
left = 0
while left < len(arr):
    right = left + 1
    while right < len(arr):
        if arr[right] != arr[left]:
            subarray_at = arr[left:right + 1]
            product=1
            for char in subarray_at:
                product*=char
            if product >max_product:
                max_product=product
                max_product_subarray=subarray_at
        right += 1
    left += 1
print(max_product)
print(max_product_subarray)
'''
#given tickets
'''
inp=[10,15,20,25,30]
count_odd_prices=0
sum_odd_prices=0
final_odd=[]
average_odd_prices=0
for i in range(len(inp)):
    if inp[i] % 2!= 0:
        count_odd_prices += 1
        sum_odd_prices += inp[i]
        final_odd.append(inp[i])
average_odd_prices=sum(final_odd)//len(final_odd)
print(f'{'count='}{count_odd_prices} {'sum='}{sum_odd_prices}')
'''
#next_permuatation
'''
permutation = [1, 2, 3]
n = 1
for i in range(1, len(permutation) + 1):
    n *= i
i = 0
while i < n:

    pivot = -1
    next_greater = float('inf')
    next_index = -1

    # find pivot
    for k in range(len(permutation) - 2, -1, -1):
        if permutation[k] < permutation[k + 1]:
            pivot = k
            break

    if pivot != -1:
        # find next greater
        for j in range(pivot + 1, len(permutation)):
            if permutation[j] > permutation[pivot] and permutation[j] < next_greater:
                next_greater = permutation[j]
                next_index = j

        # swap (OUTSIDE loop)
        permutation[pivot], permutation[next_index] = permutation[next_index], permutation[pivot]

    else:
        permutation.reverse()

    # reverse right side
    left = pivot + 1
    right = len(permutation) - 1

    while left < right:
        permutation[left], permutation[right] = permutation[right], permutation[left]
        left += 1
        right -= 1

    print(permutation)

    i += 1
'''
####some problem
'''
N=int(input())
sum_final=0
while N!=0:
    rem = N % 10
    fact = 1
    for i in range(1,rem+1):
        fact *= i
    sum_final+=fact
    N=N//10
print(sum_final)
'''
#circular linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        current=self.head
        while current:
            current=current.next
        current.next=new_node
        new_node.next=None
    def get_length(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count
    def insert_at_middle(self,data):
        new_node=Node(data)
        n=self.get_length()
        mid=n//2
        current=self.head
        count = 0
        while count<mid-1:
            current=current.next
        new_node.next=current.next
        current.next=new_node
'''
#### insertion sort
'''
arr = [4, 1, 3, 9, 7]
i=0
for j in range(i+1,len(arr)):
    i=j-1
    while i>=0 and arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
        i=i-1
print(arr)
'''
#quick sort technique
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort([4,1,3,7,9]))
'''
#train problem greedy approach
'''
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
arr.sort()
dep.sort()
i = 0
j = 0
count = 0
max_count = 0
while i<len(arr) and j<len(dep):
    if arr[i]<=dep[j]:
        count+=1
        i+=1
    else:
        count-=1
        j+=1
    max_count=max(count,max_count)
print(max_count)
'''
#########################################
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
to_be_sorted=[56,72,90,12,44,32,11]
final=merge_sort(to_be_sorted)
print(final)
'''
####toatal parking cost
'''
n=int(input())
cost=0
for i in range(1,n+1):
    if i<=2:
        cost+=100
    elif i<=5:
        cost+=50
    else:
        cost+=20
print(cost)
'''
# sum  of largest subarray
'''
arr=[2,3,4,1,5]
left=0
max_subarray_sum=0
subarray=[]
while left<len(arr):
    right=left+1
    while right<len(arr):
        if arr[right]!=arr[left]:
            sub_array=arr[left:right+1]
            if sum(sub_array)>max_subarray_sum:
                max_subarray_sum=sum(sub_array)
                subarray=sub_array
        right+=1
    left+=1
print(max_subarray_sum)
print(subarray)
'''
#####tcs  nqt question
'''
arr=list(map(int,input().split()))
max_count=0
result=arr[0]
for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count+=1
        if count>max_count:
            max_count=count
            result=arr[i]
        elif count==max_count:
            if  arr[i]<result:
                result=arr[i]
print(result)
'''
### finding the first and last postion in sorted arr
'''
nums=[5,7,7,8,8,10]
target=8
first_index=-1
last_index=-1
for i in range(len(nums)):
    if nums[i]==target:
        first_index=i
        break
if  first_index!=-1:
    for j in range(first_index,len(nums)):
        if nums[j]==target:
            last_index=j
        else:
            break
print([first_index,last_index])
'''
######## group anagrams
''''
strs = ["eat","tea","tan","ate","nat","bat"]
groups={}
for word in strs:
    key="".join(sorted(word))
    if key in groups:
        groups[key].append(word)
    else:
        groups[key]=[word]
final=list(groups.values())
print(final)
'''
#all sorting techniques for tcs
#bubble sort
'''
arr=[5,4,3,2,1]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
'''
#selection sort
'''
arr=[5,4,3,2,1]
for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)
'''
###insertion sort
'''
arr=[5,4,3,2,1]
i=1
while i<len(arr):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
    i+=1
print(arr)
'''
#merge sort
'''
def split_marge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = split_marge(left)
    right = split_marge(right)
    return merge(left, right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr=[5,4,3,2,1]
print(split_marge(arr))
'''
#quick sort
'''
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[-1]
    left=[]
    right=[]
    for i in range(len(arr)-1):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
arr = [5,4,3,2,1]
print(quick_sort(arr))
'''
#recursion problem
'''
def min_cost(cost,n):
    if n==0:
        return cost[0]
    if n==1:
        return cost[n]
    return cost[n] + min(min_cost(cost, n - 1), min_cost(cost, n - 2))
cost = [10, 15, 20]
n = len(cost)
print(min(min_cost(cost, n-1), min_cost(cost, n-2)))
'''
#reverse string using recursion
'''
def reverse_string(s,left,right):
    if left>right:
        return
    s[left],s[right]=s[right],s[left]
    reverse_string(s,left+1,right+1)
s = ["h","e","l","l","o"]
reverse_string(s, 0, len(s)-1)
print(s)
'''
#
'''
def myPow(x, n):
    if n==0:
        return 1
    return x*myPow(x, n-1)
x =2.00000
n = 10
s =myPow(x, n)
print("{:.5f}".format(s))
'''
#median of two sorted arrays
'''
nums1 = [1,2]
nums2 = [3,4]
new=sorted(nums1+nums2)
n=len(new)
if n%2==0:
    median=(new[n//2-1]+new[n//2])/2
else:
    median=new[n//2]
print(f'{median:.5f}')
'''
#longest palindromic substring
'''
string="babad"
left=0
substring=[]
max_substring=''
while left<len(string):
    right=left+1
    while right<=len(string):
        substring.append(string[left:right])
        right+=1
    left+=1
for sub in substring:
    if sub==sub[::-1] and len(sub)>len(max_substring):
        max_substring=sub
print(max_substring)
'''
##### zigzag conversion
'''
string="PAYPALISHIRING"
n=3
rows = [""] * n
row=0
going=True
for char in string:
    rows[row]+=char
    if row==0:
        going=True
    elif row==n-1:
        going=False

    if going:
        row+=1
    else:
        row-=1
final="".join(rows)
print(final)
'''
#cycle rotations tcs
'''
import math
def lcm(numbers):
    new=math.lcm(*numbers)
    return  new
Board = [2,3,1,5,4]
position_board={}
cycle=[]
numbers=[]
visited=set()
count_cycles=0
for i in range(len(Board)):
    position_board[i+1]=Board[i]
for key in position_board:
    if key not in visited:
        temp=[]
        while key not in visited:
            visited.add(key)
            temp.append(key)
            key=position_board[key]
        cycle.append(temp)
for cycle in cycle:
    nums=len(cycle)
    numbers.append(nums)
print(lcm(numbers))
'''
# tcs nqt
'''
A = list('abcab')
B = 'aaabb'
count=0
for char in set(B):
    pos=[]
    for i in range(len(A)):
        if A[i]!=char and B[i]==char:
            pos.append(i)
    if len(pos)>0:
        mini=A[pos[0]]
        for j in pos:
            if A[j]<mini:
                mini=A[j]
        if mini != char:
            print(-1)
        count+=1
        for j in pos:
            A[j]=char
print(A)
print(count)
'''
########continous subarray who sum is equal to k
'''
N = 10
K = 15
coins = [5, 3, 7, 14, 18, 1, 8, 4, 8, 3]
subarray = []
left = 0
while left < len(coins):
    right = left
    while right <= len(coins) - 1:
        sub=coins[left:right+1]
        if sum(sub)==K:
            subarray.append(sub)
        right+=1
    left+=1
print(subarray)
'''
#betting horses
'''
N = 10
K = 100
max_length=0
prices = [30,40,50,20,20,10,90,10,10,10]
left=0
final=[]
while left<len(prices):
    right=left
    while right<len(prices):
        sub=prices[left:right+1]
        if sum(sub)<K and len(sub)>max_length:
            max_length=len(sub)
            final=sub
        right+=1
    left+=1
print(final)
print(max_length)
'''
#fair subsequence
'''
A = [-1, 18, 13, 18, 2, 16, -1, -213, 11]
i=0
groups=[]
new=[]
while i<len(A):
    group=[]
    if A[i] < 0:
        while i < len(A) and A[i] < 0:
            group.append(A[i])
            i += 1
    else:
        while i<len(A) and A[i]>0:
            group.append(A[i])
            i+=1
    groups.append(group)
    if group[0]<0:
        new.append(max(group))
    else:
        new.append(max(group))
print(groups)
print(new)
'''
###
'''
prices = [2, 3, 4, 5]
volumes = [3, 4, 5, 6]
K = 7
max_volume = 0
def solve(i, total_price, total_volume):
    global max_volume
    if total_price > K:
        return
    max_volume = max(max_volume, total_volume)
    if i == len(prices):
        return
    solve(i + 1, total_price + prices[i], total_volume + volumes[i])
    solve(i + 1, total_price, total_volume)
solve(0, 0, 0)
print(max_volume)
'''
#chocolates tcs
'''
chocolates=[0,1,0,3,12,0]
write=0
for i in range(len(chocolates)):
    if chocolates[i]>=1:
        chocolates[write]=chocolates[i]
        write+=1
for j in range(write,len(chocolates)):
    chocolates[j]=0
print(chocolates)
'''
###########tyepwirites
'''
a="a##c"
b="#a#c"
res1=""
res2=""
for char in a:
    if char!="#":
        res1+=char
    else:
        res1=res1[:-1]
for char in b:
    if char!="#":
        res2+=char
    else:
        res2=res2[:-1]
if res1==res2:
    print("True")
else:
    print("false")
'''
#rangeof palindrome
'''
l=10
right=50
new=""
for i in range(l,right):
    s=str(i)
    if s==s[::-1]:
        print(i)
'''
#grocery store discount
'''
n=int(input())
amount=0
if n<1000:
    discount=5
    amount=n-((discount/100)*n)
elif n<=5000:
    discount=10
    amount = n-((discount / 100) * n)
else:
    discount=5
    amount =n- ((discount / 100) * n)
print(amount)
'''
#mergesort
'''
def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge(arr[:mid])
    right=merge(arr[mid:])
    return sort(left,right)
def sort(left,right):
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr=[5,4,3,2,1]
print(merge(arr))
'''
########insertion sort
'''
def insertion_sort(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[5,4,3,2,1]
print(insertion_sort(arr))
'''
#binary search
'''
arr = [1, 3, 5, 7, 9]
target=7
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
'''
########
'''
nums=[2,7,11,15]
target=9
seen = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in seen:
        print([seen[diff],i])
    seen[nums[i]]=i
'''
###
'''
s = "A man, a plan, a canal: Panama"
clean=""
for ch in  s:
    if ch.isalnum():
        clean+=ch.lower()
if clean==clean[::-1]:
    print("it is a palindrome")
else:
    print("No")
'''
#valid paranthesis
'''
s = "([]){}"
stack = []
for ch in s:
    if ch in "({[":
        stack.append(ch)
    else:
        if not stack:
            print("invalid")
            break

        top = stack.pop()

        if ch == ")" and top != "(":
            print("invalid")
            break
        if ch == "]" and top != "[":
            print("invalid")
            break
        if ch == "}" and top != "{":
            print("invalid")
            break
else:
    if len(stack) == 0:
        print("valid")
    else:
        print("invalid")
'''
#climb steps problem
'''
def climb_steps(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return climb_steps(n-1)+climb_steps(n-2)
print(climb_steps(3))
'''
#flipping bits
'''
arr=[0,1,0,1,1]
count=0
if arr[0]==0:
    count=1
for i in range(1,len(arr)):
    if arr[i]!=arr[i-1]:
        count+=1
print(count)
'''
############
'''
n=5
arr=[40,10,30,20,50]
index=2
element_before_sort=0
for i in range(len(arr)):
    if i==index:
        element_before_sort=arr[i]
new=sorted(arr)
for i in range(len(new)):
    if new[i]==element_before_sort:
        print(i)
'''
###########
'''
height = [1,8,6,2,5,4,8,3,7]
i=0
j=len(height)-1
max_water=0
while i<j:
    width=j-i
    h=min(height[i],height[j])
    area=width*h
    if area>max_water:
        max_water=area
    if height[i]<height[j]:
        i+=1
    else:
        j-=1
print(max_water)
'''
#################################
'''
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        # This index is in ORIGINAL array
        print("Pivot:", arr[pivot_index], "Original Index:", pivot_index, "->", arr)

        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]  # last element
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1
arr = [5, 4, 3, 2, 1]
quicksort(arr, 0, len(arr) - 1)
print("Final:", arr)
'''
#tcs status using hasing
'''
n=int(input())
values_dict={}
sum_count=0
for i in range(n):
    key,value=map(int,input().split())
    values_dict[key]=value
q=int(input())
for i in range(q):
    queruid=int(input())
    for key,values in values_dict.items():
        if key==queruid:
            if values==1:
                sum_count+=queruid
            else:
                sum_count-=queruid
            break
print(sum_count)
'''
#quicksort using pivot as 1st element
'''
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[]
    right=[]
    for i in range(1,len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
arr=[5,3,8,4,2]
print(quick_sort(arr))
'''
####correct quicksort
'''
def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=len(arr)-1
    while True:
        while i<=high and arr[i]<pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low],arr[j] = arr[j], arr[low]
    print(j,end=" ")
    return j
def quick_sort(arr,low,high):
    if low<high:
        pindex=partition(arr,low,high)
        quick_sort(arr,low,pindex-1)
        quick_sort(arr, pindex + 1, high)
n = 5
arr =[8,7,6,5,4]
quick_sort(arr, 0, n - 1)
print()
for i in range(n):
    print(arr[i], end=" ")
'''
# merge_sort
'''
def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge(left)
    right=merge(right)
    return sort(left,right)
def sort(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
arr=[5,4,3,2,1]
print(merge(arr))
'''
#spiral matrix
'''
def spiral_matrix(matrix):
    result=[]
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1

        if top<=bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top - 1, -1):
                result.append(matrix[i][left])
            left+=1
    return result
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix(matrix))
'''
###
'''
def ship_with_weight(weights,days):
    left=max(weights)
    right=sum(weights)
    while left<right:
        mid=(left+right)//2
        total=0
        needed_days=1
        for w in weights:
            if total+w>mid:
                needed_days+=1
                total=0
            total+=w

        if needed_days<=days:
            right=mid
        else:
            left=mid+1
    return left
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(ship_with_weight(weights,days))
'''
###########################################
'''
matrix=[[1,2,3],[4,5,6],[7,8,9]]
valid_matrix=10
count=0
for i in range(len(matrix)):
    sum_matrix=0
    for j in range(len(matrix[0])):
        sum_matrix+=matrix[i][j]
    if sum_matrix>valid_matrix:
        count+=1
print(count)
'''
#merge_intervals_overlap
'''
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
result=[]
for interval in intervals:
    if not result:
        result.append(interval)
    else:
        last=result[-1]
        if interval[0]<last[1]:
            last[1]=max(last[1],interval[1])
        else:
            result.append(interval)
print(result)
'''
#set matrix zeros
'''
matrix = [[1,1,1],[1,0,1],[1,1,1]]
rows=len(matrix)
cols=len(matrix[0])
zeros_rows=set()
zeros_cols=set()
for i in range(rows):
    for j in range(cols):
        if matrix[i][j]==0:
            zeros_rows.add(i)
            zeros_cols.add(j)
for i in zeros_rows:
    for j in range(cols):
        matrix[i][j]=0
for j in zeros_cols:
    for i in range(rows):
        matrix[i][j] = 0
print(matrix)
'''
#subarray sum  equal to k
'''
nums = [1, 1, 1]
k=2
count = 0
sums = 0
d = {0: 1}
for num in nums:
    sums += num
    count += d.get(sums - k, 0)
    d[sums] = d.get(sums, 0) + 1
print(count)
'''
################tcs
'''
arr=[7,4,8,2,9]
count=0
for i in range(len(arr)):
    before_elements=arr[:i]
    if arr[i]>max(before_elements):
        count+=1
print(count)
'''
#########################
'''
set_str = "bbbaaababa"
value=3
new=[]
i=0
count=0
while i<len(set_str):
    ram=[]
    for j in range(value):
        if i+j<len(set_str):
            ram.append(set_str[i+j])
    new.append(ram)
    count+=1
    if len(ram)!=value:
        count-=1
    i+=value
print(count)
'''
#international round table conference
'''
matrixA=[[1,2],
         [3,4]]
matrixB=[[5,6],
         [7,8]]
result=[]
rows=len(matrixA)
cols=len(matrixB[0])
for i in range(rows):
    row=[]
    for j in range(cols):
        sum_val = 0
        for k in range(len(matrixB)):
            sum_val+=matrixA[i][k]*matrixB[k][j]
        row.append(sum_val)
    result.append(row)
print(result)
'''
###quik sort poorna anna approach
'''
def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=len(arr)-1
    while True:
        while i<=high and arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    print(j,end="")
    return j
def quick_sort(arr,low,high):
    if low<high:
        pindex=partition(arr,low,high)
        quick_sort(arr, low, pindex - 1)
        quick_sort(arr, pindex + 1, high)
n = 5
arr =[5,4,3,2,1]
quick_sort(arr, 0, n - 1)
print()
for i in range(n):
    print(arr[i], end=" ")
'''
#sqaures of sorted array
'''
nums = [-4,-1,0,3,10]
squ_numbers=[]
for i in range(len(nums)):
    sq=nums[i]**2
    squ_numbers.append(sq)
print(sorted(squ_numbers))
'''
# https://leetcode.com/problems/task-scheduler/description/
'''
from collections import Counter
def leastInterval(tasks, n):
    freq = Counter(tasks)
    print(freq)
    maxFreq = max(freq.values())
    countMax = list(freq.values()).count(maxFreq)
    ans = (maxFreq - 1) * (n + 1) + countMax
    return max(len(tasks), ans)
tasks = ["A","C","A","B","D","B"]
n = 1
print(leastInterval(tasks,n))
'''
#tcs today questions
'''
sum_prime=0
inp=[2,3,4,5,6,7]
prime=False
for j in inp:
    for i in range(2,j):
        if j%i==0:
            prime=False
        prime=True
    if prime:
        print(j)
'''

##
'''
serial=[1,2,3,4]
benefit=[10,20,30,40]
capacity=[2,3,4,5]
N=6
dict_print={}
for i in range(len(serial)):
    for j in range(i+1,len(serial)):
        if capacity[i]+capacity[j]<=N:
            valid_pairs=(serial[i],serial[j])
            sum_benfits=benefit[i]+benefit[j]
            dict_print[valid_pairs]=sum_benfits
print(max(dict_print.values()))
'''

###length of longest substring without nonrepeating characters
'''
s="abcabcbb"
left=0
max_substring_length=0
max_substring=""
while left<len(s):
    seen=set()
    substring=""
    right=left
    while right<len(s):
        if s[right] in seen:
            break
        seen.add(s[right])
        substring+=s[right]
        if len(substring) > max_substring_length:
            max_substring_length = len(substring)
            max_substring = substring
        right += 1
        left += 1
print(max_substring_length)
print(max_substring)
'''
#longest palindromic substring
'''
s="babad"
left=0
max_longest_length_palindrome_substring=0
max_palindrome_substring=""
while left<len(s):
    right=left
    substring=""
    while right<len(s):
        substring+=s[right]
        if substring==substring[::-1] and len(substring)>max_longest_length_palindrome_substring:
            max_longest_length_palindrome_substring = len(substring)
            max_palindrome_substring = substring
        right+=1
    left+=1
print(max_longest_length_palindrome_substring)
print(max_palindrome_substring)
'''
#own question
#max consecutive bit
'''
arr = [0,1,0,1,1,1,1]
max_count = 0
count = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        count += 1
    else:
        count = 1

    if count > max_count:
        max_count = count

print(max_count)
'''
#maximum gap leetcode problem
'''
nums = [3,6,9,1]
nums.sort()
max_difference=0
for i in range(1,len(nums)):
    difference=nums[i]-nums[i-1]
    if difference > max_difference:
        max_difference=difference
print(max_difference)
'''
#group anagrams
'''
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups={}
for word in strs:
    key="".join(sorted(word))
    if key in groups:
        groups[key].append(word)
    else:
        groups[key]=[word]
final=list(groups.values())
print(final)
'''
#convert 1d into 2d array
'''
original = [1,2,3,4]
m=2
n=2
result=[]
i=0
for row in range(m):
    temp=[]
    for col in range(n):
        temp.append(original[i])
        i+=1
    result.append(temp)
print(result)
'''
#rotate image
'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]   #output should be [[7,4,1],[8,5,2],[9,6,3]]
for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for row in matrix:
    row.reverse()
print(matrix)
'''
################
'''
def totalUnique(s):
    total = 0
    i = 0
    while i < len(s):
        j = i
        while j < len(s):
            sub = s[i:j + 1]

            unique_chars = set(sub)
            count = 0

            for ch in unique_chars:
                if sub.count(ch) == 1:
                    count += 1

            total += count
            j += 1
        i += 1

    return total
print(totalUnique("ABC"))
'''
##bubblesort
'''
arr=[5,4,3,2,1]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
'''
#quicksort
'''
def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= high and arr[i] < pivot:
            i += 1

        while j >= low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    print(j, end=" ")
    return j


def quick_sort(arr, low, high):
    if low < high:
        pindex = partition(arr, low, high)

        quick_sort(arr, low, pindex - 1)
        quick_sort(arr, pindex + 1, high)


arr = [5, 4, 3, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
'''
#####4
'''
def partition(arr, low, high):
    pivot = arr[high]   # last element as pivot
    i = low - 1         # pointer for smaller elements

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pindex = partition(arr, low, high)

        quick_sort(arr, low, pindex - 1)
        quick_sort(arr, pindex + 1, high)


# Driver code
arr = [5, 4, 3, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
'''

'''

def can_complete(gas, cost):
    total = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]

        total += diff
        tank += diff

        if tank < 0:
            start = i + 1
            tank = 0

    if total >= 0:
        return start
    else:
        return -1
print(can_complete([1,2,3,4,5],[3,4,5,1,2]))
'''
###################
'''
colum_title="AB"
result=0
for ch in colum_title:
    value = ord(ch) - ord('A') + 1
    result = result * 26 + value
print(result)
'''
#mine tcs problem
'''
arr = input().split()

# Validate input
try:
    arr = list(map(int, arr))
except:
    print("Invalid Input")
    exit()

if len(arr) < 3:
    print("Invalid Input")
    exit()

n, weight = arr[0], arr[1]
values = arr[2:]

if n != len(values):
    print("Invalid Input")
    exit()

result = []

for i in range(len(values)):
    current_sum = 0
    count = 0

    for j in range(i, len(values)):
        if current_sum + values[j] <= weight:
            current_sum += values[j]
            count += 1
        else:
            break
    if count >= 2:
        result.append(values[i])

print(result)
'''
#polymorphsim
'''
class Robo():
    def learn(self):
        print("robots can  learn")
    def charge(self):
        print("robots can charge")
    def tasks(self):
        print("robots can do tasks")
def operaterobo(robo):
    robo.learn()
    robo.tasks()
    robo.charge()
robo=Robo()
operaterobo(robo)
robo2=Robo()
operaterobo(robo2)
'''

#casting  is no needed in python
'''
class Media:
    def play(self):
        print("media plays generic content")

    def display_info(self):
        print("Displaying media information")


# Child class Video
class Video(Media):
    def play(self):   # method overriding
        print("video plays with animation")

    def adjust_quality(self):
        print("adjusting video quality settings")


# Child class Photo
class Photo(Media):
    def play(self):   # method overriding
        print("photo shows with effects")

    def apply_filter(self):
        print("applying filter to photo")
mymedia=Video()
mediaphoto=Photo()
mymedia.play()
mymedia.adjust_quality()
mediaphoto.apply_filter()
'''
#decrease value of food everytime you purchase
'''
N = int(input())
M = int(input())
vd = {}
for i in range(N):
    v = int(input())
    d = int(input())

    vd[i] = [v, d]

total_best = 0
for j in range(M):
    current_best=-1
    best_food=-1
    for key,values in vd.items():
        current_taste=values[0]
        if current_taste>current_best:
            current_best=current_taste
            best_food=key
    total_best+=current_best
    vd[best_food][0]=vd[best_food][0]-vd[best_food][1]
print(total_best)
'''
#infosys 2nd question(medium problem)
'''
def kadane(arr):
    cur = arr[0]
    best = arr[0]
    for i in range(1, len(arr)):
        cur = max(arr[i], cur + arr[i])
        best = max(best, cur)
    return best
n = 5
arr = [3,-8,4,5,-2]
ans = kadane(arr)
for i in range(n):
    for j in range(i + 1, n):
        arr[i], arr[j] = arr[j], arr[i]
        ans = max(ans, kadane(arr))
        arr[i], arr[j] = arr[j], arr[i]
print(ans)
'''
#backtracking problem best
'''
def solve(remaining, ans):
    if len(remaining) == 0:
        print(ans)
        return
    for i in range(1, len(remaining) + 1):
        group = remaining[:i]
        ans.append(group)
        solve(remaining[i:], ans)
        ans.pop()
n = 3
nums = [1,2,3]
solve(nums, [])
'''
# maximum sum of non adjacent houses
'''
def solve(i, total):
    global ans
    if i >= n:
        ans = max(ans, total)
        return
    solve(i + 2, total + arr[i])  # take
    solve(i + 1, total)           # skip
arr = [3,2,7,10]
n = len(arr)
ans = 0

solve(0, 0)

print(ans)
'''
#another way of solving non adjacent houses robbery
'''
arr = [3,2,7,10,11,12]
def solve(i):
    if i >= len(arr):
        return 0
    take = arr[i] + solve(i + 2)
    skip = solve(i + 1)
    return max(take, skip)
print(solve(0))
'''
#next permutation
'''
arr=[1,2,3]
pivot=-1
for i in range(len(arr)-2,-1,-1):
    if arr[i]<arr[i+1]:
        pivot=i
        break
if pivot!=-1:
    next_biggest=float('inf')
    index=-1
    for j in range(pivot+1,len(arr)):
        if arr[j]>arr[pivot] and arr[j]<next_biggest:
            next_biggest=arr[j]
            index=j
        arr[j],arr[pivot]=arr[pivot],arr[j]
left=pivot+1
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)
'''
#recursion and backtracking
'''
def tone(i,n):
    if i==n:
        return n
    else:
        print(i)
    return tone(i+1,n)
n=3
print(tone(0,3))
'''
############
''''
def recurs(n):
    if n==0:
        return 0
    return n+recurs(n-1)
a=int(input())
print(recurs(a))
'''
######fibonacci
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))
'''
#####Tower of Hanoi algorithm
'''
def towerofhanoi(n,src,helper,destination):
    if n==1:
        print("transferdisk",n,"from",src,"to",destination)
        return
    towerofhanoi(n-1,src, destination, helper)
    print("transfer disk",n,"from",src,"to",destination)
    towerofhanoi(n-1,helper, src, destination)
n=3
towerofhanoi(n,"S",'H',"D")
'''
########string in reverse using recursion
'''
def reverse(a, i):
    if i == 0:
        print(a[i])
        return
    print(a[i])
    reverse(a, i-1)
a = "abcd"
length = len(a)-1
reverse(a, length)
'''
######
'''
arr=[0,0,1,1,1,2,2,3,3,4]

i=0

for j in range(1,len(arr)):

    if arr[i] != arr[j]:
        i += 1
        arr[i] = arr[j]

print(arr[:i+1])
'''
#infosys problem
#cost of string is balanced
'''
s = ")("
cost_of_adding_opened=2
cost_of_adding_closed=3
stack=[]
open_needed=0
for ch in s:
    if ch=="(":
        stack.append(ch)
    else:
        if stack:
            stack.pop()
        else:
            open_needed+=1
closed_needed=len(stack)
total_cost=(open_needed*cost_of_adding_opened) + (closed_needed*cost_of_adding_closed)
print(open_needed)
print(closed_needed)
print(total_cost)
'''
## josephus problem
'''
arr=[1,2,3,4,5]
n=2
i=0
while len(arr)>1:
   i=i+n-1
   while i>=len(arr):
       i=i-len(arr)
   arr.pop(i)
print(arr[0])
'''
###josephus problem using recursion
'''
k=2
def josephus(arr,i):
    if len(arr)==1:
        return arr[0]
    i=i+k-1
    while i>=len(arr):
        i=i-len(arr)
    arr.pop(i)
    return josephus(arr,i)
arr=[1,2,3,4,5]
print(josephus(arr,0))
'''
###merge two sorted_list using recursion
'''
list1=[1,2,4]
list2=[1,3,4]

def merge(list1,list2):

    if len(list1)==0:
        return list2

    if len(list2)==0:
        return list1

    if list1[0] <= list2[0]:
        return [list1[0]] + merge(list1[1:],list2)

    else:
        return [list2[0]] + merge(list1,list2[1:])

print(merge(list1,list2))
'''
########subsets of a given array  using recursion
'''
def subsets(arr):
    result=[]
    def backtrack(index,current):
        if index==len(arr):
            result.append(current[:])
            return
        current.append(arr[index])
        backtrack(index+1,current)
        current.pop()
        backtrack(index+1,current)
    backtrack(0,[])
    return result
print(subsets([1,2,3]))
'''
#top infosys
#elimination game
'''
def eliminate_game(arr):

    left = True

    while len(arr) > 1:

        new = []

        # LEFT TO RIGHT
        if left:

            for i in range(len(arr)):

                # keep alternate positions
                if i % 2 == 1:
                    new.append(arr[i])

        # RIGHT TO LEFT
        else:

            arr.reverse()

            for i in range(len(arr)):

                # keep alternate positions
                if i % 2 == 1:
                    new.append(arr[i])

            new.reverse()

        arr = new

        # change direction
        left = not left

    return arr[0]


print(eliminate_game([1,2,3,4,5,6,7,8,9]))
'''
##recursion using elimination game
'''
def recurse_eliminate(arr, n, left):

    if n == 1:
        return arr[0]

    new = []

    if left:

        for i in range(n):

            if i % 2 == 1:
                new.append(arr[i])

        return recurse_eliminate(new, n//2, False)

    else:

        arr.reverse()

        for j in range(n):

            if j % 2 == 1:
                new.append(arr[j])

        new.reverse()

        return recurse_eliminate(new, n//2, True)


print(recurse_eliminate([1,2,3,4,5,6,7,8,9], 9, True))
'''
# recursion leetcode
'''
def invert(value):

    result = ""

    for ch in value:

        if ch == "1":
            result += "0"
        else:
            result += "1"

    return result


def reverse(value):
    return value[::-1]


def bittostring(n):
    s = "0"
    for i in range(2, n + 1):
        s = s + "1" + reverse(invert(s))
    return s
def getvalue(n, k):
    found_value = bittostring(n)
    return found_value[k - 1]
n = int(input())
k = int(input())

print(getvalue(n, k))
'''
#winner of circular game
'''
def removekthperson(arr,k,index=0):
    if len(arr)<=1:
        return arr[0]
    new=[]
    remove_index=(index+k-1)%len(arr)
    for i in range(len(arr)):
        if i!=remove_index:
            new.append(arr[i])
    return removekthperson(new,k,remove_index%len(new))
print(removekthperson([1,2,3,4,5],2))
'''
#kth symbol in grammar
'''
n=int(input())
k=int(input())
def build(row,current_row):
    if current_row==n:
        return row
    new=""
    for ch in row:
        if  ch=="0":
            new+="01"
        else:
            new+="10"
    return build(new,current_row+1)
'''
#### printing numbers of insertion sort in desceinfinf order
'''
def insertion_sort(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return  arr
arr=[3,2,4,6,2]
sorted=insertion_sort(arr)
for i in range(len(sorted)-1,-1,-1):
    print(sorted[i])
'''
#### finding all permutations using backtracking
#start with empty path
'''
nums = [1,2,3]

def backtrack(path):

    if len(path) == 3:
        print(path)
        return

    for num in nums:

        if num not in path:
            path.append(num)
            backtrack(path)
            path.pop()

backtrack([])
'''
#making two arrays equal by reversing subarrays
'''
target=list(map(int,input().split()))
arr=list(map(int,input().split()))
found=False
left=0
while left<len(arr):
    right=left+1
    while right<len(arr):
        subarray=arr[left:right+1]
        arr[left:right+1]=subarray[::-1]
        if arr==target:
            print(arr)
            found=True
        arr[left:right+1]=subarray
        right+=1
    left+=1
if not found:
    print("not possible")
'''
#####partition array according to given pivot
'''
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
list1=[]
list2=[]
list3=[]
for i in range(len(nums)):
    if nums[i]<pivot:
        list1.append(nums[i])
    elif nums[i]==pivot:
        list2.append(nums[i])   
    else:
        list3.append(nums[i])
result=list1+list2+list3
print(result)
'''
# H-INDEX
'''
citations = [3,0,6,1,5]#6 5 3 1 0
citations.sort(reverse=True)
n=len(citations)
count=0
new=[]
for i in range(n):
    if citations[i]>i:
        count+=1
print(count)
'''
#two pointers
'''
nums = [2,3,4,1,5]#1 2 3 4 5
nums.sort()
left = 0
right = len(nums) - 1
target = 8
while left <= right:
    result = nums[left] * nums[right]
    if result == target:
        print(nums[left], nums[right])
        break
    elif result < target:
        left += 1
    else:
        right -= 1
'''
#char mapping transformers based on rules
'''
n=int(input())
a,b=map(str,input(" "))
arr_list=list(map(str,input().split()))
count_a=0
count_b=0
for char in arr_list:
    if char==a:
        count_a+=1
    else:
        count_b+=1
print(count_a,count_b)
print(count_a,count_b)
print("n")
print(arr_list)
return_type=arr_list.sort('asdf')
#1 row sudoku
'''
#heap sort the arr
'''
def heapify(arr, n, i):

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print(arr)
'''
#design the stacks
'''
intervals = [[1,2],[2,3],[3,4],[1,3]]
after sorting =[[1,2],[2,3],[3,3][1,4]]
end=2
count = 0

for i in range(len(intervals)):

    current_interval_start = intervals[i][0]
    current_interval_end = intervals[i][1]

    for j in range(i + 1, len(intervals)):

        if intervals[j][0] < current_interval_end and intervals[j][1] > current_interval_start:

            count += 1

            intervals.pop(j)
            break

print(count)
'''
###### largest rectangle of 1s in a grid
#initially all heights are zero
'''
def largest_rectangle_histogram(heights):
    max_area = 0

    for i in range(len(heights)):

        left = i
        while left > 0 and heights[left - 1] >= heights[i]:
            left -= 1

        right = i
        while right < len(heights) - 1 and heights[right + 1] >= heights[i]:
            right += 1

        width = right - left + 1
        current_area = heights[i] * width

        if current_area > max_area:
            max_area = current_area

    return max_area


matrix = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]

heights = [0] * len(matrix[0])

max_area = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            heights[j] += 1
        else:
            heights[j] = 0

    print("Histogram:", heights)

    area = largest_rectangle_histogram(heights)
    print("Largest Area:", area)

    if area > max_area:
        max_area = area

print("Maximum Rectangle Area =", max_area)
'''
#task manager system using linked list
#we wanted to do all the tasks and perform valid operations using linkedlist
'''
class TaskNode:
    def __init__(self,title):
        self.title = title
        self.status="pending"
        self.next=None
class TaskManager:
    def __init__(self):
        self.head=None

    def addTask(self, title):
        new_node = TaskNode(title)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def completeTask(self, index):
        current = self.head
        count = 0

        while current is not None and count < index:
            current = current.next
            count += 1

        if current is not None:
            current.status = "Completed"
    def deleteTask(self,index):
        current=self.head
        previous=None
        count=0
        while current is not None and count<index:
            previous=current
            current=current.next
            count+=1
        if current is not None:
            if previous is None:
                self.head=self.head.next
            else:
                previous.next=current.next

    def printTask(self):
        current = self.head

        while current is not None:
            print(current.title, current.status, end=" ")
            current = current.next
        print()
    def countTasks(self):
        count=0
        current=self.head
        while current is not None:
            count+=1
            current=current.next
        return count
    def countofpendingandcompleted(self):
        current=self.head
        pending_count=0
        completed_count=0
        current=self.head
        while current is not None:
            if current.status == "Completed":
                completed_count+=1
            else:
                pending_count+=1
            current=current.next
        return f'pending:{pending_count},completed:{completed_count}'



n = int(input())
new=TaskManager()
for _ in range(n):
    command = input().split()
    if command[0]=="addTask":
        new.addTask(command[1])
    elif command[0] == "completeTask":
        new.completeTask(int(command[1]))

    elif command[0] == "deleteTask":
        new.deleteTask(int(command[1]))

    elif command[0] == "printTask":
        new.printTask()

    elif command[0] == "countTasks":
        print(new.countTasks())

    elif command[0] == "countofpendingandcompleted":
        print(new.countofpendingandcompleted())

'''
#central star user
'''
n=int(input())
empty_dict={}
set_list=[]
for _ in range(n-1):
    a,b=input().split()
    set_list.append(a)
    set_list.append(b)
for char in set(set_list):
    empty_dict[char]=0
for val in set_list:
    if val in empty_dict:
        empty_dict[val]+=1
    else:
        empty_dict[val]=1
for key,values in empty_dict.items():
    if values==n-1:
        print(key)
'''
#smallest missing postive integer
'''
n = int(input())
arr = list(map(int, input().split()))
i = 0
while i < n:
    correct = arr[i] - 1
    if 1 <= arr[i] <= n and arr[i] != arr[correct]:
        arr[i], arr[correct] = arr[correct], arr[i]
    else:
        i += 1
for i in range(n):
    if arr[i] != i + 1:
        print(i + 1)
        break
else:
    print(n + 1)
'''
###
'''
days,target=input().split()
days=int(days)
target=int(target)
daily_profit_loss=list(map(int,input().split()))
max_sum=0
current_sum=0
for i in range(len(daily_profit_loss)):
    if daily_profit_loss[i]>0:
        current_sum+=daily_profit_loss[i]
    else:
        current_sum=0
    if current_sum>max_sum:
        max_sum=current_sum

freq = {0: 1}
prefix = 0
count = 0
for num in daily_profit_loss:
    prefix += num
    if prefix - target in freq:
        count += freq[prefix - target]
    freq[prefix] = freq.get(prefix, 0) + 1
print(max_sum,count)
'''
#####isomorphic strings
'''
s1=input()
s2=input()
dict_mappings={}
is_isomorphic=True
if len(s1)!=len(s2):
    is_isomorphic=False
else:
    for char in range(len(s1)):
        if s1[char] not in dict_mappings:
            if s2[char] in dict_mappings.values():
                is_isomorphic=False
                break
            dict_mappings[s1[char]]=s2[char]
        else:
            if dict_mappings[s1[char]]!=s2[char]:
                is_isomorphic=False
                break
print(is_isomorphic)
'''
#reverse a linkedlist
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def add_linked_list(self, text):
        new_node = Node(text)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def reverse_ll(self):
        prev=None
        current=self.head
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
news=LinkedList()
news.add_linked_list(4)
news.add_linked_list(3)
news.add_linked_list(2)
news.add_linked_list(1)
news.reverse_ll()
news.display()
'''
##########
'''
nums = [2, 3, -2, 4]

max_product = nums[0]
curr_max = nums[0]
curr_min = nums[0]

for i in range(1, len(nums)):
    num = nums[i]

    temp = curr_max

    curr_max = max(num, num * curr_max, num * curr_min)
    curr_min = min(num, num * temp, num * curr_min)

    max_product = max(max_product, curr_max)

print(max_product)
'''
'''
string = ["a", "a", "b", "b", "c", "c", "c"]

i = 0
index = 0
count = 1

while i < len(string)-1:

    if string[i+1] == string[i]:
        count += 1
        i += 1

    else:
        string[index] = string[i]
        index += 1

        if count > 1:
            string[index] = str(count)
            index += 1

        count = 1
        i += 1

string[index] = string[i]
index += 1

if count > 1:
    string[index] = str(count)
    index += 1

print(string[:index])
'''
###
'''
s = "3[a]2[bc]"
stack = []
for char in s:
    if char != "]":
        stack.append(char)
    else:
        new=""
        while stack[-1] != "[":
            new = stack.pop()+new
        stack.pop()
        k=stack.pop()
        new = new * int(k)
        stack.append(new)
print(stack)
'''
#monotonic stack
'''
temperatures=[73,74,75,71,69,72,76,73]
stack=[]
wait=[0]*len(temperatures)
for i in range(len(temperatures)):
    while stack and temperatures[i]>temperatures[stack[-1]]:
        index=stack.pop()
        wait[index]=i-index
    stack.append(i)
print(wait)
'''
#####Evaluate Reverse Polish Notation
'''
tokens = ["2","1","+","3","*"]
stack=[]
result=0
for char in tokens:
    if char.isnumeric():
        stack.append(int(char))
    else:
        operator=char
        first_operand=stack.pop()
        second_operand=stack.pop()
        result =eval(f'{second_operand}{operator}{first_operand}')
        stack.append(result)
print(stack[0])
'''
#sliding window maximum
'''
nums=[1,3,-1,-3,5,3,6,7]
k=3
left=0
max_elements=[]
while left<len(nums)-k:
    right=left+k
    sub=nums[left:right]
    max_elements.append(max(sub))
    left+=1
print(max_elements)
'''
#solving above using deque
'''
from collections import deque
nums=[1,3,-1,-3,5,3,6,7]
max_elements=[]
k=3
dq=deque()
j=0
for i in range(k):
    while dq and nums[dq[-1]]<nums[i]:
        dq.pop()
    dq.append(i)

max_elements.append(nums[dq[0]])
for i in range(k,len(nums)):
    while dq and dq[0]<=i-k:
        dq.popleft()
    while dq and nums[dq[-1]]<nums[i]:
        dq.pop()
    dq.append(i)
    max_elements.append(nums[dq[0]])
print(max_elements)
'''
#adding two numbers in linked list
'''
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_from_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    def add_from_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    def add_two_linked_list(self, other):
        current_1 = self.head
        current_2 = other.head
        while current_1 and current_2:
            sum_val = current_1.data + current_2.data
            print(sum_val)
            current_1 = current_1.next
            current_2 = current_2.next
LL1 = LinkedList()
LL2 = LinkedList()
LL1.add_from_last(1)
LL1.add_from_last(2)
LL1.add_from_last(3)
LL2.add_from_last(4)
LL2.add_from_last(5)
LL2.add_from_last(6)
LL1.display()
LL2.display()
LL1.add_two_linked_list(LL2)
'''
######
'''
def process_orders(orders):
    totals={}
    for user,price,quantity in orders:
        if price<0:
            print(f"invalid price for user:{user}")
        elif quantity<0:
            print(f"invalid quantity for user:{user}")
        else:
            for char in user:
                if char.isdigit():
                    print(f"suspicious for  user:{user}")
        else:
            totals[user]=price*quantity
n=int(input())
orders=[]
for _ in range(n):
    parts=input().split()
    user=parts[0]
    price=int(parts[1])
    quantity=int(parts[2])
    orders.append((user, price, quantity))
process_orders(orders)
'''
#greedy approach marble problem4
#brute force
'''
Weights = [1, 3, 5, 1]
k = 2

max_sum = 0
min_sum = float('inf')

for i in range(len(Weights) - 1):   # cut after index i

    curr_sum = 0
    i_weight = []
    j_weight = []

    for x in range(i + 1):
        i_weight.append(Weights[x])

    for j in range(i + 1, len(Weights)):
        j_weight.append(Weights[j])

    curr_sum = (i_weight[0] + i_weight[-1]) + (j_weight[0] + j_weight[-1])

    if curr_sum > max_sum:
        max_sum = curr_sum

    if curr_sum < min_sum:
        min_sum = curr_sum

final_sum = max_sum - min_sum
print(final_sum)
'''
#optimal approach
'''
def putMarbles(weights, k):
    pair_sum = []
    for i in range(len(weights) - 1):
        pair_sum.append(weights[i] + weights[i + 1])
    pair_sum.sort()
    min_sum = 0
    max_sum = 0
    for i in range(k - 1):
        min_sum += pair_sum[i]
        max_sum += pair_sum[len(pair_sum) - 1 - i]
    return max_sum - min_sum
weights = [1, 3, 5, 1]
k = 3
print(putMarbles(weights, k))
'''
# square Matrix
#read the matrix,print the original matrix, transpose it, print the transpose matrix, find both diagonals of transpose matrix, consider only even numbers, if a number appears in both diagonalscount it once, p[rint the sum
'''
matrix=[[1,2,3],[4,5,6],[7,8,9]]
#printint the transpose of a matrix
final=[]
left_diagonal=[]
right_diagonal=[]
final_fixed=[]
for i in range(len(matrix)):
    new_matrix=[]
    for j in range(len(matrix)):
        new_matrix.append(matrix[j][i])
    final.append(new_matrix)
for k in range(len(matrix)):
    left_diagonal.append(matrix[k][k])
    right_diagonal.append(matrix[k][len(matrix)-k-1])
final_fixed=set(left_diagonal+right_diagonal)
print(sum(final_fixed))
'''
#first and last occurance
'''
def searchRange(nums, target):
    first = -1
    last = -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return [first, last]
nums = [5,7,7,8,8,10]
print(searchRange(nums,8))
'''
#finding the right interval binary search
'''
intervals = [[3,4],[2,3],[1,2]]
interval_ranges = [-1] * len(intervals)
for i in range(len(intervals)):
    current_char=intervals[i]
    min_start = float("inf")
    index = -1
    for j in range(len(intervals)):
        if current_char!=intervals[j]:
            if intervals[j][0]>=current_char[1]:
                if intervals[j][0] < min_start:
                    min_start = intervals[j][0]
                    index = j
    interval_ranges[i]=index
print(interval_ranges)
'''
#same problem  with binary search
'''
intervals = [[3,4],[2,3],[1,2]]
starts = []
for i in range(len(intervals)):
    starts.append((intervals[i][0], i))
starts.sort()
answer = [-1] * len(intervals)
for i in range(len(intervals)):
    current_char = intervals[i]
    low = 0
    high = len(starts) - 1
    index = -1
    while low <= high:
        mid = (low + high) // 2
        if starts[mid][0] >= current_char[1]:
            index = starts[mid][1]
            high = mid - 1
        else:
            low = mid + 1
    answer[i] = index
print(answer)
'''
#something key value pairs using binarysearch
'''
class TimeStamp:
    answer=""
    fit_dict = {}
    def set(self, key, value, timestamp):
        if key not in self.fit_dict:
            self.fit_dict[key] = [(timestamp, value)]
        else:
            self.fit_dict[key].append((timestamp, value))
    def get(self,key,timestamp):
        if key not  in self.fit_dict:
            return ""
        else:
            left=0
            right=len(self.fit_dict[key])-1
            while left<=right:
                mid=(left+right)//2
                if self.fit_dict[key][mid][0]==timestamp:
                    return self.fit_dict[key][mid][1]
                elif self.fit_dict[key][mid][0]<timestamp:
                    self.answer=self.fit_dict[key][mid][1]
                    left=mid+1
                else:
                    right=mid-1
        return self.answer
new=TimeStamp()
new.set("foo","bar",1)
print(new.get("foo", 1))
print(new.get("foo", 3))
new.set("foo", "bar2", 4)
print(new.get("foo", 4))
print(new.get("foo", 5))
'''
#search a 2d matrix
'''
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 16
low = 0
high = len(matrix) - 1
binary_search_row=0
while low <= high:
    mid = (low + high) // 2
    if matrix[mid][0] <= target <= matrix[mid][-1]:
        binary_search_row = mid
        break
    elif target < matrix[mid][0]:
        high = mid - 1
    else:
        low = mid + 1
row = matrix[binary_search_row]
low = 0
high = len(row) - 1
while low <= high:
    mid = (low + high) // 2

    if row[mid] == target:
        print(True)
        break

    elif row[mid] < target:
        low = mid + 1

    else:
        high = mid - 1
else:
    print(False)
'''
#intenchning reverseingcharacter in string
'''
string = list("kodnest")
vowels = ['a', 'e', 'i', 'o', 'u']
left = 0
right = len(string) - 1
while left < right:
    if string[left] not in vowels and string[right] not in vowels:
        left += 1
    elif string[left] in vowels and string[right] not in vowels:
        right -= 1
    elif string[left] in vowels and string[right] in vowels:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    else:
        left += 1
print("".join(string))
'''
#fibonacci using dp

def fib(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]
n = 5
dp = [-1] * (n + 1)
print(fib(n, dp))

###climbing stairs  using dp
'''
def climbingstairs(n,dp):
    if n==1:
        return 1
    if n==2:
        return 2
    if dp[n]!=-1:
        return dp[n]
    dp[n]=climbingstairs(n-1,dp)+climbingstairs(n-2,dp)
    return dp[n]
n=3
dp=[-1]*(n+1)
print(climbingstairs(n,dp)) 
'''
#third problem based on dynamic programming
'''
def min_cost_stairs(cost):
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp[n-1], dp[n-2])
cost = [10, 15, 20]
print(min_cost_stairs(cost))
'''
#Rob money using dp
'''
def dprob(houses):
    n = len(houses)
    dp=[0]*n
    dp[0]=houses[0]
    dp[1]=max(houses[0],houses[1])
    for i in range(2,n):
        dp[i]=max(houses[i]+dp[i-2],dp[i-1])
    return dp[n-1]
houses=[1,2,3,1]
print(dprob(houses))
'''
#coin change dynamic programming
'''
def min_coins(coins, amount, dp):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    if dp[amount] != -1:
        return dp[amount]
    ans = float('inf')
    for coin in coins:
        ans = min(ans, 1 + min_coins(coins, amount - coin, dp))
    dp[amount] = ans
    return dp[amount]
coins = [1, 2, 5]
amount = 11
dp = [-1] * (amount + 1)
answer = min_coins(coins, amount, dp)
if answer == float('inf'):
    print(-1)
else:
    print(answer)
'''
#next level dynamic programming
#given an array
'''
def dparray(nums, dp):
    dp[0] = 0
    dp[1] = 0

    for i in nums:
        dp[i] = i

    for i in range(2, max(nums) + 1):
        dp[i] = max(dp[i] + dp[i-2], dp[i-1])
    return max(dp)

nums = [3, 4, 2]
dp = [0] * (max(nums) + 1)
print(dparray(nums, dp))
'''
#
'''
def solve(nums, i, dp):
    if dp[i] != -1:
        return dp[i]
    dp[i] = 1
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], solve(nums, j, dp) + 1)
    return dp[i]
nums = [10, 9, 2, 5, 3, 7, 101, 18]
dp = [-1] * len(nums)
ans = 1
for i in range(len(nums)):
    ans = max(ans, solve(nums, i, dp))
print(ans)
print(dp)
'''
#next of dynamic programming
#longest common subsequence
'''
def solve(text1,text2,i,j,dp):
    if i<0 and j<0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if text1[i]==text2[j]:
        dp[i][j] = 1+solve(text1,text2,i-1,j-1,dp)
    else:
        dp[i][j] = max(solve(text1,text2,i-1,j,dp),solve(text1,text2,i,j-1,dp))
    return dp[i][j]

text1 = "abcde"
text2 = "ace"
dp = [[-1] * len(text2) for _ in range(len(text1))]
'''
######valid subarray using kadane
'''
N = 6
k = 3
max_length = 0
arr = [1, -1, 2, -2, 3, -3]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        new = arr[i:j+1]

        count_negative = 0
        count_positive = 0
        for char in new:
            if char < 0:
                count_negative += 1
            elif char > 0:
                count_positive += 1

        if count_positive == count_negative and sum(new) % k == 0:
            current_length = len(new)
            print(new, len(new))
            if current_length > max_length:
                max_length = current_length
print(max_length)
'''
#decode the string using dynamic programming
'''
def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = 0
        # One digit is valid
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        # Two digits are valid
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[n]
s="226"
print(numDecodings(s))
'''
#smallest palindromic rearrangement
'''
s = "babab"
char_count = {}
left = ""
middle = ""
right = ""
for char in s:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1
for let in sorted(char_count):
    freq_count = char_count[let] // 2
    for i in range(freq_count):
        left += let
    if char_count[let] % 2 != 0:
        middle = let
right = left[::-1]
final=left+middle+right
print(final)
'''
#shortest palindrome
'''
s = "aacecaaa"
new = ""
for i in range(len(s) - 1, -1, -1):
    new += s[i]
    temp = new + s
    if temp == temp[::-1]:
        print(temp)
        break
'''
#best version
'''
def shortest_palindrome(s):
    if not s:
        return ""
    rev=s[::-1]
    temp=s+"#"+rev
    lps=[0]*len(temp)
    j=0
    for i in range(1,len(temp)):
        while j>0 and temp[i]!=temp[j]:
            j=lps[j-1]
        if temp[i]==temp[j]:
            j+=1
        lps[i]=j
    remaining=s[lps[-1]:]
    return remaining[::-1]+s
print(shortest_palindrome("aacecaaa"))
print(shortest_palindrome("adeaada"))
'''
### RPG Greedy method algorithm
'''
n = 2
experience = 123
power = [78, 130]
bonus = [10, 20]
mon=[]
for i in range(n):
    mon.append((power[i],bonus[i]))
mon.sort()
count=0
while True:
    max_bonus=-1
    index=-1
    for i in range(len(mon)):
        if mon[i][0]<=experience:
            max_bonus=mon[i][1]
            index=i
    if index==-1:
        break
    experience+=mon[index][1]
    count+=1
    mon.pop(index)
print(count)
print(experience)
print(max_bonus)
'''
#valid arrays
'''
n=int(input())
k=int(input())
dp=[-1*(n+1) for _ in range(k+1)]
def solve(length,last):
    if length==k:
        return 1
    if dp[length][last]!=-1:
        return dp[length][last]
    ans=0
    multiple=last
    while multiple<=n:
        ans+=solve(length+1,multiple)
        multiple+=last
    dp[length][last]=ans%10000
    return dp[length][last]
answer=0
for i in range(1,n+1):
    answer+=solve(1,i)
print(answer%10000)
'''
#


