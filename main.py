#-----------------------------------------------------
# fullname      :   s.m.mehrabul islam
# roll          :   sh-86
# email         :   smmehrabul-2017614964@cs.du.ac.bd
# institute     :   university of dhaka, bangladesh
# session       :   2017-2018
#-----------------------------------------------------

import data_structures.double_hash as double_hash
import data_structures.red_black_tree as red_black_tree

def main():
	tableSize = 5 
	double_hash_table = double_hash.DoubleHash(tableSize)
	InputElements = [4,11, 29, 1, 5]

	for i in InputElements:
		double_hash_table.insert(i)

	double_hash_table.print_table() 

if __name__ =="__main__":
	main()
