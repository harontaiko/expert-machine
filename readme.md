## Expert Machine Learning system
A dairy farming expert system, based on support vector machines, natural language processing and openAI.

## Classification process
Preparation for the data for classification: Extracting relevant features like "milk production", "breed of cattle", "feed quality", etc.

Training the SVM classifier: By splitting the data into training and testing sets, and using the training set to train the SVM classifier.(Scikit-learn)

Classify the new document: We extract the features from the prompt and use the classifier to predict the class.

Finally, we output the result as a Python JSON output along with the recommendation. 

## Datasets used
- Guide to good dairy farming practice. (FOOD AND AGRICULTURE ORGANIZATION OF THE UNITED NATIONS)
- Introduction to dairy farming. (National Council of Educational Research and Training)

## Features
- Natural language processing
- Classification
- Tokenization

## installation
- Pre requisites `python`, `nodejs`, `npm` and `pip`
- run `npm install` and `pip install`
- rub `npm run dev`
- open app on (port 3000)[http://localhost:3000]

## test questions
- What is the best feed for lactating cows?
- How do I prevent mastitis in my herd?
- What is the ideal temperature range for dairy cows?
- What is the recommended vaccination schedule for calves?