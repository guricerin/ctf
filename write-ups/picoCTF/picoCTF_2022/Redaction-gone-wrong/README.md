LibreOfficeから開くことで、黒塗り長方形のオブジェクトをどかすことが可能。  

### 追記

https://ctftime.org/writeup/33112 によれば、``pdftotext``なるコマンドがあるらしい。  
Ubuntuでの使い方は以下。  

```bash
$ sudo apt install poppler-utils
$ pdftotext Financial_Report_for_ABC_Labs.pdf
$ less  Financial_Report_for_ABC_Labs.txt
```

こっちのほうが手軽。  
