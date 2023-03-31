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

## complex questions
What are the most effective ways to prevent and control mastitis in dairy cows?
How do different types of feed and grazing systems affect milk production and cow health?
What are the economic and environmental impacts of different manure management strategies in dairy farming?
What is the role of genetics in determining milk yield, composition, and quality in dairy cows?
How can precision dairy farming technologies, such as automated milking systems and sensors, be used to optimize cow health and milk production?
What are the best practices for ensuring animal welfare in dairy farming, including housing, handling, and transportation?
How can dairy farmers effectively manage and mitigate the risk of disease outbreaks, such as foot-and-mouth disease or bovine tuberculosis?
What are the most effective strategies for reducing greenhouse gas emissions from dairy farming, including methane emissions from enteric fermentation and manure management?
What are the factors that influence the quality and safety of milk, including milk testing, processing, and storage?
How can dairy farmers best balance the demands of milk production with the need to conserve and protect natural resources, such as soil, water, and biodiversity?