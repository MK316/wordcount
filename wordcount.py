import streamlit as st
import re

def count_words(text):
    # Split the text by any whitespace and count the parts
    return len(re.findall(r'\w+', text))

def count_sentences(text):
    # Split the text by sentence delimiters and count the parts
    return len(re.findall(r'[.!?]+', text)) + 1

def main():
    st.title('Text Summary Tool')
    
    # Text area for user input
    user_input = st.text_area("Paste your text here:", height=300)
    
    if user_input:
        # Count words and sentences
        word_count = count_words(user_input)
        sentence_count = count_sentences(user_input)
        
        # Display the results
        st.write(f"**Word Count**: {word_count}")
        st.write(f"**Sentence Count**: {sentence_count}")

if __name__ == '__main__':
    main()
