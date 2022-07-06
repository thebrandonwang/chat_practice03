def read_file(filename, lines):
	with open (filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
def write_file(lines):
	for line in lines:
		s = line.split(' ')
		time = s[0][:5]
		person = s[0][5:]
		print(time)
		print(person)
			



def main():
	lines = []
	lines = read_file('3.txt', lines)
	write_file(lines)

main()

