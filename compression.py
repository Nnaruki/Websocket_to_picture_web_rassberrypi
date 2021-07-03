from PIL import Image
from io import BytesIO
import os
import time


def main():
    start = time.time()

    # コンフィグ
    COMPRESS_QUALITY = 30 # 圧縮のクオリティ

    # JPEG形式とPNG形式の画像ファイルを用意
    # jpeg_imgefile = 'gray_comp_jpeg_image.jpg'
    png_imgfile = 'decode.png'

    #############################
    #     JPEG形式の圧縮処理     #
    #############################
    # ファイル名を取得
    # file_name = os.path.splitext(os.path.basename(jpeg_imgefile))[0]
    # with open(jpeg_imgefile, 'rb') as inputfile:
    #     # バイナリモードファイルをPILイメージで取得
    #     im = Image.open(inputfile)
    #     # JPEG形式の圧縮を実行
    #     im_io = BytesIO()
    #     im.save(im_io, 'JPEG', quality = COMPRESS_QUALITY)
    # with open('comp_' + file_name + '.jpg', mode='wb') as outputfile:
    #     # 出力ファイル(comp_png_image.png)に書き込み
    #     outputfile.write(im_io.getvalue())

    #############################
    #     PNG形式の圧縮処理      #
    #############################
    # ファイル名を取得
    file_name = os.path.splitext(os.path.basename(png_imgfile))[0]
    with open(png_imgfile, 'rb') as inputfile:
        # バイナリモードファイルをPILイメージで取得
        im = Image.open(inputfile)
        # JPEG形式に変換して、圧縮を実行
        im = im.convert('RGB')
        im_io = BytesIO()
        im.save(im_io, 'JPEG', quality = COMPRESS_QUALITY)
    with open('comp_' + file_name + '.jpg', mode='wb') as outputfile:
        # 出力ファイル(comp_png_image.png)に書き込み
        outputfile.write(im_io.getvalue())


    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")