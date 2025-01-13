# **Hand Tracking & Brightness Control System**  
### **YouTube Demonstration**  
   - Check out the live demonstration of this program on YouTube:  
👉 [Hand Tracking & Brightness Control System Demo](https://youtu.be/XUucfJl2FaQ?si=-RBzqRg3SmLqhigq)

### **Overview**  
The **Hand Tracking & Brightness Control System** is an innovative Python-based application that uses hand gestures to dynamically control the screen brightness. By tracking the distance between the thumb and index finger in real-time, it adjusts the brightness level seamlessly.  

This program integrates **computer vision**, **hand tracking technology**, and an **interactive GUI** for ease of use.

### **Features**  
1. **Real-Time Hand Tracking:**  
   - Detects and tracks hand landmarks using Mediapipe's hand solution.  
   - Displays landmarks and connections on the video feed.  

2. **Dynamic Brightness Control:**  
   - Adjusts the screen brightness based on the distance between the thumb and index finger.  
   - Uses smooth interpolation to translate hand gestures into brightness levels (0%–100%).  

3. **Interactive GUI:**  
   - Start and stop the video stream with buttons.  
   - Includes menu options for program exit and information about the application.  

4. **Easy-to-Understand Visuals:**  
   - Highlights landmarks and connections with green circles and lines on the frame.  

5. **User-Friendly Design:**  
   - Intuitive GUI layout with labels, buttons, and a menu bar for navigation.  

### **How It Works**  
#### **Brightness Adjustment Logic**  
- Detects the **thumb tip** and **index tip** positions using Mediapipe.  
- Calculates the Euclidean distance between the two points using the `hypot` function.  
- Maps this distance to a brightness level range (0 to 100) using NumPy interpolation (`np.interp`).  
- Updates the brightness in real-time using the **Screen Brightness Control** library (`sbc.set_brightness`).  

#### **Hand Tracking Visualization**  
- Each detected hand's landmarks and connections are drawn on the video feed.  
- Visual feedback (circles and lines) shows the distance used for brightness calculation.

#### **GUI Design**  
- **Tkinter** is used to design a clean and minimal interface:  
  - A **video feed area** displays real-time hand tracking.  
  - **Start Video** and **Stop Video** buttons allow users to control the webcam feed.  
  - A **menu bar** offers options like program exit and an "About" dialog box.  

### **Usage Guide**  
1. **Starting the Program:**  
   - Run the Python script to launch the GUI.  

2. **Using Hand Tracking and Brightness Control:**  
   - Click the **Start Video** button to activate the webcam.  
   - Bring your thumb and index finger into the camera view:  
     - **Closer Distance** → Lowers brightness.  
     - **Farther Distance** → Increases brightness.  

3. **Stopping the Video Feed:**  
   - Click the **Stop Video** button to turn off the webcam and stop detection.  

4. **Exiting the Program:**  
   - Use the "Exit" option in the **File** menu or close the program window.  

5. **Viewing About Information:**  
   - Access the "About" option in the **Help** menu for details about the application.  

### **System Requirements**  
- A functional webcam.  
- Python 3.x installed.  
- Compatible with Windows, macOS, or Linux.  

### **Code Summary**  
#### **Key Functions:**  
1. **`process_frame()`**  
   - Captures video frames and processes them for hand tracking.  
   - Detects thumb and index finger landmarks.  
   - Calculates distance and adjusts brightness dynamically.  

2. **`update_frame()`**  
   - Updates the video feed in the Tkinter window with the processed frames.  

3. **`start_video()` and `stop_video()`**  
   - Control video capture and processing.  

4. **`on_closing()`**  
   - Ensures resources like the webcam are released when the application is closed.  

5. **Menu Options:**  
   - "Exit" closes the application.  
   - "About" displays program details.  

### **Contribution**
Feel free to fork the repository, submit issues, or suggest improvements. Contributions are always welcome!

### **License**
This project is licensed under the MIT License. See the LICENSE file for details.

Developed by **A&J** as part of the Multimodal System.
