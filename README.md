# 2020-ds-Project02-Kickstarter

## Libraries to install
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

## Data description

Column | Description
------ | ------
'backers_count' | Number of backers
'blurb' | Project summary
'category' | Category
'converted_pledged_amount' | ??? Converted to 'USD' ???
'country' | Country pledged from
'created_at' | ??? Date project created on Kickstarter ???
'creator' | ??? Person creating the project ???
'currency' | Currency used to support
'currency_symbol' | Symbol of currency
'currency_trailing_code' | Currency code 'USD', 'EUR' etc.
'current_currency' | ???  ???
'deadline' | Deadline for crowdfunding
'disable_communication' | ??? Enable or Disable communication options ???
'friends' | ??? ???
'fx_rate' | ??? Exchange rate ???
'goal' | Fundraising goal
'id' | Internal kickstarter id
'is_backing' | ??? Creator of the project is also backing other projects ???
'is_starrable' | ???  ???
'is_starred' | ???  ???
'launched_at' | Date launched on Kickstarter
'location' | ??? Location of the pledger ???
'name' | Project name
'permissions' | ???  ???
'photo' | ??? Picture of the product ???
'pledged' | Amount pledged by the crowd
'profile' | ??? Profile of the pledger ???
'slug' | ??? Tag ???
'source_url' | ??? Url ???
'spotlight' | ??? Bool value ???
'staff_pick' | ??? Bool value ???
'state' | Current condition the project is in
'state_changed_at' | ??? Date condition changed ???
'static_usd_rate' | ??? Related to exchange rate ???
'urls' | ??? Urls ???
'usd_pledged' | Amount of money pledged in 'USD'
'usd_type' | ??? Local or international 'USD' --> Money exchanged or not ???