
These are APIs of order.


.. _order:

**********************
Order
**********************


.. _order-show_menu:

Show Menu
===========

``GET /api/order/show_menu/``



Response
----------

.. code-block:: json

  {
    "menu": [
        [
            1,
            "回锅肉",
            25.6,
            false
        ],
        [
            2,
            "红烧肉",
            28,
            true
        ]
    ]
 }


.. _order-submit_order:

Submit Order
==============

``POST /api/order/submit_order/``

Parameters
----------

=================   ============    ============   ============================================
       Name           Type             Option             Description
=================   ============    ============   ============================================
  ordered_food         list           required         each item contains food id and amount
=================   ============    ============   ============================================

Response
----------


.. code-block:: json

 {
    "order_number": "20191010234539-0000000006"
 }




.. _order-food:

Food
============

ListFood
----------

``POST /api/order/food/``


FoodDetail
------------

``POST /api/order/food/<food_id>/``



.. _order-orders:

Orders
============

ListOrders
-----------

``POST /api/order/orders/``


OrderDetail
------------

``POST /api/order/orders/<order_id>/``


