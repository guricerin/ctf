いきなり``/etc/shadow``形式のファイルが表示されている。``shadow.txt``として保存しておく。  
最下段に注目してみると、  

```
user99:$6$SHA512IsStrong$DictionaryIsHere.http//ksnctf.sweetduet.info/q/14/dicti0nary_8Th64ikELWEsZFrf.txt:15491:0:99999:7:::
```

``http//ksnctf.sweetduet.info/q/14/dicti0nary_8Th64ikELWEsZFrf.txt``にアクセスして辞書ファイルを取得。``dict.txt``として保存しておく。  

ここで、パスワードクラッキングツールの``John the Ripper``をインストール。  

```bash
sudo apt install john
```

``john``に辞書を食わせて解析させる。  

```bash
$ john -w:dict.txt shadow.txt
Loaded 22 password hashes with 22 different salts (crypt, generic crypt(3) [?/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
floating         (user13)
ADDITIONAL       (user02)
（中略）
LEAVE            (user12)
21g 0:00:00:53 100% 0.3959g/s 57.35p/s 639.5c/s 639.5C/s gravekeeper..ADMIRATION
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

結果の再表示は、上にもある通りこのようにする。  

```bash
$ john --show shadow.txt
user00:FREQUENT:15491:0:99999:7:::
user01:LATTER:15491:0:99999:7:::
user02:ADDITIONAL:15491:0:99999:7:::
user03:GENDER:15491:0:99999:7:::
user04:__________:15491:0:99999:7:::
（以下省略）
```

肝心のフラグは、解析したパスワードの先頭1文字を縦読み。  

ハッシュ化されていようが、パスワードの強度がしょぼかったりハッシュ値そのものが漏洩すると非常にまずいことがわかる。  

### 参考

- [CTFのWebセキュリティにおけるPassword Cracking, ハッシュ, 暗号化 - はまやんはまやんはまやん](https://blog.hamayanhamayan.com/entry/2021/12/23/225445)
- [John the Ripper - Wikipedia](https://en.wikipedia.org/wiki/John_the_Ripper)
