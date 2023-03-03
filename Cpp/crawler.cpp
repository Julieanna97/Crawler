/**
 * @file crawler.cpp
 * @author Julie Anne Cantillep (julie.cantillep@studerande.movant.se)
 * @brief Simple find string in files (recursive) script
 * @version 1.0
 * @date 2023-03-03
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <dirent.h>

using namespace std;

// Utility function to check if a file is a directory
bool is_directory(const string& path) {
    DIR* dir = opendir(path.c_str());
    if (dir != NULL) {
        closedir(dir);
        return true;
    }
    return false;
}

// Utility function to convert a UTF-8 string to lowercase
string to_lowercase(const string& str) {
    string result = str;
    for (char& c : result) {
        if (c >= 'A' && c <= 'Z') {
            c = c - 'A' + 'a';
        }
    }
    return result;
}

// Function to search for a string in a file
void search_in_file(const string& filename, const string& search_string) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << filename << endl;
        return;
    }

    string line;
    int line_number = 0;
    while (getline(file, line)) {
        line_number++;
        if (to_lowercase(line).find(to_lowercase(search_string)) != string::npos) {
            cout << "Word " << search_string << " found in " << filename << "\n" << "in line number: " << line_number << " : " << line << endl;
        }
    }

    file.close();
}

// Recursive function to search for a string in a subdirectory
void search_in_directory(const string& path, const string& search_string) {
    DIR* dir = opendir(path.c_str());
    if (dir == NULL) {
        cerr << "Failed to open directory: " << path << endl;
        return;
    }

    vector<string> files;
    dirent* entry;
    while ((entry = readdir(dir)) != NULL) {
        string name = entry->d_name;
        if (name == "." || name == "..") {
            continue;
        }

        string full_path = path + "/" + name;
        if (is_directory(full_path)) {
            search_in_directory(full_path, search_string);
        } else {
            search_in_file(full_path, search_string);
        }
    }

    closedir(dir);
}

int main() {
    // Write the path to the directory manually here
    string path = "C:\\Users\\Julie\\Documents\\GitHub\\Crawler";
    string search_string = "HÅL";
    search_in_directory(path, search_string);
    return 0;
}
