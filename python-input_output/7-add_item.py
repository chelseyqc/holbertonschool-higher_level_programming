#!/usr/bin/python3
"""
7-add_item module
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []

filename = "add_item.json"
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
args = sys.argv[1:]

for i in args:
    my_list.append(i)

save_to_json_file(my_list, filename)
