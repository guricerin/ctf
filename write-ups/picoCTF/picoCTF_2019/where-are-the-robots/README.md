``robots.txt``を見てみる。  

```bash
$ curl https://jupiter.challenges.picoctf.org/problem/60915/robots.txt
User-agent: *
Disallow: /8028f.html
```

見るからに怪しそうなファイルを指定している。  
これを覗いて終了。  

```bash
$ curl https://jupiter.challenges.picoctf.org/problem/60915/8028f.html
```
