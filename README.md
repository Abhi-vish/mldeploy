
# Admission Prediction

This is an admission prediction feature based on a linear model trained on a dataset containing 400 records. This model aims to predict the likelihood of admission to a university based on various factors.
## Dataset

The training dataset, named "admission_predict.csv," is a collection of records that includes the following features:

- GRE Score: The score obtained in the Graduate Record Examination.

- TOEFL Score: The score obtained in the Test of English as a Foreign Language.

- University Rating: The rating of the university attended by the applicant (on a scale of 1 to 5).

- Statement of Purpose (SOP): The quality of the applicant's statement of purpose (on a scale of 1 to 5).

- Letter of Recommendation (LOR): The strength of the applicant's letter of recommendation (on a scale of 1 to 5). 

- CGPA: The Cumulative Grade Point Average achieved by the applicant.

- Research: Whether or not the applicant has research experience (0 for no, 1 for yes).
## Screenshots

#### 1. This is the homePage of the website

![home_page](https://github.com/Abhi-vish/mldeploy/assets/109618783/e33993f3-dc5c-4c10-a617-fb626a58c716)


#### 2. This is the Prediction Page Where, we have to enter Details, then it will send, Details to model, then model will predict the Prediction

![prediction_page](https://github.com/Abhi-vish/mldeploy/assets/109618783/28b8dec0-b9ca-44ec-92d0-c70fec32f42b)

#### 3. This is the output page where it will show the result of the prediction

![output_page](https://github.com/Abhi-vish/mldeploy/assets/109618783/8d0e1cb3-db81-4fc5-8585-781960ae34a1)
## Virtual Environment 


To run this project without affecting your system environment, create a virtual environment by executing the following command:

"Create a virtual environment to ensure that the project runs smoothly without any impact on your system's environment."

`python -m venv <env_name>`



## Installation

#### Install my-project in your envrionment

`step1 : clone the repo` 
- `https://github.com/Abhi-vish/mldeploy.git`

`step2 : install requirements.txt package by running commnad`
- `pip install  -r requirements.txt`

`step3 : open terminal and run commnad`
- `python app.py `
    
    
## 🚀 About Me
I'm a student...


## Lessons Learned

While building this project, I learned several key concepts and faced various challenges. Here are the details:

- I learned about Linear Regression and its application in predicting outcomes based on continuous variables.
- I gained knowledge about feature selection techniques, including methods to identify and handle collinearity and multicollinearity in the dataset.
- I became familiar with preprocessing techniques such as standard scaling, which helps in normalizing the features to ensure fair comparisons.
- I also learned about the variance influence factor and its significance in understanding the impact of individual data points on the overall model.
- Throughout the project, I worked with different libraries and tools to handle and preprocess the data effectively, ensuring its suitability for the machine learning algorithms.

