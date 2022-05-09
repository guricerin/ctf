フラグがコメントとして記載されている。  

```bash
curl http://saturn.picoctf.net:59126/
```
ローカルにサイトをミラーする。  

```bash
$ wget -m http://saturn.picoctf.net:61941/

$ l saturn.picoctf.net:61941
total 36
drwxr-xr-x 5 guri guri  4096 May  9 17:57 ./
drwxr-xr-x 4 guri guri  4096 May  9 19:11 ../
drwxr-xr-x 2 guri guri  4096 May  9 17:57 css/
drwxr-xr-x 2 guri guri  4096 May  9 17:57 images/
-rw-r--r-- 1 guri guri 15920 Mar 15 15:29 index.html
drwxr-xr-x 2 guri guri  4096 May  9 17:57 js/
```

このディレクトリを対象にgrepする。  

```bash
$ grep pico -r saturn.picoctf.net\:61941/
```
