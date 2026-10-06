Image Processing, OpenCV & YOLO

A collection of Python projects focused on image processing, data visualization, computer vision, and object detection using Matplotlib, Plotly, OpenCV, and YOLO.

This repository contains practical programs ranging from basic image visualization and processing to real-time computer vision and YOLO-based object detection.

🚀 Technologies Used
🐍 Python
📊 Matplotlib
📈 Plotly
👁️ OpenCV
🤖 YOLO
🔢 NumPy
🧠 Computer Vision
🎯 Object Detection
📂 Repository Structure
Image-Processing/
│
├── Matplotlib/
│   └── Matplotlib programs and visualization
│
├── Open Cv/
│   └── OpenCV image processing and computer vision programs
│
├── Plotly/
│   └── Interactive visualization programs
│
└── YOLO/
    └── YOLO object detection programs
📊 1. Matplotlib

The Matplotlib section contains Python programs for creating visualizations and working with image-related data.

Topics
Line plots
Bar charts
Scatter plots
Histograms
Pie charts
Subplots
Image visualization
Plot customization

Example:

import matplotlib.pyplot as plt

plt.imshow(image)
plt.axis("off")
plt.show()
📈 2. Plotly

The Plotly section contains interactive visualization programs.

Topics
Interactive charts
Line charts
Bar charts
Scatter plots
Histograms
Pie charts
Interactive image/data visualization

Plotly is useful for creating interactive visualizations that can be explored directly by the user.

👁️ 3. OpenCV

The Open Cv section focuses on computer vision and image processing using OpenCV.

Topics
Reading images
Displaying images
Saving images
Image resizing
Image cropping
Image rotation
Image translation
Color conversion
Grayscale images
Thresholding
Edge detection
Contours
Video processing
Webcam processing
Face detection
Object detection

Example:

import cv2

image = cv2.imread("image.jpg")

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
🤖 4. YOLO

The YOLO section contains programs for object detection using YOLO (You Only Look Once).

YOLO can be used to detect multiple objects in images, videos, and real-time webcam streams.

Topics
YOLO object detection
Image detection
Video detection
Webcam detection
Bounding boxes
Class labels
Confidence scores
Multiple-object detection
Real-time object detection
OpenCV + YOLO integration

Typical detection workflow:

Image / Video / Webcam
          ↓
        YOLO
          ↓
 Object Detection
          ↓
Bounding Boxes
          ↓
Class Labels
          ↓
Confidence Scores
🔥 Computer Vision Workflow

The projects in this repository demonstrate a progression from basic visualization to computer vision and AI-based object detection.

Python
  ↓
NumPy
  ↓
Matplotlib / Plotly
  ↓
Image Processing
  ↓
OpenCV
  ↓
Computer Vision
  ↓
YOLO
  ↓
Object Detection
🛠️ Installation

Clone the repository:

git clone https://github.com/sruthilayaperla/Image-Processing.git

Move into the repository:

cd Image-Processing

Install the required Python packages:

pip install numpy matplotlib plotly opencv-python ultralytics

Some programs may require additional Python packages depending on the specific project.

▶️ How to Run

Navigate to the required folder.

For example:

cd "Open Cv"

Run a Python program:

python program.py

For YOLO programs:

cd YOLO
python program.py

Make sure the required model files and input images/videos are available before running the program.

📸 Project Output

The OpenCV and YOLO projects can be used for applications such as:

Image analysis
Face detection
Object detection
Video analysis
Webcam applications
Real-time computer vision
Automated visual inspection

Screenshots and demonstration GIFs can be added here as the projects are expanded.

🎯 Learning Objectives

This repository is designed to develop practical skills in:

Python programming
Image processing
Data visualization
Computer vision
OpenCV
YOLO
Object detection
Real-time video processing
AI-based visual applications
💡 Future Projects

Planned computer vision projects include:

🚗 Vehicle Detection
🚦 Traffic Object Detection
👤 Face Detection
✋ Hand Gesture Recognition
📱 Mobile Phone Detection
🧍 Person Detection
🔢 Object Counting
🎥 Real-Time Webcam Detection
🚘 Number Plate Detection
🏃 People Tracking
👨‍💻 Author

