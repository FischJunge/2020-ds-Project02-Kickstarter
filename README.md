# 2020-ds-Project02-Kickstarter

# Table of Contents
1. Introduction<br/>
    1.1 Understanding Kickstarter<br/>
    1.2 Scenario Descripton<br/>
2. Data<br/>
    2.1 Description - Initial Data Set<br/>
    2.2 Description - Cleaned Data Set<br/>
3. Technologies<br/>
    3.1 Requirements
    3.2 Libraries Used
    3.3 Install Environment
    3.4 Usage
    3.5 Limitations

x. Future Work / Outlook

# 1 | Introduction
## 1.1 | Understanding Kickstarter
**Kickstarter** is a US-american crowdfunding-platform located in Brooklyn, New York. The companies mission is it to 'help bringing creative projects to life'. Kickstarter offers project creators the opportunity to gather money from public for their individual projects, such as films, music, stage shows, comics, journalism, video games, technology, publishing, and food-related projects etc. Therefore, the traditional ways of raising money for investments is circumvented. <br/>
They principle way of working is as following: The project creator posts his or her project idea on 
Kickstarter to initialize the fundraising process. People can support individual projects by pledging money to it (people supporting a project are also called backers). People who back Kickstarter projects are offered tangible rewards or experiences in exchange for their pledges (e.g. a board game, if the project is about developing a new board game). The period of fundraising is limited. If the preselected deadline and the minimum fundraising goal defined by the project initiator is not met by the end of the deadline, no funds are collected at all. <br/>
As of December 2019, Kickstarter has received more than $4.6 billion in pledges from 17.2 million backers to fund 445,000 projects, such as films, music, stage shows, comics, journalism, video games, technology, publishing, and food-related projects.<br/><br/>
**Source:** https://en.wikipedia.org/wiki/Kickstarter

## 1.2 | Scenario Description
### Stakeholder
Stakeholder of this data science project is the Kickstarter **C-Level Management**.

### Kickstarter's Business Model
The **more successful** a project is, the **more money** can be raised from backers (amount pledged), the **more profit** can be gained for Kickstarter (KS charges 5% fee on the total pledged amount).

### Project's Aim
The **projects aim** is to answer the following questions:<br/>
* **Main question:**<br/> How likely is it that a project is successful on Kickstarter based on an assessment of factors that contribute to success?
* **Additional question:**<br/>How much money can be pledged based on an assessment of factors that contribute to success?
 

# 2 | Data
**Source-Url:** https://webrobots.io/kickstarter-datasets/ <br/>

## 2.1 | Description - Initial Data Set
Column | Description | Drop?
------ | ------ | ------
'backers_count' | Number of backers | No
'blurb' | Project summary | Yes
'category' | Category | No
'converted_pledged_amount' | Pledged amount converted to 'USD' | Yes
'country' | Country of origin of the project | Yes
'created_at' | Date project created on Kickstarter | Yes
'creator' | Person created the project | Yes
'currency' | Currency used to support<br/>(defined by project owner) | Yes
'currency_symbol' | Symbol of currency | Yes
'currency_trailing_code' | Currency code 'USD', 'EUR' etc. | Yes
'current_currency' | (???) | Yes
'deadline' | Deadline for crowdfunding | No
'disable_communication' | Enable or Disable communication options | Yes
'friends' | 'Empty' | Yes
'fx_rate' | Exchange rate from currency to 'USD' | Yes
'goal' | Fundraising goal | No
'id' | Internal Kickstarter ID | No
'is_backing' | Creator of the project is also backing other projects (???) | Yes<br/>(doesn't contain infos)
'is_starrable' | (???) | Yes
'is_starred' | (???) | Yes
'launched_at' | Date launched on Kickstarter | Yes
'location' | Location of the project creator | Yes
'name' | Project name | Yes
'permissions' | (???) | Yes<br/>(empty)
'photo' | Picture of the product | Yes
'pledged' | Amount pledged by the crowd<br/>(in target 'currency') | Yes
'profile' | Profile of project creator (???) | Yes
'slug' | 'Like Project name' | Yes<br/>(redundant to project name)
'source_url' | URL | Yes
'spotlight' | Boolean value (???) | Yes
'staff_pick' | Boolean value (???) | Yes
'state' | Current status the project is in<br/>(e.g. successful, failed, live, cancelled, undefined and suspended) | Yes
'state_changed_at' | Date condition changed (???) | Yes
'static_usd_rate' | Exchange rate used to convert pledged to usd_pledged | Yes
'urls' | URLs of the project (???) | Yes
'usd_pledged' | Amount of money pledged in 'USD' (pledged * static_usd_rate) | No
'usd_type' | Local or international 'USD'<br/>--> Money exchanged or not (???) | Yes
<br/>

## 2.2 | Description - Cleaned Data Set
Column | Description | Feature Engineering
------ | ------ | ------
'id' | Internal Kickstarter ID | No
'backers_count' | Number of backers | No
'usd_pledged' | Amount of money pledged in 'USD' (pledged * static_usd_rate) | No<br/>(data leakage risk)
'category_name' | Name of category | Yes<br/>(extracted out of initial 'category')
'category_parent_id' | Parent ID of category | Yes<br/>(extracted out of initial 'category')
'usd_goal' | Fundraising goal in 'USD | Yes<br/>(recalculated out of initial 'goal')
'duration_days' | Duration of fundraising | Yes<br/>(calculated out of 'created_at' and 'launched_at')
'duration_days_prep' | Duration of project Preparation | Yes<br/>(calculated out of 'deadline' and 'launched_at')
'year_deadline' | Deadline for crowdfunding (year) | Yes<br/>(extracted from 'deadline')
'month_deadline' | Deadline for crowdfunding (month) | Yes<br/>(extracted from 'deadline')
'weekday_deadline' | Deadline for crowdfunding (weekday) | Yes<br/>(extracted from 'deadline')
'weekday_launched_at' | Weekday project launched on KS | Yes<br/>(extracted from 'launched_at')
'winter_deadline_True' | Deadline for crowdfunding in winter | Yes<br/>(extracted from 'deadline')
'spring_deadline_True' | Deadline for crowdfunding in spring | Yes<br/>(extracted from 'deadline')
'summer_deadline_True' | Deadline for crowdfunding in summer | Yes<br/>(extracted from 'deadline')
'deadline_weekend_True' | Project launched on a weekend | Yes<br/>(extracted from 'deadline')
'launched_weekend_True' | Project launched on a weekend | Yes<br/>(extracted from 'launched_at')
'country_US_True' | Country the project got pitched in | Yes<br/>(extracted from 'country')
'eastcoast_True' | Project got pitched on the east coast | Yes
'long_blurbe_True' | Evaluating the length of the blurb | Yes<br/>(extracted from 'blurb')
'long_name_True' | Evaluating the length of the name | Yes<br/>(extracted from 'name')
'state_b_True' | Successful state | Yes<br/>(extracted from 'state')
'long_creator_name_True' | Evaluating the length of the creator name | Yes<br/>(extracted from 'creator')

# 3 | Technologies
## 3.1 | Requirements
* condamini,
* conda or
* pyenv (with Python: 3.8.5)

## 3.2 | Libraries Used
conda create --name kickstarter python=3.8.5<br/>
conda install -n kickstarter pytest==6.1.1<br/>
conda install -n kickstarter ipython<br/>
conda install -n kickstarter jupyterlab<br/>
conda install -n kickstarter seaborn<br/>
conda install -n kickstarter scikit-learn<br/>
conda install -n kickstarter numpy<br/>
conda install -n kickstarter pandas<br/>
conda install -n kickstarter statsmodels<br/>
conda install -n kickstarter sklearn<br/>
conda install -n kickstarter bokeh<br/>
conda list --> 'Shows all packages installed'<br/>

## 3.3 | Install Environment
Having Anaconda installed then create your environment with
```bash
conda env create --file environment_kickstarter.yml
```

## 3.4 | Usage
To train the model and store the test data in the data folder as well as the model in models run:
```bash
python train.py  
```
In order to test that predict works on a test set you created run:
```bash
python predict.py models/linear_regression_model.sav data/X_test.csv data/y_test.csv
```

## 3.5 | Limitations
Development libraries are part of the production environment, normally these would be separate as the production code should be as slim as possible