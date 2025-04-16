import streamlit as st
from dotenv import load_dotenv
import os

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from htmlTemplates import css, bot_template, user_template  # Ensure this file exists

# ✅ Must be the first Streamlit command
st.set_page_config(page_title="Chat with multiple PDFs", page_icon="📚")


# -------- PDF Text Extraction --------
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
        except Exception as e:
            st.warning(f"Could not read {pdf.name}: {e}")
    return text


# -------- Chunking Text --------
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)


# -------- Create Vector Store --------
def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(texts=text_chunks, embedding=embeddings)


# -------- Build Conversation Chain --------
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )


# -------- Handle User Input --------
def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for i, message in enumerate(st.session_state.chat_history):
        template = user_template if i % 2 == 0 else bot_template
        st.write(template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

        st.markdown('<hr style="border: none; height: 1px; background-color: #ccc; margin: 10px 0;" />', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# -------- Main Streamlit App --------
def main():
    load_dotenv()
    #os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = None

    st.markdown("<h1 style='text-align: center; color: #2979FF;'>📚 Chat with your PDFs</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; margin-bottom: 30px;'>Upload your documents and start a conversation</p>", unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("<h3 style='color: #2979FF;'>📄 Your Documents</h3>", unsafe_allow_html=True)
        
        # Updated with new class how-it-works-box
        st.markdown("""
        <div class="how-it-works-box">
            <p><strong>How it works:</strong></p>
            <ol>
                <li>Upload your PDF documents</li>
                <li>Click "Process" to analyze them</li>
                <li>Ask questions about your documents</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        pdf_docs = st.file_uploader(
            "Drop your PDFs here",
            accept_multiple_files=True,
            type=["pdf"],
            help="You can upload multiple PDF files"
        )

        col1, col2 = st.columns(2)
        
        with col1:
            process_btn = st.button("✨ Process", use_container_width=True)
        with col2:
            clear_btn = st.button("🗑️ Clear", use_container_width=True)
            
        if process_btn and pdf_docs:
            with st.spinner("Processing your documents..."):
                st.markdown("""
                <div style="display: flex; justify-content: center; margin: 20px 0;">
                    <div class="loading"></div>
                </div>
                """, unsafe_allow_html=True)
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)
                st.session_state.uploaded_files = [file.name for file in pdf_docs]
                st.success("✅ Processing complete!")
                
        if clear_btn:
            st.session_state.conversation = None
            st.session_state.chat_history = None
            st.session_state.uploaded_files = None
            st.experimental_rerun()
            
        if st.session_state.uploaded_files:
            st.markdown("<h4>Active Documents:</h4>", unsafe_allow_html=True)
            for file in st.session_state.uploaded_files:
                st.markdown(f"""
                <div style="display: flex; align-items: center; margin-bottom: 5px;">
                    <span class="pdf-icon">📄</span> {file}
                </div>
                """, unsafe_allow_html=True)

    # Main chat area
    if st.session_state.conversation:
        if st.session_state.uploaded_files:
            doc_tags = " ".join([f'<span class="document-tag">{file}</span>' for file in st.session_state.uploaded_files])
            st.markdown(f"<p>Using: {doc_tags}</p>", unsafe_allow_html=True)
            
        # Updated with new class tip-box
        st.markdown("""
        <div class="tip-box">
            <p style="margin-bottom: 0;"><strong>💡 Tip:</strong> Ask specific questions about your documents for the best results!</p>
        </div>
        """, unsafe_allow_html=True)
        
        user_question = st.text_input("Ask a question:", placeholder="What information are you looking for?")
        if user_question:
            with st.spinner("Thinking..."):
                handle_userinput(user_question)
    else:
        # Updated with new class welcome-box
        st.markdown("""
        <div class="welcome-box">
            <img src="https://www.svgrepo.com/show/13695/pdf.svg" width="100" style="margin-bottom: 20px; opacity: 0.7;">
            <h3>Welcome to your PDF Assistant!</h3>
            <p>Upload your documents and click on 'Process' to start chatting with your PDFs.</p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()