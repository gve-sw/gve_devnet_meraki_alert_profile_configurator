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
import json
import os
import config

# Initialize the Meraki dashboard API
dashboard = meraki.DashboardAPI(config.API_KEY,output_log=False,log_path=False,print_console=False)
orgs = dashboard.organizations.getOrganizations()

# Export the organizations to a JSON file
with open('data_files/organizations.json', 'w') as file:
    json.dump(orgs, file, indent=4)

print("Organizations data exported to 'organizations.json'")