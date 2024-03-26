from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter

def create_db(path='../', glob="**/*.md",split=None):
    # Load Files 
    loader = DirectoryLoader(path, glob=glob, loader_cls=TextLoader, show_progress=True, use_multithreading=True)
    documents = loader.load()

    # Split Markdowns by titles and subtitles 
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]

    # Except Split 
    if split:
        headers_to_split_on = split

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    
    docs = []

    for document in documents:
        docs.extend(markdown_splitter.split_text(document.page_content))

    return docs