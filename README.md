# File Crawler
# Folder/subdirectory folder search

A __simple__ _program_ for searching through 

* [x] folders
* [x] files
* [x] file contents 

to search for a __specific__ string of *characters* using _recursion._

## How to search
1. Paste your selected folder in the root dir:
```
Example:
rootdir = ('C:\\Users\\Julie\\Documents\\GitHub\\Crawler\\TestData') <- Your file goes here
```

Or automatically set current working directory:

```
Example: os.getcwd()
```

To search recursively through every single subdirectory.

## USE:
Searching contents uses os.walk() function to search for the file contents
