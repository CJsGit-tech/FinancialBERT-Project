# MADS-Capstone: FinancialBERT-Project

## TextInspectorApp
The TextInspector app is designed to help future researchers review and conveniently edit their data. Here's the [video link](https://youtu.be/xK3TeFHRbTs) to our demonstration of this app. You can simple run this app locally by cloning this repo and run the requirements.txt for libraies install. After installation, go to the TextInspectApp folder and run
```
streamlit run main.py
```
Please note that this app is created for our datasets. This means that the app will only work properly only if your datasets contain columns of text, sentiment label, and topics. Feel free to modify the code when you see fit while you are continuing from where we left off.


## Overview of the project
The project aims to use transformer architecture for stock market index prediction, utilizing NLP models to extract text features. Specifically, we are using the [CLS] token. Nonetheless, we have noticed that research does not address the <b> potential sentiment leakage from building text features.</b> Therefore, we see this as a research opportunity in which we utilize the transformer architecture to perform text-based feature extraction and pay thoughtful attention to the aspect of sentiment leakage. 
```
An example of potential sentiment leakage from building text features can be that some words are found in 
the corpus between 2010 and 2018 but not in 2019 and above. Without proper corpus split based on timestamps, 
sentiment models peek into the future and understand the word “COVID” contributes to a negative financial movement.
```

## How to use the Repo

## Data Sources 
Our market index data came from the yahoo finance API, which was quite convenient to extract using python. Meanwhile, our text data was collected from various sources. These sources included 1) Kaggle 2) Financial Times 3) New York Times API. Since our news datasets did not have topics or sentiment labels attached to them. We utilized the pre-trained models to generate labels while assuming they were the experts in the financial industry. Generating the topic labels ensured that we kept news that were relevant to financial market movements. For example, topics like Politics and General Market.
1) [CNN](https://data.world/opensnippets/cnn-news-dataset) 
2) [Huffpost News Category](https://www.kaggle.com/datasets/rmisra/news-category-dataset)
3) [Financial News dataset for text mining](https://zenodo.org/record/5569113#.ZCUbfHZBwaa)
4) [New York Times API subscription may be required](https://developer.nytimes.com/apis)
