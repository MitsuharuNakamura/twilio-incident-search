
# Twilio Incident Keyword Search

## 概要
Twilioのステータス履歴ページから過去のインシデント情報を検索し、指定したキーワード（例: "Japan"）を含むインシデントを抽出するPythonスクリプトです。

このスクリプトは以下を行います:
1. Twilioのステータスページ（複数ページ対応）をスクレイピング。
2. インシデントデータをJSON形式で解析。
3. 特定のキーワードを含むインシデントを抽出。
4. 抽出結果をコンソールに出力。

---

## 使用方法

### 必要要件
以下のソフトウェアとライブラリが必要です：
- Python 3.7以上
- 必要なPythonライブラリ（インストール方法は後述）

### セットアップ

1. **リポジトリをクローン**:
   ```bash
   git clone https://github.com/your-repository/twilio-incident-search.git
   cd twilio-incident-search
   ```

2. **必要なライブラリをインストール**:
   必要なPythonライブラリをインストールします。
   ```bash
   pip install requests beautifulsoup4
   ```

3. **スクリプトの実行**:
   スクリプトを実行してインシデントを検索します。
   ```bash
   python search_incidents.py
   ```

---

## スクリプトの説明

### 入力
- **検索キーワード**: スクリプト内の`search_word`変数でキーワードを指定します（デフォルトは`"Japan"`）。
- **スクレイピングページ数**: `for page in range(1, 5)`で検索するページ数を指定します。

### 出力
- 検索キーワードに一致する以下の情報をコンソールに出力します:
  - **Timestamp**: インシデントの発生時刻
  - **Name**: インシデントのタイトル
  - **Message**: インシデントの詳細メッセージ

例:
```
Timestamp: 2025-01-25T12:00:00Z
Name: Japan Network Issue
Message: We are investigating a network issue in Japan.
--------------------------------------------------------------------------------
```

---

## コードのカスタマイズ

### キーワードの変更
`search_word`変数を変更することで、異なるキーワードを検索できます。
```python
search_word = 'Voice'
```

### ページ数の変更
`for page in range(1, 5)`の範囲を変更することで、検索対象のページ数を調整可能です。

### 結果の保存
抽出結果をCSVやJSONに保存するようスクリプトを拡張できます。

---

## 注意点

1. **Twilioの利用規約**:
   本スクリプトはTwilioのステータスページをスクレイピングします。利用規約を遵守してください。

2. **HTML構造の変更**:
   TwilioのWebページ構造が変更されるとスクリプトが動作しなくなる場合があります。その場合はコードを調整してください。

---

## ライセンス
このプロジェクトはMITライセンスの下で提供されています。

---

## 貢献
バグ報告や機能提案は[Issues](https://github.com/your-repository/twilio-incident-search/issues)でお知らせください。
