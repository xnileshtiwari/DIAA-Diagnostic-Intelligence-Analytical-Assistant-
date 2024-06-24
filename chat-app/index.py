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




st.title("Hi 👋🏼 I'm DIAA (Diagnostic Intelligence Analytical Assistant)")


if "model" not in st.session_state:
    st.session_state["model"] = "chat-bison@002"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = chat.send_message(
                prompt,
                context=[
                    {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
                ],
                **parameters
            )
            st.session_state.messages.append({"role": "assistant", "content": response})
