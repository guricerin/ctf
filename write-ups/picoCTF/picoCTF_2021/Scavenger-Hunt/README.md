picoCTF 2019 Insp3ct0rの類題。  

```bash
curl -i http://mercury.picoctf.net:27393/
curl -i http://mercury.picoctf.net:27393/mycss.css
```

ここから先は少し勝手が違う。  

```bash
$ curl -i http://mercury.picoctf.net:27393/myjs.js
HTTP/1.1 200 OK
Content-Type: application/javascript
Content-Length: 642
Last-Modified: Tue, 16 Mar 2021 00:51:38 GMT

function openTab(tabName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(tabName).style.display = "block";
    if(elmnt.style != null) {
        elmnt.style.backgroundColor = color;
    }
}

window.onload = function() {
    openTab('tabintro', this, '#222');
}

/* How can I keep Google from indexing my website? */
```

HTMLのメタタグやHTTPレスポンスヘッダーにそれらしき情報はなかった。であれば``robots.txt``ということになる。  

```bash
$ curl http://mercury.picoctf.net:27393/robots.txt
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

apacheといえば``.htaccess``。  

```bash
$ curl http://mercury.picoctf.net:27393/.htaccess
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

macでありがちなミスは、``.DS_Store``をサーバやgitリポジトリに送信すること。  

```bash
$ curl http://mercury.picoctf.net:27393/.DS_Store
Congrats! You completed the scavenger hunt. Part 5: _d375c750}
```

クライアントがURLを指定してアクセスできてはいけないはずのファイルにアクセスできちゃうのは、強制ブラウジングの脆弱性と呼ぶ。  
ディレクトリ・トラバーサルは相対パス指定という点で、強制ブラウジングとは異なるらしい。  

### 参考

- [クロールとインデックス登録に関するトピックの概要 - developers.google](https://developers.google.com/search/docs/advanced/crawling/overview?hl=ja)
- [Forced browsing - owasp.org](https://owasp.org/www-community/attacks/Forced_browsing)
