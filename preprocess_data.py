import re
from random import shuffle

def split_line(line):
	return re.split("[,。]", line)

def write_to_files(data, train_file, test_file, train_test_split):
	train = open(train_file, 'w', encoding= 'utf-8')
	test = open(test_file, 'w', encoding='utf-8')
	for i, line in enumerate(data):
		if i < train_test_split * len(data):
			train.write(line)
		else:
			test.write(line)

# remove title from data 
def main():
	split_ratio = 0.7
	dataFile_5 = './poetry_no_title_data_5.txt'
	validationFile_5 = './poetry_no_title_validation_5.txt'
	dataFile_7 = './poetry_no_title_data_7.txt'
	validationFile_7 = './poetry_no_title_validation_7.txt'

	f = open('./poetry.txt', encoding='utf-8')
	tmp = []
	# Remove corrupted data
	for i, line in enumerate(f.readlines()):
		newLine = line.split(':')[1]
		if ("__" in newLine or "(" in newLine or "《" in newLine):
			continue
		tmp.append(newLine)

	shuffle(tmp)
	clean_data_5 = []
	clean_data_7 = []
	count_map = {}
	#check if number of words in each sentence is the same
	for i, line in enumerate(tmp):
		chunks = split_line(line)
		standardized = True
		for chunk in chunks:
			if chunk != '\n' and len(chunk) != len(chunks[0]):
				standardized = False
		if not standardized:
			continue

		# Use this to findout what len(7 words) actually is, encoding problem??	
		if (len(chunks[0]) in count_map):
			count_map[len(chunks[0])] += 1
		else:
			count_map[len(chunks[0])] = 1

		if len(chunks[0]) == 11:
			clean_data_5.append(line)
		if len(chunks[0]) == 15:		
			clean_data_7.append(line)

	print(count_map)
	print(len(clean_data_5))
	print(len(clean_data_7))

	write_to_files(clean_data_5, dataFile_5, validationFile_5,split_ratio)
	write_to_files(clean_data_7, dataFile_7, validationFile_7,split_ratio)

if __name__ == '__main__':
    main()