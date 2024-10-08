from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_community.vectorstores import FAISS as VectorStore
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain.chains import ConversationalRetrievalChain

embeddings = GPT4AllEmbeddings()
store = VectorStore.load_local("app/vector_store", embeddings, allow_dangerous_deserialization=True)
retriever = store.as_retriever(search_kwargs={"k": 4})
llm = HuggingFaceHub(repo_id="google/flan-t5-large")

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
    llm=llm, condense_question_prompt=prompt, retriever=retriever#, memory=memory
)

### New chains can be added like this before being added as a route in server.py
##
#

## Online exemple using Hugging Face API (model under 10Gb with free version)
HF_flan_t5 = ConversationalRetrievalChain.from_llm(
    llm = HuggingFaceHub(repo_id="google/flan-t5-large"), 
    condense_question_prompt = prompt, 
    retriever = retriever
    #, memory= memory
)

## Local exemple from Hugging Face Hub (download on your server)
Home_dolly_2 = HuggingFacePipeline.from_model_id(
    model_id="databricks/dolly-v2-3b",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 10},
)