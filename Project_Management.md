# Project Management
by Jakolien & Michael

## Task / Deliverables
* **Slide deck PDF** pushed to GitHub designed for non-technical stakeholders that outline findings, recommendations, and future work (10 min presentation). 
* **Jupyter notebook** following PEP8 designed for data science/technical audience.
* **Python script** for generating (takes .csv as argument and saves the model locally)  and running your model from the terminal (takes test.csv and model as arguments and outputs accuracy and predictions as .csv). 

## Things to Think About
1. Check for data imbalance!
2. What would be the right performance metric - precision, recall, accuracy, F1 score, or something else? (Check TPR?)
3. Try different (at least 3) machine learning algorithms to check which performs best on the problem at hand.

## Time Line

### **Start: Friday, 30/10/2020, 10:00am**
Task | Task owner | Status
---- | ---------- | ------
Preparing data sets | J & M | Done
Understanding columns | J & M | Done
Gather domain knowledge <br/>(How does Kickstarter work?) | J & M | Done
Brainstorming on business (use-)case | J & M | Done

### Weekend
Task | Task owner | Status
---- | ---------- | ------
Start data cleaning | J | Done
Gather domain knowledge & Look for missing column descriptions | M | Done

### Monday
Task | Task owner | Status
---- | ---------- | ------
Initial data cleaning | J | Done
Initial EDA | M | Done
Finalize business (use-)case<br/>(e.g. stakeholder, what to predict, scenarios, select the evaluation metrics) | J & M | Done
Final data cleaning | J | Done

### Tuesday
Task | Task owner | Status
---- | ---------- | ------
Finalize full EDA | J & M | Done
Set up model | J & M | Done
Fianalize model | J & M | Done

### Wednesday
Task | Task owner | Status
---- | ---------- | ------
Presentation | M | Done
Python script | J | WIP
Tidy up Jup NB | J & M | Done
Finalize deliverables | J & M | WIP

### **End: Thursday, 05/11/2020, 09:00am**

## Way of Working
* Working on GitHub-Repo
* Create and work within branches to fullfil tasks (e.g. initial EDA)
* Do not work in the same file at the same time
* Work in an econimic way ('How much is the answere worth?')

## Brainstorming - Scenario Description
* What to predict?
    * State (success or failure)<br/>
* Stakeholder perspective?
    * Kickstarter Management
* Business case
    * People are willing to pay money for the knowledge if they succeed or fail with their project idea.

* State --> Classification problem
* Financial gain & extra --> Regression problem

### Raw Idea
* Perspective: Financial gain for Kickstarter (KS)
* Before starting a project on KS people want to know how likely it is that the project idea succeeds.
* They might be willing to pay for that knowledge.
* How much is it worth?
    * Financially evaluate the difference between sccueeding and failing projects per domain
    * Extra: Predictions for projects which are currently running.

## Model Evaluation - Performance Metric
1. F1-Score --> Balance between precision and recall
2. ROC-Curve --> Shows the separation of positive and negative events

## Applied ML-Algorithms (at least 3)
1. 
2. 
3. 
4. 

## Tips from Tereza
* Plan 1d to prepare the presentation
* Work with buffers
* Way of working within the project is a simulation of a real DS Project
* Set Deadlines
* **GOAL:** Have a presentation
* Live the stakeholder