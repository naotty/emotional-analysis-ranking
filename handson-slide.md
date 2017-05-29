# jawsug青森ハンズオン


----------


# 自己紹介
----------
- 石澤直人(Naoto Ishizawa)
- Heptagon inc.
- クラウドエンジニア
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495731505086_image.png

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
https://d2mxuefqeaa7sj.cloudfront.net/s_1CBAD57ACB43AB3D17B6A0A83BAD37BBCB739ADF637C37F0C7A259E06C187F0F_1495657541795_+2017-05-25+5.25.19.png

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


1. **アプリストアより社員名簿を選択**
https://d2mxuefqeaa7sj.cloudfront.net/s_1CBAD57ACB43AB3D17B6A0A83BAD37BBCB739ADF637C37F0C7A259E06C187F0F_1495363192151__2017-05-21_19_35_15.png



2. **「このアプリを追加」を押下**
https://d2mxuefqeaa7sj.cloudfront.net/s_1CBAD57ACB43AB3D17B6A0A83BAD37BBCB739ADF637C37F0C7A259E06C187F0F_1495369543908__2017-05-21_19_42_02.png

3. **アプリに社員名簿が追加されている**
https://d2mxuefqeaa7sj.cloudfront.net/s_1CBAD57ACB43AB3D17B6A0A83BAD37BBCB739ADF637C37F0C7A259E06C187F0F_1495369834106__2017-05-21_19_48_55.png

4. **社員情報を入力して保存**
https://d2mxuefqeaa7sj.cloudfront.net/s_1CBAD57ACB43AB3D17B6A0A83BAD37BBCB739ADF637C37F0C7A259E06C187F0F_1495369602828__2017-05-21_19_44_53.png

5. **社員情報登録完了**
https://d2mxuefqeaa7sj.cloudfront.net/s_1CBAD57ACB43AB3D17B6A0A83BAD37BBCB739ADF637C37F0C7A259E06C187F0F_1495369667402_+2017-05-21+19.48.21.png

----------
# もっと詳しく知りたい方は
## この後 **15:00 ~ のkintone Café 八戸 Vol.1** にて

(http://kintonecafe.com/2017/04/2017512-kintone-cafe-hachinohe-vol-1/)

----------
# ハンズオン
----------
- AWS Lambdaファンクション実装
- s3にバケット作成
- s3とAWS Lambda連携
- s3に画像アップロード
- kintoneで結果発表！


----------
## AWS Lambdaファンクション実装
- lambdaを検索してページを開く
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495777078570_image.png

----------
## AWS Lambdaファンクション実装
- リージョンを `バージニア北部` に設定し、 `Lambda関数の作成` を選択する。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495777357222_image.png

----------
## AWS Lambdaファンクション実装
- `Blank Function`を選択する。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495777483165_image.png

----------
## AWS Lambdaファンクション実装
- 何もせず次へ。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495777540885_image.png

----------
## AWS Lambdaファンクション実装
- `名前`,`説明`を入力する。`ランタイム`は`python2.7`を選択する。
- `コードエントリタイプ`は`S3からのファイルアップロード`を選択し、URLには `https://s3.amazonaws.com/jawsug-aomori-sample-code/emotional-analysis-ranking.zip` を入力する。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495778088727_image.png



----------
## AWS Lambdaファンクション実装
- 環境変数を設定する
- ロールを設定する
- メモリサイズとタイムアウトを設定する
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495779174254_image.png

----------
## AWS Lambdaファンクション実装
- 設定を確認し、`関数の作成`を選択する。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495779881231_image.png

https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495779900067_image.png

----------
## s3にバケット作成
- s3のページを開く
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495780174050_image.png

----------
## s3にバケット作成
- バケット名を入力。リージョンは`バージニア北部`を選択し、`作成`を選択する。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495795864049_image.png



----------
## s3とAWS Lambda連携
- 作成作成したバケットを選択する。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495797453164_image.png

----------
## s3とAWS Lambda連携
- `プロパティ`を選択する。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495797501682_image.png

----------
## s3とAWS Lambda連携
- 画面下部の`Events`を選択する。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495797542319_image.png

----------
## s3とAWS Lambda連携
- `名前`を入力。イベントは`ObjectCreate(All)`を選択。送信先を`Lambda関数`とし、先ほど作成したLambda関数を選択して`保存`する。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495797630815_image.png

----------
## s3に画像アップロード
- 自分の写真をs3にアップロード！
- 無い方は自撮りを！！
- `オブジェクト`、`アップロード`を選択してアップロードを行う。ファイル名は`Naoto_Ishizawa.jpg`のように自分の名前にする。
https://d2mxuefqeaa7sj.cloudfront.net/s_8D11739D38D180335B4D08A923AA714991D4C98D5CDAF51BB04977DC2635390D_1495797886993_image.png



----------
## kintoneで結果発表！
----------
- 使用したLambda functionコード
  - https://github.com/jaws-ug-tohoku/emotional-analysis-ranking

