``level5.py``を以下のように書き換え。  

```python
def level_5_pw_check():
    user_pws = open('dictionary.txt').readlines()
    user_pws = [u.strip() for u in user_pws]
    for user_pw in user_pws:
        user_pw_hash = hash_pw(user_pw)

        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
```
