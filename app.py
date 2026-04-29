import streamlit as st
from main import classify_email

st.set_page_config(page_title="AI Email Classifier", layout="centered")

st.title("📩 AI Customer Support Assistant")
st.write("Classifies customer emails and generates responses (EN + AR)")

user_input = st.text_area("Enter customer email:")

if st.button("Analyze"):
    if user_input.strip():
        result = classify_email(user_input)

        st.subheader("📊 Classification")
        st.write(f"**Intent:** {result.get('intent')}")
        st.write(f"**Urgency:** {result.get('urgency')}")
        st.write(f"**Confidence:** {result.get('confidence')}")

        st.subheader("🧠 Reasoning")
        st.write(result.get("reasoning"))

        st.subheader("✉️ Reply (English)")
        st.write(result.get("reply_en"))

        st.subheader("🌍 Reply (Arabic)")
        st.write(result.get("reply_ar"))

    else:
        st.warning("Please enter some text.")