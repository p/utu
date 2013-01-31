utu - underscore style for Python unittest module
=================================================

`Apparently <http://www.quora.com/Will-Pythons-unittest-module-become-pythonic-anytime-soon>`_
there are no plans to provide a PEP-8 compliant API for the unittest module.

Utu is an attempt to offer such an API.

Current features
----------------

- setup/teardown for setUp/tearDown
- setup_class/teardown_class for setUpClass/tearDownClass
- assert_foo for assertFoo

Compatibility
-------------

py.test treats setup_class/teardown_class as fixture methods.
A possible workaround is to use setupclass/teardownclasss instead.

Tests
-----

.. image:: https://api.travis-ci.org/p/owebunit.png
  :target: https://travis-ci.org/p/owebunit

License
-------

Released under the 2 clause BSD license.
