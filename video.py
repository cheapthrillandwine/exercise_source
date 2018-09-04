'''
参考URL
https://qiita.com/hitomatagi/items/caac014b7ab246faf6b1
http://motojapan.hateblo.jp/entry/2017/08/17/081917
https://qiita.com/bohemian916/items/4d3cf6506ec7d8f628f3
'''

import numpy as np
import cv2 as cv

# 動画入力
cap = cv.VideoCapture(0)

ret, frame1 = cp.read()
frame2 = frame1

# AKAZE検出器
detector = cv.AKAZE_create()

gray1 = cv.cvtColor(frame1, cv.COLOR_RGB2GRAY)
gray2 = cv.cvtColor(frame2, cv.COLOR_RGB2GRAY)

keypoints1, descriptors1 = detector.detectAndCompute(gray1, None)
keypoints2, descriptors2 = detector.detectAndCompute(gray2, None)

# キーポイントマッチング
# Brute-Force＝比較器の作成
bf = cv.BFMatcher()

# matchesの要素数はqueryDescriptionsの要素数に一致
# 上位k個の特徴点を返す
matches = bf.knnMatch(queryDescriptions = descriptors1, trainDescriptors = descriptors2, k=2)

# good_matches = matchesから選びだしたもの
frame3 = cv.drawMatchesKnn(frame1, keypoints1, frame2, keypoints2, good_matches, None, flags=2)

# 透視投影変換行列を求める(RANSAC)
# src_points/dst_pointsは、good_matchesからindexでアクセスしたquery/trainのkeypoint座標である。
#求めたいMの順にsrc_points/dst_pointsの入力順を決める
M, mask = cv2.findHomography(src_points, dst_points, cv.RANSAC, 5.0)

# 画像を回転する
frame2_train = cv2.warpPerspective(frame2, np.linalig.inv(M),size)
