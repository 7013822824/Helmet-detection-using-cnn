🚦 Advanced Helmet Detection at Traffic Signals Using CNN

📌 Project Overview

This project is a deep learning-based system designed to detect helmet violations at traffic signals. Using YOLOv5 for object 
detection and CNN for classification, the system identifies motorcyclists, checks for helmet compliance, and extracts vehicle 
license plate details using OCR. Upon detecting a violation, an automated e-challan (traffic fine ticket) is generated and sent 
to the registered vehicle owner's email.

🛠️ Technologies Used

Deep Learning Framework: YOLOv5, CNN (Convolutional Neural Networks)

Programming Languages: Python, HTML, CSS

Libraries & Tools: OpenCV, NumPy, TensorFlow/Keras, Tesseract OCR, Flask (for Web Interface)

Database: SQLite (for storing vehicle and violation records)

Deployment: Edge devices (optional) & cloud integration

🔧 Installation & Setup

Clone the repository:

git clone https://github.com/your-username/helmet-detection.git
cd helmet-detection

Install dependencies:

pip install -r requirements.txt

Download YOLOv5 model weights and place them in the weights/ directory.

Run the project:

python app.py

Access the web interface at http://localhost:5000.

🚀 Features

✅ Real-time helmet detection using YOLOv5
✅ Automatic license plate recognition (OCR-based)
✅ Violation logging and database storage
✅ Automated challan generation via email
✅ Web-based dashboard for monitoring violations
✅ Scalable for smart city traffic management

📂 Project Structure

📁 helmet-detection/
│-- 📁 models/            # Pretrained YOLOv5 & CNN models
│-- 📁 static/            # Web assets (CSS, images)
│-- 📁 templates/         # HTML templates for the web interface
│-- 📁 uploads/           # Video/Image uploads for detection
│-- app.py               # Main Flask application
│-- detect.py            # Helmet detection logic
│-- ocr.py               # License plate recognition module
│-- generate_challan.py  # Automated challan generation script
│-- README.md            # Project documentation
│-- requirements.txt     # Dependencies

📊 Results & Discussion

The system achieves high accuracy in detecting motorcyclists and identifying helmet violations. 
However, license plate recognition accuracy may vary due to lighting, motion blur, and occlusions. 
Future improvements will focus on enhanced OCR models, night vision support, and multi-angle detection.

🔮 Future Enhancements

Improved OCR accuracy for license plate recognition

Night vision & low-light detection enhancements

Multi-angle helmet detection for better violation tracking

Integration with traffic databases for real-time fine processing

Deploying on edge devices for real-time inference

📜 License

This project is open-source under the MIT License. Feel free to use and improve it.

👥 Contributors

[PNS Narendra] - Developer & Researcher

Open for contributions! Feel free to submit a pull request.

⭐ Acknowledgment

This project was developed as part of the Final Year Major Project in the field of Deep Learning and AI.

📢 If you find this project useful, give it a ⭐ on GitHub! 🚀

