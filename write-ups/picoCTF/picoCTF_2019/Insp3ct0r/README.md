```bash
$ curl https://jupiter.challenges.picoctf.org/problem/44924/
<!doctype html>
<html>
  <head>
    <title>My First Website :)</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="mycss.css">
    <script type="application/javascript" src="myjs.js"></script>
  </head>

  <body>
    <div class="container">
      <header>
        <h1>Inspect Me</h1>
      </header>

      <button class="tablink" onclick="openTab('tabintro', this, '#222')" id="defaultOpen">What</button>
      <button class="tablink" onclick="openTab('tababout', this, '#222')">How</button>

      <div id="tabintro" class="tabcontent">
        <h3>What</h3>
        <p>I made a website</p>
      </div>

      <div id="tababout" class="tabcontent">
        <h3>How</h3>
        <p>I used these to make this site: <br/>
          HTML <br/>
          CSS <br/>
          JS (JavaScript)
        </p>
        <!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
      </div>

    </div>

  </body>
</html>
```

HTML内にコメントとしてフラグの一部が記載されている。  
ヘッダー部にcssファイル名とjsファイル名が記載されているので試しにアクセスしたら、やはり同じように記載されているのでそれらをつなぎ合わせて解答。  

```bash
curl https://jupiter.challenges.picoctf.org/problem/44924/mycss.css
curl https://jupiter.challenges.picoctf.org/problem/44924/myjs.js
```
