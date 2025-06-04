import requests
from faker import Faker
fake = Faker()

import os

from dotenv import load_dotenv
load_dotenv()

API_URL=os.getenv("API_URL")
TOKEN=os.getenv("TOKEN")
TEAM_ID=os.getenv("TEAM_ID")


my_headers = {"Authorization": TOKEN}


def get_goals():
    return requests.get(API_URL+"/team/"+TEAM_ID+"/goal/", headers=my_headers)

def create_goal(g_name):
    my_body = {
        "name": g_name
    }
    return requests.post(API_URL+"/team/"+TEAM_ID+"/goal/", headers=my_headers, json=my_body)

def rename_goal(g_id,new_g_name):
    my_body = {
        "name": new_g_name,
    }
    return requests.put(API_URL+"/goal/" + g_id, headers=my_headers, json=my_body)

def get_goal_by_id(id):
    return requests.get(API_URL+"/goal/" + id, headers=my_headers)

def del_goal_by_id(id):
    return requests.delete(API_URL+"/goal/" + id, headers=my_headers)