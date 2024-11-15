# **Multilingual News Summarization API**

This project provides a multilingual **news summarization** API, capable of generating concise summaries for articles in **English** and **Arabic**. The API utilizes the **Hugging Face mT5 model** fine-tuned for news summarization tasks, and is implemented using **FastAPI** for high performance and scalability.

## **Project Structure**

- **`app.py`**: FastAPI application serving the multilingual summarization model.
- **`notebooks/`**: Jupyter notebooks that cover the entire model development pipeline: data preparation, model selection, fine-tuning, and evaluation.
- **`requirements.txt`**: Lists all the Python dependencies required to run the project.
- **`Procfile`**: Configuration file for deployment (e.g., on Heroku).
- **`README.md`**: Documentation for setting up, running, and understanding the project.

## **Model Development Workflow**

This project includes detailed notebooks documenting the model development process, from data preparation through fine-tuning:

1. **`data_preparation`**: Data curation and preprocessing for training the multilingual summarization model. It includes steps for cleaning, tokenizing, and structuring the dataset.
2. **`model_selection`**: Evaluation of various pre-trained transformer models, including mT5, to identify the most suitable model for the summarization task.
3. **`fine_tuning`**: Fine-tuning the **mT5 model** on curated multilingual datasets (English and Arabic) to improve summarization accuracy.
4. **`evaluation`**: Evaluation of the fine-tuned model using **ROUGE metrics**, with a focus on summary quality, coherence, and relevance.

## **Running the API Locally**

### 1. Clone the repository:

```bash
git clone https://github.com/youssef-yasser-ali/multilingual-news-summarizer.git
```

### 2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI app:

```bash
uvicorn app:app --reload
```

### 4. Access the API:

Once the app is running, visit the following URL to interact with the API:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

The **Swagger UI** will provide an easy interface to interact with the API and test the summarization functionality.

## **API Usage**

### **Request Format**

You can send a `POST` request to the `/summarize` endpoint to generate a summary for any news article.

**Request Example:**

```json
{
  "text": "The global economy is facing challenges as inflation rises across major economies, impacting consumer spending..."
}
```

**Response Example:**

```json
{
  "summary": "The global economy is facing inflation challenges, affecting consumer spending across major economies."
}
```

### **Supported Languages**

Currently, the API supports **English** and **Arabic** news articles. The summarization model (`mT5`) was fine-tuned on multilingual datasets to provide accurate summaries in both languages.

## **Model Highlights**

- **Multilingual Summarization**: The system supports summarization of news articles in **English** and **Arabic**.
- **Transformer Model**: Built upon the **mT5 (Multilingual T5)** architecture, a state-of-the-art model for text-to-text tasks.
- **Evaluation Metrics**: The model's performance was evaluated using **ROUGE metrics**, ensuring the generated summaries are coherent and high-quality.
- **FastAPI Backend**: The API is built using **FastAPI**, providing asynchronous request handling for better performance and scalability.

## **Notebooks and Model Development**

The `notebooks/` directory includes the following key notebooks, which document the entire model development pipeline:

1. **`preparing_dataset.ipynb`**: Describes the data collection, cleaning, and preprocessing process for preparing multilingual datasets.
2. **`summarize-en-ar-news-mt5.ipynb`**:Covers the selection, fine-tuning, and evaluation of the mT5 model for summarizing English and Arabic news articles.

## **Key Features**

- **Multilingual Support**: Summarization of both **English** and **Arabic** news articles.
- **High-Quality Summaries**: The **mT5 model**, fine-tuned with ROUGE evaluation, produces accurate and coherent summaries.
- **Scalable API**: Built using **FastAPI** for fast, asynchronous handling of summarization requests, ready to be deployed in production environments.

## **Deployment**

To deploy this project to the cloud (e.g., **Heroku**, **AWS**, or **Azure**), follow the instructions provided in the `Procfile` for easy deployment configuration.
