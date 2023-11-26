# ML-Application
Receipt count prediction using XGBoost Regressor and LSTM
# File Structure and Code Explanation:
1. The folder final-fetch contains 4 different subfolders . The **Final** folder contains all the main files to run the model and host the website.
2. The other three subfolders are:
   1. **Linear Regression model** : This folder contains the ipynb folder, where I implemented a Linear Regression model. I initally fitted a linear line with just one X 
      predictor i.e dayofyear . But this gave me very high RMSE Value around  9551151 .I further changed the model by introduction l1 and l2 regularization terms and              increasing the data strength by appending more data columns like 'dayofweek','quarter' ,'month','dayofyear,'dayofmonth','weekofyear' . This further reduced the RMSE         Value . Even though the data follows a linear trend , the linear regression model performs poorly .
   2. **LSTM model** : This folder contains the ipynb folder, where I implemented a LSTM model. As this is a classic time series forecasting problem . I implemeted a              recurrent neural network with 467601 neurons. This model gave me a pretty descent RMSE value of 312023.15 . I used this model to predict with new test cases                 for year 2022 . A plot has been attached which shows the predicted monthly receipt counts for year 2022.
   3. **XGBoost model** : This folder contains the ipynb folder, where I implemented my final model using XGBoost regressor . Similar as what I did for the linear                 regression model ,I increased the strength of dataset appending more data columns. I trained with a set of hyperparamters . I was able to get an RMSE value of               218030.78, which is lesser than the other two models implemeted earlier.

   Though I did a scratch level implemtation of linear regression and LSTM model . I will be using XGBoost Regressor for the following reasons :
      1. XGBoost provides a natural way to handle feature importance, which I think could be crucial in understanding the factors that contribute to the predictions.
      2. It is robust to outliers due to its tree-based structure.
      3. The predictions in LSTM model for year 2022 followed a non linear trend , which I think shouldn't happen as the data in 2021 is linear. XGBoost predictions follows          a linear trend as the kernel is itself linear.
      4. I was able to get a very less RMSE Value(218030.78) for XGBoost regressor as compared to others.
       
3. The main folder **Final** contains a client folder and **app.py** which is the server py file .

4. The **app.py** file which does the following functionalities :
   1. Import all the necessary libraries needed.The installation libraries are given below.
   2. Initialize the flask application.
   3. Load the model we trained before. Download the model from here https://drive.google.com/drive/folders/19CRYp8LyB3WIlZOWcGwXXF2W3EXHppKW?usp=sharing . You should copy 
      the model in the Final folder.
   4. The create_features function takes the date as input and creates additional columns such as 'dayofweek','quarter' ,'month','dayofyear,'dayofmonth','weekofyear',             drawing critical insights from the data and adding more strength to it.
   5. The value_for_month function takes user_input which is a month . This function uses the trained model to predict and return the receipt_count for that particular            month for year 2022.
   6. The data_for_month function takes user_input which is a month . This function uses the trained model to predict and return the receipt_count for all the days in that        particular selected month for year 2022.
   7. The data_for_year function just prints all the predicted receipt counts for year 2022.
   8. Define a single POST route ('/') to handle incoming search requests. The search function is executed when a POST request is made to the root endpoint ('/').
   9. Depending on the selected search option,It applies all the three functions and returns the json object which will be used in the client side.
   10. The application is run when the script is executed.

5. The main file **app.jsx** which does the functionality of front end is found in the **Final/client/src** directory.
    1. Import various dependencies and assets, including React hooks (useState, useEffect), Axios for making HTTP requests.
    2. Do the state management.
    3. The useEffect hook is triggered when the query state changes.If the query is not empty, it sends a POST request to the specified API endpoint with the search 
       parameters and updates the results state with the response data.
    4. I have used chartjs2 to create a interactive line chart visualization which updates based on user input.
    5. UI rendering and CSS styling is done accordingly.
    6. The server communication component communicates with a server located at http://127.0.0.1:5000. It sends a POST request to this server when the user performs a 
       search. 

# Installation libraries :
There is requirements file at **Final** which has all the libraries needed to run the code.
python3, node , npm , flask , pip , tensorflow ,numpy, pandas, xgboost,joblib,flask_cors,calender.

# Instructions on how to run the tool locally :
1. Move to the Final/client folder and run the command : npm i (Installs all the packages)
2. Open a new terminal and move into Final where the app.py server code is : run python app.py
3. This will start server on port 5000 . (http://localhost:5000)
4. Move to the client folder again and run the command : npm run dev (Starts client side program)
5. Navigate to http://localhost:5173 or any of the networks displayed.
6. Dockerfile is also included in the repo and I think this is the right way to run the model.You can also build the container locally:
   1. To build a client :
      1. Navigate to the client folder. Run : docker build -t client .
      2. docker run -p 5173:5173 client
   2. To build the server:
      1. Navigate to the Final folder. Run : docker build -t server .
      2. docker run -p 5000:5000 server
7. Select one of the options (Month in 2022) . 
9. The first value is the predicted receipt count for that selected month.
10. The next visualization is a line chart which shows the predicted receipt counts for all the days in that selected month. Feel free to hover over the plot and check the readings
11. The last plot is a line chart which shows the values predicted for the entire year(2022).

# Output :

**Predicted Receipt counts for the month selected**

<img width="597" alt="pic1" src="https://github.com/surya-bit/ML-Application/assets/61753483/e42605c8-1ec3-460b-b397-257e1a89f3c9">


**Predicted Receipt counts for all the days in the month selected**

<img width="947" alt="pic2" src="https://github.com/surya-bit/ML-Application/assets/61753483/1d7d0ae0-6c0b-45e6-9bb0-ce5aa40e7956">

**Predicted Receipt counts for the entire 2022 year**

<img width="952" alt="pic3" src="https://github.com/surya-bit/ML-Application/assets/61753483/c15783ff-80c6-4db1-a7f1-b3ad3b2e6263">


# Instructions on how to run the tool locally on docker containers :
Two dockerfiles have been created . One for client and other for server. These files could be found on their respective directorier in Final Folder
1. I have packaged my app in a Docker containers .Please feel free to pull it from DockerHub by running the below commands :
   1. docker pull suryarajmachani/fetch-ml-project:client
   2. docker pull suryarajmachani/fetch-ml-project:server
2. To build and run locally . Follow the instructions below:
   1. Run the command : docker run -p 5000:5000 suryarajmachani/fetch-ml-project:server
   2. Run the command : docker run -p 5173:5173 suryarajmachani/fetch-ml-project:client
3. Navigate to http://localhost:5173 
