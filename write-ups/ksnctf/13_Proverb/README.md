```bash
$ ssh q13@ctfq.u1tramarine.blue -p 10013
q13@ctfq.u1tramarine.blue's password:
This server will destruct in 10 minutes.
Keep your progress by yourself.
```

```
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
