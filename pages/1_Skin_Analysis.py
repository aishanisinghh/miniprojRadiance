import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
from datetime import datetime

class FaceCapture:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
    
    def detect_faces(self, image_array):
        """Detect faces in image using OpenCV"""
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        return faces

def main():
    st.title("📸 Skin Analysis")
    
    face_capture = FaceCapture()
    
    # Create directories
    os.makedirs("images/captures", exist_ok=True)
    
    # Input method selection
    input_method = st.radio(
        "Choose input method:",
        ["📷 Take Photo with Webcam", "📁 Upload Existing Image"]
    )
    
    if input_method == "📷 Take Photo with Webcam":
        st.subheader("🎥 Live Webcam Capture")
        captured_image = st.camera_input("Smile! Click the camera to capture")
        
        if captured_image is not None:
            process_image(captured_image, face_capture, "webcam")
    
    else:  # Upload Existing Image
        st.subheader("📁 Upload Image")
        uploaded_file = st.file_uploader(
            "Choose a face image", 
            type=['jpg', 'jpeg', 'png']
        )
        
        if uploaded_file is not None:
            process_image(uploaded_file, face_capture, "upload")

def process_image(image_input, face_capture, source_type):
    """Process the image and perform face detection"""
    # Convert to PIL Image and numpy array
    if source_type == "webcam":
        img = Image.open(image_input)
        img_array = np.array(img)
    else:  # upload
        img = Image.open(image_input)
        img_array = np.array(img)
    
    # Display original image
    st.image(img, caption="Original Image", use_column_width=True)
    
    # Detect faces
    faces = face_capture.detect_faces(img_array)
    
    if len(faces) > 0:
        st.success(f"✅ Found {len(faces)} face(s)")
        
        # Draw bounding boxes
        result_img = img_array.copy()
        for i, (x, y, w, h) in enumerate(faces):
            # Draw rectangle
            cv2.rectangle(result_img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            
            # Add face number
            cv2.putText(result_img, f"Face {i+1}", (x, y-10), 
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Display detection result
        st.image(result_img, caption="Face Detection Result", use_column_width=True)
        
        # Show individual faces
        for i, (x, y, w, h) in enumerate(faces):
            with st.expander(f"📸 Face {i+1} Analysis"):
                face_roi = img_array[y:y+h, x:x+w]
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.image(face_roi, caption=f"Face {i+1}", use_column_width=True)
                
                with col2:
                    st.write("🔍 Analyzing your skin...")
                    
                    # TODO: Add actual model inference here
                    results = {
                        "Skin Type": "Oily",
                        "Concerns": ["Acne", "Pigmentation"],
                        "Skin Tone": "Medium",
                        "Moisture Level": "65%",
                        "Oiliness": "High"
                    }
                    
                    st.json(results)
                    
                    # Save to session state for other pages to use
                    if 'skin_analysis' not in st.session_state:
                        st.session_state.skin_analysis = {}
                    
                    st.session_state.skin_analysis[f'face_{i+1}'] = results
                    st.success("Analysis saved! Check Recommendations page.")
        
        # Save the main detection result
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_path = f"images/captures/face_detection_{timestamp}.jpg"
        cv2.imwrite(result_path, cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR))
        
    else:
        st.error("❌ No faces detected. Please try again with a clearer image.")
        
        # Still show mock analysis if no faces detected (for demo purposes)
        st.write("🔍 Mock Analysis (no face detected):")
        results = {
            "Skin Type": "Unknown",
            "Concerns": ["Unable to analyze - no face detected"],
            "Skin Tone": "Unknown"
        }
        st.json(results)

if __name__ == "__main__":
    main()