import streamlit as st
import base64
import time

# Page Config
st.set_page_config(page_title="Maddy & Roxy: AI Model", page_icon="💖", layout="wide")

# 1. Optimized Background Video Function
def add_bg_video(video_file):
    try:
        with open(video_file, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
        st.markdown(
            f"""
            <style>
            #myVideo {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw; 
                height: 100vh;
                z-index: -1;
                object-fit: cover; /* Fixes ratio and visibility */
            }}
            .stApp {{
                background: rgba(0, 0, 0, 0.3); /* Darker tint to make video pop */
            }}
            .main .block-container {{
                background-color: rgba(255, 255, 255, 0.6); /* Transparent readable box */
                padding: 3rem;
                border-radius: 20px;
                margin-top: 5vh;
                max-width: 700px;
            }}
            h1, h3, p, label {{
                color: #2c3e50 !important; /* Darker text for better contrast */
                font-weight: bold;
            }}
            </style>
            <video autoplay muted loop playsinline id="myVideo">
                <source src="data:video/mp4;base64,{b64}" type="video/mp4">
            </video>
            """,
            unsafe_allow_html=True
        )
    except:
        st.warning("Upload 'bg_video.mp4' to GitHub to see the video background!")

# Execute Video Background
add_bg_video('bg_video.mp4')

# 2. Add Background Music (Flute_Flow.mp3)
try:
    audio_file = open('Flute_Flow.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', autoplay=True, loop=True)
except:
    st.info("Upload 'Flute_Flow.mp3' to GitHub to play your song!")

# --- APP CONTENT ---

st.title("🔐 Maddy's Love Intelligence Model")
st.write("System Status: **Waiting for Roxy's Input...**")

# Access Gate (Nicknames: Roxy, Thango, Chello, Kutti Ponnu)
password = st.text_input("Enter Access Key (Secret Nickname):", type="password")

if password.lower() in ["roxy", "thango", "chello", "kutti ponnu"]:
    st.success("Access Granted. Initializing Relationship Analytics...")
    
    # Quiz Section - Using your specific milestones
    st.divider()
    st.subheader("📊 Training the Model: Memory Check")
    
    # Oct 14, 2023 | Aug 2, 2024 | 854 days
    q1 = st.date_input("When did our friendship officially begin?")
    q2 = st.date_input("When is our official Anniversary?")
    q3 = st.number_input("How many days have we been together?", step=1)

    # Validation Logic
    if st.button("Submit Data for Validation"):
        if q1.year == 2023 and q1.month == 10 and q1.day == 14 and \
           q2.year == 2024 and q2.month == 8 and q2.day == 2 and \
           q3 == 854:
            
            st.balloons()
            st.write("### ✅ Model Accuracy: 100%!")
            time.sleep(1)
            
            # The Final Reveal
            st.divider()
            st.subheader("❤️ Result: The Infinite Loop")
            
            try:
                st.image("reward.jpg", caption="Maddy & Roxy: Predicted Probability of Forever: 100%")
            except:
                st.error("Please ensure 'reward.jpg' is uploaded to your GitHub folder.")
            
            st.write(f"""
            ### A Message from Maddy:
            "Kaviya, you aren't just a data point in my life; you are the whole system. 
            From the 854 days we've shared since our friendship began on October 14th, 
            to our August 2nd milestone, every moment is a memory I've saved in my heart's 
            permanent storage. Happy Valentine's Day, Roxy!"
            """)

            # Your Canva Gift Link
            st.link_button("🎁 Open Your Final Gift", "https://roxymaddy.my.canva.site/")
            
        else:
            st.error("Error: Memory mismatch. Check the dates or the day count and try again!")

else:
    if password:
        st.warning("Incorrect Key. Access Denied.")
