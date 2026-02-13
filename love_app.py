import streamlit as st
import time
import base64

# Page Config
st.set_page_config(page_title="Maddy & Roxy: AI Model", page_icon="💖")

# 1. Function to add Background Image
def add_bg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string.decode()}");
        background-size: cover;
        background-position: center;
    }}
    /* Making text readable over background */
    .main .block-container {{
        background-color: rgba(255, 245, 245, 0.8);
        padding: 3rem;
        border-radius: 20px;
    }}
    h1 {{ color: #ff4b4b; font-family: 'Helvetica'; }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Use your background file
try:
    add_bg('bg.jpg')
except:
    st.warning("Upload 'bg.jpg' to GitHub to see the custom background!")

# 2. Add Background Music
try:
    audio_file = open('remo_flute.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', autoplay=True, loop=True)
except:
    st.info("Upload 'music.mp3' to GitHub to play your song!")

# --- APP CONTENT ---

st.title("🔐 Maddy's Love Intelligence Model")
st.write("System Status: **Waiting for Roxy's Input...**")

# Access Gate
password = st.text_input("Enter Access Key (Secret Nickname):", type="password")

if password.lower() in ["roxy", "thango", "chello", "kutti ponnu"]:
    st.success("Access Granted. Initializing Relationship Analytics...")
    
    # Quiz Section
    st.divider()
    st.subheader("📊 Training the Model: Memory Check")
    
    q1 = st.date_input("When did our friendship officially begin?")
    q2 = st.date_input("When is our official Anniversary?")
    q3 = st.number_input("How many days have we been together?", step=1)

    # Validation (Oct 14, 2023 | Aug 2, 2024 | 854 days)
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
        else:
            st.error("Error: Memory mismatch. Check the dates or the day count and try again!")

else:
    if password:
        st.warning("Incorrect Key. Access Denied.")
