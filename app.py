import streamlit as st
from ai_functionality import generate_ai_response  # Corrected function name

# Set initial message
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello there, how can I help you?"}
    ]

with st.sidebar:
    # API key input
    api_key = st.text_input("Enter your OpenAI API key", type="password")

    # Language selection
    selected_language = st.selectbox(
        'Select A Language',
        ("English", "Hindi", "French")
    )

    # JSON result fields
    traits = st.multiselect(
        "Select Behaviour traits You Are Interested In",
        ['Funny', 'rude',
         'normal', 'black',
         "white", "news reporter",
         "childish", "mature",
         "charismatic", "compassion",
         "agreeableness", "creative",
         "optimism", "confident",
         "ambitious"],
        ['Funny', 'charismatic']
    )

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

if st.session_state.messages[-1]["role"] != "assistant" and api_key:
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response, context = generate_ai_response(
                api_key=api_key,  # Pass the API key to the function
                user_prompt=user_prompt,
                traits=traits,
                language=selected_language
            )
            st.write(ai_response)
            st.write(context)

    new_ai_message = {"role": "assistant", "content": ai_response}
    st.session_state.messages.append(new_ai_message)
elif not api_key:
    st.warning("Please enter your API key to proceed.")
