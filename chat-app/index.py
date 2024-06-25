import io
import streamlit as st
import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="DIAA-PALM-427310", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@002")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.4,
    "top_p": 1
},


chat = chat_model.start_chat(
    context="""You are medical chatbot who is good at history-taking, communication and empathy. Ask as much question you need to reach to acurate diagnosis""",
)





response = chat.send_message("""Hello""", **parameters)
print(f"Response from Model: {response.text}")




st.markdown("<h1 style='text-align: center;'>Hi 👋🏼 I'm DIAA👩🏼‍⚕️</h1>", unsafe_allow_html=True)



if "model" not in st.session_state:
    st.session_state["model"] = "chat-bison@002"

for message in st.session_state.messages:
    #works from 2 question
    with st.chat_message(message["role"], avatar=f"{(message['role'] == 'user' and 'boy.png') or 'doctor (1).png'}"):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "avatar": 'boy.png', "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user", avatar='boy.png'):
        st.markdown(prompt)
        time.sleep(2)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar='doctor (1).png'):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "avatar": 'doctor (1).png', "content": response})
