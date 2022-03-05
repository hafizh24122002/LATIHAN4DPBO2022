from header import *

class Vehicle():
	__fuelType: string
	__maxPassengers: int

	def __init__(
		self, 
		fuelType: string = None,
		maxPassenger: int = None
	):
		self.__fuelType = fuelType
		self.__maxPassengers = maxPassenger

	def setFuelType(self, fuelType:string): self.__fuelType = fuelType
	def setMaxPassenger(self, maxPassenger): self.__maxPassengers = maxPassenger

	def getFuelType(self): return self.__fuelType
	def getMaxPassenger(self): return self.__maxPassengers

	def move(self, object:string):
		print("%s is Moving!" %(object))

	def printVehicle(self):
		print("Tipe bahan bakar : ", self.__fuelType)
		print("Kapasitas maksimal penumpang : ", self.__maxPassengers)