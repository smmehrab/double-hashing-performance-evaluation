#-----------------------------------------------------
# fullname      :   s.m.mehrabul islam
# roll          :   sh-86
# email         :   smmehrabul-2017614964@cs.du.ac.bd
# institute     :   university of dhaka, bangladesh
# session       :   2017-2018
#-----------------------------------------------------

import os
import sys
import random

MAX_KEY = 2147483647
NUMBER_OF_KEYS = 10000
NUMBER_OF_INSERT = 10000
NUMBER_OF_SEARCH = 3000
NUMBER_OF_INSERT_SEARCH = 13000

INSERT_OPCODE = 0
SEARCH_OPCODE = 1

# data path                 :   ./data/
#-----------------------------------------------------
# key set                   :   key_set.txt
# insertion sequence        :   key_set.txt
# search sequence           :   search_sequence.txt
# insert-search sequence    :   insert_search_sequence.txt
#-----------------------------------------------------

DATA_PATH = os.path.join(os.path.abspath(os.getcwd()), "data")
KEY_SET_FILE = os.path.join(DATA_PATH, "key_set.txt")
SEARCH_SEQUENCE_FILE = os.path.join(DATA_PATH, "search_sequence.txt")
INSERT_SEARCH_SEQUENCE_FILE = os.path.join(DATA_PATH, "insert_search_sequence.txt")

# functions
#-----------------------------------------------------
# initialize_files()
# append_csv(file_name, key)
# append_command(file_name, opcode, key)
# read_csv(file_name)
# read_commands(file_name)
#-----------------------------------------------------

def initialize_files():
    with open(KEY_SET_FILE, "w") as file_object:
        file_object.write("")
    with open(SEARCH_SEQUENCE_FILE, "w") as file_object:
        file_object.write("")
    with open(INSERT_SEARCH_SEQUENCE_FILE, "w") as file_object:
        file_object.write("")

def append_csv(file_name, value):
    with open(file_name, "a") as file_object:
        file_object.write(str(value) + ",")

def read_csv(file_name):
    with open(file_name, "r") as file_object:
        values = file_object.read().split(",")
        values = values[:-1]
        return values

def append_command(file_name, opcode, key):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(str(opcode) + " " + str(key))

def read_commands(file_name):
    with open(file_name, "r") as file_object:
        commands = file_object.read().split("\n")
        return commands

#-----------------------------------------------------
# main
#-----------------------------------------------------

def main():

    initialize_files()

    # -----------------------------------
    # key set generation
    # -----------------------------------

    key_set = []
    for i in range(NUMBER_OF_INSERT):
        key = random.randint(0, MAX_KEY)
        append_csv(KEY_SET_FILE, key)
    key_set = read_csv(KEY_SET_FILE)

    # -----------------------------------
    # search sequence generation
    # -----------------------------------

    search_key_set = []
    for i in range(NUMBER_OF_SEARCH):
        p1 = random.randint(1, 10)
        if(p1<=7):
            p2 = random.randint(1, 5)
            if(p2==1):
                search_key_set = read_csv(SEARCH_SEQUENCE_FILE)
                if(len(search_key_set)>0):
                    search_key_set_index = random.randint(0, len(search_key_set)-1)
                    append_csv(SEARCH_SEQUENCE_FILE, search_key_set[search_key_set_index])
            else:
                key_set_index = random.randint(0, NUMBER_OF_KEYS-1)
                append_csv(SEARCH_SEQUENCE_FILE, key_set[key_set_index])
        else:
            key = random.randint(0, MAX_KEY)
            append_csv(SEARCH_SEQUENCE_FILE, key)

    search_key_set = read_csv(SEARCH_SEQUENCE_FILE)

    # -----------------------------------
    # insert search sequence generation
    # -----------------------------------

    key_set_index = 0
    search_key_set_index = 0

    entry = 0
    while entry<NUMBER_OF_INSERT_SEARCH:
        p = random.randint(1, 10)
        if(p<=7):
            if(key_set_index<NUMBER_OF_INSERT):
                append_command(INSERT_SEARCH_SEQUENCE_FILE, INSERT_OPCODE, key_set[key_set_index])
                key_set_index += 1
                entry += 1
        else:
            if(search_key_set_index<NUMBER_OF_SEARCH):
                append_command(INSERT_SEARCH_SEQUENCE_FILE, SEARCH_OPCODE, search_key_set[search_key_set_index])
                search_key_set_index += 1
                entry += 1

    insert_search_command_set = read_commands(INSERT_SEARCH_SEQUENCE_FILE)

    # debug
    # print(str(len(key_set)))
    # print(str(len(search_key_set)))
    # print(str(len(insert_search_command_set)))

if __name__ =="__main__":
	main()
