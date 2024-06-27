from sklearn import linear_model
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import pickle

def trimmimg(img):
    # 画像を読み込む
    image = cv2.imread(img)

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

X=[]
for i in range(10):
    img = 'numbers/img'+ str(i) +'.jpg'
    myImgData, myImg_thresh = trimmimg(img)
    
    X += [myImgData]
    im_list = np.array(myImg_thresh)
    plt.imshow(im_list)
    plt.show()

y = [0,1,2,3,4,5,6,7,8,9]

clf = linear_model.LogisticRegression(max_iter=10000)
clf.fit(X,y)
print(clf.score(X,y))

with open('numbers/model.pickle', mode='wb') as f:
    pickle.dump(clf,f,protocol=2)
