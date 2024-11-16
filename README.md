# Image Recognition for Quality Control  

This repository showcases a Flask-based web application designed to enhance product quality control by identifying and highlighting visible defects or impurities in images of products. By leveraging the YOLO model for object detection, the app provides an efficient and accurate solution for real-time defect detection.  

## Features  
- **AI-Powered Detection**: Utilizes the YOLO model to identify and highlight defects in product images.  
- **Web-Based Interface**: Built with Flask and styled with CSS, providing a clean, user-friendly experience.  
- **Streamlined Workflow**: Easy-to-use process for uploading and analyzing images in just a few clicks.  
- **Dynamic Results**: Displays both the original and defect-annotated images for quick and clear insights.  

## How It Works  
1. **Upload**: The user uploads an image of the product (e.g., a shampoo bottle) through the application.  
2. **Analyze**: On clicking the "Analyze" button, the YOLO model processes the image, identifying and annotating areas with defects.  
3. **View Results**: The app presents both the uploaded image and the processed image with highlighted defects, providing an immediate visual representation of quality issues.  

## Installation  
Follow these steps to set up and run the application locally:  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/image-recognition-quality-control.git  
   cd image-recognition-quality-control  
   ```  
2. Install the required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Run the Flask application:  
   ```bash  
   python app.py  
   ```  
4. Open your browser and navigate to:  
   ```
   http://127.0.0.1:5000  
   ```  

## Technologies Used  
- **Flask**: For backend application development and routing.  
- **YOLO (You Only Look Once)**: A powerful model for real-time object detection.  
- **PIL and NumPy**: For image processing and handling.  
- **CSS**: For styling the user interface.  

## Example Use Case  
Imagine a production line inspecting shampoo bottles for defects such as scratches, dents, or impurities. By uploading images of the products, manufacturers can automate and streamline their quality control process using this application.  

## Contribution  
This was a collaborative **team project**, developed to explore and implement real-world applications of AI in quality control systems. Contributions are welcome to enhance the functionality and scalability of the application.  

## Future Scope  
- Adding support for multiple product types.  
- Enhancing the model for detecting a wider range of defects.  
- Implementing cloud integration for scalability and remote access.  
