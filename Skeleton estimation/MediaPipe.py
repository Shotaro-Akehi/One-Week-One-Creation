import cv2
import mediapipe as mp

# MediaPipeのポーズ推定モジュールをインスタンス化
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Webカメラを開く
cap = cv2.VideoCapture(0)

# カメラが開けない場合のエラーハンドリング
if not cap.isOpened():
    print("Error: Camera not found.")
    exit()

# 画像処理ループ
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # BGRからRGBに変換（MediaPipeはRGB形式を期待するため）
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # MediaPipeで骨格推定を実行
    results = pose.process(rgb_frame)

    # 結果を描画
    if results.pose_landmarks:
        # 骨格のランドマークを描画
        mp.solutions.drawing_utils.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # 画像を表示
    cv2.imshow("Pose Estimation", frame)

    # 'q'を押すと終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()

