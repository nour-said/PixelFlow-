# PixelFlow — Hand-Controlled Pixel Manipulation

PixelFlow is an interactive computer vision project that combines hand tracking with real-time image manipulation.

The project uses **MediaPipe** to detect hand gestures, **OSC** to send the detected controls to **TouchDesigner**, and **GLSL** to process the image in real time.

## Features

* Real-time hand tracking using MediaPipe
* Finger-count based color manipulation
* Grayscale, Red, Green, Blue, and RGB modes
* Hand-controlled pixel swirl effect
* Gesture-based reset
* Real-time communication using OSC
* Real-time image processing with GLSL

## Interaction

### Left Hand — Color Control

| Fingers | Effect       |
| ------- | ------------ |
| 0       | Grayscale    |
| 1       | Red          |
| 2       | Green        |
| 3       | Blue         |
| 5       | Original RGB |

### Right Hand — Pixel Swirl

* **Thumb + index finger angle** → Controls the pixel swirl
* **Closed hand** → Resets the image to its original state

The image itself remains fixed while the pixels are manipulated around the center, creating a localized swirl effect.

## How It Works

```text
Camera
   ↓
MediaPipe
   ↓
Hand Tracking & Gesture Detection
   ↓
OSC
   ↓
TouchDesigner
   ↓
GLSL
   ↓
Real-Time Pixel Manipulation
```

## Technologies

* Python
* OpenCV
* MediaPipe
* OSC
* TouchDesigner
* GLSL

## Project Structure

```text
PixelFlow/
├── python/
│   ├── hand_tracking.py
│   └── config.py
├── touchdesigner/
├── assets/
│   └── models/
│       └── hand_landmarker.task
├── README.md
└── .gitignore
```

## About the Project

PixelFlow is the first stage of my **Interactive Computer Vision** project series, exploring how computer vision can be connected to real-time visual interaction and creative coding.
