jpegファイルのExif情報をターミナルから確認するには、``imagemagick``をインストールし``identify``コマンドを使用する。  

```bash
sudo apt install imagemagick
identify -verbose river.jpg | grep "exif"
```

撮影日時だのGPS情報だのいろいろ表示されるが、フラグが直接埋め込まれているわけではない。  
ので、画像から場所を割り出す適当なwebツール使って川の名前を割り出し、それをローマ字に置き換えて解答。  
