```python
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE067d3eh2bN"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """
# （省略）
```

コメントにあるように、シーザー暗号の鍵は符号化・復号化で同一。  
ファイルの最下段に``decode_secret(bezos_cc_secret)``を挿入して実行すればフラグ入手。  
``choose_greatest()``の存在理由は不明。単なるミスディレクション？  
