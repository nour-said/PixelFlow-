# PixelFlow — Hand-Controlled Pixel Manipulation

An interactive computer vision experiment using Python,
MediaPipe, TouchDesigner, OSC, and GLSL.

## Features

- Hand tracking with MediaPipe
- Finger-count based color manipulation
- Grayscale, Red, Green, Blue, and RGB modes
- Hand-controlled pixel swirl distortion
- Gesture-based reset
- Real-time OSC communication
- GLSL-based image processing

## Interaction

### Left Hand
0 fingers → Grayscale
1 finger → Red
2 fingers → Green
3 fingers → Blue
5 fingers → RGB

### Right Hand
Hand angle → Controls pixel swirl
Closed hand → Resets the distortion

## Pipeline

Camera
↓
MediaPipe
↓
Hand Gestures
↓
OSC
↓
TouchDesigner
↓
GLSL
↓
Interactive Image

## Technologies

Python
MediaPipe
OpenCV
TouchDesigner
GLSL
OSC
