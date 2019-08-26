def getCsvData(filename):
    with open(filename, "r", encoding="utf-8") as f:
        d = f.readlines()
        # print(d)
        list = []
        for i in range(1, len(d)):
            newD = tuple(d[i].strip('\n').split(','))
            # print(newD)
            list.append(newD)
        # print(list)
        return list

# if __name__ == '__main__':
#     getCsvData()