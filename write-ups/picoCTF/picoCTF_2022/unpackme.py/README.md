暗号化されたPythonコードをデコードし、それを実行するスクリプトとなっている。  
以下のようにデコードされたPythonコードを表示させればOK。  

```python
plain = f.decrypt(payload)
+ print(plain)
exec(plain.decode())
```
