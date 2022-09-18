# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

try:
    from devpi_server.auth import AuthException
    from devpi_server.log import threadlog

except ImportError:  # No devpi_server available
    class AuthException(Exception):
        pass

    import logging
    threadlog = logging

from keycloak import Keycloak, Token

threadlog.info("Keycloak plugin triggered")

keycloak_url = os.getenv("KEYCLOAK_URL")
if not keycloak_url:
    threadlog.exception("Keycloak missing URL")
    exit(1)
threadlog.info("Keycloak URL : %s",keycloak_url)

keycloak_realm = os.getenv("KEYCLOAK_REALM")
if not keycloak_realm:
    threadlog.exception("Keycloak missing realm name")
    exit(1)
threadlog.info("Keycloak realm name : %s",keycloak_realm)

def devpiserver_auth_user(userdict, username, password):
    global keycloak_url
    global keycloak_realm

    service: Keycloak = Keycloak(
        keycloak_url,
        keycloak_realm,
        "admin-cli"
    )

    status = "rejected"
    
    try:
        token: Token = service.auth(username,password)
        if (token.check_auth()):
            token.logout()
            status = "ok"
            threadlog.info("kc-auth '%s' authenticate",username)
        else:
            threadlog.exception("kc-auth failed to authenticate")
    except:
        threadlog.exception("kc-auth failed to authenticate")

    return {'status': status}

