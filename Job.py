from header import *

class Job():
	__id: int
	__companyName: string
	__position: string

	def __init__(
		self,
		id: int = None,
		companyName: string = None,
		position: string = None,
	):
		self.__id = id
		self.__companyName = companyName
		self.__position = position

	def setId(self, id:int): self.__id = id
	def setCompanyName(self, companyName:string): self.__companyName = companyName
	def setPosition(self, position:string): self.__position = position

	def getId(self): return self.__id
	def getCompanyName(self): return self.__companyName
	def getPosition(self): return self.__position

	def printJob(self):
		print("NIP : ", self.__id)
		print("Nama Perusahaan : ", self.__companyName)
		print("Jabatan : ", self.__position)