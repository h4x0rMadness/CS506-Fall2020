def read_csv(file_path):
    res = []
    for line in open(file_path):
        row = []
        clean_line = line.strip()
        for elem in clean_line.split(','):
            if elem.isdigit() or (elem[0] == '-' and elem[1:len(elem)].isdigit()):
                row.append(int(elem))
            else:
                row.append(elem.replace('"', ''))
        res.append(row)
    return res

##print(read_csv("../tests/test_files/dataset_3.csv"))

