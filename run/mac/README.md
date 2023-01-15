# Contents
+ `setting.command`
    + 初期設定用
+ `camera_capture.command`
    + １台のカメラから静止画を取得するテストコード
    + 撮影モード："c"で静止画撮影、"esc"で終了
    + 出力先：../../capture/capture
    + > 主な実行コード：../../capture/camera_capture.py camera_capture()
+ `camera_check.command`
    + ID指定したカメラからの映像を確認するテストコード
    + "esc"で終了
    + > 主な実行コード：../../capture/camera_capture.py check_camera()
+ `camera_multithread.command`
    + （１台のパソコンで）複数カメラを並列的に制御するコード
    + 準備完了の合図："All connected."
    + 撮影モードに入る合図（picture）："c = capture, esc = exit"
    + 撮影モードに入る合図（movie）："c = capture start, esc = exit"
    + 撮影モード："c"で撮影、"esc"で終了
    + 出力先：../../capture/capture
    + > 主な実行コード：../../capture/camera_multithread.py main()
+ `camera_multicast_server.command`
    + 複数のカメラを複数のパソコンで分散並列的に制御するコード（server側）
    + 準備完了の合図："All connected."
    + 撮影モードに入る合図（picture）："c = capture, esc = exit"
    + 撮影モードに入る合図（movie）："c = capture start, esc = exit"
    + 撮影モード："c"で撮影、"esc"で終了
    + 出力先：../../capture/capture
    + > 主な実行コード：../../capture/camera_multicast_server.py main()
+ `camera_multicast_client.command`
    + 複数のカメラを複数のパソコンで分散並列的に制御するコード（client側）
    + 準備完了の合図："All connected."
    + 撮影モード：server側のPCで操作（"c"で撮影、"esc"で終了）
    + 出力先：../../capture/capture
    + > 主な実行コード：../../capture/camera_multicast_client.py main()
+ `convert_movie_picture.command`
    + 入力した動画を静止画に変換して出力（指定した時間分）
    + (変換する時間はコード内で指定します)
    + 入力：../capture/captureにあるMP4ファイル
    + 出力：./pictureにJPG形式で出力
    + > 主な実行コード：../../drawing/convert_movie_picture.py main()
+ `convert_movie_picture_bara.command`
    + 入力した動画を静止画に変換して出力（指定したフレームの前後10フレーム分）
    + (フレームの指定は動画ごとにコード内でします)
    + 入力：../capture/captureにあるMP4ファイル
    + 出力：./pictureにJPG形式で出力
    + > 主な実行コード：../../drawing/convert_movie_picture_bara.py main()

# How to
## Setting
+ "setting.command"をクリックする
+ （初期設定なので、はじめの一回だけでいいです）
+ （すべてcommandファイルにパスを通して、実行権限を与えているだけです）
## How to
+ 以下のコードは、クリックするだけで実行できる
    + camera_capture.command
    + camera_check.command
    + convert_movie_picture.command
    + convert_movie_picture_bara.command
+ 以下のコードはいくつか変数を指定してから、クリックして実行する
    + camera_multithread.command
    + camera_multicast_server.command
    + camera_multicast_client.command
+ 変数を指定する方法
    + コマンドファイルをテキスト形式で開く
    ```
    python FUNCTION 'MODE' WIDTH HEIGHT FPS BRIGHT
    ```
    + FUNCTION = 対象とする関数（そのままで！）
    + MODE = picture（静止画）or movie（動画）
    + WIDTH = 画素数（列方向）
    + HEIGHT = 画素数（行方向）
    + FPS = フレームレート（１秒間に何枚撮影するか）
    + BRIGHT = 明るさ

    例：解像度1920x1080で、動画を撮影したいとき
    ```
    python camera_multithread.py 'movie' 1920 1080 30 30
    ```

# Author
Uchii Ukyo(https://github.com/uchii01ukyo)
