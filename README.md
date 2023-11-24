# ML-Application
Receipt count prediction using XGBoost Regressor and LSTM
# File Structure:
1. The folder fetch-ML contains 4 different subfolders . The Final folder contains all the main files to run the model and host the website.
2. The other three subfolders are:
   1. Linear Regression model : This folder contains the ipynb folder, where I implemented a Linear Regression model. I initally fitted a linea line with just one X 
      predictor i.e dayofyear . But this gave me very high RMSE Value around  9551151 .I further changed the model by introduction l1 and l2 regularization terms and              increasing the data strength by appending more data columns like 'dayofweek','quarter' ,'month','dayofyear,'dayofmonth','weekofyear' . This further reduced the RMSE         Value . Even though the data follows a linear trend , the linear regression model performs poorly .
       
4. Renamed the brand_belongs_to_category to product_category as both conveyed the same information.
5. Dropped the category_id from the categories.
6. Performed an outer merge on all the three datasets and dropped the missing values. 

7. In the server directory is the server.py file which does the following functionalities :
   1. Import all the necessary libraries needed.The installation libraries are given below.
   2. Initialize the flask application.
   3. Load the BERT model and tokenizer.
   4. Define a function compute_cosine_similarity to calculate cosine similarity between a query and a set of text embeddings.
   5. Define the search functions . These functions filter the dataset based on the user's input for category, brand, or retailer, respectively.
   6. Defines a function compute_similarity that takes a query and a list of texts as input. It tokenizes the query and texts, obtains BERT embeddings for them, and then 
      calculates cosine similarity scores between the query and each text.
   7. Define a single POST route ('/') to handle incoming search requests. The search function is executed when a POST request is made to the root endpoint ('/').
   8. Depending on the selected search option, it calls one of the three search functions ('search_by_category', 'search_by_brand', or 'search_by_retailer') to filter the 
      dataset based on the user's input.
   9. If relevant offers are found in the dataset, it calculates similarity scores between the user's input and the offers using the compute_similarity function. It then 
      adds these scores to the DataFrame, sorts the offers by similarity score in descending order, and converts the relevant offers and their similarity scores to JSON.
   10. The application is run when the script is executed.

