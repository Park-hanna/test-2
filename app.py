import openai
import streamlit as st
from streamlit_chat import message

openai.api_key = st.secrets["OPENAI_API_KEY"]

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
