import cv2
import mediapipe as mp
import base64
from io import BytesIO
from PIL import Image
import time
import os
import threading
from tqdm import tqdm
import logging
from openai import OpenAI
import datetime

# 获取当前脚本文件所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 配置日志记录
log_file_path = os.path.join(script_dir, 'face_detection_log.log')
if not os.path.exists(log_file_path):
    with open(log_file_path, 'w') as f:
        pass

# 设置日志记录器
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 移除默认的所有处理程序
for handler in logger.handlers[:]:
    logger.removeHandler(handler)

# 创建文件处理程序并添加到日志记录器
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# 设置OpenAI API的基础URL和API密钥
BASE_URL = os.getenv("OPENAI_API_BASE", "http://8.130.209.127:8000/v1")
API_KEY = "51d5350a075931c7.fa2eab916c0705fd6b120434ddd98e96"

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

# 初始化MediaPipe人脸检测模块
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)

# 打开摄像头
cap = cv2.VideoCapture(0)

def frame_to_base64(frame):
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    base64_url = f"data:image/jpeg;base64,{img_str}"
    return base64_url

def request_openai(base64_url, response_ready_event):
    try:
        result = client.chat.completions.create(
            model="660d7a0614c0acd012a10dc4",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "file",
                            "file_url": {
                                "url": base64_url
                            }
                        },
                        {
                            "type": "text",
                            "text": "判断画面"
                        }
                    ]
                }
            ],
            stream=False
        )
        response_content = result.choices[0].message.content
        logging.info("OpenAI response: %s", response_content)
        print("\nOpenAI response:\n", response_content)

        # 记录日志文件生成的时间
        log_file_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Log file generated at: {log_file_time}")
    except Exception as e:
        logging.error("Error while requesting OpenAI: %s", e)
    finally:
        response_ready_event.set()

last_base64_time = time.time()
interval = 60
response_ready_event = None
main_progress_bar = tqdm(total=interval, desc="Main Progress", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} seconds', leave=False)
response_progress_bar = tqdm(total=interval, desc="Response Progress", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} seconds', leave=False)

logging.info("Starting face detection application.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        logging.error("Failed to read frame from camera.")
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)

    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(frame, detection)

    current_time = time.time()
    elapsed_time = current_time - last_base64_time

    main_progress_bar.n = elapsed_time
    main_progress_bar.refresh()

    if elapsed_time >= interval:
        base64_url = frame_to_base64(frame)
        logging.info("Generated base64 URL.")
        
        response_ready_event = threading.Event()
        request_thread = threading.Thread(target=request_openai, args=(base64_url, response_ready_event))
        request_thread.start()
        logging.info("Started thread to request OpenAI.")
        
        last_base64_time = current_time
        main_progress_bar.reset()

    if response_ready_event and not response_ready_event.is_set():
        response_elapsed_time = current_time - last_base64_time
        response_progress_bar.n = response_elapsed_time
        response_progress_bar.refresh()

    cv2.imshow('Real-Time Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        logging.info("Exiting application.")
        break

cap.release()
cv2.destroyAllWindows()
main_progress_bar.close()
response_progress_bar.close()
logging.info("Application closed.")