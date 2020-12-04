# My-Sweet-Virus

This is a simple that affects all the files with .py and .pyw extensions without affecting the actual functionality.

the file named myvirus.py is the file that contains the actual malicious code.
what it really do is whenever a file with extension .py pr.pwy is opened  in same directory that contains myvirus.py the malicious code run first along with the actual code of the opened file without affecting the functionality of the opened file.i have imported two libraries sys and glob.now i only put just a print message saying "your files have been corrupted" but instead of that you can put any functionality there and you can also change the scope of the virus from python files to any kind of files by calling it in the glob function.



second file named virustest.py is a sample python program that got affected by the myvirus.py file.


conclusion


if you this file in any directory in your system that contains .py files and if you run the main file once it will affect all the .py file and turning the affected files into a malicious one.
