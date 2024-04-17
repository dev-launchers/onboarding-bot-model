from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_community.vectorstores import FAISS as VectorStore
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain.chains import ConversationalRetrievalChain

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
memory = ConversationBufferWindowMemory(memory_key="chat_history", ai_prefix="Chatbot", k=2)

chain = ConversationalRetrievalChain.from_llm(
    OpenAI(temperature=0), condense_question_prompt=prompt, retriever=retriever, memory=memory
)