# Neon Smart Traffic Management System

## Description
The **Neon Smart Traffic Management System** uses computer vision and AI to monitor and manage traffic on roads. It detects moving vehicles and categorizes traffic based on its density. The system is designed to provide real-time insights into traffic conditions, helping authorities optimize traffic management and reduce congestion. The system also supports video recording of detected traffic, offering a record of traffic flow over time.

### Key Features:
- **Traffic Density Detection:** Monitors vehicle movement to classify lanes as light, moderate, or heavy traffic.
- **Dynamic Lane Categorization:** Automatically updates lane status based on real-time traffic data.
- **Video Recording:** Records video when movement is detected, allowing for future analysis.
- **Real-Time Traffic Monitoring:** Displays real-time traffic data with timestamped insights.

## Features:
- Traffic detection using OpenCV's frame differencing method.
- Classification of traffic density into light, moderate, or heavy based on vehicle count.
- Automatic recording of traffic when movement is detected.
- Real-time visual display of the traffic condition.
- Customizable threshold for movement detection to suit different traffic environments.
  
## Installation Steps

### Dependencies:
- Python 3.x
- OpenCV (`opencv-python` package)
- NumPy (for efficient mathematical operations)

### To set up the project:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/Neon-Smart-Traffic-Management-System.git
   cd Neon-Smart-Traffic-Management-System
