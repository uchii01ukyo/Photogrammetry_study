# Contents
+ `camera_capture.py`
    + １台のカメラを使った基本コード
    + camera_capture
        + 撮影モード："c"で静止画撮影、"esc"で終了
    + check_camera
        + ID指定したカメラからの映像を確認する
        + "esc"で終了
+ `camera_multithread.py`
    + （１台のパソコンで）複数カメラを並列的に制御するコード
    + 接続カメラがすべて準備完了したのを確認し、同時に撮影モードに入る
    + 接続カメラ準備完了の合図："All connected."
    + 撮影モードに入る合図（picture）："c = capture, esc = exit"
    + 撮影モードに入る合図（movie）："c = capture start, esc = exit"
    + 撮影モード："c"で撮影、"esc"で終了
+ `camera_multicast_client.py`
    + 複数のカメラを複数のパソコンで分散並列的に制御するコード（server側）
    + 接続カメラがすべて準備完了したのを確認し、同時に撮影モードに入る
    + 接続カメラ準備完了の合図："All connected."
    + 撮影モードに入る合図（picture）："c = capture, esc = exit"
    + 撮影モードに入る合図（movie）："c = capture start, esc = exit"
    + 撮影モード："c"で撮影、"esc"で終了
+ `camera_multicast_server.py`
    + 複数のカメラを複数のパソコンで分散並列的に制御するコード（client側）
    + 接続カメラがすべて準備完了したのを確認し、同時に撮影モードに入る
    + 接続カメラ準備完了の合図："All connected."
    + 撮影モード：server側のPCで操作（"c"で撮影、"esc"で終了）

# How to 
+ ディレクトリ"run"に入っている実行コマンドをクリックすることで実行できる

# Author
Uchii Ukyo(https://github.com/uchii01ukyo)