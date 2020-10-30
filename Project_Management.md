# Project Management
by Jakolien & Michael

## Task / Deliverables
* **Slide deck PDF** pushed to GitHub designed for non-technical stakeholders that outline findings, recommendations, and future work (10 min presentation). 
* **Jupyter notebook** following PEP8 designed for data science/technical audience.
* **Python script** for generating (takes .csv as argument and saves the model locally)  and running your model from the terminal (takes test.csv and model as arguments and outputs accuracy and predictions as .csv). 

## Things 
1. Check for data imbalance! 
2. What would be the right performance metric - precision, recall, accuracy, F1 score, or something else? (Check TPR?)
3. Try different (at least 3) machine learning algorithms to check which performs best on the problem at hand.

## Time Line

* Start: Friday, 30/10/2020, 10:00am
        * Preparing data sets | Jakolien & Michael
        * Understanding columns | Jakolien & Michael
        * Gather domain knowledge (How does Kickstarter work?) | Jakolien & Michael
        * Brainstorming on business (use-)case | Jakolien & Michael
* Weekend
    * Start data cleaning | Jakolien
    * Gather domain knowledge & Look for missing column descriptions | Michael
* Monday
    * Initial data cleaning | Jakolien
    * Initial EDA | Michael
    * Finalize business (use-)case (e.g. stakeholder, what to predict, scenarios, select the evaluation metrics) | Jakolien & Michael
    * Final data cleaning | Michael
    * Finalize full EDA | Jakolien
* Tuesday
    * Set up model
    * Fianalize model
* Wednesday
    * Presentation
    * Python script
    * Tidy up Jup NB
    * Finalize deliverables
* End: Thursday, 05/11/2020, 09:00am

## Way of working

* Working on GitHub-Repo
* Create and work within branches to fullfil tasks (e.g. initial EDA)
* Do not work in the same file at the same time
* Work in an econimic way ('How much is the answere worth?')

## Brainstorming

What to predict? | State (Success or Failure)
Stakeholder perspective | Kickstarter
Business case | People are willing to pay money for the knowledge if they succeed or fail with their project idea.

* State --> Classification problem
* Financial gain & Extra --> Regression problem

###

* Perspective: Financial gain for Kickstarter (KS)
* Before starting a project on KS people want to know how likly it is that the project idea succeeds.
* They might be willing to pay for that knowledge.
* How much is it worth?
    * Financially evaluate the difference between sccueeding and failing projects per domain
    * Extra: Predictions for projects which are currently running.