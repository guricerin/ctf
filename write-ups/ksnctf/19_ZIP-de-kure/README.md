パスワード付きのzipファイル。  

```bash
$ file flag.zip
flag.zip: Zip archive data, at least v1.0 to extract

$ zipinfo flag.zip
Archive:  flag.zip
Zip file size: 256719 bytes, number of entries: 2
-rw-a--     2.0 fat      304 Bl stor 12-Jun-03 18:14 flag.html
-rw-a--     2.0 fat   255964 Bl stor 12-Jun-03 18:10 Standard-lock-key.jpg
2 files, 256268 bytes uncompressed, 256268 bytes compressed:  0.0%
```

``zipinfo``が出力した各ファイル情報の3列目に``fat``とあることから、Windows環境でzip化されたことがわかる。  

```
$ unzip flag.zip
Archive:  flag.zip
Hint:
- It is known that the encryption system of ZIP is weak against known-plaintext attacks.
- We employ ZIP format not for compression but for encryption.
[flag.zip] flag.html password:
```

``known-plaintext attacks``でググる。``既知平文攻撃``というらしい。ついでに``pkcrack``というパスワード付きzipのクラックツールを知る。  
https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack/download1.html からソースをダウンロードしてビルド。  

```bash
$ pwd
/home/guri

$ tar xzvf pkcrack-1.2.2.tar.gz
$ cd pkcrack-1.2.2/src
$ make
```

``pkcrack``の使い方。  

```bash
$ pwd
/home/guri/pkcrack-1.2.2/src

$ ./pkcrack
Usage: ./pkcrack -c <crypted_file> -p <plaintext_file> [other_options],
where [other_options] may be one or more of
 -o <offset>    for an offset of the plaintext into the ciphertext,
                        (may be negative)
 -C <c-ZIP>     where c-ZIP is a ZIP-archive containing <crypted_file>
 -P <p-ZIP>     where p-ZIP is a ZIP-archive containing <plaintext_file>
 -d <d-file>    where d-file is the name of the decrypted archive which
                will be created by this program if the correct keys are found
                (can only be used in conjunction with the -C option)
 -i     switch off case-insensitive filename matching in ZIP-archives
 -a     abort keys searching after first success
 -n     no progress indicator
```

``Standard-lock-key.jpg``でググったら[Wikipediaのページ](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Standard-lock-key.jpg)がヒットした。  
画像をダウンロード。**ただし、``2010年8月29日 (日) 18:53``に追加されたほうをだ。クソッタレ。ファイルサイズが2012年当時とは違うことに気づくのにやたら時間かかっちまった**``Standard-lock-key-P.jpg``という名前で保存しておく。  

実行。  

```bash
$ pwd
/home/guri/pkcrack-1.2.2/src

$ ./pkcrack -C flag.zip -c Standard-lock-key.jpg -p Standard-lock-key-P.jpg -d flag-dec
Files read. Starting stage 1 on Fri May  6 15:44:33 2022
Generating 1st generation of possible key2_255975 values...done.
Found 4194304 possible key2-values.
Now we're trying to reduce these...
Lowest number: 986 values at offset 248213
Lowest number: 948 values at offset 248202
Lowest number: 945 values at offset 247980
Lowest number: 928 values at offset 247965
Lowest number: 894 values at offset 247957
Lowest number: 883 values at offset 244764
Lowest number: 825 values at offset 244113
Lowest number: 820 values at offset 243180
Lowest number: 769 values at offset 243179
Lowest number: 758 values at offset 243175
Lowest number: 723 values at offset 243172
Lowest number: 702 values at offset 243171
Lowest number: 694 values at offset 243170
Lowest number: 657 values at offset 243162
Lowest number: 653 values at offset 243151
Lowest number: 652 values at offset 243149
Lowest number: 638 values at offset 243143
Lowest number: 621 values at offset 243106
Lowest number: 567 values at offset 243104
Lowest number: 546 values at offset 243103
Lowest number: 534 values at offset 243102
Lowest number: 510 values at offset 243073
Lowest number: 498 values at offset 243054
Lowest number: 476 values at offset 242992
Lowest number: 472 values at offset 242990
Lowest number: 396 values at offset 242989
Lowest number: 359 values at offset 242984
Lowest number: 321 values at offset 242983
Lowest number: 311 values at offset 242977
Lowest number: 310 values at offset 242939
Lowest number: 296 values at offset 242935
Lowest number: 270 values at offset 242934
Lowest number: 268 values at offset 242921
Lowest number: 244 values at offset 242915
Lowest number: 224 values at offset 242880
Lowest number: 215 values at offset 242879
Lowest number: 209 values at offset 242878
Lowest number: 188 values at offset 242877
Lowest number: 187 values at offset 242867
Lowest number: 186 values at offset 242866
Lowest number: 167 values at offset 242865
Lowest number: 164 values at offset 242670
Lowest number: 157 values at offset 242669
Lowest number: 141 values at offset 242655
Lowest number: 132 values at offset 242654
Lowest number: 112 values at offset 242652
Lowest number: 91 values at offset 242651
Done. Left with 91 possible Values. bestOffset is 242651.
Stage 1 completed. Starting stage 2 on Fri May  6 15:44:40 2022
Ta-daaaaa! key0=7adffffe, key1=468d5ff6, key2=259a116a
Probabilistic test succeeded for 13329 bytes.
Ta-daaaaa! key0=7adffffe, key1=468d5ff6, key2=259a116a
Probabilistic test succeeded for 13329 bytes.
Ta-daaaaa! key0=7adffffe, key1=468d5ff6, key2=259a116a
Probabilistic test succeeded for 13329 bytes.
Ta-daaaaa! key0=7adffffe, key1=468d5ff6, key2=259a116a
Probabilistic test succeeded for 13329 bytes.
Ta-daaaaa! key0=7adffffe, key1=468d5ff6, key2=259a116a
Probabilistic test succeeded for 13329 bytes.
Ta-daaaaa! key0=7adffffe, key1=468d5ff6, key2=259a116a
Probabilistic test succeeded for 13329 bytes.
Ta-daaaaa! key0=7adffffe, key1=468d5ff6, key2=259a116a
Probabilistic test succeeded for 13329 bytes.
Ta-daaaaa! key0=7adffffe, key1=468d5ff6, key2=259a116a
Probabilistic test succeeded for 13329 bytes.
Stage 2 completed. Starting zipdecrypt on Fri May  6 15:44:43 2022
Decrypting flag.html (250d8b78ce908fe210d7c091)... OK!
Decrypting Standard-lock-key.jpg (037d8119e2c2884a4a665d91)... OK!
Finished on Fri May  6 15:44:43 2022
```

展開して答えを見る。  

```bash
$ mkdir out
$ unzip flag-dec -d out
$ less out/flag.html
```
