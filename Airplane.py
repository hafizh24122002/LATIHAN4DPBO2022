from header import *

class Airplane(Vehicle):
	# Airplane types are based on the FAA type ratings (https://registry.faa.gov/TypeRatings/)
	__type: string
	__age: int
	__wingspan: float

	def __init__(
		self,
		type: string = None,
		age: int = None,
		wingspan: float = None,
		fuelType: string = None,
		maxPassenger: int = None
	):
		super().__init__(fuelType, maxPassenger)
		self.__type = type
		self.__age = age
		self.__wingspan = wingspan

	def setType(self, type:string): self.__type = type
	def setAge(self, age:int): self.__age = age
	def setWingspan(self, wingspan:float): self.__wingspan = wingspan

	def getType(self): return self.__type
	def getAge(self): return self.__age
	def getWingspan(self): return self.__age

	def printAirplane(self):
		self.printVehicle()
		print("Tipe pesawat : ", self.__type)
		print("Umur pesawat : ", self.__age)
		print("Bentang sayap pesawat : %s m" %(self.__wingspan))

	def moveAirplane(self):
		self.move("Airplane")