# The current Python file was created to define a module that contains the function query_question from the Jupyter Notebook 02_RAG_process.
# And use it to perform the ROUGE metric in the 03_Test Jupyter Notebook
# To make the ROUGE's results more "readable", most of the prints from the original function will be deleted,
# reducing the noice that the print of the chunks (for example) could generate.

# Import the needed libraries

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

# Define the configuration for the needed to use Ollama

VECTOR_DATABASE_PATH = r"C:\Users\lonel\OneDrive\Escritorio\Re Zero NLP Project\vector_database"
MODEL_NAME = "llama3.1:8b"

# Initialize the Embedding Model

embedding_model = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

# Connect the embedding model to the vector database

vector_database = Chroma(persist_directory=VECTOR_DATABASE_PATH,
                        embedding_function=embedding_model)

# Connect to Ollama

llm = ChatOllama(model=MODEL_NAME)

# Create a function that performs the vector similarity search

def query_question(question):
    """The current function takes as the input a question in the Terminal"""

    print("Searching in the vector database for the question {}".format(question))

    # Perform the search (Retrieve)

    retrieves = vector_database.similarity_search(question, k=3) # K is the number of chunks the model will retrieve to answer the question.

    if not retrieves:
        print("No relevant information found with the current data stored in my memory. Try adding more data.")
        return
    
    # Combine the retrieved text into one context block

    context_text = "\n\n---\n\n".join([retrieve.page_content for retrieve in retrieves])

    # Define the prompt to guide the answer (Augment)

    prompt = f"""
    You are a helpful assistant for the novel Re:Zero. 
    Use the following pieces of retrieved context to answer the user's question.
    If the answer is not in the context, just say that you don't know.
    
    Context:
    {context_text}
    
    Question:
    {question}
    
    Answer:
    """

    # Ask to the LLM (Generate)

    print("The LLM has been asked the question and is now generating the answer!")

    response = llm.invoke(prompt)

    # Print the result

    print("\n" + "="*30)
    print(f"Question: {question}")
    print(f"Answer: {response.content}")
    print("="*30)

    # Return the result to use it in ROUGE test

    return response.content