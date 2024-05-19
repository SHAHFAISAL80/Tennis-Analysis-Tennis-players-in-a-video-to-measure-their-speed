from ultralytics import YOLO 

model = YOLO(r'F:\tennis project\tennis_analysis-main\models\yolov8x.pt')

result = model.track(r'F:\tennis project\tennis_analysis-main\input_videos\input_video.mp4',conf=0.2, save=True)
# print(result)
# print("boxes:")
# for box in result[0].boxes:
#     print(box)