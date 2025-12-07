"""
Created on 6 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

https://fastapi.tiangolo.com/tutorial/testing/#extended-fastapi-app-file
https://fastapi.tiangolo.com/tutorial/testing/#using-testclient
"""

import json
import os

from fastapi.testclient import TestClient

from mrcs_core.admin.user.user import User
from mrcs_core.data.json import JSONify

from mrcs_web.app.main import app


# --------------------------------------------------------------------------------------------------------------------

client = TestClient(app)


def test_find_all():
    response = client.get('/user/find_all/')
    assert response.status_code == 200
    jdict = response.json()
    assert len(jdict) == 1

    user = User.construct_from_jdict(jdict[0])
    assert user.email == 'bbeloff@me.com'


def test_find():
    response = client.get('/user/find_all/')
    jdict = response.json()
    user = User.construct_from_jdict(jdict[0])

    response = client.get(f'/user/find/{user.uid}/')
    assert response.status_code == 200

    user = User.construct_from_jdict(response.json())
    assert user.email == 'bbeloff@me.com'


def test_find_404():
    response = client.get(f'/user/find/123/')
    assert response.status_code == 404


def test_create():
    user = load_user('new_user.json')
    jdict = JSONify.as_jdict(user)
    jdict['password'] = 'pass'
    response = client.post('/user/create/', json=jdict)
    assert response.status_code == 201

    created = User.construct_from_jdict(response.json())
    assert created.created is not None

    response = client.delete(f'/user/delete/{created.uid}/')
    assert response.status_code == 200


def test_create_clash():
    user = load_user('admin_user.json')
    jdict = JSONify.as_jdict(user)
    jdict['password'] = 'pass'
    response = client.post('/user/create/', json=jdict)
    assert response.status_code == 409


def test_create_bad_email():
    user = load_user('new_user.json')
    jdict = JSONify.as_jdict(user)
    jdict['email'] = 'JUNK'
    jdict['password'] = 'pass'
    response = client.post('/user/create/', json=jdict)
    assert response.status_code == 400


def test_create_bad_role():
    user = load_user('new_user.json')
    jdict = JSONify.as_jdict(user)
    jdict['role'] = 'JUNK'
    jdict['password'] = 'pass'
    response = client.post('/user/create/', json=jdict)
    assert response.status_code == 400


def test_update():
    user = load_user('new_user.json')
    jdict = JSONify.as_jdict(user)
    jdict['password'] = 'pass'
    response = client.post('/user/create/', json=jdict)
    assert response.status_code == 201

    created = User.construct_from_jdict(response.json())
    assert created.created is not None

    jdict = JSONify.as_jdict(created)

    response = client.put(f'/user/update/', json=jdict)
    assert response.status_code == 200

    response = client.delete(f'/user/delete/{created.uid}/')
    assert response.status_code == 200


# --------------------------------------------------------------------------------------------------------------------

def load_user(rel_filename):
    abs_filename = os.path.join(os.path.dirname(__file__), 'data', rel_filename)
    with open(abs_filename) as fp:
        jdict = json.load(fp)

    return User.construct_from_jdict(jdict)
