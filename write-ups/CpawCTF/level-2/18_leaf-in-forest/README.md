pcap形式だった。  

```bash
file misc100
```

しかし、Wiresharkから開こうとしても失敗。  
``cat``で中身を見てみる。``lovelive!``という文字列がバイナリ形式で大量に書き込まれている怪文書らしい。  
バイナリファイル中の文字列を取り出す``strings``コマンドと逆grepを組み合わせてみる。  

```bash
strings misc100 | grep -v "lovelive!"
```

なんも表示されない。``grep``に食わせたデータは改行のない文字列扱いになっていたからか。  
気を取り直して普通に``grep``。  

```bash
strings misc100 | grep "lovelive!"
```

見にくいが、どうやら``lovelive!``以外の文字列が埋め込まれている模様。  
つなげてみたら``CCCPPPAAAWWW{{{MMMGGGRRREEEPPP}}}``だった。  
同じ文字を3回繰り返しているようなので、それぞれ1文字ずつにしたら``CPAW{MGREP}``。  
問題文にある通り``フラグはすべて小文字``とのことなので、``cpaw{mgrep}``が正解。  
