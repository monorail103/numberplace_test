
import numpy as np
import matplotlib.pyplot as plt

# gridは１次元配列で渡す
def solve(grid):
    testgrid = grid.copy()
    # 0の位置を取得
    zeroidx = check_zero_index(grid)
    # 0の位置と同じ桁の数字を作成
    allslv = len(zeroidx)*"1"
    print(zeroidx)
    for j in range(10**len(zeroidx)):
        # print(allslv)
        if "0" not in allslv:
            # 0の位置に数字を入れるためのリストを作成
            slvlist = list(allslv)
            for i,idx in enumerate(zeroidx):
                testgrid[idx] = int(slvlist[i])
            if(check_ans(testgrid)):
                return testgrid
            else:
                if(len(allslv) != len(str(int(allslv)+1))): break
                else: allslv = str(int(allslv)+1)
                testgrid = grid.copy()
        else:
            if(len(allslv) != len(str(int(allslv)+1))): break
            else: allslv = str(int(allslv)+1)
    
    return False
            
def check_ans(grid, n=3):
    grid = flat_to_array(grid, n)
    # 行のチェッ
    sum_row = [sum(row) for row in grid]
    sum_col = [sum(x[i] for x in grid) for i in range(n)]
    ans = sum_row[0]

    for i in range(n):
        if ans != sum_row[i]: return False
    for i in range(n):
        if ans != sum_col[i]: return False

    return True

def check_zero_index(grid):
    tmp = []
    for i in range(len(grid)):
        if grid[i] == 0:
            tmp.append(i)
    return tmp

def flat_to_array(flat, n):
    tmp_plt = []
    numplt = []

    for i in range(len(flat)):
        if(i%n == 0 and i != 0):
            numplt += [tmp_plt]
            tmp_plt = []
        tmp_plt.append(int(flat[i]))
    numplt += [tmp_plt]
    return numplt

def flat_to_flat(flat):
    numplt = []

    for i in range(len(flat)):
        numplt.append(int(flat[i]))

    return numplt

def main():
    card = "210021030"
    cdlist = flat_to_flat(card)
    print(cdlist)
    print(solve(cdlist))

if __name__ == '__main__':
    main()