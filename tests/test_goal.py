# import pytest
# import requests
# import os
#
# from dotenv import load_dotenv
# load_dotenv()

from faker import Faker
from pytest_steps import test_steps

from modules.goal_methods import create_goal, rename_goal, del_goal_by_id, get_goal_by_id, get_goals

fake = Faker()

# API_URL=os.getenv("API_URL")
# TOKEN=os.getenv("TOKEN")
# TEAM_ID=os.getenv("TEAM_ID")
#
#
# my_headers = {"Authorization": TOKEN}

def test_get_goals():
   result = get_goals()
   assert result.status_code == 200
   print("Test 1 passed")
   assert result.json()["goals"][0]["name"] == "ssss"
   print("Test 2 passed")


@test_steps("Create new goal", "Delete goal")
def test_create_goal():
   g_name = fake.first_name()
   result = create_goal(g_name)
   assert result.status_code == 200
   assert result.json()["goal"]["name"] == g_name
   yield
   goal_id = result.json()["goal"]["id"]
   result = del_goal_by_id(goal_id)
   yield

@test_steps("Create new goal", "Update (rename) created goal", "Delete goal")
def test_update_goal():
    g_name = fake.first_name()
    result = create_goal(g_name)
    goal_id = result.json()["goal"]["id"]
    print("New goal`s name is: "+result.json()["goal"]["name"])
    new_g_name = fake.last_name()
    print("Rename to: " + new_g_name)
    yield
    result = rename_goal(goal_id, new_g_name)
    assert result.status_code == 200
    assert result.json()["goal"]["name"] == new_g_name
    print("Goal name updated")
    yield
    result = del_goal_by_id(goal_id)
    yield

@test_steps("Create new goal", "Get new goal by id", "Delete goal")
def test_get_goal_by_id():
    g_name = fake.first_name()
    result = create_goal(g_name)
    goal_id = result.json()["goal"]["id"]
    yield
    result = get_goal_by_id(goal_id)
    assert result.json()["goal"]["name"] == g_name
    yield
    result = del_goal_by_id(goal_id)
    assert result.status_code == 200
    yield

@test_steps("Create new goal", "Delete goal", "Get deleted goal (RC:404)")
def test_delete_goal():
    g_name = fake.first_name()
    result = create_goal(g_name)
    goal_id = result.json()["goal"]["id"]
    yield
    result = del_goal_by_id(goal_id)
    assert result.status_code == 200
    yield
    result = get_goal_by_id(goal_id)
    assert result.status_code == 404
    yield