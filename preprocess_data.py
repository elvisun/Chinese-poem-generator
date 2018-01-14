# remove title from data 
def main():
	f = open('./poetry.txt', encoding='utf-8')
	targetFile = open('./poetry_no_title.txt', 'w', encoding='utf-8')
	for i, line in enumerate(f.readlines()):
		targetFile.write(line.split(':')[1])
		print(i)


if __name__ == '__main__':
    main()