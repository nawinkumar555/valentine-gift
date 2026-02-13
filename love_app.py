import streamlit as st
import base64
import time

# Page Config
st.set_page_config(page_title="Maddy & Roxy: AI Model", page_icon="💖", layout="wide")

# 1. Function to Layer Image + Video
def add_layered_bg(image_file, video_file):
    try:
        # Load Background Image
        with open(image_file, "rb") as i:
            img_data = base64.b64encode(i.read()).decode()
        
        # Load Background Video
        with open(video_file, "rb") as v:
            vid_data = base64.b64encode(v.read()).decode()
            
        st.markdown(
            f"""
            <style>
            /* Bottom Layer: Static Background Image */
            .stApp {{
                background-image: url("data:image/png;base64,{img_data}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            
            /* Middle Layer: Video with Transparency */
            #myVideo {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw; 
                height: 100vh;
                z-index: -1;
                object-fit: contain; 
                opacity: 0.5; /* Adjust this (0.1 to 1.0) to see more/less of the video */
            }}
            
            /* Top Layer: Content Box */
            .main .block-container {{
                background-color: rgba(255, 255, 255, 0.8); 
                padding: 3rem;
                border-radius: 20px;
                margin-top: 5vh;
                max-width: 600px;
                margin-left: auto;
                margin-right: auto;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }}
            
            h1, h3, p, label {{
                color: #1a1a1a !important; 
                font-weight: bold;
            }}
            </style>
            
            <video autoplay muted loop playsinline id="myVideo">
                <source src="data:video/mp4;base64,{vid_data}" type="video/mp4">
            </video>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Error loading media: {e}")

# Run the layered background
add_layered_bg('bg.jpg', 'bg_video.mp4')

# 2. Add Background Music
try:
    audio_file = open('Flute_Flow.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', autoplay=True, loop=True)
except:
    st.info("Upload 'Flute_Flow.mp3' to GitHub to play your song!")

# --- APP CONTENT ---
st.title("🔐 Maddy's Love Intelligence Model")
st.write("System Status: **Waiting for Roxy's Input...**")

password = st.text_input("Enter Access Key (Secret Nickname):", type="password")

if password.lower() in ["roxy", "thango", "chello", "kutti ponnu"]:
    st.success("Access Granted.")
    st.divider()
    st.subheader("📊 Training the Model: Memory Check")
    
    # Validation Dates (Friendship: Oct 14, 2023 | Anniversary: Aug 2, 2024 | Days: 854)
    q1 = st.date_input("When did our friendship officially begin?")
    q2 = st.date_input("When is our official Anniversary?")
    q3 = st.number_input("How many days have we been together?", step=1)

    if st.button("Submit Data for Validation"):
        if q1.year == 2023 and q1.month == 10 and q1.day == 14 and \
           q2.year == 2024 and q2.month == 8 and q2.day == 2 and \
           q3 == 854:
            
            st.balloons()
            st.write("### ✅ Model Accuracy: 100%!")
            time.sleep(1)
            
            st.divider()
            st.subheader("❤️ Result: The Infinite Loop")
            
            try:
                st.image("reward.jpg", caption="Maddy & Roxy: 100% Match")
            except:
                st.error("Upload 'reward.jpg' to GitHub!")
            
            st.write(f"""
            ### A Message from Maddy:
            "Kaviya, you aren't just a data point in my life; you are the whole system. 
            From the 854 days we've shared since October 14, 2023, every moment 
            is a memory I've saved in my heart's permanent storage. Happy Valentine's Day, Roxy!"
            """)

            st.link_button("🎁 Open Your Final Gift", "https://roxymaddy.my.canva.site/")
        else:
            st.error("Error: Memory mismatch. Try again, Roxy!")

else:
    if password:
        st.warning("Incorrect Key. Access Denied.")
