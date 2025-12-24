'''
def sum_addition(a,b):
    return a+b
num1=4
num2=5
print(sum_addition(num1,num2))
'''
from django.core.files import temp
from numpy._core.strings import upper
from sklearn.covariance import ledoit_wolf
from sympy.codegen.cnodes import sizeof

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
####

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





