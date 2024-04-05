'''single inheritance'''

# # parent class
# class office:
#     def office_details(self):
#      self.office_name=input('Enter the company name :')
#      self.office_add=input('Enter the office address :')    
# # child class    
# class emp(office):
#    def emp_details(self):
#        self.name=input('Enter the emp name :')
#        self.salary=int(input('enter the emp salary :'))      
# obj=emp()
# obj.office_details()
# obj.emp_details()

'''multiple inheritance'''

# # parent class
# class company:
#     def company_details(self):
#      self.company_name=input('Enter the company name :')
#      self.company_add=input('Enter the office address :')    
# # parent class    
# class manager:
#    def manager_details(self):
#        self.manager_id=input('Enter the manager ID :')
#        self.manager_name=input('Enter the manager name :')
#        self.salary=int(input('enter the manager salary :'))
# # child calss
# class emp(company,manager):
#    def emp_details(self):
#       self.emp_name=input('Enter the emp name :')
#       self.emp_address=input('Enter the emp address :')
#       self.salary=input('Enter the emp salary :')
# obj=emp()
# obj.company_details()
# obj.manager_details()
# obj.emp_details()

'''multilevel inheritance'''

# # parent class
# class school:
#     def school_info(self):
#         self.school_name=input('Enter the school name :')
#         self.school_address=input('Enter school address :')
# # child class
# class teachers(school):
#     def teacher_details(self):
#         self.teacher_name=input('Enter teacher name :')
#         self.sub=input('Enter sub name :')
# # child class 
# class student(teachers):
#      def student_details(self):
#         self.student_name=input('Enter student name :')
#         self.sub=input('Enter sub name :')
# obj=student()
# obj.school_info()
# obj.teacher_details()
# obj.student_details()

'''Hierarchical Inheritance'''

# # parent class
# class school:
#     def school_info(self):
#         self.school_name=input('Enter the school name :')
#         self.school_address=input('Enter school address :')
# # child class
# class teachers(school):
#     def teacher_details(self):
#         self.teacher_name=input('Enter teacher name :')
#         self.subject_name=input('Enter sub name :')
# # child class 
# class student(school):
#      def student_details(self):
#         self.student_name=input('Enter student name :')
#         self.subject_name=input('Enter sub name :')
# obj1=teachers()
# obj1.school_info()
# obj1.teacher_details()

# obj=student()
# obj.school_info("ABC School","Bangaloruru")
# obj.student_details()


'''Hybrid Inheritance'''

# parent class
# class school:
#     def __init__(self,school_name,school_address):
#         self.school_name=school_name
#         self.school_address=school_address
#         print(self.school_name,self.school_address,"I am parent class")
# # child class
# class teachers(school):
#     def teacher_details(self):
#         self.teacher_name=input('Enter teacher name :')
#         self.subject_name=input('Enter sub name :')
#         print(self.school_name,self.school_address,"I am parent class")
# # child class 
# class student1(school):
#      def student1_details(self):
#         self.student_name=input('Enter student name :')
#         self.subject_name=input('Enter sub name :')
#         print(self.school_name,self.school_address,"I am parent class")
# # child class/parent class:
# class student2(teachers,student1):
#      def student2_details(self):
#         self.student_name=input('Enter student name :')
#         self.subject_name=input('Enter sub name :')
#         print(self.school_name,self.school_address,"I am parent class")

# # Create an object of the teacher class
# obj1=teachers()
# obj1.school_info()
# obj1.teacher_details()

# # # Create an object of the Student1 class
# obj=student1()
# obj.school_info()
# obj.student1_details()
# obj2=student2()

# # Create an object of the Student2 class

# obj2.school_info()
# obj2.teacher_details()
# obj2.student2_details()











