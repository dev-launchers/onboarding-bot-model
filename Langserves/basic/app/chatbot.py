from langchain.chains.question_answering import load_qa_chain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_community.vectorstores import FAISS as VectorStore
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain.chains import ConversationalRetrievalChain

import dotenv
dotenv.load_dotenv()

embeddings = GPT4AllEmbeddings()
store = VectorStore.load_local("app/vector_store", embeddings, allow_dangerous_deserialization=True)
retriever = store.as_retriever(search_kwargs={"k": 4})

template = """You are a chatbot having a conversation with a human.

Given the following extracted parts of a long document and a question, create a final answer.

{context}

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input", "context"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")

chain = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), condense_question_prompt=prompt, retriever=retriever, memory=memory)