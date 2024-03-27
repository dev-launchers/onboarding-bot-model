from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter, HTMLHeaderTextSplitter, RecursiveCharacterTextSplitter

def markdowns_from(files_directory="../"):
    ## init
    docs = []
    # Load Files 
    loader = DirectoryLoader(path=files_directory, glob="**/*.md", loader_cls=TextLoader, show_progress=True, use_multithreading=True)
    documents = loader.load()

    # Split Markdowns by titles and subtitles 
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

    for document in documents:
        docs.extend(markdown_splitter.split_text(document.page_content))

    return docs


def html_from(files_directory="../"):
    ## init
    docs = []
    # Load Files 
    loader = DirectoryLoader(path=files_directory, glob="**/*.html", loader_cls=TextLoader, show_progress=True, use_multithreading=True)
    documents = loader.load()

    # Parametters :
    # Split HTML by header and subheader
    headers_to_split_on = [
        ("h1", "Header 1"),
        ("h2", "Header 2"),
        ("h3", "Header 3"),
    ]
    html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

    # Split large sentences by chunks
    chunk_size = 500
    chunk_overlap = 30
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    for document in documents:
        try:
            html_header_splits = html_splitter.split_text(document.page_content) # Split by tag
            splits = text_splitter.split_documents(html_header_splits) # Split by chunk

            docs.extend(splits)
        except:
            pass

    return docs