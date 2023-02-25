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

def crawl():

    # Enter the file directory you want to search the string for
    #rootdir = ('C:\\Users\\Julie\\Documents\\GitHub\\Crawler\\TestData')

    # Or use current working directory
    cwd = os.getcwd()

    search_str = input("-----------------\nSearch for a string:\n-----------------\n")

    # loops through tuple list of format for search
    extensions = ('.txt', '.md', '.docx')

    # recursively walk through a folder and it's contents using os.walk()
    for folder, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(extensions):
                dir_path = os.path.join(folder, file)
                with open(dir_path, 'r', encoding = "utf8") as f:
                    for line in f:
                        if search_str.lower() in line.lower():
                            print("{} can be found at:\n{}".format(search_str, dir_path))
                            break
                        
    if not os.path.isfile(dir_path):
        print("Error: File doesn't exist")


if __name__ == '__main__':

    crawl()