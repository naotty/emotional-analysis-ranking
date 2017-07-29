# JAWS-UG沖縄 画像認識サービスを使ってみようハンズオン

---

# 今回のハンズオンについて

### 第6回JAWS-UG青森 で開催されたハンズオンの再演です。

こちらの資料のS3とLambda連携部分を変更したものを使用しています。
画像はスライドの方で表示します。

[emotional\-analysis\-ranking/handson\-slide\.md at master · jaws\-ug\-tohoku/emotional\-analysis\-ranking](https://github.com/jaws-ug-tohoku/emotional-analysis-ranking/blob/master/handson-slide.md)

----------


# 自己紹介
----------
- 石澤直人(Naoto Ishizawa)
- Heptagon inc.
- クラウドエンジニア

----------
- 福井 烈 (Takeshi Fukui)
- Piece of Cake, inc. (since 2015. 3 ~)
  - cakes ([https://cakes.mu](https://cakes.mu/))
  - note ([https://note.mu](https://note.mu/))
  - Railsで開発 & 運用
- Born in 弘前. Living in 弘前.
- リモートワーカー (会社は東京)
- 2児の父 👦👦


----------
# 今日やること
----------
## **AWS Lambda**  + **Amazon Rekognition** + **Kintone**を利用して**感情ランキングアプリ**を作る


----------
# 全体の構成と流れ



----------
# デモ
----------
# 各サービスの概要
----------
# Amazon S3とは
- ストレージサービス
- イレブンナイン(99.999999999%)の堅牢性
- 従量課金、データ総量無制限


----------
# AWS Lambdaとは
- サーバーのセットアップや管理なしでコードを実行できる (Function as a Serviceとも呼ばれる)
- コードの実行時間に対して料金が発生
- リクエスト数に応じて自動でスケール
- 特定のイベントをトリガーとして実行可能 ← 今回はS3に画像がアップロードをされたことをトリガーとする
- 従量課金


----------
# Amazon Rekognitionとは
- 深層学習(ディープラーニング)をベースとした画像認識サービス
  - 物体とシーンの検出 (Detect Labels)
  - 顔分析 (Detect Faces) ← 今回はこちらを利用する
  - 顔の比較 (Compare Faces)
  - 顔認識 (Moderate Images)
- 従量課金


----------
# kintoneとは


- プログラミングなしで業務に合わせたシステムを簡単に作れるサイボウズ社から提供されている業務アプリ構築サービス
- FileMaker(http://www.filemaker.com/jp/) やAccess(https://products.office.com/ja-jp/access) のクラウド版


----------
# e.g. 社員名簿を管理するアプリを作る

割愛


----------
# ハンズオン
----------

### ・AWS Lambdaファンクション実装
### ・s3にバケット作成
### ・s3とAWS Lambda連携
### ・s3に画像アップロード
### ・kintoneで結果発表！


----------
## AWS Lambdaファンクション実装
- lambdaを検索してページを開く


----------
## AWS Lambdaファンクション実装
- リージョンを `バージニア北部` に設定し、 `Lambda関数の作成` を選択する。

----------
## AWS Lambdaファンクション実装
- `Blank Function`を選択する。


----------
## AWS Lambdaファンクション実装
- 何もせず次へ。


----------
## AWS Lambdaファンクション実装
- `名前`,`説明`を入力する。`ランタイム`は`python2.7`を選択する。
- `コードエントリタイプ`は`S3からのファイルアップロード`を選択し、URLには `https://s3.amazonaws.com/jaws-ug-okinawa-20170725/emotional-analysis-ranking.zip` を入力する。


----------
## AWS Lambdaファンクション実装
- 環境変数を設定する
   - KINTONE_URL
   - KINTONE_APP_ID
   - KINTONE_API_TOKEN
- ロールを設定する
   - Rekognitionサービスへのアクセス権が必要
- メモリサイズとタイムアウトを設定する
   - メモリ: 512MB
   - タイムアウト: 1分


----------
## AWS Lambdaファンクション実装
- 設定を確認し、`関数の作成`を選択する。

----------
## s3にバケット作成
- s3のページを開く

----------
## s3にバケット作成
- バケット名を入力。リージョンは`バージニア北部`を選択し、`作成`を選択する。



----------
## s3とAWS Lambda連携
- 作成したLambdaの画面に移動して、`トリガー`を選択する。


----------
## s3とAWS Lambda連携
- `トリガーを追加`を選択する。


----------
## s3とAWS Lambda連携
- 点線の枠をクリックし、`S3`を選択する。
- バケットは先程作成したものを選択する。
- イベントタイプは`オブジェクトの作成(全て)`を選択する。
- 上記を選択したら、送信ボタンをクリックする。


----------
## s3に画像アップロード
- 自分の写真をs3にアップロード！
- 無い方は自撮りを！！
- `オブジェクト`、`アップロード`を選択してアップロードを行う。ファイル名は`Naoto_Ishizawa.jpg`のように自分の名前にする。
- `このオブジェクトにパブリック読み取りアクセス権限を付与する`を選択してアップロードする。


----------
## kintoneで結果発表！
----------
- 使用したLambda functionコード
  - https://github.com/jaws-ug-tohoku/emotional-analysis-ranking
