#-----------------------------------------------------
# fullname      :   s.m.mehrabul islam
# roll          :   sh-86
# email         :   smmehrabul-2017614964@cs.du.ac.bd
# institute     :   university of dhaka, bangladesh
# session       :   2017-2018
#-----------------------------------------------------

class DoubleHash:

	#-----------------------------------------------------
	# k 				= key
	# p					= a prime < table_size
	#-----------------------------------------------------
	# double_hash(k) 	= (h1(k) - i*h2(k)) % table_size
	# h1(k) 			= k % table_size
	# h2(k) 			= p - (k % p)
	#-----------------------------------------------------

	def __init__(self, table_size):
		self.table_size = table_size
		self.table = [None]*self.table_size
		self.number_of_elements = 0
		self.prime = self.nearest_prime()

	def nearest_prime(self):
		for n in range((self.table_size-1), 1, -1):
			isPrime = True
			for divisor in range(2, int(n**0.5)+1):
				if(n%divisor == 0):
					isPrime = False
					break
			if(isPrime):
				return n
		return 3

	def h1(self, key):
		return (key % self.table_size)

	def h2(self, key):
		return self.prime - (key % self.prime)

	def insert(self, key):
		if(self.number_of_elements == self.table_size):
			print("Hash Table - Full")
			return (-1, -1)

		isInserted = False
		probe = 0
		while not isInserted:
			index = (self.h1(key) + probe*self.h2(key)) % self.table_size
			if(self.table[index] == None):
				self.table[index] = key
				# print(f"[INSERTED] key {key} at index {index}")
				isInserted = True
				self.number_of_elements +=1
			else:
				probe += 1
				
		return (index, (probe+1))

	def search(self, key):
		isFound = False
		canFind = True
		probe = 0
		while ((not isFound) and canFind):
			index = (self.h1(key) + probe*self.h2(key)) % self.table_size
			if(self.table[index] == key):
				# print(f"[FOUND] key {key} at index {index}")
				isFound = True
			elif(self.table[index] == None):
				index = -1
				probe = -2
				canFind = False
			else:
				probe += 1
		return (index, (probe+1))

	def print_table(self):
		for i in range(0, len(self.table)):
			print(str(i) + "	|	" + str(self.table[i]))
