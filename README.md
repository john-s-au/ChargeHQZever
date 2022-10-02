# ChargeHQZever
Zever Solar script for ChargeHQ


## Background

This a script for ZeverSolar inverters to be used with Charge HQ's Push API method of providing inverter power. Tested on a Raspberry Pi 3. Installation instruction may differ with non unix based OS
See: https://chargehq.net/kb/push-api

## Install Steps
1. Create Charge HQ account
1. Request your SiteId using Charge HQ's contact form. https://chargehq.net/contact or emailing info@chargehq.net
1. Save zever.py and configure zever.py with the `SiteId` and `Address` fields 
1. Install Python
1. Install zeversolarlocal (https://github.com/sander76/zeversolarlocal) `pip install zeversolarlocal`

## Testing
1. Test by running `python zever.py`

## Running the script
1. Edit crontab. The below example runs the script every 1 minute between 6am and 8pm. See crontab.guru to for other schedule examples

`*/1 6-20 * * * /usr/bin/python /<location of script>/zever.py`


