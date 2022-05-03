``ssh``接続と``ls``と``cd``のチュートリアル的問題。  

指示通りにssh接続。  

```bash
$ ssh ctf-player@venus.picoctf.net -p 58004
（中略）
ctf-player@pico-chall$ pwd
/home/ctf-player/drop-in
ctf-player@pico-chall$ ls -alF
total 16
drwxr-xr-x 1 ctf-player ctf-player 4096 Mar 16  2021 ./
drwxr-xr-x 1 ctf-player ctf-player 4096 May  3 14:13 ../
-rw-r--r-- 1 ctf-player ctf-player   14 Mar 16  2021 1of3.flag.txt
-rw-r--r-- 1 ctf-player ctf-player   56 Mar 16  2021 instructions-to-2of3.txt
```

それぞれのファイルを覗いてみる。  

```bash
ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_
ctf-player@pico-chall$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`
```

そういうノリね。  
フラグ文字列はローカルでメモっておく。後は同じような作業を2回繰り返すことになる。
