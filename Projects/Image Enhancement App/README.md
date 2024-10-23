### Image Enhancement App using EDSR Model 🖼️
This repository contains a Streamlit-based web app that enhances image quality using the EDSR (Enhanced Deep Super-Resolution) model. The app allows users to upload an image and apply super-resolution techniques to enhance its clarity and quality.

## Features 🚀
- 📷 Image Upload: Supports .jpg, .jpeg, and .png formats.
- 🔄 Real-time Enhancement: Uses the EDSR model to enhance uploaded images.
- ⚙️ User-friendly Interface: Built with Streamlit for easy use.
- 📂 Reusable Code: Easy to modify and deploy for other super-resolution models.

## Usage 📖
- Launch the app and open the Streamlit web page in your browser.
- Upload an image file using the file uploader.
- The enhanced image will be displayed after processing by the EDSR model.

## Project Structure 📂
├── app.py              # Main Streamlit app script
├── edsr_model.h5       # Pre-trained EDSR model
├── requirements.txt    # List of dependencies
├── README.md           # Project documentation (this file)

## Technologies Used 💻
- Python: Backend logic and image processing
- TensorFlow: For loading the EDSR model
- Streamlit: Web interface
- Pillow: For image handling

## Requirements 📝
Python 3.8+
TensorFlow 2.x
Streamlit
Pillow

## Troubleshooting 🔧
- Model Loading Error: Ensure that edsr_model.h5 is in the project’s root directory.
- Streamlit App Not Running: Verify Streamlit installation with pip show streamlit and try running the app again.
- FileNotFoundError: Use an absolute path to edsr_model.h5 if the relative path fails.

## Contributing 🤝
Contributions are welcome! If you'd like to improve the code or add new features, feel free to open a pull request or issue.

## Acknowledgements 🙏
- [EDSR Model Paper](https://arxiv.org/abs/1707.02921)
- Streamlit Documentation
