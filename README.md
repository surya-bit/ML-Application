# ML-Application
Receipt count prediction using XGBoost Regressor and LSTM
# File Structure:
1. The folder fetch-ML contains 4 different subfolders . The **Final** folder contains all the main files to run the model and host the website.
2. The other three subfolders are:
   1. **Linear Regression model** : This folder contains the ipynb folder, where I implemented a Linear Regression model. I initally fitted a linear line with just one X 
      predictor i.e dayofyear . But this gave me very high RMSE Value around  9551151 .I further changed the model by introduction l1 and l2 regularization terms and              increasing the data strength by appending more data columns like 'dayofweek','quarter' ,'month','dayofyear,'dayofmonth','weekofyear' . This further reduced the RMSE         Value . Even though the data follows a linear trend , the linear regression model performs poorly .
   2. **LSTM model** : This folder contains the ipynb folder, where I implemented a LSTM model. As this is a classic time series forecasting problem . I implemeted a              recurrent neural network with 467601 neurons. This model gave me a pretty descent RMSE value of 312023.15 . I used this model to predict with new test cases                 for year 2022 . A plot has been attached which shows the predicted monthly receipt counts for year 2022.
   3. **XGBoost model** : This folder contains the ipynb folder, where I implemented my final model using XGBoost regressor . Similar as what I did for the linear                 regression model ,I increased the strength of dataset appending more data columns. I trained with a set of hyperparamters . I was able to get an RMSE value of               218030.78, which is lesser than the other two models implemeted earlier.

Though I did a scratch level implemtation of linear regression and LSTM model . I will be using XGBoost Regressor for the following reasons :
   1. XGBoost provides a natural way to handle feature importance, which I think could be crucial in understanding the factors that contribute to the predictions.
   2. It is robust to outliers due to its tree-based structure.
   3. The predictions in LSTM model for year 2022 followed a non linear trend , which I think shouldn't happen as the data in 2021 is linear. XGBoost predictions follows a        linear trend as the kernel is itself linear.
   4. I was able to get a very less RMSE Value(218030.78) for XGBoost regressor as compared to others.
       
3. The main folder **Final** contains a client folder and **app.py** which is the server py file .

4. In the **server directory** is the **app.py** file which does the following functionalities :
   1. Import all the necessary libraries needed.The installation libraries are given below.
   2. Initialize the flask application.
   3. Load the model we trained before (xgb_model.pkl).
   4. The create_features function takes the date as input and creates additional columns such as 'dayofweek','quarter' ,'month','dayofyear,'dayofmonth','weekofyear',             drawing critical insights from the data and adding more strength to it.
   5. The value_for_month function takes user_input which is a month . This function uses the trained model to predict and return the receipt_count for that particular            month in year 2022.
   6. The data_for_month function takes user_input which is a month . This function uses the trained model to predict and return the receipt_count for all the days in that        particular selected month in year 2022.
   7. The data_for_year function just prints all the predicted receipt counts for year 2022.
   8. Define a single POST route ('/') to handle incoming search requests. The search function is executed when a POST request is made to the root endpoint ('/').
   9. Depending on the selected search option,It applies all the three functions and returns the json object which will be used in the client side.
   10. The application is run when the script is executed.

