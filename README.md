# Multilingual News Summarization API with FastAPI and Hugging Face

This project provides a web API for multilingual news summarization using the Hugging Face `mt5-summarize-ar-en` model. The API is built using FastAPI and supports text summarization in multiple languages.

## Structure

- `app.py`: FastAPI application for serving the model.
- `notebooks/`: Jupyter notebooks for model development, including data preparation, model selection, and fine-tuning.
- `requirements.txt`: Required Python dependencies.
- `Procfile`: Deployment configuration (if using Heroku).

## Running the API Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/$REPO_NAME.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI app:
   ```bash
   uvicorn app:app --reload
   ```

4. Access the API at `http://127.0.0.1:8000/docs`.

## Notebooks

- **data_preparation.ipynb**: Steps for preparing the dataset for fine-tuning.
- **model_selection.ipynb**: A notebook where different models are evaluated.
- **fine_tuning.ipynb**: The notebook used for fine-tuning the model on the summarization task.
