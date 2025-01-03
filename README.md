# **Multilingual News Summarization API**

This project provides a multilingual **news summarization** API, capable of generating concise summaries for articles in **English** and **Arabic**. The API utilizes the **Hugging Face mT5 model** fine-tuned for news summarization tasks, and is implemented using **FastAPI** for high performance and scalability. Below is a step-by-step guide to running the API locally and interacting with it.

---

## **Live Demo**

You can try the **Multilingual News Summarization API** directly in your browser by visiting the Hugging Face Space:

👉 **[Live Demo on Hugging Face](https://huggingface.co/spaces/YoussefAnwar/News-Summerization)**

---

## **Project Overview**

### **Key Features**
- **Multilingual Support**: Summarize news articles in **English** and **Arabic**.
- **High-Quality Summaries**: Powered by the **mT5 model**, fine-tuned for accuracy and coherence.
- **Scalable API**: Built with **FastAPI** for fast and efficient request handling.
- **Easy Deployment**: Ready for deployment on platforms like **Heroku**, **AWS**, or **Azure**.

---

## **How to Run the API Locally**

### **Step 1: Clone the Repository**
Clone the project repository to your local machine:
```bash
git clone https://github.com/youssef-yasser-ali/multilingual-news-summarizer.git
cd multilingual-news-summarizer
```

### **Step 2: Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **Step 3: Run the FastAPI App**
Start the FastAPI server:
```bash
uvicorn app:app --reload
```

### **Step 4: Access the API**
Once the server is running, open your browser and navigate to:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

This will open the **Swagger UI**, where you can interact with the API and test the summarization functionality.

---

## **API Usage**

### **Request Format**
Send a `POST` request to the `/summarize` endpoint with the following JSON payload:

**Example Request:**
```json
{
  "text": "The global economy is facing challenges as inflation rises across major economies, impacting consumer spending..."
}
```

### **Response Format**
The API will return a summarized version of the input text:

**Example Response:**
```json
{
  "summary": "The global economy is facing inflation challenges, affecting consumer spending across major economies."
}
```

---

## **Supported Languages**
The API currently supports **English** and **Arabic** news articles. The **mT5 model** was fine-tuned on multilingual datasets to ensure high-quality summaries in both languages.

---

## **Model Development Workflow**

The project includes detailed Jupyter notebooks in the `notebooks/` directory, covering the entire model development pipeline:

1. **`data_preparation`**: Data collection, cleaning, and preprocessing.
2. **`model_selection`**: Evaluation of pre-trained models for summarization tasks.
3. **`fine_tuning`**: Fine-tuning the **mT5 model** on multilingual datasets.
4. **`evaluation`**: Performance evaluation using **ROUGE metrics**.

---

## **Deployment**

To deploy the API to a cloud platform (e.g., **Heroku**, **AWS**, or **Azure**), follow the instructions in the `Procfile` for easy configuration.

---

## **Try It Out!**

👉 **[Live Demo on Hugging Face](https://huggingface.co/spaces/YoussefAnwar/News-Summerization)**

---

This project is designed to be user-friendly, scalable, and ready for production use. Whether you're summarizing news articles for research, business, or personal use, this API has you covered! 🚀
