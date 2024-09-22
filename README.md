# Parking Space Counter

This project uses OpenCV to count the number of available parking spaces from a video feed. The system can detect and update the status of parking spots in real-time based on the number of cars occupying them.

## Project Overview
This project provides a simple parking space counter application using image processing techniques with OpenCV. It allows the user to:
- Define parking spots on a reference image.
- Count the available parking spots based on a video input feed.
- View results with real-time updates of available parking spots.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/TOUZOUZ-Adnane/Parking-Space-Counter.git
2. Navigate to the project directory:
   ```bash
   cd Parking-Space-Counter
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
## Installation
The project consists of two parts:
1. Parking Spot Selection:
- This part allows you to manually select the parking spots by clicking on an image. The coordinates of the selected spots are stored in a .pkl file for later use.
2. Parking Spot Detection:
- A video feed (e.g., from a camera) is analyzed to determine whether each parking spot is occupied. The available spots are highlighted in green, and occupied spots are shown in red.
## Key Libraries:
- **OpenCV**: A powerful library for image processing and computer vision tasks. It provides tools for reading images, processing them, and analyzing visual data.
- **Pickle**: A Python module for serializing and deserializing Python objects. In this project, it's used to save and load the positions of parking spots.
- **cvzone**: A library that simplifies the use of OpenCV for tasks like displaying text and drawing shapes on images.
## Usage:
1. Parking Spot Selection:
To mark parking spots on an image:
- Run the script that allows manual selection of spots:
  ```bash
  python ParckingSpacePicker.py
- Left-click on the image to add a parking spot, and right-click to remove one.
- The coordinates will be saved in 'assets/positions.pkl'.
2. Parking Spot Detection:
To start the parking space counter:
- Run the detection script:
  ```bash
  python main.py
- The available parking spots will be shown on the video with real-time updates.
## Contact
If you have any questions or need further assistance, feel free to contact me:

- **LinkedIn**: [Adnane Touzouz](https://www.linkedin.com/in/adnane-touzouz/)
- **Email**: adnane.touzouz.ta@gmail.com

