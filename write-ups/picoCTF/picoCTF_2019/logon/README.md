``Username``は適当に、``Password``は空欄のままボタンをクリックしたら``https://jupiter.challenges.picoctf.org/problem/15796/flag``に遷移する。  
ここでデベロッパーツールを開きクッキーを覗いてみると``admin``フィールドが設定されているので、これの値を``True``に変更してページ再読み込みしたらフラグを入手。  
