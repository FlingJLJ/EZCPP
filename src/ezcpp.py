import os

version = '0.1.0'

f = open('ezcpp', 'r')
sourceList = f.read()
f.close()
del f

print(f'''EZCPP
version {version}
''')

for f in sourceList.split('\n'):
	isError = os.system(f'g++ {f} -c')
	if isError != 0:
		input()
		exit()

isError = os.system('g++ *.o -O3')
if isError != 0:
	input()
	exit()

input()