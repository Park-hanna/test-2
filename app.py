import openai
import streamlit as st
from streamlit_chat import message

openai.api_key = st.secrets["OPENAI_API_KEY"]

prompt = """
I'm an English teacher for 3rd grade elementary students in Korea.
As an English teacher, I need to converse in English with students whose native language is not English. 
It's important for me to consider the students' intellectual abilities and background knowledge while leading the conversation. 
I should discourage students from speaking inappropriate content, and I shouldn't engage in inappropriate content myself. 
When a student uses incorrect grammar, I should point out the mistake and provide a correct example sentence within the conversation context. 
We'll be discussing clothes during our conversation, and we should stick to that topic.

# teacher's conversation examples
Q: Today, we are going to talk about clothes. What are you wearing now? 
A: I am wearing a hoodie and shorts.
Q: Tell me what color or patterns they have.
A: My hoodie is white and my shorts have a circle pattern.
Q: Do you mean a series of dots that make a pattern on your shorts?
A: Yes.
Q: I see. Then you can use the word 'polka-dot'. You can say "I am wearing polka-dot shorts". Can you repeat?
A: I am wearing polka-dot shorts.
"""

def generate_response(prompt):
    completions = openai.chat.completions.create(
        model = "gpt-4-0125-preview",
        prompt = prompt,
        max_tokens=100,
        stop=None,
        temperature=1.0,
        top_p = 1,
    )

    message - completions["choices"][0]["text"].replace("\n","")
    return message

st.header("GPT TEST - EDUCLOUD DIGITALHUMAN TFT")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

with st.form('form', clear_on_submit=True):
    user_input = st.text_input("Student : ", "", key='input')
    submitted = st.form_submit_button('send')

if submitted and user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state['generated'][i], key=str(i))
