#------------------------------------------------------
# Filename: crawler.py
# Author: Julie Anne Cantillep (julie.cantillep@studerande.movant.se)
# Purpose: Simple find string in files (recursive) script
# Usage: Search for string of characters in subdirectories incl. 'TestData' folder
#        [File Filters(ex/default: ".txt", ".md", ".docx")]
# Requirements: Files must be text
# WARNING: None
#
#------------------------------------------------------

import os

def main():

    # Enter the file directory you want to search the string for
    rootdir = ('C:\\Users\\Julie\\Documents\\GitHub\\Crawler\\TestData')

    search_str = input("-----------------\nSearch for a string:\n-----------------\n")

    # loops through tuple list of format for search
    extensions = ('.txt', 'md', '.docx')

    for folder, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(extensions):
                fullpath = os.path.join(folder, file)
                with open(fullpath, 'r', encoding="utf8") as f:
                    for line in f:
                        if search_str.lower() in line.lower():
                            print("{} can be found at: {}".format(search_str, fullpath))
                            break

    if search_str.lower() not in line.lower():
        print("String {} can't be found".format(search_str))
        g = input("Press enter to exit...\n")

main()