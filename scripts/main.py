"""
Copyright (c) 2024 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import meraki
import config
import json
import csv

# Initialize the Meraki dashboard API
dashboard = meraki.DashboardAPI(config.API_KEY,output_log=False,log_path=False,print_console=False)

def read_serials_from_csv(csv_filepath):
    with open(csv_filepath, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        serials = [row['Serial'] for row in csv_reader]
    return serials

def push_alert_settings_to_networks(alert_settings, network_serials):
    try:
        # Get the list of all networks in the organization
        networks = dashboard.organizations.getOrganizationNetworks(config.ORG_ID)
        for network in networks:
            network_devices = dashboard.networks.getNetworkDevices(networkId=network['id'])
            # Filter for devices that are in the network_serials list
            matched_serials = [device['serial'] for device in network_devices if device['serial'] in network_serials]
            if matched_serials:
                # Update the alert settings with the matched serials
                updated_alert_settings = alert_settings.copy()
                updated_alert_settings['serials'] = matched_serials
                
                # Push the alert profile
                dashboard.sensor.createNetworkSensorAlertsProfile(
                    networkId=network['id'],
                    **updated_alert_settings
                )
                print(f"Alert profile with serials {matched_serials} pushed to network: {network['name']}")
            else:
                print(f"No matched serials for network: {network['name']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
# Load the alert settings from the JSON file
with open('data_files/alert_settings.json', 'r') as json_file:
    alert_settings_template = json.load(json_file)

# Read the serial numbers from the CSV file
csv_filepath = 'data_files/devices.csv'  # Replace with the path to your CSV file
network_serials = read_serials_from_csv(csv_filepath)

# Push the alert settings to the networks
push_alert_settings_to_networks(alert_settings_template, network_serials)
