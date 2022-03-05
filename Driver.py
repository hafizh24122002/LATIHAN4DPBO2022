from header import *

VehicleTypes = Enum('Vehicle Types', 'A B1 B2 C D')

class Driver():
	__licenseNum: int
	__activeUntil: date
	__vehicleType: VehicleTypes

	def __init__(
		self,
		licenseNum: int = None,
		activeUntil: date = None,
		vehicleType: VehicleTypes = None
	):
		self.__licenseNum = licenseNum
		self.__activeUntil = activeUntil
		self.__vehicleType = vehicleType

	def setlicenseNum(self, licenseNum:int): self.__licenseNum = licenseNum
	def setActiveUntil(self, activeUntil:date): self.__activeUntil = activeUntil
	def setVehicleType(self, vehicleType:VehicleTypes): self.__vehicleType = vehicleType

	def getlicenseNum(self): return self.__licenseNum
	def getActiveUntil(self): return self.__activeUntil
	def getVehicleType(self): return self.__vehicleType

	def printDriver(self):
		print("Nomor SIM : ", self.__licenseNum)
		print("Berlaku sampai dengan : ", self.__activeUntil)
		if ((self.__vehicleType not in VehicleTypes._member_names_) and (self.__vehicleType != None)):
			raise ValueError('Incorrect value of vehicle type! (must be a member of `VehicleTypes`)')
		else:
			print("Tipe kendaraan : ", self.__vehicleType)