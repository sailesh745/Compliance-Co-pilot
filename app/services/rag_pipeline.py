from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from app.services.embeddings import load_vectorstore
from app.core.config import settings

def get_rag_chain():
    db = load_vectorstore()
    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=settings.OPENAI_API_KEY
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
