import streamlit as st
import random

# Define responses for different user inputs
positive_responses = ['That sounds great!', "I'm glad to hear that.", 'Positive vibes to you!']
negative_responses = ["I'm sorry to hear that.", "It's okay not to be okay.", "Remember, you're not alone."]
support_responses = ["I'm here for you.", "You're not alone; reach out to someone you trust."]
jokes = [
    'Why did the scarecrow win an award? Because he was outstanding in his field!',
    'What do you call fake spaghetti? An impasta!',
    'I told my wife she should embrace her mistakes. She gave me a hug!'
]

# Inspirational quotes
quotes = [
    "You are stronger than you think.",
    "Every day may not be good, but there is something good in every day.",
    "It's okay to not be okay as long as you are not giving up.",
    "Believe you can and you're halfway there.",
    "You are worth it.",
    "Your mental health is a priority. Your happiness is essential. Your self-care is a necessity."
]

# Streamlit app with sidebars
st.title('Mental Health Chatbot')
st.sidebar.header('Options')

# Main sidebar options
user_input = st.text_input('How are you feeling today?')
show_quotes = st.sidebar.checkbox('Show Inspirational Quotes')
show_info = st.sidebar.checkbox('Show Additional Information')

bot_response = st.empty()

if st.button('Talk to Chatbot'):
    if user_input:
        # Simple rule-based responses for mental health
        user_input_lower = user_input.lower()

        if 'good' in user_input_lower or 'happy' in user_input_lower:
            bot_response.write(random.choice(positive_responses))
        elif 'bad' in user_input_lower or 'sad' in user_input_lower:
            bot_response.write(random.choice(negative_responses))
        elif 'support' in user_input_lower or 'help' in user_input_lower:
            bot_response.write(random.choice(support_responses))
        elif 'joke' in user_input_lower:
            bot_response.write(random.choice(jokes))
        else:
            bot_response.write("I'm here to support you. If you need someone to talk to, consider reaching out to friends, family, or a mental health professional.")

# Additional features based on sidebars options
if show_quotes:
    st.sidebar.subheader('Inspirational Quote')
    if st.sidebar.button('Show Quote'):
        inspirational_quote = random.choice(quotes)
        st.sidebar.write('Quote:', inspirational_quote)

if show_info:
    st.sidebar.subheader('Additional Information')
    st.sidebar.info(
        "This chatbot is here to provide support and positivity. "
        "It's not a substitute for professional advice. "
        "If you need immediate help, please contact a mental health professional."
    )

# Add a video
st.subheader('Watch this Inspirational Video')
video_url = 'https://www.youtube.com/watch?v=Ub66IkMiDLc&pp=ygUSbW90aXZhdGlvbmFsIHZpZGVv'
st.video("https://www.youtube.com/watch?v=Ub66IkMiDLc&pp=ygUSbW90aXZhdGlvbmFsIHZpZGVv")
