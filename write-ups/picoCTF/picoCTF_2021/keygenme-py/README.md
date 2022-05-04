注目すべき箇所は以下（解析用におれが挿入した``print()``あり）。  

```python
...
username_trial = "FREEMAN"
bUsername_trial = b"FREEMAN"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
...
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial

    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")


def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        print(f"len(key) != len({key_full_template_trial})")
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                print(f"key[{i}] != {c}: key[i] = {key[i]}")
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            print(f"hexdigest()[4]: i: {i}, key[i]: {key[i]}, hexdigest()[4]: {hashlib.sha256(username_trial).hexdigest()[4]}")
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            print(f"hexdigest()[5]: i: {i}, key[i]: {key[i]}, hexdigest(): {hashlib.sha256(username_trial).hexdigest()[5]}")
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            print(f"hexdigest()[3]: i: {i}, key[i]: {key[i]}, hexdigest(): {hashlib.sha256(username_trial).hexdigest()[3]}")
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            print(f"hexdigest()[6]: i: {i}, key[i]: {key[i]}, hexdigest(): {hashlib.sha256(username_trial).hexdigest()[6]}")
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            print(f"hexdigest()[2]: i: {i}, key[i]: {key[i]}, hexdigest(): {hashlib.sha256(username_trial).hexdigest()[2]}")
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            print(f"hexdigest()[7]: i: {i}, key[i]: {key[i]}, hexdigest(): {hashlib.sha256(username_trial).hexdigest()[7]}")
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            print(f"hexdigest()[1]: i: {i}, key[i]: {key[i]}, hexdigest(): {hashlib.sha256(username_trial).hexdigest()[1]}")
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            print(f"hexdigest()[8]: i: {i}, key[i]: {key[i]}, hexdigest(): {hashlib.sha256(username_trial).hexdigest()[8]}")
            return False



        return True
...
```

- ライセンスキーは``picoCTF{1n_7h3_|<3y_of_xxxxxxxx}``と同じ文字数
- ``xxxxxxxx``は``hashlib.sha256(b"FREEMAN").hexdigest()``を一部抜き出したもの

これらさえわかれば後は簡単。  
