import streamlit as st
from email_response_agent import generate_reply

st.set_page_config(page_title="AI Email Response Agent", page_icon="📧", layout="wide")

st.title("📧 AI Email Response Agent")
st.markdown("Generate professional email replies using AI")

# Input form
with st.form("email_form"):
    col1, col2 = st.columns([1, 1])
    
    with col1:
        sender_name = st.text_input("Sender Name", value="Customer", placeholder="Enter sender's name")
        subject = st.text_input("Email Subject", placeholder="Enter email subject")
    
    with col2:
        st.write("")  # Spacing
    
    body = st.text_area("Email Body", height=150, placeholder="Enter the email content you received...")
    
    submitted = st.form_submit_button("Generate Reply", type="primary", use_container_width=True)

# Generate and display reply
if submitted:
    if subject and body:
        with st.spinner("Generating professional reply..."):
            try:
                reply = generate_reply(subject, body, sender_name)
                
                st.success("Reply generated successfully!")
                
                # Display the reply in a nice format
                st.subheader("📝 Suggested Reply:")
                st.text_area("", value=reply, height=200, disabled=True)
                
                # Copy button functionality
                st.code(reply, language=None)
                
            except Exception as e:
                st.error(f"Error generating reply: {str(e)}")
                st.info("Please check your API key and internet connection.")
    else:
        st.warning("Please fill in both the subject and body fields.")

# Sidebar with info
with st.sidebar:
    st.header("ℹ️ How to Use")
    st.markdown("""
    1. Enter the sender's name
    2. Add the email subject
    3. Paste the email body
    4. Click 'Generate Reply'
    5. Copy the generated response
    """)
    
    st.header("⚙️ Settings")
    st.info("Make sure your OPENROUTER_API_KEY is set in your .env file")