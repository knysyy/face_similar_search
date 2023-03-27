# face-similar-search
## 前提条件
poetryをインストール済み。

## 環境
```
poetry install
```

## 準備
static/targetに類似検索の対象にしたい画像を保存する。

queryに類似検索したい画像を保存する。

## 実行方法
- indexの作成

以下を実行する。
```
poetry run python ./face_similar_search/create_index.py
```

- 作成したindexをもとに検索

search_image.pyのファイル名を修正して以下を実行する。
類似順に5件ファイル名を出力する。
```
poetry run python ./face_similar_search/search_image.py
```
