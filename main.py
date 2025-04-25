from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

pdf_path = Path(__file__).parent / "data" / "Array.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

print(docs[12])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

texts = text_splitter.split_documents(documents=docs)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


result = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=texts)

print(result.embeddings)


def main():
    print("Hello from ai-pdf-reader!")


if __name__ == "__main__":
    main()
