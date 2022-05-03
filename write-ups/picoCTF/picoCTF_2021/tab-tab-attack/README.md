ファイル形式を調べてから展開。  

```bash
$ file Addadshashanammu.zip
Addadshashanammu.zip: Zip archive data, at least v1.0 to extract
$ unzip Addadshashanammu.zip
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
```

``cd``の際にtabキーを連打して``./Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/``まで移動。  
あやしげなバイナリファイルがある。  

```bash
$ ls -alF
total 20
drwxr-xr-x 2 guri guri 4096 Mar 16  2021 ./
drwxr-xr-x 3 guri guri 4096 Mar 16  2021 ../
-rwxr-xr-x 1 guri guri 8320 Mar 16  2021 fang-of-haynekhtnamet*
$ file fang-of-haynekhtnamet
fang-of-haynekhtnamet: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=55548d0314fdf7999b966728d19712cdf8a52e58, not stripped
```

まあ別に実行しても問題なかったというか実行させたら答えが表示される。  
