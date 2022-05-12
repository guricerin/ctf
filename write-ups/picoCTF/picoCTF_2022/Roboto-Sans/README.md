問題タイトルがヒント。  

まずミラー。  

```bash
$ wget -m saturn.picoctf.net:64710/

$ l saturn.picoctf.net\:64710
total 40
drwxr-xr-x 5 guri guri  4096 May 12 16:38 ./
drwxr-xr-x 5 guri guri  4096 May 12 16:38 ../
drwxr-xr-x 2 guri guri  4096 May 12 14:57 css/
drwxr-xr-x 2 guri guri  4096 May 12 14:57 images/
-rw-r--r-- 1 guri guri 15920 Mar 15 15:29 index.html
drwxr-xr-x 2 guri guri  4096 May 12 14:57 js/
-rw-r--r-- 1 guri guri   229 May 12 16:33 robots.txt
```

``robots.txt``を見てみる。  

```bash
$ cat robots.txt
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

``robots.txt``に記載するには通常ありえない形式の文字列が含まれている。  
base64で解読できた部分は以下。  

```
flag1.txt;js/myfi
js/myfile.txt
,z;(ha.nh^
```

試しに``/js/myfile.txt``を覗いてみたらフラグ入手。  

```bash
$ curl http://saturn.picoctf.net:64710/js/myfile.txt
```
