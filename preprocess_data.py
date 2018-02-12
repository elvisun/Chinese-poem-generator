import re
from random import shuffle


def split_line(line):
    return re.split("[，。]", line)


def write_to_files(data, train_file, test_file, train_test_split):
    train = open(train_file, 'w', encoding='utf-8')
    test = open(test_file, 'w', encoding='utf-8')
    for i, line in enumerate(data):
        if i < train_test_split * len(data):
            train.write(line)
        else:
            test.write(line)

# remove title from data


def main():
    split_ratio = 0.7
    dataFile_5_jueju = './poetry_no_title_data_5_jueju.txt'
    dataFile_5_lueshi = './poetry_no_title_data_5_lueshi.txt'
    validationFile_5_jueju = './poetry_no_title_validation_5_jueju.txt'
    validationFile_5_lueshi = './poetry_no_title_validation_5_lueshi.txt'
    dataFile_7_jueju = './poetry_no_title_data_7_jueju.txt'
    dataFile_7_lueshi = './poetry_no_title_data_7_lueshi.txt'
    validationFile_7_jueju = './poetry_no_title_validation_7_jueju.txt'
    validationFile_7_lueshi = './poetry_no_title_validation_7_lueshi.txt'

    f = open('./poetry.txt', encoding='utf-8')
    tmp = []
    # Remove corrupted data
    for i, line in enumerate(f.readlines()):
        newLine = line.split(':')[1]
        if ("__" in newLine or "(" in newLine or "《" in newLine):
            continue
        tmp.append(newLine)

    shuffle(tmp)
    clean_data_5_jueju = []
    clean_data_5_lueshi = []
    clean_data_7_jueju = []
    clean_data_7_lueshi = []
    clean_data_others = []
    count_map = {}
    # check if number of words in each sentence is the same
    for i, line in enumerate(tmp):
        chunks = split_line(line.strip())
        chunks = list(filter(None, chunks))
        if len(chunks) < 4:
            continue
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

        if len(chunks[0]) == 5 and len(chunks) == 4:
            clean_data_5_jueju.append(line)
        elif len(chunks[0]) == 5 and len(chunks) == 8:
            clean_data_5_lueshi.append(line)
        elif len(chunks[0]) == 7 and len(chunks) == 4:
            clean_data_7_jueju.append(line)
        elif len(chunks[0]) == 7 and len(chunks) == 8:
            clean_data_7_lueshi.append(line)
        else:
            clean_data_others.append(line)

    print(count_map)
    # print(len(clean_data_5))
    print(len(clean_data_others))

    write_to_files(clean_data_5_jueju, dataFile_5_jueju,
                   validationFile_5_jueju, split_ratio)
    write_to_files(clean_data_7_jueju, dataFile_7_jueju,
                   validationFile_7_jueju, split_ratio)
    write_to_files(clean_data_5_lueshi, dataFile_5_lueshi,
                   validationFile_5_lueshi, split_ratio)
    write_to_files(clean_data_7_lueshi, dataFile_7_lueshi,
                   validationFile_7_lueshi, split_ratio)
    #write_to_files(clean_data_others, dataFile_7, validationFile_7,split_ratio)

if __name__ == '__main__':
    main()
