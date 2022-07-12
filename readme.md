<h1>README Submission</h1>
herokuapp: https://noshow-ml.herokuapp.com/<br><br>
-----------------<br>

This project has been uploaded onto heroku <br>



The section as follow<br>
1. Overview of the submitted folder and the folder structure.<br>
2. Assumptions <br>
3. Data Cleaning and EDA<br>
4. EDA Results<br>
3. Machine Learning models<br>
6. Deployment<br>
7. Instructions for executing the pipeline and modifying any parameters.<br>

<h2>1. Overview of the submitted folder and the folder structure</h2>
├── src<br>
│   └── templates<br>
│    .   └── index.html<br>
│   └── appy.py<br>
│   └── main.ipynb<br>
│   └── decisiontree<br>
│   └── lgbm_model<br>
│   └── xgboost<br>
├── README.md<br>
├── eda.ipynb<br>
├── requirements.txt<br>




<h2>1. Overview of the submitted folder and the folder structure</h2>
<img alt="alt_text" src="https://github.com/nnnvnnn/NoShow-Heroku/blob/main/Capture.PNG" /><br>
<h2>2. Assumptions</h2>
1. Prices that are stated <i>none</i> to be assumed guests received free hotel stays, be it via vouchers or giveaways etc. Hence, <i>none</i> are converted to <i>SGD $0.00</i><br>
2. Prices that are in USD will be converted to SGD, assuming real-time conversion.
3. Year for dates (arrival and checkout) are not given, only month and day are given. Hence, arrival date and checkout date are concated with corresponding month and day. Year is assumed to be 2020 or 2019 depending on checkout and arrival date. <br><br>



<h2>3. Data Cleaning and EDA</h2>
Data is "cleaned" with ealier assumptions. Graphs and numerical statistics show the No Show cusomters demographics. Categorical data was also one-hot encoded for better results. 

<h2>4. EDA Results</h2>
The average loss amount incurred due to No-Show Customers is SGD$695.69 and the maximum is SGD$2119.71<br>
On average, the no shows tend to book 5.38 months in advanced and tend to book for a stay of an average of 2.16 days.<br>

<h2>5.Machine Learning</h2>
5 models were executed, 1. XGBoost, 2. LightGBM, 3. Decision Tree, 4. Random Forest 5. Neural Network.<br><br>
All models are capable of large data and categorical data, though we have already one-hot enconded the categorical data.<br>
All models are compared with accuracy, precision and f1 scores. <br><br>
The top 3 performing ones are <b>1. XGboost 2. Decision Tree and 3. Neural Netowork.</b> Hence these 3 models were chosen for deployment<br>

<h2>6. Deployment</h2>
Once machine learning model has been chosen, we allow for deployment using user inputs.<br>
A simple locally-hosted web app was created, that reads users' input and predicts the No-Show of customers based on the selected 3 models. <br>

<h2>7. Instructions for executing the pipeline and modifying any parameters.<br></h2>
Run eda.ipynb first for data cleaning then run src/main.py
