まず``1584891``と``3438478``が互いに素（最大公約数が1）であるかを確認。  

```bash
$ python3 coprime.py
1584891 3438478
True
```

各modが互いに素なので中国剰余定理を適用可能。  

```bash
$ python3 crt.py
2
32134 1584891
193127 3438478
cpaw{35430270439}
```

なお、理論的な詳細はまったく理解できていない。  

- 参考
  - [中国剰余定理 (CRT) の解説と、それを用いる問題のまとめ](https://qiita.com/drken/items/ae02240cd1f8edfc86fd)
  - [『詳解セキュリティコンテスト』](https://book.mynavi.jp/ec/products/detail/id=122750)
