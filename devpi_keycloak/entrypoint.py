# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from keycloak import Keycloak, Token

def devpiserver_auth_request(request, userdict, username, password):
    keycloak_url = os.getenv("KEYCLOAK_URL")
    if not keycloak_url:
        return

    keycloak_realm = os.getenv("KEYCLOAK_REALM")
    if not keycloak_realm:
        return

    service: Keycloak = Keycloak(
        keycloak_url,
        keycloak_realm,
        "admin-cli"
    )
    
    try:
        token: Token = service.auth(username,password)
        if (token.check_auth()):
            token.logout()
            return {"status":"ok"}
        else:
            return None
    except:
        return None
