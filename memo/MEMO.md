# Description
# camera controls
+ 本コードはすべてcv2を用いてカメラ制御をしている

## about camera ID
+ パソコンに接続されたカメラにはランダムにID（0からの整数）が振られる
+ (基本はパソコン内蔵のインカメラが0、外付け接続のカメラが1から順に割り振られることが多い)
+ 以下のコードでIDを指定して、カメラを識別する
    + > cap = cv2.VideoCapture(0) # ID=0
+ IDの割り振りは毎度変わる可能性があるので注意

## about camera setting
+ カメラには多くの設定値（変数）が含まれる
+ カメラ固有のものとPC固有のものがある（どちらもメーカーによって設定値に差がある）
+ カメラ固有の設定値は以下のコードで確認できる
    > print("FRAME_WIDTH  : " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    > print("FRAME_HEIGHT : " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    > print("FPS          : " + str(cap.get(cv2.CAP_PROP_FPS)))
    > print("BRIGHTNESS   : " + str(cap.get(cv2.CAP_PROP_BRIGHTNESS)))
    > print("CONTRAST     : " + str(cap.get(cv2.CAP_PROP_CONTRAST)))
    > print("SATURATION   : " + str(cap.get(cv2.CAP_PROP_SATURATION)))
    > print("HUE          : " + str(cap.get(cv2.CAP_PROP_HUE)))
    > print("GAIN         : " + str(cap.get(cv2.CAP_PROP_GAIN)))
    > print("EXPOSURE     : " + str(cap.get(cv2.CAP_PROP_EXPOSURE)))
+ カメラ固有の設定は、以下のコードから任意の値に設定を変更できる場合がある
+ (カメラによっては設定できない項目もある)
    > cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(value))
    > cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(value))
    > cap.set(cv2.CAP_PROP_FPS, int(value))
    > cap.set(cv2.CAP_PROP_BRIGHTNESS, int(value))
    > cap.set(cv2.CAP_PROP_CONTRAST, int(value))
    > cap.set(cv2.CAP_PROP_SATURATION, int(value))
    > cap.set(cv2.CAP_PROP_HUE, int(value))
    > cap.set(cv2.CAP_PROP_GAIN, int(value))
    > cap.set(cv2.CAP_PROP_EXPOSURE, int(value))
+ PC固有の設定は、PCの設定等からいくつかの設定を変更できる

# multithread
+ いくつかのプロセスを複数スレッドに分けて並列処理する方法
+ 並列的に処理できるため、高速かつ効率的。
+ 今回の場合は、１つのスレッドが１つのカメラを受け持つため、他カメラの処理待ちがなく、ラグが少なくなる

## Basic code
+ ライブラリ："threading"を用いる
> import threading

+ 以下のコードでmultithreadを宣言する
    + TARGET: 対象とする関数
    + NAME: threadの名前（正直なんでもいい）
    + args: 関数に使う引数
    > th=threading.Thread(target=TARGET, name=NAME, args=(HIKISU,))

+ multithreadを開始する
> th.start()

+ multithreadが終了したら（対象関数から抜けたら）、main-threadのここに合流する
+ (main-threadはsub-threadが合流するまでここで待つ)
> th.join()

# multicast
+ 同一ネットワークに接続されている特定の複数デバイスに対して、同時にデータを通信する方法
+ （送信元は１つ、受信先は複数）
+ （例：学校Wifiに接続されているパソコンAとパソコンBに同じデータを送信したい）
+ 今回の場合、１台のパソコンで撮影アクションを確認し、他パソコンに撮影コマンドを送ることで、複数パソコンの同時制御を実現している

## basic code
ライブラリ："socket"を用いる
> import socket

+ 基本コードはフォーマットでほぼ決まっているので、この形式で書けばいい
+ 設定値（変数）の定義
    > local_address = '192.168.11.8'
    > multicast_group = '239.255.0.1'
    > port = 4000
    > bufsize = 4096
    + local_address = デバイスが接続しているネットワークのIPv4アドレス
        + コマンドから以下のように調べられる
        + Windows: コマンドプロンプトで、"ipconfig"と入力
        + Mac: ターミナルで、"ifconfig" と入力
    + multicast_group = データを送受信できるグループ
        + 基本的に'239.255.0.1'でいい
        + 使うデバイスすべて同じ数字列にしておけば、同じグループに所属できる
    + port = 送受信に使うポート。"4000"でいい
    + bufsize = データのバッファーサイズ。特に大きなデータを送らないなら"4096"で十分。

+ 設定
    > sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    > sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    > sock.bind(('', port))
    > sock.setsockopt(socket.IPPROTO_IP,
    >                 socket.IP_ADD_MEMBERSHIP,
    >                 socket.inet_aton(multicast_group) + socket.inet_aton(local_address))

## about UDP/TCP
+ 同一ネットワークに接続されている特定のデバイスに対して、データを通信する方法
+ (送信元は１つ、受信先は基本的に１つ。１対１通信。)
+ multicastの元になっている通信手法