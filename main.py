from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from google import genai
from google.genai import types
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

# Load environment variables from .env file
load_dotenv()

pdf_path = Path(__file__).parent / "data" / "little_red_riding_hood.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# print(docs[12])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

split_docs = text_splitter.split_documents(documents=docs)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=os.getenv("GEMINI_API_KEY"))


# Use the Google Generative AI model to generate a response
while True:
    print("1. store")
    print("2. ask")

    choice = input("Please select whether you want to store document or ask question on stored document (store/ask): ")

    if choice.lower() == 'store':
        vector_store = QdrantVectorStore.from_documents(
            documents=[],
            collection_name="learning_lanchain",
            url="http://localhost:6333",
            embedding=embeddings,
        )

        vector_store.add_documents(split_docs)
        print("Document stored successfully.")
        break
    elif choice.lower() == 'ask':
        retriever = QdrantVectorStore.from_existing_collection(
            collection_name="learning_lanchain",
            url="http://localhost:6333",
            embedding=embeddings,
        )
        user_input = input("Enter your question (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        relevant_chunks = retriever.similarity_search(query=user_input)

        SYSTEM_PROMPT = f"""
        You are a helpful assistant that answers questions based on the provided context.

        context: {relevant_chunks}
        """

        # Generate a response using the Google Generative AI model
        system_prompt = SYSTEM_PROMPT
        response = client.models.generate_content(
                model="gemini-2.0-flash", 
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                ),
                contents=user_input,
            )
        print("Response:", response.text)
        break
    else:
        print("Invalid choice. Please enter 'store' or 'ask'.")