import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# App UI
st.set_page_config(page_title="AI Story Generator", page_icon="📖")

st.title(" AI Story Generator")
st.write("Create your own AI-generated story based on your preferences.")

# User Inputs
genre = st.selectbox(
    "Choose Genre",
    ["Fantasy", "Sci-Fi", "Horror", "Romance", "Adventure", "Mystery"]
)

tone = st.selectbox(
    "Choose Tone",
    ["Dark", "Funny", "Emotional", "Suspenseful", "Inspirational"]
)

setting = st.text_input("Enter Setting (e.g., Mars colony, ancient kingdom)")
character = st.text_input("Main Character (e.g., brave astronaut, lost prince)")

length = st.slider("Story Length", 100, 1000, 300)

# Generate Button
if st.button("Generate Story"):
    if not setting or not character:
        st.warning("Please fill in all fields!")
    else:
        with st.spinner("Generating your story..."):

            prompt = f"""
            Write a {tone} {genre} story set in {setting}.
            The main character is {character}.
            Keep the story engaging and descriptive.
            Limit it to around {length} words.
            """

            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a creative storyteller."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.8
                )

                story = response.choices[0].message.content

                st.subheader(" Your Story")
                st.write(story)

            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Successfully generated stories can be saved to a file for later enjoyment. Just click the 'Save Story' button after generating your story!")