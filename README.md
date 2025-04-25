# PDF Query with LangChain

This project allows you to query PDF documents using LangChain and Google GenAI. It is designed to extract and process information from PDF files efficiently.

## Features
- Query PDF documents using natural language.
- Leverage LangChain and Google GenAI for advanced language processing.
- Easy setup and deployment using `uv`.

## Prerequisites
- Python 3.13 or higher.
- Docker and Docker Compose installed on your system.

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd pdf_query_langchain
```

### 2. Install Dependencies
This project uses `uv` for dependency management. To set up the environment, run:
```bash
uv sync
```

### 3. Add Your PDF Files
Place your PDF files in the `data/` directory. For example:
```
data/
  little_red_riding_hood.pdf
```

### 4. Run the Application
Start the application using Docker Compose:
```bash
docker-compose up
```

The application will be available at `http://localhost:8000`.

## Usage
- Access the application in your browser.
- Upload or select a PDF file from the `data/` directory.
- Enter your query in natural language to extract information from the PDF.

## Project Structure
```
.
├── data/                     # Directory for storing PDF files
├── docker-compose.yml        # Docker Compose configuration
├── main.py                   # Main application script
├── pyproject.toml            # Project configuration
├── README.md                 # Project documentation
├── uv.lock                   # Dependency lock file
```

## Dependencies
The project uses the following key dependencies:
- `langchain`
- `google-genai`
- `pypdf`
- `dotenv`

For a full list of dependencies, see the `uv.lock` file.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.