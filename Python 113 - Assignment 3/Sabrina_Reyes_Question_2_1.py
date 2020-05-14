#Sabrina Reyes
#Assignment 3
#Question 2
'''
Design Python3 classes for the UML diagram given below:
***check code***
Note: You are not concerned with the functionality of the methods,
but your class/instances must have initializer, string
representation, length representation wherever it is necessary.
'''

#you have the class
#then a sample object

class Person():
	def __init__(self, name, age, gender):
		print("initializer of Person class")
		self.name = name;
		self.age = age;
		self.gender = gender;
	def __str__(self):
		return "Name: {} \nAge: {} \nGender: {}\n".\
			format(self.name, self.age, self.gender)
Stranger = Person("Unknown", 0, 'NA')
print(Stranger.__str__())

class mallEmployees(Person):
	def __init__(self, name, age, gender, idNo, salary, jobDescription):
		super().__init__(name, age, gender)
		print("initializer of mallEmployees class")
		self.idNo = idNo
		self.salary = salary
		self.jobDescription = jobDescription
	def __str__(self):
		return "id No: {}\nsalary: {}\njob Description: {}\n".\
			format(self.idNo, self.salary, self.jobDescription)
	def getInfo():
		pass
Lowe = mallEmployees("Lowe", 19, 'M', 3242, 40000, "Cashier")
print(Lowe.__str__())

class Customer(Person):
	def __init__(self, name, age, gender, telephone, itemPurchased):
		super().__init__(name, age, gender)
		print("initializer of Customer class")
		self.telephone = telephone
		self.itemPurchased = itemPurchased
	def __str__(self):
		return "telephone: {} \nitemPurchased: {}\n".\
			format(self.telephone, self.itemPurchased)
	def getInfo():
		pass
Sarah = Customer("Sarah", 19, 'F', 3475208888, "Hand Cream")
print(Sarah.__str__())

class Owner(Person):
	def __init__(self, name, age, gender, ownerName, email):
		super().__init__(name, age, gender)
		print("initializer of Owner class")
		self.ownerName = ownerName
		self.age = age
		self.email = email
	def __str__(self):
		#shortened this one
		#only info about owner
		return "Owner name: {} \nAge: {} \nEmail: {}\n".\
			format(self.ownerName, self.age, self.email)
	def getinfo():
		pass
First = Owner("Sr. Jackson", 41,'M', "Michael Jackson", "johndawson01@gmail.com")
print(First.__str__())

class Items(Customer):
	def __init__(self, name, age, gender, telephone,
				 itemPurchased, itemName, itemPrice):
		super().__init__(name, age, gender, telephone, itemPurchased)
		print("initializer of Items class")
		self.itemName = itemName
		self.itemPrice = itemPrice
	def __str__(self):
		return "Item name: {} \nItem price: {}\n".\
			format(self.itemName, self.itemPrice)
	def getInfo():
		pass
Call_of_Duty = Items("Joseph", 23, 'M', 545678909, "COD", "Call of Duty", 50.43)
print(Call_of_Duty.__str__())

class Payments():
	def __init__(self, billNo, date, totalBill):
		print("initializer of Payments class")
		self.billNo = billNo
		self.date = date;
		self.totalBill = totalBill;
	def __str__(self):
		return "billNo: {} \ndate: {}\ntotalBill: {}\n".\
			format(self.billNo, self.date, self.totalBill)
	def __len__(self):
		return self.totalBill
	def cashreceived():
		pass
	def cashreturned():
		pass
bill_One = Payments(121, "03/29/2000", 20)
print(bill_One.__str__()) #the amount of money spent on the bill

class mallParking():
	def __init__(self, total_Space, space_Available, space_Filled):
		super(mallParking, self).__init__()
		print("initializer of mallParking class")
		self.total_Space = total_Space
		self.space_Available = space_Available
		self.space_Filled = space_Filled
	def __len__(self): #???? encompass the whole parking lot
		return self.total_Space
	def __str__(self):
		return "total space: {}\nspace available: {} \nspace filled: {}\n".\
			format(self.total_Space, self.space_Available, self.space_Filled)
	def showspaceleft(self):
		#i just wanted to do this, but it's not perfect..
		if self.space_Available > self.total_Space or self.space_Filled >self.total_Space:
			return "Total space should not be less than space available or space filled.\n"
		else:
			if self.space_Available > 1 and self.space_Available < self.total_Space:
				return "There are " + str(self.space_Available) + " spaces left.\n"
			elif self.space_Available == 1:
				return "There is 1 space left.\n"
			else:
				return "Invalid amount.\n"
Parking_Lot_A = mallParking(50, 1, 49)
print(Parking_Lot_A.__str__())
print("Total amount is space is ", len(Parking_Lot_A))
print(Parking_Lot_A.showspaceleft())

class Mall():
	def __init__(self, no_of_shops, managerName):
		self.no_of_shops = no_of_shops
		self.managerName = managerName
		print("initializer of the Mall class")
	def __len__(self):
		return self.no_of_shops
	def display(self):
		pass
	def __str__(self):
		#ALL VALUES
		return "manager name: {}\nnumber of shops: {}\n".\
			format(self.managerName, self.no_of_shops)

New_Jersey_Mall = Mall(13, "Jone Jones")
print(New_Jersey_Mall.__str__())
New_Jersey_Mall.display()
print("There are", len(New_Jersey_Mall), "stores in this mall.\n")

class Shops():
	def __init__(self, attribute, attribute2, attribute3, attribute4):
		print("initializer of Shops class")		
		self.attribute = attribute
		self.attribute2 = attribute2
		self.attribute3 = attribute3
		self.attribute4 = attribute4
	def __str__(self):
		return "attribute: {}\nattribute2: {}\nattribute3: {}\nattribute4: {}\n".\
		format(self.attribute,self.attribute2,self.attribute3,self.attribute4)
	def getInfo(self):
		pass
Sephora = Shops("skincare", "beauty", "makeup", "feminine")
print("Sephora")
print(Sephora.__str__())