#------------------------------------------------------
# Filename: crawler.py
# Author: Julie Anne Cantillep (julie.cantillep@studerande.movant.se)
# Purpose: Simple find string in files (recursive) script
#          Store file address as values to keywords[key] in a hash map
# Usage: Search for string of characters in subdirectories incl. 'TestData' folder
#        by keywords
#        [File Filters(ex/default: ".txt", ".md", ".docx")]
# Requirements: Files must be text
# WARNING: None
# Version: 1.0
# Date: 2023-02-26
#------------------------------------------------------

import os


class HashMap:
        """ Hash map which uses strings for keys. Value can be any object. 
        Provides optional map operations, and searches for values by keywords."""

        def __init__(self, capacity = 1000):
                """ Capacity defaults to 1000. """

                # construct start at 0
                # initialized hash table of size
                self.capacity = capacity
                self.size = 50               
                self.map = [None] * self.size     

        def get_hash(self, key):
                """ computes hash codes using mod % 
                to assign keys to specific hash table index """

                hash = 0
                # calculate hash code for every key
                for char in str(key):
                        hash += ord(char)
                return hash % self.size
	
        def add(self, key, value):
                """ Adds key-value pair into hash table. If key already exists, then the object will be
                updated. If the key has multiple values, it will associate multiple values
                with that key """

                key_hash = self.get_hash(key)
                key_val = [key, value]
		
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key ,value])
                        return True
                else:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_val[1])
                        return True
        
        # delete function only for test (not working)
        """def delete(self, key):
                key_hash = self._get_hash(key)
		
                if self.map[key_hash] is None:
                        return False
                for i in range (0, len(self.map[key_hash])):
                        if self.map[key_hash][i][0] == key:
                                self.map[key_hash].pop(i)
                                return True
                return False"""
        
        def keys(self):
                """ prints key found during 'keyword' search """

                arr = []
                for i in range(0, len(self.map)):
                        if self.map[i]:
                                arr.append(self.map[i][0])
                return arr
		
        def print(self):
                """ prints out the hash map """

                print('----HASH MAP----')
                for item in self.map:
                        if item is not None:
                                print(str(item))


        def crawl(self):
                """ search through files to find the keyword and store it in the hash table """

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
                                    # .lower() to implement case insensitivity during input and search
                                    if search_str.lower() in line.lower():
                                        print("{} can be found at:\n-----------\n{}\n-----------".format(search_str, dir_path))
                                        key, value = search_str, dir_path
                                        self.add(key, value)
                                        break
                                    
                # if file is invalid                             
                if not os.path.isfile(dir_path):
                       print("CHECK THE ADDRESS FILE... Seems to be something wrong with the file directory!")
                

# Driver code
if __name__ == '__main__':

        h = HashMap()

        # crawl() searches for text of strings or characters in subdirs/cwd
        h.crawl()
        
        # prints the hash table
        h.print()

        # prints key in a hash table
        print(h.keys())

        # loop condition
        is_running = True

        # get user input repeatedly until user quits
        while is_running:
               search_again = input("\nDo you want to search again?\n\nPress Y or N: ")
               if search_again.upper() == "Y":
                h.crawl()
                h.print()
                print(h.keys())
               elif search_again.upper() == "N":
                print("--------------\nHave a nice day! :)\n--------------")
                is_running = False
               else:
                      print("\nPlease enter Y or N.")
               