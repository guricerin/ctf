```bash
$ file leak.tar
leak.tar: POSIX tar archive (GNU)
$ tar -xf leak.tar
$ l leak
total 32
drwxr-xr-x 2 guri guri  4096 Mar 15 15:29 ./
drwxr-xr-x 4 guri guri  4096 May  8 18:46 ../
-rwxr-xr-x 1 guri guri 13130 Mar 15 15:29 passwords.txt*
-rwxr-xr-x 1 guri guri  7531 Mar 15 15:29 usernames.txt*
```

ユーザ``cultiris``に対応するパスワードを探すため、行番号を取得する。  

```bash
$ grep -n "cultiris" usernames.txt
378:cultiris
```

``passwords.txt``の378行目は``cvpbPGS{P7e1S_54I35_71Z3}``。  
これをROT13デコードした文字列が答え。  
