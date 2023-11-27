from ultralytics import YOLO
import torch
import torchvision


if __name__ == '__main__':
    model = YOLO('yolov8n.pt')
    model.train(data="C:\\Users\\Nikita\\Desktop\\[]\\job\\dataset\\dataset_2.7\\data.yaml", epochs=60, classes = [4])
    results = model("C:\\Users\\Nikita\\Desktop\\для предикта\\2023-10-31_22-34-32.png", save=True)