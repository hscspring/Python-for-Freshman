
These are APIs of authenticate.


.. _auth:

**********************
Authentication
**********************


.. _auth-sign_up:

SignUp
=======

``POST /api/auth/sign_up/``


Parameters
----------

=================   ============   ============  =========================================
   Name               Type           Option               Description
=================   ============   ============  =========================================
  phone               string         required          user phone
  password            string         required          user password
  identity            int            optional      0(default): normal, 1: VIP, 2: VVIP
  nickname            string         optional      ""(default)
=================   ============   ============  =========================================

Response
----------

.. code-block:: json

  {
    "data": "success"
  }


.. _auth-login:

Login
=========

``POST /api/auth/login/``

Parameters
----------

=================   ============    ============   ===============================
       Name           Type             Option             Description
=================   ============    ============   ===============================
  username            string          required             user phone
  password            string          required             user password
=================   ============    ============   ===============================

Response
----------


.. code-block:: json

 {
    "refresh": "eyJ0eXAiO*******UHmGI4TdVR97TRpFgkdAzi3gI1g",
    "access": "eyJ0eXAiOi*******u7HVQCjKMqCIxi3e_j6eGg",
    "nickname": "Yam0"
 }



:program:`Attention` : The access token only valid in 5 minutes, after that, you need to refresh.


.. _auth-refresh:

Refresh
=========

``POST /api/auth/refresh/``

Parameters
----------

=================   ============    ============      ===============================
  Name                Type             Option               Description
=================   ============    ============      ===============================
  refresh              string          required          the refresh token
=================   ============    ============      ===============================

Response
----------


.. code-block:: json

 {
    "access": "eyJ0eXAiOiJKV1QiLCJ********D2Nhj_O8nq_jOpvsMm9to"
 }


.. _auth-users:

Users
============

ListUsers
----------

``POST /api/auth/users/``


UserDetail
------------

``POST /api/auth/users/<user_id>/``


