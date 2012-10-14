Documentation
=============

FISTA
-----

.. automodule:: fista

   .. autoclass:: Fista
      :members:

Mixed norms
-----------

.. autofunction:: fista.mixed_norm

Dual mixed norms
----------------

.. autofunction:: fista.dual_mixed_norm


Compute the Lipschitz constant
------------------------------

.. autofunction:: fista._load_Lipschitz_constant

Proximity functions
-------------------

p=2 q=2 r=2
+++++++++++

.. autofunction:: fista.prox_l22

p=1 q=1 r=2
+++++++++++

.. autofunction:: fista.prox_l11

p=1 q=2 r=2
+++++++++++

.. autofunction:: fista.prox_l12

p=2 q=1 r=2
+++++++++++

Proximity function
******************

.. autofunction:: fista.prox_l21 

Sub-function (computing Ml)
***************************

.. autofunction:: fista.compute_M

