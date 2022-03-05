from header import *

def main():
	# Vehicle: Ship
	ship1 = Ship(20, 'Passenger', 'Ferry', 'Indonesia', 'Biodiesel', 120)
	ship1.moveShip()
	ship1.printShip(), print("\n")

	ship2 = Ship(12, 'Cargo', 'Tanker', 'United-Arab-Emirates', 'Diesel', 110)
	ship2.printShip(), print("\n")

	ship3 = Ship(18, 'Industrial', 'Fishing Vessels', 'Indonesia', 'Gasoline', 5)
	ship3.printShip(), print("\n")

	ship4 = Ship(5, 'Passenger', 'Cruise ship', 'United-States-of-America', 'Electricity', 576)
	ship4.printShip(), print("\n")

	ship5 = Ship(50, 'Miscellaneous', 'Icebreaker', 'Canada', 'Diesel', 87)
	ship5.printShip(), print("\n")

	# Vehicle: Airplane
	plane1 = Airplane('A-380', 5, 80.0, 'Avgas', 656)
	plane1.moveAirplane()
	plane1.printAirplane(), print("\n")

	plane2 = Airplane('A-300', 20, 44.84, 'Avgas', 300)
	plane2.printAirplane(), print("\n")

	plane3 = Airplane('B-747', 7, 64.4, 'Avgas', 366)
	plane3.printAirplane(), print("\n")

	plane4 = Airplane('B-707', 15, 39.88, 'Avgas', 137)
	plane4.printAirplane(), print("\n")

	plane5 = Airplane('SJ30', 4, 12.9, "Avgas", 7)
	plane5.printAirplane(), print("\n")

	# Person data
	person1 = Person(2006945, 'Hafizh', 'Male', 2006945, 'UPI', 'Mahasiswa', 1234125, date(2002, 12, 24), 'C')
	person1.sleep()
	person1.printPerson(), print("\n")

	person2 = Person(123456, 'Lutfi', 'Male', 123456, 'UPI', 'Mahasiswa', 123456, date(2022, 3, 5), 'A')
	person2.printPerson(), print("\n")

	person3 = Person(654321, 'Hidayat', 'Male', 654321, 'UPI', 'Mahasiswa', '654321', date(2011, 10, 1), 'B1')
	person3.printPerson(), print("\n")

	person4 = Person(102938, 'Ren', 'Female', 102938, 'Generic Company', 'Manager', 102938, date(2010, 2, 28), 'A')
	person4.printPerson(), print("\n")

	person5 = Person(120938, 'Yuki', 'Female', 120938, 'Records', 'Director', 120938, date(2025, 11, 27), 'A')
	person5.printPerson()

if __name__ == "__main__":
	main()