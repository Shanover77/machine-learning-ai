# Assignment-1: News title category prediction | Word vectorization | Lemmatization | SVC

## Description
This repository sub-folder contains the code and resources for Assignment-1, which focuses on word vectorization for predicting the category of news titles. The goal of this assignment is to train a model on scraped data, consisting of news titles and their corresponding categories. The trained model will then be used to predict the category of new news titles.

Please note that this project is currently undergoing development and may not be in its final state.

## Approach
Our approach for this assignment involves the following steps:

1. Data Scraping: We have scraped a dataset of news titles along with their categories. The scraped data provides the training set for our model.

2. Word Vectorization: We employ word vectorization techniques to represent words in a numerical format suitable for machine learning models. By transforming words into vectors, we capture semantic relationships between words and enable machine learning algorithms to process textual data effectively.

3. Model Training: Using the word vectorized data, we train a model to predict the category of news titles. The choice of the model will depend on the specific requirements and characteristics of the dataset.

4. Evaluation: We assess the performance of the trained model using appropriate evaluation metrics, such as accuracy, precision, recall, or F1 score. This step helps us gauge how well the model performs in predicting the categories of news titles.

5. Prediction: Once the model is trained and evaluated, it can be used to predict the category of new news titles. By inputting a news title into the trained model, it will provide the corresponding category prediction.

## Repository Structure
The repository sub-folder 'Assignment-1' is organized as follows:

```
Assignment-1/
  ├── data/                   # Directory for storing the scraped data
  │   ├── business_news_data.csv
  │   ├── education_news_data.csv
  │   ├── entertainment_news_data.csv
  │   ├── environment_news_data.csv
  │   ├── health_news_data.csv
  │   ├── lifestyle_news_data.csv
  │   ├── politics_news_data.csv
  │   ├── programming_news_data.csv
  │   ├── sports_news_data.csv
  │   └── technology_news_data.csv
  ├── models/                 # Directory for storing trained models
  ├── src/                    # Source code directory
  │   ├── title_category_prediction.ipynb
  │   └── topic_title_scraper.ipynb
  ├── README.md               # Readme file (you are here)
  └── .gitignore              # Git ignore file to exclude certain files and directories

```

## Requirements
To run the code and replicate the project, the following dependencies need to be installed:

- Python 3.7 or above
- Libraries: numpy, pandas, scikit-learn, nltk (for preprocessing), and any additional libraries specified in the code

Ensure that the required packages are installed by running the following command:

```
pip install -r requirements.txt
```

## Usage
To use this repository, follow these steps:

1. Clone the repository:

```
git clone https://github.com/Shanover77/repo-name.git
```

2. Navigate to the 'Assignment-1' sub-folder:

```
cd Assignment-1
```

3. Store the scraped news data in the 'data' directory (e.g., 'news_data.csv').

4. Run the necessary preprocessing steps by executing the 'preprocessing.py' script:

```
python src/preprocessing.py
```

5. Train the predictive model using the 'model_training.py' script:

```
python src/model_training.py
```

6. Evaluate the model's performance and make predictions on new news titles as desired.

## Contributing
This project is currently undergoing development and is not open for contributions at the moment.

## License
This project is not licensed and is meant for educational purposes.

## Acknowledgments
We would like to acknowledge the contributions of all team members involved in this assignment. Their efforts have been instrumental in the progress made
