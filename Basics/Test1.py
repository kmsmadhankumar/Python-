from datetime import datetime
filenames = ["file1.txt","file2.txt","file3.txt"]

'''
import glob2
filenames = glob2.glob("*.txt")
'''

with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt","w") as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
