import os
import sys
def remove_duplicate(csvfile):
	with open(csvfile,'r') as in_file, open('temp.csv','w') as out_file:
		seen = set() # set for fast O(1) amortized lookup
		for line in in_file:
			if line in seen: continue # skip duplicate

			seen.add(line)
			out_file.write(line)
	os.remove(csvfile)
	os.rename("temp.csv",csvfile)
if __name__ == '__main__':
	if len(sys.argv) > 1:
		remove_duplicate(sys.argv[1])
	else:
		print("Please input the argument!")