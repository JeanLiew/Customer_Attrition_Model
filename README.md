# Telco Customer Attrition Model

-- 
## Problem Statement

> There is a big difference between a satisfied customer and a loyal customer - Shep Hyken

With spewing yet saturated competitions in the telecommunication industry, in order to stay ahead in the competition, customer satisfaction should always a the business driver with customer attrition as a goal.

Customer Attrition is also known as customer churn where customer ends the commercial relationship with the business. Customer lifetime value (CLTV) an important key metric to measure the health of business. Since change is inevitable the business goal is to reduce custome churn.

Churn rate is expressed as a rate that indicates the number of customers lost over a given period of time. With the cost of acquisition often greater than customer retention [(Customer Retention Strategy, 2016)](https://blog.exitbee.com/8-simple-customer-retention-strategies-to-decrease-your-churn-rate/), being able to identify why and when a customer is leaving, allows business to take on proactive approach and win the customer back. 

--
## Executive Summary  

Align with marketing strategy, the first step is to understanding our customer base also known as customer segmentation in order to provide a strong value proposition. Using analytics, the customer database are segmented into 4 main cluster, namely **Vanilla**, **Heavyweight**, **Minimalist** and **Price-Sensitive**. 

With the cluster identified, we will process this as part of the classification model. As customer attrition in the database is only 23% , the datasets are deem imbalanced. However for the training, we have used several models including Logistic Regression, Random Forest, and Support Vector Machine (SVM) along with Synthetic Minority Oversampling Technique (SMOTE) for model. 

The factors affecting the customer churn rate is as follow:

Married users are 1.51 times more likely to churn, whereas contract users of two years are 0.43 times more likely to stay. In summary, internet_service using fiber optic, payment method using electronic check, offer E, and streaming tv services are features that the business needs to look into. The driving factors that affects the customer churn are month-to-month basis contract customers, payment via electronic checks, fibre optic and streaming services connectivity which requires more investigation on the logistics and hardware of the actual services.

Alternatively, the long term contracts offers, online security, tech support, online back up has prove to be a value-added service to the users as the subscription to it led to user more likely to stay with the business. 

As a direct call to action,  the customer based has been identified in simpler fashion for marketing / management's action. 

![Customer Quadrant](/images/cluster_quadrant.png)

As recommendation, such model of customer attrition is able to be further developed for different business models. With modification on the features and especially on the customer segmentation, the model will be able to predict for business customer churn anticiptation. 

--
## Technical Findings

With Random Forest we have achieved 69% F1 Score with 73% AUC. This means that our model will be able to distinguish the churn customers and those who stayed, 73% of the time. However, being able to predict churn customer from historical data is biased and lagging, which is why we have also made additional prediction that would be necessary to quantify expected churn period. 

In this, we have implemented survival analysis to predict the expected tenure length to churn. From 5174 customer that has yet to churn, our Random Forest model has manage to find relationship with 94% customer base with high churn tendency that overlaps the survival analysis prediction. 

![Survival Curve](/images/surv_kmf_cohort.png)

As we do not have time-series datae survival analysis has also verified the following where cluster behaviour is consistent to the expectation on the customer churn. 
