# Telco Customer Attrition Model


## Problem Statement

> There is a big difference between a satisfied customer and a loyal customer - Shep Hyken

With spewing yet saturated competitions in the telecommunication industry, in order to stay ahead in the competition, customer satisfaction should always the heart of the business model with customer attrition as long-term strategy.

Customer Attrition is also known as customer churn where customer ends the commercial relationship with the business. Customer lifetime value (CLTV) an important key metric to measure the health of business. Since change is inevitable, the business's main goal is to increase customer retention.

Churn rate is expressed as a rate that indicates the number of customers lost over a given period of time. With the cost of acquisition often greater than customer retention [(Customer Retention Strategy, 2016)](https://blog.exitbee.com/8-simple-customer-retention-strategies-to-decrease-your-churn-rate/), being able to identify why and when a customer is leaving, allows business to take on proactive approach to win the customer back. 


## Executive Summary  

<<<<<<< HEAD
Aligned with the general marketing strategy, the first step to customer-driven business is to understand our customer base. Customer behaviour also known as customer segmentation aids to provide a strong value proposition. Using analytics, the customer database are segmented into 4 clusters, namely **Vanilla**, **Heavyweight**, **Minimalist** and **Price-Sensitive**. 
=======
Aligned with the general marketing strategy, the first step to customer-driven business is to understand our customer base. Customer behaviour clustering also known as customer segmentation aids to provide a strong value proposition. Using analytics, the customer database are segmented into 4 clusters, namely **Vanilla**, **Heavyweight**, **Minimalist** and **Price-Sensitive**. 
>>>>>>> 332d68f8db9ee29ad79726ee76e5c67ceb71627e

With the cluster identified, we will process this as part of the classification model to learn what other features affecting the customer churn for instance, married users are 1.51 times more likely to churn, whereas contract users of two years are 0.43 times more likely to stay. 

In summary, internet_service using fiber optic, payment method using electronic check, offer E, and streaming tv services are features that the business needs to look into. The driving factors that affects the customer churn are 1) month-to-month basis contract customers which naturally allows leeway for customer to leave as and when intended, 2) payment via electronic checks, 3) fibre optic internet services and 4) streaming services connectivity which requires more investigation on the logistics and hardware and why has it been a setback to the business. Alternatively, the long term contracts, online security, tech support, online back up has prove to be a value-added service to the users as the subscription to it led to user more likely to stay with the business. 

As a direct call to action, the customers has been identified in simpler fashion for marketing / management's action. The below are namely the customer quadrant that allows a relatively simple decision making on its retention plans.
![Customer Quadrant](/images/cluster_quadrant.png)

Finally, as recommendation, such model of customer attrition is able to be further developed for different business models. With modification on the features and especially on the customer segmentation, the model will be able to predict for business customer churn anticipation. 

### Data Dictionary

The following are the data dictionary for the features used in the analysis and modelling.

|                 Feature             |  Type   |                           Description                            |
|-------------------------------------|---------|------------------------------------------------------------------|
|               customer_id           | object  | Customer unique identification number |
|                 gender              | integer | Gender identification of customer in binary (1 - Female, 0 - Male ) |
|                  age                | integer | Age of customer |
|                under_30             | integer | Age category of customer under 30 years old in binary ( 1- Yes, 0 - No) |
|             senior_citizen          | integer | Age category of customer above 65 years old in binary ( 1- Yes, 0 - No) |
|                 married             | integer | Marriage status of customer ( 1- Yes, 0 - No) |
|               dependents            | integer | Status if the customer lives with any dependents: grandparents and childen inclusive ( 1- Yes, 0 - No) |
|         number_of_dependents        | integer | Indicates the number of dependents that live with the customer |
|                 city                | object  | Customer's primary residence  |
|               zip_code              | integer | Zipcode of customer's primary residence |
|               latitude              |  float  | The latitude of the customer’s primary residence |
|              longitude              |  float  | The longitude of the customer’s primary residence |
|             tenure_months           | integer | Total amount of months that the customer has been with the business nby the end of the quarter |
|             phone_service           | integer | Indicates if the customer subscribes to home phone service with the company ( 1- Yes, 0 - No) |
|            multiple_lines           | integer | Indicates if the customer subscribes to multiple telephone lines with the company (1- Yes, 0 - No) |
|           internet_service          | object  |   Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic, Cable |
|              online_security        | integer | Indicates if the customer subscribes to an additional online security service provided by the company (1- Yes, 0 - No) |
|             online_backup           | integer | Indicates if the customer subscribes to an additional online backup service provided by the company (1- Yes, 0 - No) |
|          device_protection          | integer | Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company (1- Yes, 0 - No) |
|            tech_support             | integer | Indicates if the customer subscribes to an additional technical support plan from the company (1- Yes, 0 - No) |
|            streaming_tv             | integer | Indicates if the customer uses their Internet service to stream television programing from a third party provider (1- Yes, 0 - No) |
|           streaming_movies          | integer | Indicates if the customer uses their Internet service to stream movies from a third party provider (1- Yes, 0 - No) |
|               contract              | object  | Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year |
|          paperless_billing          | integer | Indicates if the customer has chosen paperless billing (1- Yes, 0 - No) |
|            payment_method           | object  | Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check |
|             churn_reason            | object  | A customer’s specific reason for leaving the company. Directly related to Churn Category | 
|           referred_a_friend         | integer | Indicates if the customer has ever referred a friend or family member to this company | 
|          number_of_referrals        | integer | Indicates the number of referrals to date that the customer has made |
|                 offer               | object  | Identifies the last marketing offer that the customer accepted, if applicable. Values include None, Offer A, Offer B, Offer C, Offer D, and Offer E |
|   avg_monthly_long_distance_charges |  float  | Indicates the customer’s average long distance charges, calculated to the end of the quarter |
|             internet_type           | object  | Indicates if the customer subscribes to Internet type with the company: No, DSL, Fiber Optic | 
|       avg_monthly_gb_download       | integer | Indicates the customer’s average download volume in gigabytes, calculated to the end of the quarter specified above |
|           streaming_music           | integer | Indicates if the customer uses their Internet service to stream music from a third party provider (1- Yes, 0 - No) |
|             unlimited_data          | integer | Indicates if the customer has paid an additional monthly fee to have unlimited data downloads/uploads (1- Yes, 0 - No)  |
|             monthly_charge          |  float  | Indicates the customer’s current total monthly charge for all their services from the company | 
|              total_charges          |  float  |  Indicates the customer’s total charges, calculated to the end of the quarter specified above |
|            total_refunds            |  float  | Indicates the customer’s total refunds, calculated to the end of the quarter specified above |
|       total_extra_data_charges      | integer | Indicates the customer’s total charges for extra data downloads above those specified in their plan, by the end of the quarter specified above |
|     total_long_distance_charges     |  float  | Indicates the customer’s total charges for long distance above those specified in their plan, by the end of the quarter specified above |
|             total_revenue           |  float  | Total revenue from the customer's charges, by the end of the quarter specified above |
|           satisfaction_score        | integer | A customer’s overall satisfaction rating of the company from 1 (Very Unsatisfied) to 5 (Very Satisfied) | 
|             customer_status         | integer |  Indicates the status of the customer at the end of the quarter (1 - Churned, 0 - Active) |
|               new_user              | integer | Indicates the status of the customer at the end of the quarter (1 - New, 0 - Existing) |
|             churn_category          | object  | A high-level category for the customer’s reason for churning: Attitude, Competitor, Dissatisfaction, Other, Price. When they leave the company, all customers are asked about their reasons for leaving. Directly related to Churn Reason |
|                pop_density          | integer | Population density of the city | 


## Technical Findings

As customer churn in the database is only 23% , the datasets are deemed imbalanced. However for the model training, we have used several models including Logistic Regression, Random Forest, and Support Vector Machine (SVM) along with Synthetic Minority Oversampling Technique (SMOTE) for model. 

With Random Forest we have achieved 69% F1 Score with 73% AUC. This means that our model will be able to distinguish the churn customers and those who stayed, 73% of the time. However, being able to predict churn customer from historical data is biased and lagging, which is why we have also made additional prediction that would be necessary to quantify expected churn period. 

From 5174 customer that has yet to churn, our Random Forest model has manage to find relationship with 94% accuracy predicting the customer base with high churn tendency. 

The model has its fair share of limitations. As we do not have time-series features, the model itself is not able to confirm its performance in predicting future churn class. Hence, the survival analysis using Lifelines is used to measure the accuracy in the model expected performance.

For more visualisation of the project, you can find more information in the dashboard with link as follow :

[Customer Attrition Dashboard](https://customer-attrition-dashboard.herokuapp.com)

