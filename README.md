# AI-Quality-Control-Inspector

"Computer Vision based defect detection system"[cite: 2]

This project automates quality control on manufacturing assembly lines. By leveraging Computer Vision and AI, the system identifies defective products (such as cracks, scratches, missing labels, or incomplete fills) in real-time, matching the speed and precision required for industrial-level deployment.

## Features
* **Real-Time Defect Detection:** Processes video feeds from overhead cameras instantly to flag anomalies.
* **High Accuracy Classification:** Utilizes state-of-the-art object detection models to differentiate between standard and defective items.
* **Automated Sorting Readiness:** Designed to output signals that can trigger hardware rejection mechanisms (like servo-motor pushers or robotic arms) on a conveyor belt.

## Tech Stack
* **Language:** Python
* **Computer Vision:** OpenCV
* **AI/Deep Learning Model:** YOLO (You Only Look Once) 
* **Target Hardware:** PC, Raspberry Pi, or NVIDIA Jetson Nano

## Prerequisites
Ensure you have the following installed on your system:
* Python 3.8+
* Pip (Python package installer)
* A working webcam or industrial vision camera

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/shubhamm2035-dotcom/AI-Quality-Control-Inspector.git](https://github.com/shubhamm2035-dotcom/AI-Quality-Control-Inspector.git)
   Navigate to the project directory:

Bash
cd AI-Quality-Control-Inspector
Install the required dependencies:

Bash
pip install -r requirements.txt
Usage
Connect your camera or set up your video file source in the configuration.

Run the main detection script:

Bash
python main.py
The system will open a video window displaying real-time bounding boxes around detected defects. Press q to terminate the application safely.

Author
Shubham Kakasaheb Gaikwad
