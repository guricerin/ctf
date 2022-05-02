ソースコードを見てみたら第一引数に暗号文を、第二引数に数値を与えればよいことがわかる。  
``ruoYced_ehpigniriks_i_llrg_stae``がアナグラムっぽい。これを第一引数とする。  
第二引数は二分探索的に色々と試してみた。結果的には以下のようにすれば正解が表示される。  

```bash
gcc crypto100.c
./a.out ruoYced_ehpigniriks_i_llrg_stae 4
```
