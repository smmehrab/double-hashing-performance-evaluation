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
import statistics

from data_structures.double_hash import DoubleHash as DoubleHash
from data_structures.red_black_tree import RedBlackTree as RedBlackTree

# data structure path       :   ./data_structures/
#-----------------------------------------------------
# double hash               :   double_hash.py
# red black tree            :   red_black_tree.py
#-----------------------------------------------------

DATA_PATH = os.path.join(os.path.abspath(os.getcwd()), "data")
KEY_SET_FILE = os.path.join(DATA_PATH, "key_set.txt")
INSERT_SEARCH_SEQUENCE_FILE = os.path.join(DATA_PATH, "insert_search_sequence.txt")

PERFORMANCE_PATH = os.path.join(os.path.abspath(os.getcwd()), "performance")
DOUBLE_HASH_PERFORMANCE_DATA_FILE = os.path.join(PERFORMANCE_PATH, "double_hash_performance.txt")
RED_BLACK_TREE_PERFORMANCE_DATA_FILE = os.path.join(PERFORMANCE_PATH, "red_black_tree_performance.txt")

# data path                 :   ./data/
#-----------------------------------------------------
# key set                   :   key_set.txt
# insert-search sequence    :   insert_search_sequence.txt
#-----------------------------------------------------

INSERT_OPCODE = 0
SEARCH_OPCODE = 1

KEY_SET = []
INSERT_SEARCH_SEQUENCE = []

DOUBLE_HASH_PERFORMANCE_DATA = []
DOUBLE_HASH_PERFORMANCE_DATA_ONLY_VALID = []

RED_BLACK_TREE_PERFORMANCE_DATA = []
RED_BLACK_TREE_PERFORMANCE_DATA_ONLY_VALID = []

NUMBER_OF_ROWS_IN_DATA_COMPARISON_TABLE = 100

def initialize_files():
    with open(DOUBLE_HASH_PERFORMANCE_DATA_FILE, "w") as file_object:
        file_object.write("")
    with open(RED_BLACK_TREE_PERFORMANCE_DATA_FILE, "w") as file_object:
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
    global DOUBLE_HASH_PERFORMANCE_DATA
    
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
        
        if(index != -1):
            DOUBLE_HASH_PERFORMANCE_DATA_ONLY_VALID.append(probe)

        DOUBLE_HASH_PERFORMANCE_DATA.append(probe)
        append_csv(DOUBLE_HASH_PERFORMANCE_DATA_FILE, probe)
        # print(str(index) + "    " + str(probe))
    # print(DOUBLE_HASH_PERFORMANCE_DATA)
    return

def perform_red_black_tree():
    global INSERT_SEARCH_SEQUENCE
    global RED_BLACK_TREE_PERFORMANCE_DATA
    
    red_black_tree = RedBlackTree()
    
    opcode = -1
    key = -1
    node_key = -1
    number_of_inspection = -1

    for command in INSERT_SEARCH_SEQUENCE:
        opcode = int(command[0])
        key = int(command[1])

        if(opcode == INSERT_OPCODE):
            response, number_of_inspection = red_black_tree.insert_node(key)
        elif(opcode == SEARCH_OPCODE):
            response, number_of_inspection = red_black_tree.search_node(key)
        
        if(response != -1):
            RED_BLACK_TREE_PERFORMANCE_DATA_ONLY_VALID.append(number_of_inspection)

        RED_BLACK_TREE_PERFORMANCE_DATA.append(number_of_inspection)
        append_csv(RED_BLACK_TREE_PERFORMANCE_DATA_FILE, number_of_inspection)
        # print(str(response) + "    " + str(number_of_inspection))

    # print(RED_BLACK_TREE_PERFORMANCE_DATA)
    return

def clear_console():
    # windows
    if os.name == 'nt':
        os.system('cls')
    # linux/mac
    else:
        os.system('clear')

def descriptive_statistics():
    # double hashing
    mean_double_hashing = round(statistics.mean(DOUBLE_HASH_PERFORMANCE_DATA_ONLY_VALID), 3)
    stdev_double_hashing = round(statistics.stdev(DOUBLE_HASH_PERFORMANCE_DATA_ONLY_VALID), 3)
    max_double_hashing = round(max(DOUBLE_HASH_PERFORMANCE_DATA_ONLY_VALID), 3)
    min_double_hashing = round(min(DOUBLE_HASH_PERFORMANCE_DATA_ONLY_VALID), 3)

    # red black tree
    mean_red_black_tree = round(statistics.mean(RED_BLACK_TREE_PERFORMANCE_DATA_ONLY_VALID), 3)
    stdev_red_black_tree = round(statistics.stdev(RED_BLACK_TREE_PERFORMANCE_DATA_ONLY_VALID), 3)
    max_red_black_tree = round(max(RED_BLACK_TREE_PERFORMANCE_DATA_ONLY_VALID), 3)
    min_red_black_tree = round(min(DOUBLE_HASH_PERFORMANCE_DATA_ONLY_VALID), 3)

    print('{:<35}'.format("Descriptive Statistics"))
    print('{:<35}'.format("------------------------"))
    print()
    print("We've calculated mean and standard deviation for both\nof the algorithms. Comparison between those statistical\nmeasures are given below:")
    print()
    print('{:<50}'.format("------------------------------------------------------------------------"))
    print(' {:<15}    {:<5}    {:<5}    {:<10}    {:<10}'.format("", "Min", "Max", "Mean", "Standard Deviation"))
    print('{:<50}'.format("------------------------------------------------------------------------"))
    print(' {:<15}    {:<5}    {:<5}    {:<10}    {:<10}'.format("Double Hashing", min_double_hashing, max_double_hashing, mean_double_hashing, stdev_double_hashing))
    print(' {:<15}    {:<5}    {:<5}    {:<10}    {:<10}'.format("Red Black Tree", min_red_black_tree, max_red_black_tree, mean_red_black_tree, stdev_red_black_tree))
    print('{:<50}'.format("------------------------------------------------------------------------"))
    print()
    print()

def tabular_statistics():
    print('{:<35}'.format("Tabular Statistics"))
    print('{:<35}'.format("------------------------"))
    print()
    print("As we've generated the insert-search sequence randomly\nif we take the performance measures of the last 100 \ninsert-search sequence for both of the algorithms, we\nshould get a useful comparison between both algorithms\nbased on some random insert-search sequence.\n\nBecause taking last 100 insert-search will ensure that\nwe are comparing between a largely populated double\nhash table & a largely populated red black tree over a\nrandom set of operations on some random set of data.\n\nSo, the comparison is given below:")
    print()

    print('{:<50}'.format("------------------------------------------------------------"))
    print(' {:<15}    {:<20}    {:<20}'.format("Insert-Search", "Double Hashing", "Red Black Tree"))
    print('{:<50}'.format("------------------------------------------------------------"))

    offset = len(DOUBLE_HASH_PERFORMANCE_DATA)-100
    index = 0
    while(index<NUMBER_OF_ROWS_IN_DATA_COMPARISON_TABLE):
        print(' {:<15}    {:<20}    {:<20}'.format(offset+index+1, DOUBLE_HASH_PERFORMANCE_DATA[offset+index], RED_BLACK_TREE_PERFORMANCE_DATA[offset+index]))
        index += 1

    print('{:<50}'.format("------------------------------------------------------------"))
    print()
    print()

def visual_statistics():
    pass



def display_statistics():
    clear_console()

    print()
    print('{:<35}'.format("----------------------------------"))
    print('{:<35}'.format("Double Hashing VS Red Black Tree"))
    print('{:<35}'.format("----------------------------------"))
    print()
    print("Here, the units of performance measurements are:")
    print()
    print('{:<15}:    {:<15}'.format("Double Hashing", "Number of Probes"))
    print('{:<15}:    {:<15}'.format("Red Black Tree", "Number of Inspections"))
    print()
    print()

    descriptive_statistics()
    tabular_statistics()
    # visual_statistics()


def main():

    initialize_files()
    load_datasets()

    perform_double_hashing()
    perform_red_black_tree()

    display_statistics()

if __name__ =="__main__":
	main()
