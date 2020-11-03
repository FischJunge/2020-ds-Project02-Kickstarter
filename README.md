# 2020-ds-Project02-Kickstarter

# Table of Contents
Y. Introduction
Z. Data
x. Future Work / Outlook

# Introduction

## Understanding Kickstarter
**Kickstarter** is a US-american crowdfunding-platform located in Brooklyn, New York. The companies mission is it to 'help bringing creative projects to life'. Kickstarter offers project creators the opportunity to gather money from public for their individual projects, such as films, music, stage shows, comics, journalism, video games, technology, publishing, and food-related projects etc. Therefore, the traditional ways of raising money for investments is circumvented. <br/>
They principle way of working is as following: The project creator posts his or her project idea on 
Kickstarter to initialize the fundraising process. People can support individual projects by pledging money to it (people supporting a project are also called backers). People who back Kickstarter projects are offered tangible rewards or experiences in exchange for their pledges (e.g. a board game, if the project is about developing a new board game). The period of fundraising is limited. If the preselected deadline and the minimum fundraising goal defined by the project initiator is not met by the end of the deadline, no funds are collected at all. <br/>
As of December 2019, Kickstarter has received more than $4.6 billion in pledges from 17.2 million backers to fund 445,000 projects, such as films, music, stage shows, comics, journalism, video games, technology, publishing, and food-related projects.<br/>

**Source:** https://en.wikipedia.org/wiki/Kickstarter

## The Project's Aim


# Examples of use


# Data
## Source

## Data Description

Column | Description | Drop
------ | ------ | ------
'backers_count' | Number of backers | 
'blurb' | Project summary |
'category' | Category | 
'converted_pledged_amount' | Pledged amount converted to 'USD' | !
'country' | Country of origin of the project | 
'created_at' | Date project created on Kickstarter | 
'creator' | Person created the project | x
'currency' | Currency used to support (defined by project owner) | ???
'currency_symbol' | Symbol of currency | x
'currency_trailing_code' | Currency code 'USD', 'EUR' etc. | x
'current_currency' | ???  ??? | 
'deadline' | Deadline for crowdfunding | 
'disable_communication' | Enable or Disable communication options | x
'friends' | 'Empty' | x
'fx_rate' | Exchange rate from currency to 'USD' | 
'goal' | Fundraising goal | 
'id' | Internal Kickstarter ID | 
'is_backing' | Creator of the project is also backing other projects ??? | x (doesn't contain infos)
'is_starrable' | ??? | x
'is_starred' | ??? | x
'launched_at' | Date launched on Kickstarter | 
'location' | Location of the project creator | 
'name' | Project name | 
'permissions' | ??? | x (empty)
'photo' | Picture of the product | x
'pledged' | Amount pledged by the crowd (in target 'currency') | !
'profile' | Profile of project creator ??? | x
'slug' | ??? | x (redundant to project name)
'source_url' | Url ??? | x
'spotlight' | Boolean value ??? | x
'staff_pick' | Boolean value ??? | x
'state' | Current status the project is in (e.g. successful, failed, live, cancelled, undefined and suspended) | !
'state_changed_at' | Date condition changed ??? | 
'static_usd_rate' | Exchange rate used to convert pledged to usd_pledged | 
'urls' | Urls of the project ??? | x
'usd_pledged' | Amount of money pledged in 'USD' (pledged * static_usd_rate) | !
'usd_type' | Local or international 'USD' --> Money exchanged or not ??? | x

# Technologies
## Libraries Used
conda create --name kickstarter python=3.8.5<br/>
conda install -n kickstarter pytest==6.1.1<br/>
conda install -n kickstarter ipython<br/>
conda install -n kickstarter jupyterlab<br/>
conda install -n kickstarter seaborn<br/>
conda install -n kickstarter scikit-learn<br/>
conda install -n kickstarter numpy<br/>
conda install -n kickstarter pandas<br/>
conda install -n kickstarter statsmodel<br/>
conda install -n kickstarter sklearn<br/>
conda install -n kickstarter bokeh<br/>
conda list --> 'Shows all packages installed'<br/>

## 