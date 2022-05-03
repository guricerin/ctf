自力解答ならず。  

まずはメタデータを見てみる。  

```bash
$ exiftool cat.jpg
ExifTool Version Number         : 11.88
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 kB
File Modification Date/Time     : 2022:05:03 09:42:44+09:00
File Access Date/Time           : 2022:05:03 09:44:40+09:00
File Inode Change Date/Time     : 2022:05:03 09:44:11+09:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

あやしそうなのは``Current IPTC Digest``と``License``のフィールド値。  
だが形式からしてハッシュ値というわけではないっぽい。https://hashtoolkit.com/decrypt-hash/ で一応調べたがやはり違う。  
というわけでここで詰まる。  

正解はBase64。なぜ気づかなかった。  

```bash
echo -n "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
```
