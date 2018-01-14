# remove title from data 
def main():
	split_ratio = 0.7
	f = open('./poetry.txt', encoding='utf-8')
	dataFile = open('./poetry_no_title_data.txt', 'w', encoding='utf-8')
	validationFile = open('./poetry_no_title_validation.txt', 'w', encoding='utf-8')
	
	lineNumber = len(f.readlines())
	
	f = open('./poetry.txt', encoding='utf-8')
	for i, line in enumerate(f.readlines()):
		newLine = line.split(':')[1]
		if (i < lineNumber * split_ratio):
			dataFile.write(newLine)
		else:
			validationFile.write(newLine)


if __name__ == '__main__':
    main()