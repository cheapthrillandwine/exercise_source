## 画像の幾何学変換
画像の内容は変更せずにピクセルグリッドだけを変形して。変形したグリッドを出力画像にマッピングする。実際には、サンプリングによる余計な値や不定な値を除去するために、出力画像から入力画像という逆方向マッピングが行われる。つまり、出力画像の各ピクセル(x,y)に対して、入力画像中の対応する「ドナー」ピクセルの座標をもめ、そのピクセル値をコピーする。
ユーザが成獣のマッピングを指定した場合、OpenCVの関数は最初に、対応する逆マッピングを求めてから幾何学変換を行う。
### cv2.getPerspectiveTransform(const Point2f src[], const Pointsf dst[])
４組の対応点から透視変換を求めます。
src:入力画像上の四角形の頂点の座標
dst:出力画像上の対応する四角形の頂点の座標
この関数は透視変換を表す3*3の行列を求める。

### resize(const Mat&src, Mat&dst, size dsize, double fx=0, double fy=0,int interpolation=INTER_LINEAR)
src:入力画像
dst:出力画像。サイズはdsize(0でない場合)か、またはsrc.size(),fx,fyから計算される値になる。dstの型はsrcと同じになる。
dsize:出力画像のサイズ。これが0の場合以下のように計算される。
dsize = Size(round(fx*src.cols), round(fy*src.rows))
必ずdsizeが非0あるいはfxとfyの両方が非0でなければならない
fx:水平軸方向のスケールファクタ。これが0の場合は以下のように計算される。
(double)dsize.width/src.cols
fy:垂直軸方向のスケールファクタ。これが0の場合は以下のように計算される。
(double)dsize.height/src.rows
interpolation:
補間手法
INTER_NEAREST 最近傍補間
INTER_LINEAR バイリニア補間（デフォルト）
INTER_AREA ピクセル領域の関係を利用したリサンプリング．画像を大幅に縮小する場合は，モアレを避けることができる良い手法です．しかし，画像を拡大する場合は， INTER_NEAREST メソッドと同様になります
INTER_CUBIC 4x4 の近傍領域を利用するバイキュービック補間
INTER_LANCZOS4 8x8 の近傍領域を利用する Lanczos法の補間
関数resizeは画像srcを指定されたサイズに縮小、拡大する。dstの型やサイズは考慮されない。その代わりに型やサイズはsrc,dsize,fx,fyから求められる。あらかじめ用意しておいたdstとぴったり同じになるようにsrcのサイズを変更したい場合は次のような関数呼び出しができる。
dsize=dst.size():を明示的に指定する
resize(src, dst, dst.size(), 0, 0, interpolation);
各方向に二分の一に縮小したい場合は次のような関数呼び出しができる
resize(src, dst, Size(), 0.5, 0.5, interpokation);

### python
if __name__ == '__main__':
__name__という変数が自動です作成され、さらに実行しているスクリプトのモジュール名が自動的に代入される。
Pythonスクリプトを直接実行したときにはスクリプトファイルは__main__というモジュールとして認識される。そのためスクリプトファイルを実行すると__name__変数のなｋに自動で__main__という値が代入される。
「直接実行された場合のみ実行し、それ以外の場合は実行しない」という意味。
