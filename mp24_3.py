import cv2

# 画像を読み込む
image = cv2.imread('numbers/img1.jpg')

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

# トリミングした画像を保存
cv2.imwrite('trimmed_image.jpg', trimmed_image)
