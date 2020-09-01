# x = "piyush"
# for  index,letter in enumerate(x):
#     print(index)
#     print(letter)
#     print("\n")


# mylist1 = [1,2,3,4,5,6]
# mylist2 = ['p','i','y','u','s','h']
# mylist3 = [100,200,300,400,500]
# for item in zip(mylist1,mylist2,mylist3):
#     print(item)


# mylist1 = [1,2,3,4,5,6]
# mylist2 = ['p','i','y','u','s','h']
# mylist3 = [100,200,300,400,500]
# print(list(zip(mylist1,mylist2,mylist3)))


# #  lambda function

# x = [1,2,3,4,5,6,7]
# for item in x:
#     item = item**2
#     print(item)
   


# x = [1,2,3,4,5,6,7]
# square = lambda num:num**2
# print(list(map(square,x)))



# class computer:
#     def __init__(self):
#         self.name = "piyush"
#         self.age = 22
#     def update(self):
#         self.age = 30
        

# c1 = computer()
# c2 = computer()

# c1.name = "rashi"
# c2.age = 12

# c1.update()

# print(c1.name)
# print(c2.name)







# class car:
#     wheels = 4

#     def __init__(self):
#         self.mil = 10
#         self.com = "BMW"
#     def update(self):
#         self.mil = 20
#         self.com = "audi"

# c1 = car()
# c2 = car()

# car.mil = 8
# car.wheels = 5

# c2.update()

# print(c1.com , c1.mil ,c1.wheels)
# print(c2.com , c2.mil ,c2.wheels)






# class student:

#     school = "telusko"

#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)

#     # def get_m1(self):
#     #     return self.m1
#     # def set_m1(self,value):
#     #     self.m1 = value
#     @classmethod
#     def getschool(cls):
#         return cls.school 
#     def info():
#         print("This is student class..in abc module")

# s1 = student(34,67,32)
# s2 = student(89,32,12)

# print(s1.avg())
# print(student.getschool())

# student.info()

# lass student:

#     school = "telusko"

#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)

#     # def get_m1(self):
#     #     return self.m1
#     # def set_m1(self,value):
#     #     self.m1 = value
#     @classmethod
#     def getschool(cls):
#         return cls.school 
#     def info():
#         print("This is student class..in abc module")

# s1 = student(34,67,32)
# s2 = student(89,32,12)

# print(s1.avg())
# print(student.getschool())

# student.info()




# class student:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.laptop()
    
#     def show(self):
#         print(self.name , self.rollno)
#         self.lap.show()

#     class laptop:
#         def __init__(self):
#             self.brand = "hp"
#             self.cpu = "i5"
#             self.ram = 8

#         def show(self):
#             print(self.brand , self.cpu , self.ram)


# s1 = student("piyush", 18)
# s2 = student("sanket", 20)


# s1.show()
# s2.show()


# # Inheritance
# class A:
#     def __init__(self):
#         print("init A")
#     def feat1(self):
#         print("feat1 is working")
#     def feat2(self):
#         print("feat2 is working")

# class B:
#     def __init__(self):
#         print("init B")
#     def feat3(self):
#         print("feat3 is working")
#     def feat4(self):
#         print("feat4 is working")

# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         print("init C")
#     def feat5(self):
#         print("feat5 is working")



# a1 = A()
# c1 = C()

# a1.feat1()
# c1.feat5()


# # Polymorphism


# class vs_code:
#     def execute(self):
#         print("compile")
#         print("running")

# class laptop:
#     def execute(self):
#         print("output")
#         print("compile")
#         print("running")

# class pycharm:
#     def code(self,ide):
#         ide.execute()

# ide = laptop()

# vs = vs_code()
# lap = laptop()
# py = pycharm()

# vs.execute()
# py.code(ide)


# # Operator overloading



















