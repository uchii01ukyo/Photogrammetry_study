# Contents
## camera
### picture
+ `camera_capture.py`
    + 1台のカメラを制御する基本コード 
    + 撮影モード："c"で撮影、"esc"で終了 
+ `camera_capture_multithread.py`
    + 複数カメラを並列的に制御するコード
    + 準備完了したカメラから順にそれぞれ撮影モードに入る
    + 撮影モード："c"で撮影、"esc"で終了
+ `camera_caoture_multithread_fps.py`
    + 複数カメラを並列的に制御するコード
    + 準備完了したカメラから順にそれぞれ撮影モードに入る
    + 撮影モードに入ってすぐ連続撮影（連写）を始める
    + 撮影モード："esc"で終了
+ `camera_capture_sametiming.py`
    + 複数カメラを並列的に制御するコード
    + 接続カメラがすべて準備完了したのを確認し、同時に撮影モードに入る
    + 撮影モードに入る合図："---capture = c, exit = esc---"
    + 撮影モード："c"で撮影、"esc"で終了
+ `camera_capture_multicast_server.py`
    + 複数のカメラを複数のパソコンで分散並列的に制御するコード（server側）
    + 接続カメラがすべて準備完了したのを確認し、同時に撮影モードに入る
    + 撮影モードに入る合図："---capture = c, exit = esc---"
    + 撮影モード："c"で撮影、"esc"で終了
+ `camera_capture_multicast_client.py`
    + 複数のカメラを複数のパソコンで分散並列的に制御するコード（client側）
    + 接続カメラがすべて準備完了したのを確認し、同時に撮影モードに入る
    + 撮影モードに入る合図："All connected."
    + 撮影モード：server側のPCで操作

### movie
+ `camera_view.py`
    + カメラからの映像を確認する基本コード
    + "esc"で終了
+ `camera_movie.py`
    + 1台のカメラを制御する基本コード
    + 撮影モードに入ってすぐ撮影開始される
    + 撮影モードに入る合図："Recording ... exit = esc"
    + 撮影モード："esc"で撮影終了
+ `camera_movie_multithread.py`
    + 複数カメラを並列的に制御するコード
    + 接続カメラがすべて準備完了したのを確認し、同時に撮影モードに入る
    + 撮影モードに入ってすぐ撮影開始される
    + 撮影モードに入る合図："Recording ... exit = esc"
    + 撮影モード："esc"で撮影終了

## element codes
+ `multithread.py`
    + multithreadを使った並列処理の基本コード
+ `multicast_server.py`
    + multicastを使った複数PCによる分散処理（多重処理）の基本コード（server側）
+ `multicast_client.py`
    + multicastを使った複数PCによる分散処理（多重処理）の基本コード（client側）
+ `get_ip_adress.py`
    + 接続しているネットワークのIPアドレスを取得するコード

## plot
+ `plot_matplotlib.py`
    + matplotlibを用いた点群描画コード
    + (点数が多すぎると処理に時間がかかりすぎるため断念)
+ `plot_pyqtgraph.py`
    + PyQtGraphを用いた点群描画コード
    + （点数が多すぎると処理に時間がかかりすぎるため断念）
    
# Warning
+ メモ程度に書かれているので、実際に動くかは検証していません。
+ 参考程度にしてください。
+ 動かない場合でも、多少の修正ですぐ動くはずです。（変数名を合わせる、変数の受け渡しを確認する等）

# Author
Uchii Ukyo(https://github.com/uchii01ukyo)