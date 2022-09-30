# multithreaded_unzip
Provide python code to unzip zip files with multithreading support

## Libraries

The libraries used are very likely already installed:

- time
- multiprocessing
- sys
- zipfile

## Script Arguments 
the script takes two arguments : the number of threads you want the script to use and the targeted zip file.
On Ubuntu, you can also use it as an executable after allowing the file to be executed (chmod +x unzip-multi-threaded.py).

## Example
The following command is using all the computer threads:

python3 unzip-multi-threaded.py -1 archive.zip

The following command is using two threads

python3 unzip-multi-threaded.py 2 archive.zip
