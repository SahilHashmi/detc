# import cv2
# import numpy as np
# from ultralytics import YOLO

# # Load the YOLOv8 vehicle detection model
# vehicle_model = YOLO("D:/techno/vehicle_detection/models/yolov8n.pt")

# # Load the license plate detection model (this could also be YOLO or any pre-trained model)
# license_plate_model = YOLO("D:/techno/vehicle_detection/models/license_plate_detector.pt")

# # Function to detect vehicles
# def detect_vehicles(image):
#     results = vehicle_model(image)
#     vehicles = []
#     for result in results.xyxy[0]:  # xyxy format: [x_min, y_min, x_max, y_max, confidence]
#         if result[5] == 2:  # Class '2' corresponds to vehicles in YOLO
#             vehicles.append({
#                 "x_min": int(result[0]),
#                 "y_min": int(result[1]),
#                 "x_max": int(result[2]),
#                 "y_max": int(result[3]),
#                 "confidence": float(result[4]),
#             })
#     return vehicles

# # Function to detect license plates in the detected vehicles
# def detect_license_plates(image):
#     results = license_plate_model(image)
#     license_plates = []
#     for result in results.xyxy[0]:  # xyxy format
#         license_plates.append({
#             "x_min": int(result[0]),
#             "y_min": int(result[1]),
#             "x_max": int(result[2]),
#             "y_max": int(result[3]),
#             "confidence": float(result[4]),
#         })
#     return license_plates

# # Function to detect both vehicles and license plates
# def detect_all(image):
#     vehicles = detect_vehicles(image)
#     license_plates = detect_license_plates(image)
#     return {"vehicles": vehicles, "license_plates": license_plates}


# import cv2
# import numpy as np
# from ultralytics import YOLO

# # Load the YOLOv8 vehicle detection model
# vehicle_model = YOLO("D:/techno/vehicle_detection/models/yolov8n.pt")

# # Load the license plate detection model (this could also be YOLO or any pre-trained model)
# license_plate_model = YOLO("D:/techno/vehicle_detection/models/license_plate_detector.pt")

# # Function to detect vehicles
# def detect_vehicles(image):
#     results = vehicle_model(image)
#     vehicles = []
#     for result in results[0].boxes:  # Access the 'boxes' attribute
#         if result.cls == 2:  # Class '2' corresponds to vehicles in YOLO
#             vehicles.append({
#                 "x_min": int(result.xyxy[0]),
#                 "y_min": int(result.xyxy[1]),
#                 "x_max": int(result.xyxy[2]),
#                 "y_max": int(result.xyxy[3]),
#                 "confidence": float(result.conf),
#             })
#     return vehicles

# # Function to detect license plates in the detected vehicles
# def detect_license_plates(image):
#     results = license_plate_model(image)
#     license_plates = []
#     for result in results[0].boxes:  # Access the 'boxes' attribute
#         license_plates.append({
#             "x_min": int(result.xyxy[0]),
#             "y_min": int(result.xyxy[1]),
#             "x_max": int(result.xyxy[2]),
#             "y_max": int(result.xyxy[3]),
#             "confidence": float(result.conf),
#         })
#     return license_plates

# # Function to detect both vehicles and license plates
# def detect_all(image):
#     vehicles = detect_vehicles(image)
#     license_plates = detect_license_plates(image)
#     return {"vehicles": vehicles, "license_plates": license_plates}

# import cv2
# import numpy as np
# from ultralytics import YOLO

# # Load the YOLOv8 vehicle detection model
# vehicle_model = YOLO("D:/techno/vehicle_detection/models/yolov8n.pt")

# # Load the license plate detection model (this could also be YOLO or any pre-trained model)
# license_plate_model = YOLO("D:/techno/vehicle_detection/models/license_plate_detector.pt")

# # Function to detect vehicles
# def detect_vehicles(image):
#     results = vehicle_model(image)
#     vehicles = []
#     for result in results[0].boxes:  # Access the 'boxes' attribute
#         if result.cls == 2:  # Class '2' corresponds to vehicles in YOLO
#             vehicles.append({
#                 "x_min": int(result.xyxy[0].item()),  # Use .item() to convert tensor to scalar
#                 "y_min": int(result.xyxy[1].item()),  # Use .item() to convert tensor to scalar
#                 "x_max": int(result.xyxy[2].item()),  # Use .item() to convert tensor to scalar
#                 "y_max": int(result.xyxy[3].item()),  # Use .item() to convert tensor to scalar
#                 "confidence": float(result.conf.item()),  # Use .item() for the confidence
#             })
#     return vehicles

# # Function to detect license plates in the detected vehicles
# def detect_license_plates(image):
#     results = license_plate_model(image)
#     license_plates = []
#     for result in results[0].boxes:  # Access the 'boxes' attribute
#         license_plates.append({
#             "x_min": int(result.xyxy[0].item()),  # Use .item() to convert tensor to scalar
#             "y_min": int(result.xyxy[1].item()),  # Use .item() to convert tensor to scalar
#             "x_max": int(result.xyxy[2].item()),  # Use .item() to convert tensor to scalar
#             "y_max": int(result.xyxy[3].item()),  # Use .item() to convert tensor to scalar
#             "confidence": float(result.conf.item()),  # Use .item() for the confidence
#         })
#     return license_plates

# # Function to detect both vehicles and license plates
# def detect_all(image):
#     vehicles = detect_vehicles(image)
#     license_plates = detect_license_plates(image)
#     return {"vehicles": vehicles, "license_plates": license_plates}

# 

# 

# import torch  # Ensure torch is imported
# import cv2
# import numpy as np
# from ultralytics import YOLO

# # Load the YOLOv8 vehicle detection model
# vehicle_model = YOLO("D:/techno/vehicle_detection/models/yolov8n.pt")

# # Load the license plate detection model (this could also be YOLO or any pre-trained model)
# license_plate_model = YOLO("D:/techno/vehicle_detection/models/license_plate_detector.pt")

# # Function to detect vehicles
# def detect_vehicles(image):
#     results = vehicle_model(image)
#     vehicles = []
#     for result in results[0].boxes:  # Access the 'boxes' attribute
#         if result.cls == 2:  # Class '2' corresponds to vehicles in YOLO
#             # Convert each element of result.xyxy tensor separately to scalar
#             x_min = result.xyxy[0].item() if isinstance(result.xyxy[0], torch.Tensor) else result.xyxy[0]
#             y_min = result.xyxy[1].item() if isinstance(result.xyxy[1], torch.Tensor) else result.xyxy[1]
#             x_max = result.xyxy[2].item() if isinstance(result.xyxy[2], torch.Tensor) else result.xyxy[2]
#             y_max = result.xyxy[3].item() if isinstance(result.xyxy[3], torch.Tensor) else result.xyxy[3]
            
#             vehicles.append({
#                 "x_min": int(x_min),  # Convert to int after extracting the scalar
#                 "y_min": int(y_min),
#                 "x_max": int(x_max),
#                 "y_max": int(y_max),
#                 "confidence": float(result.conf.item()) if isinstance(result.conf, torch.Tensor) else float(result.conf),
#             })
#     return vehicles

# # Function to detect license plates in the detected vehicles
# def detect_license_plates(image):
#     results = license_plate_model(image)
#     license_plates = []
#     for result in results[0].boxes:  # Access the 'boxes' attribute
#         # Convert each element of result.xyxy tensor separately to scalar
#         x_min = result.xyxy[0].item() if isinstance(result.xyxy[0], torch.Tensor) else result.xyxy[0]
#         y_min = result.xyxy[1].item() if isinstance(result.xyxy[1], torch.Tensor) else result.xyxy[1]
#         x_max = result.xyxy[2].item() if isinstance(result.xyxy[2], torch.Tensor) else result.xyxy[2]
#         y_max = result.xyxy[3].item() if isinstance(result.xyxy[3], torch.Tensor) else result.xyxy[3]
        
#         license_plates.append({
#             "x_min": int(x_min),  # Convert to int after extracting the scalar
#             "y_min": int(y_min),
#             "x_max": int(x_max),
#             "y_max": int(y_max),
#             "confidence": float(result.conf.item()) if isinstance(result.conf, torch.Tensor) else float(result.conf),
#         })
#     return license_plates

# # Function to detect both vehicles and license plates
# def detect_all(image):
#     vehicles = detect_vehicles(image)
#     license_plates = detect_license_plates(image)
#     return {"vehicles": vehicles, "license_plates": license_plates}


import torch  # Ensure torch is imported
import cv2
import numpy as np
from ultralytics import YOLO

# Load the YOLOv8 vehicle detection model
vehicle_model = YOLO("D:/techno/vehicle_detection/models/yolov8n.pt")

# Load the license plate detection model (this could also be YOLO or any pre-trained model)
license_plate_model = YOLO("D:/techno/vehicle_detection/models/license_plate_detector.pt")

# Function to detect vehicles
def detect_vehicles(image):
    results = vehicle_model(image)
    vehicles = []
    for result in results[0].boxes:  # Access the 'boxes' attribute
        if result.cls == 2:  # Class '2' corresponds to vehicles in YOLO
            # Convert xyxy to numpy and extract the individual coordinates
            xyxy = result.xyxy.cpu().numpy()  # Convert tensor to numpy array
            x_min, y_min, x_max, y_max = xyxy[0]  # Extract coordinates
            
            vehicles.append({
                "x_min": int(x_min),
                "y_min": int(y_min),
                "x_max": int(x_max),
                "y_max": int(y_max),
                "confidence": float(result.conf.item()) if isinstance(result.conf, torch.Tensor) else float(result.conf),
            })
    return vehicles

# Function to detect license plates in the detected vehicles
def detect_license_plates(image):
    results = license_plate_model(image)
    license_plates = []
    for result in results[0].boxes:  # Access the 'boxes' attribute
        # Convert xyxy to numpy and extract the individual coordinates
        xyxy = result.xyxy.cpu().numpy()  # Convert tensor to numpy array
        x_min, y_min, x_max, y_max = xyxy[0]  # Extract coordinates
        
        license_plates.append({
            "x_min": int(x_min),
            "y_min": int(y_min),
            "x_max": int(x_max),
            "y_max": int(y_max),
            "confidence": float(result.conf.item()) if isinstance(result.conf, torch.Tensor) else float(result.conf),
        })
    return license_plates

# Function to detect both vehicles and license plates
def detect_all(image):
    vehicles = detect_vehicles(image)
    license_plates = detect_license_plates(image)
    return {"vehicles": vehicles, "license_plates": license_plates}
