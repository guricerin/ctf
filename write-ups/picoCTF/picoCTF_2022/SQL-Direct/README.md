まずは問題文の指示に従って接続。  

テーブル一覧を確認して全件取得でOK。  

```sql
\pico=# \d
            リレーション一覧
 スキーマ | 名前  |  タイプ  |  所有者
----------+-------+----------+----------
 public   | flags | テーブル | postgres
(1 行)


pico=# select * from flags;
```