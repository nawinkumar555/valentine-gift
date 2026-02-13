import streamlit as st
import base64
import time

# Page Config
st.set_page_config(page_title="Maddy & Roxy: AI Model", page_icon="💖", layout="wide")

# Helper to encode media
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Initial Static Background (October 14, 2023 Milestone)
def add_static_bg(image_file):
    try:
        img_b64 = get_base64(image_file)
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{img_b64}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            .main .block-container {{
                background-color: rgba(255, 255, 255, 0.8); 
                padding: 3rem;
                border-radius: 20px;
                margin-top: 5vh;
                max-width: 600px;
                margin-left: auto;
                margin-right: auto;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }}
            h1, h3, p, label {{ color: #1a1a1a !important; font-weight: bold; }}
            
            /* CSS to make BOTH buttons have White Text */
            div.stButton > button {{
                color: white !important;
                background-color: #ff4b4b !important;
                border-radius: 10px;
                font-weight: bold;
                width: 100%;
                border: none;
            }}
            
            div.stLinkButton > a {{
                color: white !important;
                background-color: #ff4b4b !important;
                border-radius: 10px;
                font-weight: bold;
                text-decoration: none;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                padding: 10px;
                border: none;
            }}

            div.stButton > button:hover, div.stLinkButton > a:hover {{
                background-color: #e03a3a !important;
                color: white !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        st.warning("Initial background 'bg.jpg' not found on GitHub.")

# Video Reveal Function (August 2, 2024 Anniversary Reveal)
def add_reveal_video(video_file):
    try:
        vid_b64 = get_base64(video_file)
        st.markdown(
            f"""
            <style>
            #revealVideo {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw; 
                height: 100vh;
                z-index: -2;
                object-fit: cover;
                opacity: 0.95;
            }}
            .stApp {{ background: transparent !important; }}
            </style>
            <video autoplay muted loop playsinline id="revealVideo">
                <source src="data:video/mp4;base64,{vid_b64}" type="video/mp4">
            </video>
            """,
            unsafe_allow_html=True
        )
    except:
        st.error("Video 'bg_video.mp4' failed to load. Ensure it is uploaded to GitHub!")

# Start with the static image
add_static_bg('bg.jpg')

# --- APP CONTENT ---
st.title("🔐 Maddy's Love Intelligence Model")
st.write("System Status: **Waiting for Roxy's Input...**")

# Access Gate (Nicknames: Roxy, Thango, Chello, Kutti Ponnu)
password = st.text_input("Enter Access Key (Secret Nickname):", type="password")

if password.lower() in ["roxy", "thango", "chello", "kutti ponnu"]:
    st.success("Access Granted. Initializing Relationship Analytics...")
    st.subheader("📊 Training the Model: Memory Check")
    
    # Quiz Answers based on your milestones: Oct 14, 2023 | Aug 2, 2024 | 854 days
    q1 = st.date_input("When did our friendship officially begin?") 
    q2 = st.date_input("When is our official Anniversary?") 
    q3 = st.number_input("How many days have we been together?", step=1) 

    if st.button("Submit Data for Validation"):
        if q1.year == 2023 and q1.month == 10 and q1.day == 14 and \
           q2.year == 2024 and q2.month == 8 and q2.day == 2 and \
           q3 == 854:
            
            # 1. TRIGGER VIDEO AND AUDIO REVEAL
            add_reveal_video('bg_video.mp4')
            try:
                audio_bytes = open('Flute_Flow.mp3', 'rb').read()
                st.audio(audio_bytes, format='audio/mp3', autoplay=True)
            except:
                st.info("Upload 'Flute_Flow.mp3' for the soundtrack!")

            st.balloons()
            st.write("### ✅ Model Accuracy: 100%!")
            time.sleep(1) 
            
            # 2. INFINITY LOOP CONTENT REVEAL
            st.divider()
            st.subheader("❤️ Result: The Infinite Loop")
            
            try:
                st.image("reward.jpg", caption="Maddy & Roxy: 100% Match Probability")
            except:
                st.error("Please ensure 'reward.jpg' is uploaded to your GitHub folder.")
            
            # 3. PERSONALIZED RED/PINK MESSAGE
            st.markdown(f"""
            ### A Message from Maddy:
            <p style='color: #ff4b4b; font-size: 20px; font-weight: bold; text-shadow: 1px 1px 2px #ffffff; line-height: 1.5;'>
            "Kaviya, you aren't just a data point in my life; you are the whole system. 
            From the 854 days we've shared since October 14, 2023, every moment 
            is a memory I've saved in my heart's permanent storage. Happy Valentine's Day, Roxy!"
            </p>
            """, unsafe_allow_html=True)

            # 4. FINAL GIFT LINK
            st.link_button("🎁 Open Your Final Gift", "https://roxymaddy.my.canva.site/")
            
        else:
            st.error("Error: Memory mismatch. Check the dates or the day count and try again, Roxy!")

else:
    if password:
        st.warning("Incorrect Key. Access Denied.")
