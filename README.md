# Streamlit App: Movie Review Sentiment Classifier

This project is a Movie Review Sentiment Classifier created using a Streamlit app and a machine learning pipeline. It analyzes IMDB movie reviews to predict whether the user's review is **positive** or **negative**. The model was trained using a Naive Bayes classifier with TF-IDF vectorization on a labeled dataset of movie reviews. Users can input a movie review into the app, and it will display the predicted sentiment along with the model's confidence level.

---



## Note: Docker is needed to be installed and running on your machine:

- [Docker](https://www.docker.com/) 

---

## How to Run

Follow these steps to build and run the application in a Docker container:

1. **Clone this repository:**

   ```bash
   git clone <YOUR_REPO_URL>
   cd <YOUR_PROJECT_DIRECTORY>

2. **Build the Docker image:**

   ```bash
   docker build -t sentiment-app .

3. **Run Docker:**

   ```bash
   docker run -d -p 8501:8501 --name sentiment-container sentiment-app

4. **Open the app in web browser by visiting:**

http://localhost:8501

You should see the Streamlit local site where you can enter a review and have it analyzed!





