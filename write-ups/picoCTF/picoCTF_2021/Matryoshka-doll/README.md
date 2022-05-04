``binwalk``と``foremost``と``unzip``のチュートリアル的問題。  

```bash
$ binwalk dolls.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378952, uncompressed size: 383937, name: base_images/2_c.jpg
651610        0x9F15A         End of Zip archive, footer length: 22
```

そもそもjpegじゃないし、zipが埋め込まれていた。  

```bash
$ foremost dolls.jpg
Processing: dolls.jpg
|foundat=base_images/2_c.jpgUT
*|
$ cd ./output/zip
$ unzip 00000532.zip
Archive:  00000532.zip
  inflating: base_images/2_c.jpg
$ cd base_images/
$ binwalk 2_c.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196042, uncompressed size: 201444, name: base_images/3_c.jpg
383804        0x5DB3C         End of Zip archive, footer length: 22
383915        0x5DBAB         End of Zip archive, footer length: 22
```

問題タイトルから予想はしてたけど、どこまで続くねーん。  

```bash
guri@alpha: ~/sandbox/output/zip/base_images/output/zip/base_images/output/zip/base_images/output/zip on ☁️
$ l
total 16
drwxr-xr-- 2 guri guri 4096 May  4 09:55 ./
drwxr-xr-- 4 guri guri 4096 May  4 09:55 ../
-rw-r--r-- 1 guri guri  229 May  4 09:55 00000155.zip
-rw-r--r-- 1 guri guri   81 Mar 16  2021 flag.txt
```

4階層目でフラグ入手。  
