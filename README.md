# Helmet Safety Detection using YOLOv10
## Hướng dẫn chạy ứng dụng
Chạy file train_model.ipynb để train model với custom dataset
Sau khi train model xong tải file theo đường dẫn 'runs/detect/train/weights/best.pt' về
Đổi tên file 'best.pt' thành 'model.pt'
Sử dụng lệnh sau để chạy ứng dụng streamlit:
`streamlit run helmet_safety_detection.py`