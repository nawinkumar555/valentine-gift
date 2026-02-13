import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Maddy & Roxy: AI Model", page_icon="💖")

# Custom CSS for a "Fancy" look
st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    h1 { color: #ff4b4b; font-family: 'Helvetica'; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔐 Maddy's Love Intelligence Model")
st.write("System Status: **Waiting for Roxy's Input...**")

# 1. Access Gate
password = st.text_input("Enter Access Key (Secret Nickname):", type="password")

if password.lower() == "roxy" or password.lower() == "thango":
    st.success("Access Granted. Initializing Relationship Analytics...")
    
    # 2. The Quiz Section
    st.divider()
    st.subheader("📊 Training the Model: Memory Check")
    
    q1 = st.date_input("When did our friendship officially begin?")
    q2 = st.date_input("When is our official Anniversary?")
    q3 = st.number_input("How many days had we been talking at our 500-day mark?", step=1)

    # Check Answers (October 13, August 2, 793)
  # Check Answers (October 14, 2023 | August 2, 2024 | 854 days)
    if st.button("Submit Data for Validation"):
        if q1.year == 2023 and q1.month == 10 and q1.day == 14 and \
           q2.year == 2024 and q2.month == 8 and q2.day == 2 and \
           q3 == 854:
            st.balloons()
            st.write("### ✅ Model Accuracy: 100%!")
            time.sleep(1)
            
            # 3. The Final Reveal
            st.divider()
            st.subheader("❤️ Result: The Infinite Loop")
            # Make sure your image from Step 1 is saved as 'reward.jpg' in the same folder
            st.image("reward.jpg", caption="Maddy & Roxy: Predicted Probability of Forever: 100%")
            
            st.write("""
            ### A Message from the Developer (Maddy):
            "Kaviya, you aren't just a data point in my life; you are the whole system. 
            From 793 days of talking to our August 2nd milestone, every moment 
            is a memory I've saved in my heart's permanent storage. Happy Valentine's Day!"
            """)
        else:
            st.error("Error: Memory mismatch. Try again, Roxy!")

else:
    if password:

        st.warning("Incorrect Key. Access Denied.")
