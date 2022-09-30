#!/usr/bin/python3

# MIT License

# Copyright (c) 2022 afm215

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import multiprocessing
from multiprocessing import Pool
import zipfile
import sys
global unzip_file

def unzip_file(arg):
    file_path, zip_path = arg
    auxiliar_reader = zipfile.ZipFile(zip_path)
    if(file_path[-1] == "/"):
        return 2
    else:
        try:
            auxiliar_reader.extract(file_path)
        except Exception as e:
            print(e)
            print(file_path)
            raise e
        return 1

def custom_unzip(zip_path, nb_threads):
    if nb_threads == -1 :
        nb_threads = multiprocessing.cpu_count()
    print("extracting ", zip_path, " with ", nb_threads, " threads")
    archive  = zipfile.ZipFile(zip_path)
    begin = time.perf_counter()
    
    with Pool(processes=nb_threads) as pool: 
        total_number_of_tasks = len(archive.namelist())
        progress_bar_length = 22
        progress_bar = [' ' for i in range(progress_bar_length)]
        progress_bar[0] = '['
        progress_bar[-1] = ']'
        return_state = []
        completed_state_number = 0
        for state in pool.imap_unordered(unzip_file, 
                                         list(map(lambda elt : (elt, zip_path), archive.namelist()))):
        
            return_state.append(state)
            completed_state_number +=1
            progress_percentage = completed_state_number / total_number_of_tasks 
            for i in range(1, int((progress_bar_length - 2) * progress_percentage)):
                progress_bar[i + 1] = '#'
               
            progress_percentage = format(progress_percentage * 100, '.2f')
            print("".join(progress_bar), ' ', progress_percentage,"%", end='\r')
    end  = time.perf_counter()
    print("extraction completed. Ellapsed time is ", end - begin, 'secs')

## Main commands

print(sys.argv)
assert len(sys.argv) == 3, "incorrect number of arguments: " + str(len(sys.argv) - 1) + ". Expected to be 2 : NB_Threads, archive_path"
NB_THREAD = int(sys.argv[0])
ZIP_PATH = sys.argv[2]
custom_unzip(ZIP_PATH, NB_THREAD)

