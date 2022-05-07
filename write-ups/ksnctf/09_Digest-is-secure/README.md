徳丸氏の[この動画](https://www.youtube.com/watch?v=aGS26pW2gY4)の作業をほぼそのまま実行することでフラグが入手可能。  

Digest認証というらしい。  
以下は[Wiki](https://ja.wikipedia.org/wiki/Digest%E8%AA%8D%E8%A8%BC)からの引用。

> クライアントが計算するresponseは以下のようにして求められる：
> A1 = ユーザ名 ":" realm ":" パスワード
> A2 = HTTPのメソッド ":" コンテンツのURI
> response = MD5( MD5(A1) ":" nonce ":" nc ":" cnonce ":" qop ":" MD5(A2) )
> サーバ側では、MD5(A1) をあらかじめ計算し格納してある。nonce, nc, cnonce, qopとHTTPのメソッド（GETなど）とコンテンツのURIはクライアントから送られてくるので、サーバ側でもresponseの正解を計算できる。

重要なのは、徳丸氏の動画タイトルそのままだが、Digest認証ではパスワードが不明でもハッシュ値がわかれば不正ログイン可能ということ。  

データを見やすくするため``q9.pcap``をWiresharkで開いて、プロトコルが``HTTP``の行を右クリック -> ``追跡`` -> ``HTTPストリーム`` -> ``保存``。  
保存したHTTPストリームを見ると、``http://ctfq.u1tramarine.blue/q9/flag.html``が入手すべきフラグ、````http://ctfq.u1tramarine.blue/q9/htdigest``がDigest認証用の登録済みユーザを記載したファイルだとわかる。  
しかも``htdigest``については中身がバッチリ漏れている。最終行がそれにあたる。この文字列をコピっておく。    

徳丸氏の作業環境を再現する。  

```bash
cd work/
docker-compose up -d
```

ブラウザで``localhost:8000``に接続。``credentail``に先程コピーした文字列を貼り付け。  

OWASP ZAPを用意し``http://ctfq.u1tramarine.blue/q9/flag.html``を開いた後は、動画の通りにやればフラグ入手。  

### 参考

- [Digest認証](https://ja.wikipedia.org/wiki/Digest%E8%AA%8D%E8%A8%BC)
- [Digest認証のハッシュ値が漏洩すると直ちに不正ログインできる](https://www.youtube.com/watch?v=aGS26pW2gY4)
- [RFC7616](https://datatracker.ietf.org/doc/html/rfc7616)
