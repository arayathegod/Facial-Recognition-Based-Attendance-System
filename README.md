# Facial Recognition Attendance System

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Library](https://img.shields.io/badge/Library-face__recognition-green)

This is a simple Python-based facial recognition attendance system. It captures video from your webcam, recognizes faces, and marks the attendance of known individuals in a CSV file. The system is built using the `face_recognition` library and OpenCV.

## Features

- Recognizes known individuals in real-time using your webcam.
- Captures the current date and time for attendance records.
- Stores attendance data in CSV files, with one file generated per day.

## Prerequisites

Before running the system, make sure you have the following prerequisites installed:

- Python 3.7 or higher
- `face_recognition` library
- OpenCV library

You can install the required libraries using `pip`:

```bash
pip install cmake
pip install face_recognition
pip install opencv-python

Usage
Clone the repository to your local machine.
git clone https://github.com/yourusername/facial-recognition-attendance.git

Navigate to the project directory.
cd facial-recognition-attendance

Run the main script.
python main.py

The system will capture video from your webcam and recognize known faces. The recognized individuals will be marked as present in the generated CSV file for the current date.

To exit the system, press the 'q' key.

Configuration
You can configure known faces and names by adding image files and encodings in the faces directory.
Data
Attendance records are stored in CSV files, with one file generated for each day. Each CSV file contains the names of individuals and the time they were marked as present.

Author
Sudiksha Sharma

License
This project is licensed under the MIT License.


