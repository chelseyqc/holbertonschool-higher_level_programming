#!/usr/bin/python3
"""
7-add_item module
"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

new_items = sys.argv[1:]
for i in new_items:
    items.append(i)
save_to_json_file(items, filename)
