``https://jupiter.challenges.picoctf.org/problem/50522/flag``を見てみると、``User-Agent``ヘッダを識別している様子。  
以下でフラグ取得。  

```bash
$ curl -H 'User-Agent: picobrowser' https://jupiter.challenges.picoctf.org/problem/50522/flag
```
