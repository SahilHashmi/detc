import cv2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from .utils import detect_vehicles, detect_license_plates, detect_all

@api_view(['POST'])
def detect_vehicles_view(request):
    if 'file' not in request.FILES:
        return Response({"error": "No file uploaded"}, status=400)
    
    image_file = request.FILES['file']
    image_path = default_storage.save(image_file.name, image_file)
    
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Detect vehicles
    vehicles = detect_vehicles(image)
    
    return Response({"vehicles": vehicles}, status=200)


@api_view(['POST'])
def detect_license_plate_view(request):
    if 'file' not in request.FILES:
        return Response({"error": "No file uploaded"}, status=400)
    
    image_file = request.FILES['file']
    image_path = default_storage.save(image_file.name, image_file)
    
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Detect license plates
    license_plates = detect_license_plates(image)
    
    return Response({"license_plates": license_plates}, status=200)


@api_view(['POST'])
def detect_all_view(request):
    if 'file' not in request.FILES:
        return Response({"error": "No file uploaded"}, status=400)
    
    image_file = request.FILES['file']
    image_path = default_storage.save(image_file.name, image_file)
    
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Detect vehicles and license plates
    detection_results = detect_all(image)
    
    return Response(detection_results, status=200)
