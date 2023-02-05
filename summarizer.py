# Importing dependencies
import openai
import streamlit as st

# Set the OpenAI GPT-3 API Key 
openai.api_key = st.secrets['pass']

st.header("Summarizer App Using OpenAI + Streamlit")

article_text = st.text_area("Enter your text which you want to summarize ...")

if len(article_text) > 100:
    temp = st.slider("Temperature", 0.0, 1.0, 0.13) #.5
    if st.button("Generate Summary"):
        # Use GPT-3 to generate summry of the article
        response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = article_text, #"Please summarize this scientific artcile for me in a few sentences",
        max_tokens = 516,
        temperature = temp
        )
        
        # Print the summary generated 
        res = response["choices"][0]["text"]
        st.info(res)
        
        st.download_button("Download Response", res)
        
else:
    st.warning("The sentence is not long enough.")
        