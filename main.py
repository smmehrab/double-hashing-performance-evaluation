#-----------------------------------------------------
# fullname      :   s.m.mehrabul islam
# roll          :   sh-86
# email         :   smmehrabul-2017614964@cs.du.ac.bd
# institute     :   university of dhaka, bangladesh
# session       :   2017-2018
#-----------------------------------------------------

import os
import math
import sys
from data_structures.double_hash import DoubleHash as DoubleHash
from data_structures.red_black_tree import RedBlackTree as RedBlackTree

# data structure path       :   ./data_structures/
#-----------------------------------------------------
# double hash               :   double_hash.py
# red black tree            :   red_black_tree.py
#-----------------------------------------------------

DATA_PATH = os.path.join(os.path.abspath(os.getcwd()), "data")
STATISTICS_PATH = os.path.join(os.path.abspath(os.getcwd()), "statistics")
KEY_SET_FILE = os.path.join(DATA_PATH, "key_set.txt")
INSERT_SEARCH_SEQUENCE_FILE = os.path.join(DATA_PATH, "insert_search_sequence.txt")
DOUBLE_HASHING_STATISTICS_FILE = os.path.join(STATISTICS_PATH, "double_hashing_statistics.txt")
RED_BLACK_TREE_STATISTICS_FILE = os.path.join(STATISTICS_PATH, "red_black_tree_statistics.txt")

# data path                 :   ./data/
#-----------------------------------------------------
# key set                   :   key_set.txt
# insert-search sequence    :   insert_search_sequence.txt
#-----------------------------------------------------

INSERT_OPCODE = 0
SEARCH_OPCODE = 1

KEY_SET = []
INSERT_SEARCH_SEQUENCE = []
DOUBLE_HASH_STATISTICS = []
RED_BLACK_TREE_STATISTICS = []

def initialize_files():
    with open(DOUBLE_HASHING_STATISTICS_FILE, "w") as file_object:
        file_object.write("")
    with open(RED_BLACK_TREE_STATISTICS_FILE, "w") as file_object:
        file_object.write("")

def read_csv(file_name):
    with open(file_name, "r") as file_object:
        values = file_object.read().split(",")
        values = values[:-1]
        return values

def append_csv(file_name, value):
    with open(file_name, "a") as file_object:
        file_object.write(str(value) + ",")

def read_commands(file_name):
    with open(file_name, "r") as file_object:
        command_lines = file_object.read().split("\n")
        commands = []
        for command_line in command_lines:
            command = command_line.split(" ")
            commands.append(command)
        return commands

def load_datasets():
    global KEY_SET
    global INSERT_SEARCH_SEQUENCE
    KEY_SET = read_csv(KEY_SET_FILE)
    INSERT_SEARCH_SEQUENCE = read_commands(INSERT_SEARCH_SEQUENCE_FILE)

def perform_double_hashing():
    global KEY_SET
    global INSERT_SEARCH_SEQUENCE
    global DOUBLE_HASH_STATISTICS
    
    opcode = -1
    key = -1
    index = -1
    probe = -1

    table_size = math.ceil(len(KEY_SET)*1.2)
    double_hash_table = DoubleHash(table_size)

    for command in INSERT_SEARCH_SEQUENCE:
        opcode = int(command[0])
        key = int(command[1])

        if(opcode == INSERT_OPCODE):
            index, probe = double_hash_table.insert(key)
        elif(opcode == SEARCH_OPCODE):
            index, probe = double_hash_table.search(key)
        
        # op_info = []
        # op_info.append(index)
        # op_info.append(probe)
        # DOUBLE_HASH_STATISTICS.append(op_info)
        append_csv(DOUBLE_HASHING_STATISTICS_FILE, probe)
        # print(str(index) + "    " + str(probe))

def perform_red_black_tree():
    
    
    return

def show_performance(data_structure_name):

    if(data_structure_name == "DoubleHashing"):

    elif(data_structure_name == "RedBlackTree"):


def main():

    initialize_files()
    load_datasets()

    perform_double_hashing()
    show_performance("DoubleHashing")

    perform_red_black_tree()
    show_performance("RedBlackTree")


    # table_size = 5
    # input_elements = [4,11, 29, 1, 5]
    # double_hash_table = DoubleHash(table_size)
    # for i in input_elements:
    #     double_hash_table.insert(i)
    # double_hash_table.print_table()

    # rbt = RedBlackTree()
    # rbt.insert_node(10)
    # rbt.insert_node(20)
    # rbt.insert_node(30)
    # rbt.insert_node(5)
    # rbt.insert_node(4)
    # rbt.insert_node(2)
    # (k, n) = rbt.insert_node(19)
    # print(k)
    # print(n)
    # rbt.print_tree()

if __name__ =="__main__":
	main()
