from header import *

Gender = Enum('Gender', 'Male Female')

class Person(Job, Driver):
	__id: int
	__name: string
	__gender: Gender

	def __init__(
		self,
		id: int = None,
		name: string = None,
		gender: Gender = None,
		jobId: int = None,
		companyName: string = None,
		position: string = None,
		licenseNum: int = None,
		activeUntil: date = None,
		vehicleType: VehicleTypes = None
	):
		Job.__init__(self, jobId, companyName, position)
		Driver.__init__(self, licenseNum, activeUntil, vehicleType)
		self.__id = id
		self.__name = name
		self.__gender = gender

	def setId(self, id:int): self.__id = id
	def setName(self, name:string): self.__name = name
	def setGender(self, gender:Gender): self.__gender = gender

	def getId(self): return self.__id
	def getName(self): return self.__name
	def getGender(self): return self.__gender

	def printPerson(self):
		print("NIK : ", self.__id)
		print("Nama : ", self.__name)
		if ((self.__gender not in Gender._member_names_) and (self.__gender != None)):
			raise ValueError('Incorrect value of gender! (must be a member of `Gender`)')
		else:
			print("Jenis Kelamin : ", self.__gender)
		self.printJob()
		self.printDriver()

	def sleep(self):
		print("%s is sleeping" %(self.__name))