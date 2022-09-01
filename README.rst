devpi-keycloak: keycloak auth plugin for devpi-server
=====================================================

Installation
------------

``devpi-keycloak`` needs to be installed alongside ``devpi-server``.

You can install it with::

    pip install devpi-keycloak

For ``devpi-server`` there is no configuration needed, as it will automatically discover the plugin through calling hooks using the setuptools entry points mechanism.

Configuration
-------------

You need to pass environment variables to configure the plugin.

- ``KEYCLOAK_HOOK`` to adjust the keycloak URL used.
- ``KEYCLOAK_REALM`` to adjust the keycloak realm used.
