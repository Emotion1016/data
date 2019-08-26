import xlrd

class read_excel:
# 定义excel文档读取方法
    def read_it(self,path,index=0):
    # 返回整个excel文件，其中包含多个sheet
        book = xlrd.open_workbook(path)
        # 获取指定索引的sheet表
        sheet = book.sheets()[index]
        return sheet


if __name__ == '__main__':
    s = read_excel().read_it('../data/agileonetestcase.xls')
    # 取得sheet表的所有行数
    for i in range(s.nrows):
    # 取得sheet表的所有列数
        for j in range(s.ncols):
            # 通过行列坐标找到每个单元格的内容
            print(s.cell(i,j).value,end='\t')
        print('')