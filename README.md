# gve_devnet_meraki_alert_profile_configurator
python prototype leveraging the Meraki Dashboard API to manage environmental alert conditions and enables users to configure temperature, humidity, water detection, and door status alerts.


## Contacts
* Jorge Banegas

## Solution Components
* Meraki MT

## Prerequisites
#### Meraki API Keys
In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:
1. Login to the Meraki dashboard
2. In the left-hand menu, navigate to `Organization > Settings > Dashboard API access`
3. Click on `Enable access to the Cisco Meraki Dashboard API`
4. Go to `My Profile > API access`
5. Under API access, click on `Generate API key`
6. Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. In case you lose the key, then you have to revoke the key and a generate a new key. Moreover, there is a limit of only two API keys per profile.

> For more information on how to generate an API key, please click [here](https://developer.cisco.com/meraki/api-v1/#!authorization/authorization). 

> Note: You can add your account as Full Organization Admin to your organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).

## Installation/Configuration

1. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).
2. Install the requirements with `pip3 install -r requirements.txt`

3. Add Meraki API key to the config.py python file, run python scripts/output_org.py if you need to find ORG_ID
```python
API_KEY = ''
ORG_ID = ''
```

4. Fill out datafiles/devices.csv and enter the list of device serials for the sensors to attach to the Alert Profile

```
Serial
XXXX-XXXX-XXXX
XXXX-XXXX-XXXX
XXXX-XXXX-XXXX
XXXX-XXXX-XXXX
```

5. Edit data_files/alert_settings.json file to configure the Alert Profile settings to your choice, refer to the [API Documentation](https://developer.cisco.com/meraki/api-v1/create-network-sensor-alerts-profile/) if needed.

![/IMAGES/alert_settings.png](/IMAGES/alert_settings.png)

## Usage

To run the program, use the command:
```
$ python3 scripts/main.py
```

# Screenshots

![/IMAGES/output.jpg](/IMAGES/output.jpg)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.