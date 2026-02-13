import streamlit as st
import base64
import time

# Page Config
st.set_page_config(page_title="Maddy & Roxy: AI Model", page_icon="💖", layout="wide")

# 1. Layered Background Function (Image + Video)
def add_layered_bg(image_file, video_file):
    try:
        # Load Image
        with open(image_file, "rb") as i:
            img_data = base64.b64encode(i.read()).decode()
        # Load Video
        with open(video_file, "rb") as v:
            vid_data = base64.b64encode(v.read()).decode()
            
        st.markdown(
            f"""
            <style>
            /* Layer 1: The Static Image at the very bottom */
            .stApp {{
                background-image: url("data:image/png;base64,{img_data}");
                background-size: cover;
                background-position: center;
            }}
            /* Layer 2: The Video floating over the image */
            #myVideo {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw; 
                height: 100vh;
                z-index: -1;
                object-fit: contain; 
                opacity: 0.6; /* Makes video see-through so bg image shows */
            }}
            /* Layer 3: The Content Box */
            .main .block-container {{
                background-color: rgba(255, 255, 255, 0.75); 
                padding: 3rem;
                border-radius: 20px;
                margin-top: 5vh;
                max-width: 650px;
                margin-left: auto;
                margin-right: auto;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
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
    except:
        st.warning("Ensure 'bg.jpg' and 'bg_video.mp4' are uploaded to GitHub!")

# Execute the Layered Background
add_layered_bg('bg.jpg', 'bg_video.mp4')

# 2. Add Background Music (Flute_Flow.mp3)
try:
    audio_file = open('Flute_Flow.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', autoplay=True, loop=True)
except:
    st.info("Upload 'Flute_Flow.mp3' to play your song!")

# --- APP CONTENT ---
st.title("🔐 Maddy's Love Intelligence Model")
st.write("System Status: **Waiting for Roxy's Input...**")

password = st.text_input("Enter Access Key (Secret Nickname):", type="password")

if password.lower() in ["roxy", "thango", "chello", "kutti ponnu"]:
    st.success("Access Granted. Initializing Relationship Analytics...")
    
    st.divider()
    st.subheader("📊 Training the Model: Memory Check")
    
    # Quiz Answers
    q1 = st.date_input("When did our friendship officially begin?") # Answer: Oct 14, 2023
    q2 = st.date_input("When is our official Anniversary?") # Answer: Aug 2, 2024
    q3 = st.number_input("How many days have we been together?", step=1) # Answer: 854

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
                st.image("reward.jpg", caption="Maddy & Roxy: 100% Match Probability")
            except:
                st.error("Upload 'reward.jpg' to GitHub!")
            
            st.write(f"""
            ### A Message from Maddy:
            "Kaviya, you aren't just a data point in my life; you are the whole system. 
            From the 854 days we've shared since our friendship began on October 14th, 
            to our August 2nd milestone, every moment is a memory I've saved in my heart's 
            permanent storage. Happy Valentine's Day, Roxy!"
            """)

            st.link_button("🎁 Open Your Final Gift", "https://roxymaddy.my.canva.site/")
        else:
            st.error("Error: Memory mismatch. Try again, Roxy!")

else:
    if password:
        st.warning("Incorrect Key. Access Denied.")
