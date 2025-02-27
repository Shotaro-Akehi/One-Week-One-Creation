# MediaPipeを使った骨格推定
## 環境準備
骨格推定を行うために必要なライブラリのインストールを行います。mediapipeをインストール（仮想環境推奨）
```ruby:ライブラリのインストール
pip3 install mediapipe
```
## 実装
以下のコマンドを実行する
### 全身推定
```ruby:全身
python3 MediaPipe.py --pattern pose
```
### 手推定
```ruby:手
python3 MediaPipe.py --pattern pose_hands
```
### 顔推定
```ruby:顔
python3 MediaPipe.py --pattern pose_face
```
