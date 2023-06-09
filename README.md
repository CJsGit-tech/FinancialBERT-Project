# MADS-Capstone: FinancialBERT-Project

## Overview of the project
The project aims to use transformer architecture for stock market index prediction, utilizing NLP models to extract text features. Specifically, we are using the [CLS] token. Nonetheless, we have noticed that research does not address the <b> potential sentiment leakage from building text features as well as lacking cross validation results of model performances.</b> Therefore, we see this as a research opportunity in which we utilize the transformer architecture to perform text-based feature extraction and pay thoughtful attention to the aspect of sentiment leakage. 
```
An example of potential sentiment leakage from building text features can be that some words are found in 
the corpus between 2010 and 2018 but not in 2019 and above. Without proper corpus split based on timestamps, 
sentiment models peek into the future and understand the word “COVID” contributes to a negative financial movement.
```
<p align="center">
  <img src='visualizations/model_architecture.PNG' height=300px width=400px> </img>
</p>


[LINK TO OUR REPORT](https://drive.google.com/file/d/12Ceu-oVn9y0euJOsCV8bOmGvYbsjH1X6/view?usp=share_link)

## How to use the Repo
**sample notebooks**<br>
This folder contains most of the compnents to allow future researchers to replicate our work. You will find a few notebooks dedicate to data processing and some others are model building. Under this folder there are subfolders titled in 
1) data (where datasets and models are saved) <br>
2) DataProcessing (EDA and label generation) <br>
3) Modeling (Models for Regression and Classification)
<br>

**txtInspect**<br>
This folder has the original code for our text inspector app. This app is desinged for reviewing your processed data in a web application fashion. Meanwhile, it provides interactive components where users could modify dataset and download it as a new copy.
<br>

**visualizations**<br>
This folder includes our results and a few visualizations that we constructed for our report. See report link.


## TextInspectorApp
The TextInspector app is designed to help future researchers review and conveniently edit their data. Here's the [video link](https://youtu.be/xK3TeFHRbTs) to our demonstration of this app. You can simple run this app locally by cloning this repo and run the requirements.txt for libraies install. After installation, go to the TextInspectApp folder and run
```
streamlit run main.py
```
Please note that this app is created for our datasets. This means that the app will only work properly only if your datasets contain columns of text, sentiment label, and topics. Feel free to modify the code when you see fit while you are continuing from where we left off.

## Data Sources 
Our market index data came from the yahoo finance API, which was quite convenient to extract using python. Meanwhile, our text data was collected from various sources. These sources included 1) Kaggle 2) Financial Times 3) New York Times API. Since our news datasets did not have topics or sentiment labels attached to them. We utilized the pre-trained models to generate labels while assuming they were the experts in the financial industry. Generating the topic labels ensured that we kept news that were relevant to financial market movements. For example, topics like Politics and General Market.
1) [CNN](https://data.world/opensnippets/cnn-news-dataset) 
2) [Huffpost News Category](https://www.kaggle.com/datasets/rmisra/news-category-dataset)
3) [Financial News dataset for text mining](https://zenodo.org/record/5569113#.ZCUbfHZBwaa)
4) [New York Times API subscription may be required](https://developer.nytimes.com/apis)
