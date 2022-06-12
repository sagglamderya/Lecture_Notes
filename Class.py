class Employee: #creates a class named Employee

    raise_percent=1.05 #this is class variable, you cannot change its value outside of class. 
    num_emp=0

    def __init__(self, name, last, age, pay): #creates an attribute in class for name, last, age and pay
        self.name= name #creates name object in class, you can use these objects for different variables over and over
        self.last= last
        self.age= age
        self.pay= pay
        Employee.num_emp+=1 #counts employees in the class

    def fullname(self):
        print(f"{self.name} {self.last}")

    def apply_raise(self):
        self.pay=self.pay* Employee.raise_percent # "self.raise_percent" is also can be written instead of "Employee.raise_percent"

    @classmethod #you can change the raise_percent with @classmethod
    def set_raise(cls,amount):
        cls.raise_percent= amount

    @classmethod
    def from_string(cls, emp_str):
        name, last, age, pay= emp_3_str.split("-")
        return cls(name, last, int(age), float(pay)) #if attributes are not given one by one but in one line of string you can define attributes like this

    @staticmethod #if you want to define something which is not depend on instance or class you can use @staticmethod. This function wont be change according to instance in class
    def holiday_print(day):
        if day=="weekend":
            print("This is an off day")
        else:
            print("This is not an off day")

emp_1= Employee("James", "Hughes", "32", 5000) #creates an instance variable in Employee class
emp_2=Employee("Derya","Sağlam","21",4000)
emp_1.name #you can call the name attribute of emp_1 like this
emp_1.fullname() #you can use a function in class like this--> instanceVariable.functionName()
emp_1.apply_raise() #pay of emp_1 is updated 
emp_2.apply_raise()
emp_1.experience=10 #you can also add attribute outside of the class like this --> instanceVariable.nameOfAttribute=value
print(emp_1.__dict__) #you can call the attribute of class like this--> instanceVariable.__dict__
print(Employee.num_emp)
emp_3_str= "Can-Gox-36-5200"
emp_3= Employee.from_string(emp_3_str)
print(emp_3.__dict__)
Employee.holiday_print("weekend")
emp_3.holiday_print("monday")

#inheritence is a subclass of a main class
class IT(Employee): #this is a inheritence example
    raise_percent=2.26 #changes in subclasses do not effect main class
    def __init__(self, name, last, age, pay, lang):
        super().__init__(name, last, age,pay) #if you want to implement same objects under subclass you can use super() like this--> super().__init__(ob1,ob2,...)
        self.lang=lang #other objects can be created under subclass
it_1=IT("Cem","Karaca", "68", 5800, "English")
isinstance(it_1, Employee) #you can check if it_1 instance of Employee or not
issubclass(IT, Employee) #you can check if IT subclass of Employee or not

#magic methods
class IK(Employee):
    def __str__(self): #str method makes easy to read output. You could not type print(ik_1) before but now you can.
        return f"Employee (name={self.name}, last={self.last}, age={self.age}, pay={self.pay})"

    def __add__(self,other): #when you use "+" it will work like that;
        return self.pay - other.pay #(payment of first+payment of second) but it will give you the difference between payments not sum of these because here you wrote "-"

    def __len__(self):
        return len(self.name) #returns the lenght of name of an object

ik_1=IK("Elvis","Presley", "78", 252)
ik_2=IK("Damla", "Sağlam", "19", 800)
print(ik_1 + ik_2)
print(len(ik_1)) 