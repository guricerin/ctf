まっとうな``docx``ファイル。  
``docx``は``xml``ファイルをzip圧縮したものというのは初めて知った。  

```bash
$ binwalk paper.docx

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, compressed size: 464, uncompressed size: 2504, name: [Content_Types].xml
1033          0x409           Zip archive data, at least v2.0 to extract, compressed size: 243, uncompressed size: 590, name: _rels/.rels
1837          0x72D           Zip archive data, at least v2.0 to extract, compressed size: 395, uncompressed size: 2123, name: word/_rels/document.xml.rels
2554          0x9FA           Zip archive data, at least v2.0 to extract, compressed size: 4816, uncompressed size: 42869, name: word/document.xml
7417          0x1CF9          Zip archive data, at least v2.0 to extract, compressed size: 421, uncompressed size: 1222, name: word/header3.xml
7884          0x1ECC          Zip archive data, at least v2.0 to extract, compressed size: 421, uncompressed size: 1222, name: word/footer2.xml
8351          0x209F          Zip archive data, at least v2.0 to extract, compressed size: 421, uncompressed size: 1222, name: word/footer1.xml
8818          0x2272          Zip archive data, at least v2.0 to extract, compressed size: 421, uncompressed size: 1222, name: word/header2.xml
9285          0x2445          Zip archive data, at least v2.0 to extract, compressed size: 421, uncompressed size: 1222, name: word/header1.xml
9752          0x2618          Zip archive data, at least v2.0 to extract, compressed size: 463, uncompressed size: 1466, name: word/endnotes.xml
10262         0x2816          Zip archive data, at least v2.0 to extract, compressed size: 463, uncompressed size: 1472, name: word/footnotes.xml
10773         0x2A15          Zip archive data, at least v2.0 to extract, compressed size: 421, uncompressed size: 1222, name: word/footer3.xml
11240         0x2BE8          Zip archive data, at least v1.0 to extract, compressed size: 11849, uncompressed size: 11849, name: word/media/image1.png
23140         0x5A64          Zip archive data, at least v2.0 to extract, compressed size: 1715, uncompressed size: 7084, name: word/theme/theme1.xml
24906         0x614A          Zip archive data, at least v2.0 to extract, compressed size: 1227, uncompressed size: 3110, name: word/settings.xml
26180         0x6644          Zip archive data, at least v2.0 to extract, compressed size: 258, uncompressed size: 428, name: word/webSettings.xml
26488         0x6778          Zip archive data, at least v2.0 to extract, compressed size: 2329, uncompressed size: 17515, name: word/stylesWithEffects.xml
28873         0x70C9          Zip archive data, at least v2.0 to extract, compressed size: 2201, uncompressed size: 16762, name: word/styles.xml
31119         0x798F          Zip archive data, at least v2.0 to extract, compressed size: 362, uncompressed size: 727, name: docProps/core.xml
31792         0x7C30          Zip archive data, at least v2.0 to extract, compressed size: 629, uncompressed size: 2060, name: word/fontTable.xml
32469         0x7ED5          Zip archive data, at least v2.0 to extract, compressed size: 376, uncompressed size: 713, name: docProps/app.xml
34498         0x86C2          End of Zip archive, footer length: 22
```

展開してみる。  

```bash
$ mkdir content
$ unzip paper.docx -d content/
$ cd content
$ l
total 24
drwxr-xr-x 5 guri guri 4096 May  5 16:43  ./
drwxr-xr-x 5 guri guri 4096 May  5 16:42  ../
-rw-r--r-- 1 guri guri 2504 Jan  1  1980 '[Content_Types].xml'
drwxr-xr-x 2 guri guri 4096 May  5 16:43  _rels/
drwxr-xr-x 2 guri guri 4096 May  5 16:43  docProps/
drwxr-xr-x 5 guri guri 4096 May  5 16:43  word/
```

このディレクトリをvscodeで開いてgrep検索してたりなんやかんやしてたりするうちに、``word/document.xml``で``<pic:cNvPr id="0" name="Picture 2" descr="C:\Users\FLxAG_hogehoge\Documents\paper\P is equal to NP\remove_x\200px-Complexity_subsets_pspace.svg.png"/>``というWindowsのユーザ名部分に怪しい文字列を発見。  
``FLxAG_hogehoge``から``x``を抜いた文字列を提出して解答。  

### 参考

- [Office Open XML | Wikipedia](https://ja.wikipedia.org/wiki/Office_Open_XML)
