# 前提

エディタがあれば python はインストールする必要なし<br>

## git のインストール

### git のインストール方法

以下に git のインストール方法を示します。もうインストールしてある人は読み飛ばして下さい。

- https://git-scm.com/download/win
  このサイトからダウンロードしてインストールしてください。
- 同意を押したら`Choosing the default editor used by Git`まで next を押してください。
- `Choosing the default editor used by Git`が出てきたら使用しているエディタの設定を選んで next を押してください。
- `Use Git from Git Bash only`を選んで next を押してください。
- `Use the OpenSSL library`を選んで next を押してください。
- `Use MinTTY (the default terminal of MSYS2)`を選んで next を押してください。
- 全てに ✅ を入れて next を押してください。
- 何も選択せずに install を押してください。<br>
  <br>
  **分からない場合は`Git 導入`と調べると色々なサイトで説明されているのでそちらを参考にしてください**

### Git をインストールしたらやること

Git Bash を起動して

```bash
git config --global user.name "Your Name
```

と入力してください。

```bash
git config --global user.email "Your Email"
```

と入力してください。<br>
※Your Name と Your Email は自分のを入力してください。

### **これで初期設定は終了です。**

# 書き換える箇所

<br>
1.

```python
user_id = 'your mail address'
user_pass = 'your account password'
```

<br>
2.

```python
wenhook_url = 'discordのwebhookのurl'
```

これらの箇所を自分のものに書き換えください

# heroku に push しよう

## 下準備

cmd を起動してインストールしたフォルダへ移動してください。

```
cd path/to/save
```

で移動できます。

## heroku の設定

- heroku のアカウントが無ければ heroku に登録してください。
- heroku に登録したら、`Create a new app`を押してください。
- `Name`に`app name`と入力してください。<br>
  ※このときの`app name`は自分で考えてください。

## 2.buildpacks の設定

以下のものを設定してください<br>

- heroku/python
- https://github.com/heroku/heroku-buildpack-chromedriver.git
- https://github.com/heroku/heroku-buildpack-google-chrome.git

## デプロイ

- `Deploy`を押してください。
- `Deploy`の書いてある通りに行えばデプロイされます。

## heroku scheduler の設定

**heroku scheduler を設定には、クレジットカードが必要です。<br>※バンドルカードでも可能**
<br>
heroku scheduler は、**UTC**なので、それに気を付けて設定してください。
<br>
時間を設定したら、

```bash
python main.py
```

と入力してください。

### **これで終了です。**
