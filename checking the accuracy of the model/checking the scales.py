from ultralytics import YOLO

model = YOLO("C:\\Nikita\\Desktop\\[]\\job\\RUNы\\DS1.7 yolon-100\\runs\\segment\\train\\weights\\last.pt")  # load a custom model

source = "C:\\Users\\Desktop\\for pred\\online-audio-convert.com.mp4"
# Run inference on the source
model.predict(source="C:\\Nikita\\Desktop\\for pred\\online-audio-convert.com.mp4", save=True)  # predict on the video

results = model
