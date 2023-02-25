# Hash Map
import os

class HashMap:
        def __init__(self):
                self.size = 6
                self.map = [None] * self.size
		
        def _get_hash(self, key):
                hash = 0
                for char in str(key):
                        hash += ord(char)
                return hash % self.size
		
        def add(self, key, value):
                key_hash = self._get_hash(key)
                key_value = [key, value]
		
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key_value])
                        return True
                else:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_value)
                        return True
			
        def get(self, key):
                key_hash = self._get_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None
			
        def delete(self, key):
                key_hash = self._get_hash(key)
		
                if self.map[key_hash] is None:
                        return False
                for i in range (0, len(self.map[key_hash])):
                        if self.map[key_hash][i][0] == key:
                                self.map[key_hash].pop(i)
                                return True
                return False
	
        def keys(self):
                arr = []
                for i in range(0, len(self.map)):
                        if self.map[i]:
                                arr.append(self.map[i][0])
                return arr
			
        def print(self):
                print('---HASH MAP----')
                for item in self.map:
                        if item is not None:
                                print(str(item))

        def crawl(self):
               # Enter the file directory you want to search the string for
                #rootdir = ('C:\\Users\\Julie\\Documents\\GitHub\\Crawler\\TestData')

                # Or use current working directory
                cwd = os.getcwd()

                search_str = input("-----------------\nSearch for a string:\n-----------------\n")

                # loops through tuple list of format for search
                extensions = ('.txt', '.md', '.docx')

                # recursively walk through a folder and it's contents using os.walk()
                for folder, dirs, files in os.walk(cwd):
                    found = False
                    for file in files:
                        if file.endswith(extensions):
                            dir_path = os.path.join(folder, file)
                            with open(dir_path, 'r', encoding = "utf8") as f:
                                for line in f:
                                    if search_str.lower() in line.lower():
                                        print("{} can be found at:\n-----------\n{}\n-----------".format(search_str, dir_path))
                                        key, value = search_str, dir_path
                                        self.add(key, value)
                                        found = True
                                        break
if __name__ == '__main__':
        h = HashMap()
        h.crawl()
        h.print()		
        """h.delete('Bob')
        h.print()
        print('Ming: ' + h.get('Ming'))
        print(h.keys())"""