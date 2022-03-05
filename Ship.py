from header import *

ShipTypes = Enum('ShipType', '''Service
								Industrial
								Passenger
								Cargo
								Miscellaneous''')
# Notes
# Service vessels	 (to provide propulsive power to other vessels, i.e. tugs/towing vessels)
# Industrial ships	 (to carry out an industrial process at sea, i.e. fishing vessel, oil drilling/production rigs, or incinerator ships)
# Passenger carriers -> Cruise ships
#					 -> Ferries
# Cargo carriers	 -> Tankers
# 					 -> Container ships
# 					 -> Barge-carrying ships
# 					 -> Roll-on/roll-off ships
# 					 -> Dry-bulk ships
#					 -> General cargo ships
# Miscellaneous		 (i.e. icebreakers or research vessels)
# ref(https://www.britannica.com/technology/ship/Types-of-ships#ref64211)

Countries = Enum('Countries', '''Afganistan Albania Algeria Andorra Angola Antigua-and-Barbuda Argentina Armenia Australia Austria Azerbaijan 
								 Bahamas Bahrain Bangladesh Barbados Belarus Belgium Belize Benin Bhutan Bolivia 
								 Bosnia-and-Herzegovina Botswana Brazil Brunei Bulgaria Burkina-Faso Burundi Cabo-Verde Cambodia 
								 Cameroon Canada Central-African-Republic Chad Chile China Colombia Comoros Congo Costa-Rica 
								 Croatia Cuba Cyprus Czechia Democratic-Republic-of-the-Congo Denmark Djibouti Dominica Dominican-Republic Ecuador 
								 Egypt El-Salvador Equatorial-Guinea Eritrea Estonia Eswatini Ethiopia Fiji Finland France 
								 Gabon Gambia Georgia Germany Ghana Greece Grenada Guatemala Guinea Guinea-Bissau 
								 Guyana Haiti Holy-See Honduras Hungary Iceland India Indonesia Iran Iraq 
								 Ireland Israel Italy Jamaica Japan Jordan Kazakhstan Kenya Kiribati Kuwait 
								 Kyrgyzstan Laos Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg 
								 Madagascar Malawi Malaysia Maldives Mali Malta Marshall-Islands Mauritania Mauritius Mexico 
								 Micronesia Moldova Monaco Mongolia Montenegro Morocco Mozambique Myanmar Namibia Nauru 
								 Nepal Netherlands New-Zealand Nicaragua Niger Nigeria North-Korea North-Macedonia Norway Oman 
								 Pakistan Palau Palestine Panama Papua-New-Guinea Paraguay Peru Philippines Poland Portugal 
								 Qatar Romania Russia Rwanda Saint-Kitts-and Nevis Saint-Lucia Saint-Vincent-and-the-Grenadines Samoa San-Marino Sao-Tome-and-Principe 
								 Saudi-Arabia Senegal Serbia Seychelles Sierra-Leone Singapore Slovakia Slovenia Solomon-Islands Somalia 
								 South-Africa South-Korea South-Sudan Spain Sri-Lanka Sudan Suriname Sweden Switzerland Syria 
								 Tajikistan Tanzania Thailand Timor-Leste Togo Tonga Trinidad-and-Tobago Tunisia Turkey Turkmenistan 
								 Tuvalu Uganda Ukraine United-Arab-Emirates United-Kingdom United-States-of-America Uruguay Uzbekistan Vanuatu Venezuela 
								 Vietnam Yemen Zambia Zimbabwe''')

class Ship(Vehicle):
	__age: int
	__type: ShipTypes
	__typeDesc: string
	__countryOfManufacture: Countries

	def __init__(
		self,
		age: int = None,
		type: ShipTypes = None,
		typeDesc: string = None,
		countryOfManufacture: Countries = None,
		fuelType: string = None,
		maxPassenger: int = None
	):
		super().__init__(fuelType, maxPassenger)
		self.__age = age
		self.__type = type
		self.__typeDesc = typeDesc
		self.__countryOfManufacture = countryOfManufacture

	def setAge(self, age:int): self.__age = age
	def setType(self, type:ShipTypes): self.__type = type
	def setTypeDesc(self, typeDesc:string): self.__typeDesc = typeDesc
	def setCountryOfManufacture(self, countryOfManufacture:Countries): self.__countryOfManufacture = countryOfManufacture

	def getAge(self): return self.__age
	def getType(self): return self.__type
	def getTypeDesc(self): return self.__typeDesc
	def getCountryOfManufacture(self): return self.__countryOfManufacture

	def printShip(self):
		self.printVehicle()
		print("Umur kapal : ", self.__age)
		if ((self.__type not in ShipTypes._member_names_) and (self.__type != None)):
			raise ValueError('Incorrect value of ship type! (must be a member of `ShipTypes`)')
		else:
			print("Tipe kapal : ", self.__type)
		print("Deskripsi tipe kapal : ", self.__typeDesc)
		if ((self.__countryOfManufacture not in Countries._member_names_) and (self.__countryOfManufacture != None)):
			raise ValueError('Incorrect value of countries! (must be a member of `Countries`)')
		else:
			print("Negara pembuat kapal : ", self.__countryOfManufacture)

	def moveShip(self):
		self.move("Ship")