## 矩形抽出してキャプチャするには

### 輪郭抽出
#### 前提
1. 二値化画像を使うため、閾値処理やCannyのエッジ検出などが必要
2. cv2.findContours()関数は入力画像を変える処理。輪郭検出後の処理で入力画像を使用する必要がある場合は、別の変数にあらかじめコピーしておく。
3. OpenCVの輪郭検出は黒い背景から白い物体の輪郭を検出することを仮定している。

cv2.findContours()は少なくとも３つの引数を取る関数。第１引数は入力画像、第２引数は輪郭抽出モード、第３引数は輪郭検出方法を指定するフラグ。出力は輪郭画像と輪郭、輪郭の階層情報の３つである。輪郭とは検出された全輪郭をPythonのlistとして出力するものでlist内の各輪郭は輪郭上の点の(x,y)座標をNumpyのarrayとして保存されている。

### 輪郭描画
この関数は境界上に点を持つ形状であれば、輪郭以外の形容の描画にも使える。
第１引数は入力画像、第２引数はPythonのlistとして保存している輪郭。第３引数contourIdxは描画したい輪郭のインデックス(第２引数で与えられた輪郭のlistから一つの輪郭だけを描画したいとき、輪郭の指定に使う。全輪郭を描画するときは-1を指定する。以降は輪郭を描画する色や線の太さ(thickness))
