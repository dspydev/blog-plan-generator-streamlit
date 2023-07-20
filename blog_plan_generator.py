import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title="📝 Blog's Plan Generator App")
st.title('📝 Blog\'s Plan Generator App')

def generate_response(topic, openai_api_key):
    """
    Generates a blog outline for the given topic using the OpenAI GPT-3 model.
    
    :param topic: The topic to generate a blog outline for.
    :type topic: str
    :param openai_api_key: The OpenAI API key to use for generating the response.
    :type openai_api_key: str
    :return: The generated blog outline.
    :rtype: str
    """
    llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)
    template = 'As an experienced data scientist and technical writer, generate an outline for a blog about {topic}.'
    prompt = PromptTemplate(input_variables=['topic'], template=template)
    prompt_query = prompt.format(topic=topic)
    response = llm(prompt_query)
    return response

def main():
    """
    Main function for the Streamlit app.
    """
    st.sidebar.header('Instructions')
    st.sidebar.write('1. Enter your OpenAI API key in the sidebar.')
    st.sidebar.write('2. Enter the topic you want to generate a blog outline for in the main form.')
    st.sidebar.write('3. Click the "Submit" button to generate and display the blog outline.')
    
    openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
    
    with st.form('myform'):
        topic_text = st.text_input('Enter keyword:', '')
        submitted = st.form_submit_button('Submit')
        
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        
        if submitted and openai_api_key.startswith('sk-'):
            response = generate_response(topic_text, openai_api_key)
            st.info(response)

if __name__ == '__main__':
    main()
