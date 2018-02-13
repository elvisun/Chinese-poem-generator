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
    poetry_types = [
        'jueju_5',
        'jueju_7',
        'lvshi_5',
        'lvshi_7',
        'others'
    ]

    f = open('./poetry.txt', encoding='utf-8')
    tmp = []
    # Remove corrupted data
    for i, line in enumerate(f.readlines()):
        newLine = line.split(':')[1]
        if ("__" in newLine or "(" in newLine or "《" in newLine):
            continue
        tmp.append(newLine)

    shuffle(tmp)
    count_map = {}
    data_set = {}
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
            data_set.setdefault("jueju_5", []).append(line)
        elif len(chunks[0]) == 5 and len(chunks) == 8:
            data_set.setdefault("lvshi_5", []).append(line)
        elif len(chunks[0]) == 7 and len(chunks) == 4:
            data_set.setdefault("jueju_7", []).append(line)
        elif len(chunks[0]) == 7 and len(chunks) == 8:
            data_set.setdefault("lvshi_7", []).append(line)
        else:
            data_set.setdefault("others", []).append(line)

    for t in poetry_types:
        write_to_files(data_set.get(t, []), 'poetry_no_title_data_' + t +
                       '.txt', 'poetry_no_title_validation_' + t + '.txt', split_ratio)

if __name__ == '__main__':
    main()
