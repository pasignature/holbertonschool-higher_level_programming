#!/usr/bin/python3
import sys
savefile = __import__('7-save_to_json_file').save_to_json_file
loadfile = __import__('8-load_from_json_file').load_from_json_file


"""Load, Add, Save"""


if __name__ == '__main__':
    try:
        lst = loadfile("add_item.json")
    except:
        lst = []
    for i in range(1, len(sys.argv)):
        lst.append(sys.argv[i])
    savefile(lst, "add_item.json")
