from __future__ import annotations
from pprint import pformat
from typing import List, Set, Tuple
import cv2
import numpy as np
import pickle
import matplotlib.pyplot as plt
import notinclude.mp24_5 as mp24_5
import mp24_6

def trimimg(image):

    # グレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二値化
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # 輪郭を見つける
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 最大の輪郭を見つける
    cnt = max(contours, key=cv2.contourArea)
    # 最小外接矩形を取得
    x, y, w, h = cv2.boundingRect(cnt)
    # 余白をトリミング
    trimmed_image = image[y:y+h, x:x+w]

    myImg_gray = cv2.cvtColor(trimmed_image, cv2.COLOR_BGR2GRAY)
    myImg_resized=cv2.resize(myImg_gray,(32,32))
    _,myImg_thresh=cv2.threshold(myImg_resized,110,255,cv2.THRESH_BINARY)
    myImgData = np.asarray(myImg_thresh,dtype=float)
    myImgData = myImgData.flatten()

    return myImgData, myImg_thresh

def flat_to_array(flat):
    tmp_plt = []
    numplt = []

    for i in range(len(flat)):
        if(i%9 == 0 and i != 0):
            numplt += [tmp_plt]
            tmp_plt = []
        tmp_plt.append(int(flat[i]))
    numplt += [tmp_plt]
    return numplt

def main():
    rects = []

    # カメラから画像取得
    img = cv2.imread('numbers/pic1.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # グレー化
    _, img_bit = cv2.threshold(gray,130,255,cv2.THRESH_BINARY_INV)    # 二値化
    contours, hierarchy = cv2.findContours(img_bit, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    rects = []

    # 矩形輪郭を検出・保存
    for i, contour in enumerate(contours):
        x,y,w,h = cv2.boundingRect(contour)
        if 120 > w > 100 and 120> h > 100:
            rects += [[(x,y),(x+w-1,y+h-1),((x+x+w-1)/2,(y+y+h-1)/2)]]

    rects = sorted(rects, key=lambda x: x[0][0])

    rects = sorted(rects, key=lambda x: x[0][1])

    with open('numbers/model.pickle', mode='rb') as f:
            clf = pickle.load(f)

    preds= ""

    # 矩形輪郭を描画 
    for i,rect in enumerate(rects):

        imgpt = img[rect[0][0] : rect[1][0]-6, rect[0][1]+6 : rect[1][1]]

        myImgData, myImg_thresh = trimimg(imgpt)

        y_pred=clf.predict(myImgData.reshape(1,-1))

        im_list = np.array(myImg_thresh)
        preds += str(y_pred[0])

    print(preds)
    print(len(preds))
    print(flat_to_array(preds))

    # 縦で取得されているので転置
    grid1 = flat_to_array(preds)
    grid1 = np.array(grid1)
    grid1 = grid1.T
    grid1 = np.ndarray.tolist(grid1)
    # グリッドを定義してから解く
    grid = mp24_5.Grid(grid1)
    results = mp24_5.solve_all(grid)
    for r in results:
        print(r)

    print(mp24_6.solve(grid1))

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()