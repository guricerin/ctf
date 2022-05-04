ページを検証してみると、``GET``リクエストなら赤色表示、``POST``リクエストなら青色表示に切り替えていることがわかる。  
パラメータは関係ない。HTTPメソッドの種類だけで判断している。  

問題文のタイトルが大ヒント。``HEAD``リクエストを送信でクリア。  

```bash
curl --head http://mercury.picoctf.net:15931
```

ちなみに他のメソッドだと``{background-color: ?;}``としたページを返す。  

### 参考

- [HEAD - MDN](https://developer.mozilla.org/ja/docs/Web/HTTP/Methods/HEAD)
