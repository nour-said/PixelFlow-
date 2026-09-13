# PixelFlow — Hand-Controlled Pixel Manipulation

PixelFlow is an interactive computer vision project that combines real-time hand tracking with visual manipulation.

The project uses **MediaPipe** to detect hand gestures, **OSC** to send the detected controls from Python to **TouchDesigner**, and **GLSL** to process the image in real time.

## Features

* Real-time hand tracking using MediaPipe
* Finger-count based color manipulation
* Grayscale, Red, Green, Blue, and RGB modes
* Hand-controlled pixel swirl effect
* Gesture-based reset
* Real-time OSC communication
* GLSL-based image processing

## Interaction

### Left Hand — Color Control

| Fingers | Effect    |
| ------- | --------- |
| 0       | Grayscale |
| 1       | Red       |
| 2       | Green     |
| 3       | Blue      |
| 5       | RGB       |

### Right Hand — Pixel Swirl

* **Thumb + index finger angle** → Controls the pixel swirl
* **Closed hand** → Resets the image to its original state

The image remains fixed while the pixels are manipulated around the center, creating a real-time swirl effect.

## System Pipeline

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
Real-Time Image Manipulation
```

## Project Structure

```text
PixelFlow/
├── python/
│   ├── hand_tracking.py
│   └── config.py
│
├── touchdesigner/
│   └── PixelFlow.toe
│
├── assets/
│
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/nour-said/PixelFlow-.git
cd PixelFlow-
```

### 2. Set up the Python environment

Create and activate a virtual enviro
