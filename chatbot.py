# Import necessary libraries
from PyPDF2 import PdfReader
from transformers import pipeline

# Load the PDF file
def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()  # Fixed syntax issue here
    return text

# Initialize a simple chatbot
def chatbot():
    # Load the text from your PDF file
    pdf_text = load_pdf("example.pdf")  # Replace with your PDF file name
    
    # Load a question-answering model
    qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    
    print("Chatbot is ready! Ask your question (type 'exit' to quit):")
    while True:
        user_question = input("You: ")
        if user_question.lower() == "exit":
            print("Goodbye!")
            break
        # Check if the user question is empty
        if not user_question.strip():
            print("Please ask a valid question.")
            continue
        try:
            # Generate the response
            response = qa_model(question=user_question, context=pdf_text)
            print("Chatbot:", response["answer"])
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    chatbot()

