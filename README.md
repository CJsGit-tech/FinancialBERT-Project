# MADS-Capstone: FinancialBERT-Project

## TextInspectorApp
The TextInspector app is designed to help future researchers review and conveniently edit their data. Here's the video link to our demonstration of this app. You can access this app via streamlit cloud. [LINK]

## Overview of the project
The project aims to use transformer architecture for stock market index prediction, utilizing NLP models to extract text features. Specifically, we are using the [CLS] token. Nonetheless, we have noticed that research does not address the <b> potential sentiment leakage from building text features.</b> Therefore, we see this as a research opportunity in which we utilize the transformer architecture to perform text-based feature extraction and pay thoughtful attention to the aspect of sentiment leakage. 
```
An example of potential sentiment leakage from building text features can be that some words are found in 
the corpus between 2010 and 2018 but not in 2019 and above. Without proper corpus split based on timestamps, 
sentiment models peek into the future and understand the word “COVID” contributes to a negative financial movement.
```

## Repo Structure Overview
visualizations
- A
- B
- C

utils
- A
- B
- C

sample notebooks
- A
- B
- C

## Data Sources 
- A
- B
- C
- D
