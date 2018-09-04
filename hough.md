### cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dp=, minDist=, param1=, param2=, minRadius=, maxRadius= )
dp:処理するときに元画像の解像度を落として検出する場合には増やす。たとえば、1だとそのままの画質で処理して、2だと1/2に縮小して処理する。
minDist:検出される円と円の最小距離
param1:Cannyのエッジ検出器で用いる2つの閾値の高い方。低いほどいろんなエッジを検出する。
param2:中心検出計算時の閾値。低いほど円じゃないものも検出する。
minRadius:最小半径
maxRadius:最大半径

返り値
[x,y,radius]
