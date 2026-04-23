# ISY503 Assessment 3 – NLP Sentiment Analysis

## Project Overview
This project aims to build a Natural Language Processing (NLP) system capable of performing sentiment analysis on Amazon product reviews. The system classifies reviews as either positive or negative using a trained machine learning model.

## Dataset
We are using the Multi-Domain Sentiment Dataset, which contains labeled Amazon product reviews across multiple categories.

## Project Objective
The objective is to train a neural network model that can:
- Analyse input text
- Predict sentiment (positive or negative)
- Provide results through a simple user interface

## Project Structure
- data/raw → original dataset
- data/processed → cleaned dataset
- src → source code
- model → trained models
- app → application (web interface)
- results → evaluation outputs
- templates/index.html -> Frontend UI (sentiment analysis webpage)
  Built by Yeeun. Contains the text input, "Analyse" button, and result display on the bottom
  Mock prediction function placed temporarily until predict.py is connected.

## To connect the UI
In app.py, add this route:
  return render_template("index.html")

## Team Members and Roles
- Isha → Data preprocessing
- Rosa → Model training (baseline) & repository management
- Lincoln → Model training (alternative models)
- Yeeun Park → Web / deployment

## Technologies
- Python
- Machine Learning / Deep Learning
- NLP techniques
- GitHub for version control

## Notes
This project follows the requirements of ISY503 Assessment 3, including data preprocessing, model training, evaluation, and deployment.
