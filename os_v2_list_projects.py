# @splash
# inspired by http://stackoverflow.com/questions/15525827/is-it-possible-to-ge-the-list-of-tenants-a-user-is-associated-with-in-openstack
#
# in v2, lists all projects the user has access to without requiring admin privileges

from keystoneclient.v2_0 import client
from keystoneclient.v2_0 import tokens
import os
import requests

username = os.environ.get('OS_USERNAME')
password = os.environ.get('OS_PASSWORD')
auth_url = os.environ.get('OS_AUTH_URL')

keystone = client.Client(username=username, password=password, auth_url=auth_url)
token = keystone.auth_token
headers = {'X-Auth-Token': token }
tenant_url = auth_url
tenant_url += '/tenants'
r = requests.get(tenant_url, headers=headers)
tenant_data = r.json()


for tenant in tenant_data['tenants']: 
   print tenant['name']
