# Machine Learning Based Data Sensitivity Classification System for Preventing AI Model Leakage

## 1. Introduction

Artificial Intelligence (AI) systems are trained on massive volumes of user data. While this improves performance, it creates serious privacy risks. Modern AI models may unintentionally memorize and leak sensitive information such as phone numbers, bank details, medical records, or identification numbers. This issue is known as Model Leakage.

To solve this problem, AI systems must be able to distinguish between safe and sensitive data before using it. This project introduces a Data Sensitivity Level Classifier that automatically categorizes text into different privacy levels using Machine Learning.

The system ensures that sensitive information is identified and controlled before it reaches any AI model, thus protecting user privacy.

## 2. Problem Statement

Most AI systems do not verify the privacy sensitivity of their input data. As a result:

Private data may be stored in AI training sets

Models may repeat sensitive information in outputs

Users’ privacy can be violated

Legal regulations like GDPR and DPDP Act can be breached

There is no built-in mechanism in many AI pipelines to classify and block sensitive data.

## 3. Objective

The objectives of this project are:

To classify text into Public, Internal, Confidential, and Restricted categories

To train a machine learning model for sensitivity detection

To create a web-based system for real-time classification

To prevent sensitive data from being exposed to AI models

To demonstrate how model leakage can be avoided

## 4. Scope of the Project

This system can be used in:

AI chatbots

Data collection platforms

AI training pipelines

Cloud-based AI services

Government and enterprise systems

It provides a foundation for privacy-aware AI development.

## 5. System Architecture
User Input  
     ↓  
Text Preprocessing  
     ↓  
ML Sensitivity Classifier  
     ↓  
Sensitivity Label (Public / Internal / Confidential / Restricted)  
     ↓  
Privacy Control / Display Result  

## 6. Data Sensitivity Levels
Level	Meaning	Example
Public	Safe to share	News, education text
Internal	Organization use	Team schedules
Confidential	Private business or user data	Phone numbers, salary
Restricted	Highly sensitive	Aadhaar, passwords, biometrics

## 7. Dataset Description

A dataset of over 1,200 text samples was created and labeled into four sensitivity classes:

Public

Internal

Confidential

Restricted

Each row contains:

A text message

Its sensitivity label

This dataset is used to train the machine learning model.

## 8. Machine Learning Model

The system uses:

TF-IDF Vectorization to convert text into numerical features

Naive Bayes Classifier for multi-class classification

Naive Bayes is chosen because:

It works well for text classification

It is fast and memory efficient

It provides good accuracy for NLP tasks

## 9. Training Process

Load dataset

Split text and labels

Convert text to TF-IDF vectors

Train the Naive Bayes model

Save trained model and vectorizer

This model learns patterns that distinguish sensitive and non-sensitive text.

## 10. Web Application

A Flask web application allows users to:

Enter any text

Submit it for classification

View the predicted sensitivity level

The backend:

Loads the trained ML model

Predicts the class

Displays the result

## 11. Working of the System

User enters text

The text is vectorized

ML model predicts sensitivity

Result is shown

Sensitive data can be blocked or masked before sending to AI

This prevents AI model leakage.

## 12. How This Prevents Model Leakage

By identifying sensitive data before it reaches AI systems:

Private data is never stored

AI models cannot memorize it

No sensitive data is leaked in outputs

This acts as a privacy firewall for AI.

## 13. Advantages

Protects user privacy

Prevents data misuse

Ensures legal compliance

Improves AI trustworthiness

Real-time classification

## 14. Applications

AI chatbots

Healthcare systems

Banking AI

Government AI portals

Corporate data processing

## 15. Limitations

Depends on training data quality

Cannot detect completely new patterns

Needs continuous updating

## 16. Future Enhancements

Use deep learning models

Integrate with large AI systems

Automatic data masking

Multi-language support

## 17. Conclusion

This project demonstrates how machine learning can be used to protect privacy in AI systems. By classifying data into sensitivity levels, the system prevents model leakage and ensures that AI operates in a secure, ethical, and lawful manner.

## 18. Output
<img width="1534" height="774" alt="image" src="https://github.com/user-attachments/assets/6fa730eb-ed2b-4d52-a529-12cf46156af5" />

