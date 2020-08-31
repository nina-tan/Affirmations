# Affirmations

## Description

Displays affirmations in a notification from Notification Center.

## Visuals

![Alt Text](https://github.com/nina-tan/Affirmations/blob/master/affirmation_demo.gif)

## Steps

- Clone the repository
- Create a list of affirmations or use a webscraper to gather affirmations in `affirmation.txt`
- Enter `python3 affirmation_popup.py` in the command line to run `affirmation_popup.py` and prompt an affirmation in the Notification Center

## Automation

To automate `affirmation_popup.py` and receive affirmation notifications regularly, set up a [cron](https://crontab.guru/) job.

For example, I ran `crontab -e` and then entered:  
 `0 * * * * cd <location_of_project>; python3 affirmation_popup.py`
