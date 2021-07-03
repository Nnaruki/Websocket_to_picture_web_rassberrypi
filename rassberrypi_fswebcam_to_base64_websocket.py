import asyncio
import os
import websockets
import base64
import time
import cv2

import compression




# クライアント接続すると呼び出す。
async def accept(websocket, path):
        #Base64でエンコードする画像のパス
    target_file=r"decode.png"
    #エンコードした画像の保存先パス
    encode_file=r"comp_decode.jpg"


    try:
        capture = cv2.VideoCapture(1) # /dev/video*
        while(capture.isOpened()): # Open
            start =  time.time()
            retval, image = capture.read() # キャプチャー
            if retval is False:
                raise IOError
            cv2.imshow('Frame', image) # 表示
            cv2.imwrite(target_file, image)
            cv2.waitKey(1) # 1ミリ秒キーボードの入力を待ち受ける
            elapsed_time = time.time() - start
            print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
            
            compression.main()

            with open(encode_file, 'rb') as f:
                data = f.read()

            #Base64で画像をエンコード
            encode=base64.b64encode(data)
            await websocket.send(str(encode))
            elapsed_time = time.time() - start

    except KeyboardInterrupt:
        pass
    finally:
        capture.release () # VideoCaptureのClose
        cv2.destroyAllWindows() # Window削除
        
    
 
# WebSocketサーバー生成。ホストはlocalhost、portは9998に生成する。
start_server = websockets.serve(accept, "192.168.0.31", 8080)
# 非同期でサーバを待機する。
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()