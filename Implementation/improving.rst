Improving prox p=2, q=1
=======================

First implementation
--------------------

The fist implementation was the following :

.. code::

    def test_prox_l21(u, l, n_samples, n_kernels):
        """
        proximity operator l(2, 1, 2) norm, see prox_l11
        """
        res = np.zeros(n_samples*n_kernels)
        for i in range(n_kernels):
            res[i*n_samples:(i-1)*n_samples] =\
                    max(1. - l/norm(u[i*n_samples:(i-1)*n_samples], 2), 0.)
        res = res*u
        return res


Second implementation
---------------------

The second implementation was this one : 

.. code::

   def prox_l21(u, l, n_samples, n_kernels):
       """
       proximity operator l(2, 1, 2) norm, see prox_l11
       """
       for i in range(n_kernels):
           u[i*n_samples:(i-1)*n_samples] * =\
                   max(1. - l/norm(u[i*n_samples:(i-1)*n_samples], 2), 0.)
       return u


Test program
++++++++++++

We used memory_profiler for the tests :

.. code::

   from fista import prox_l21, test_prox_l21
   import numpy as np

   u = np.arange(5000*10)

   @profile
   def profile(u):
     for i in range(1500):
         u = prox_l21(u, 0.5, 5000, 10)

   profile(u)

Results
+++++++

For the fist implementation :
*****************************

=======  ==========  =========  ==============
Line #    Mem usage  Increment   Line Contents
=======  ==========  =========  ==============
     6                           @profile
     7     26.19 MB    0.00 MB   def profile(u):
     8     26.19 MB    0.00 MB       for i in range(1500):
     9                                   u = test_prox_l21(u, 0.5, 5000, 10)
=======  ==========  =========  ==============


For the second implementation :
*******************************

=======  ==========  =========  ==============
Line #    Mem usage  Increment   Line Contents
=======  ==========  =========  ==============
     6                           @profile
     7     24.75 MB    0.00 MB   def profile(u):
     8     24.75 MB    0.00 MB       for i in range(1500):
     9                                   u = prox_l21(u, 0.5, 5000, 10)
=======  ==========  =========  ==============


Execution time
--------------

>>> u = np.arange(5000*10)

For the fist implementation
+++++++++++++++++++++++++++

>>> %timeit test_prox_l21(u, 0.5, 5000, 10)
1000 loops, best of 3: 381 us per loop


For the second implementation
+++++++++++++++++++++++++++++

>>> %timeit prox_l21(u, 0.5, 5000, 10)
1000 loops, best of 3: 415 us per loop

Conclusion
----------
The fist method is slightly faster than the second, whereas using about the same amount of memory.
Therefore we chose the fist method

Another improvement
--------------------

Code
++++

.. code::

    def test_prox_l21(u, l, n_samples, n_kernels):
        for i in u.reshape(n_kernels, n_samples):
            u = u * max(1. - l/norm(u, 2), 0)
        return u

Execution_time
++++++++++++++

Last version :
**************

>>> n = 4000

>>> p = 8

>>> u = np.arange(n*p)

>>> %timeit prox_l21(u, 0.5, n, p)
1000 loops, best of 3: 271 us per loop


New version :
*************


>>> u = np.arange(n*p)

>>> %timeit test_prox_l21(u, 0.5, n, p)
100 loops, best of 3: 2.51 ms per loop

return res*u vs res=res*u; return res
-------------------------------------

Return after affectation
+++++++++++++

Tested code : 
*************
.. code::

   res = res * u
   return res

Result
******

>>> %timeit prox_l21(u, 0.5, n, p)
1000 loops, best of 3: 271 us per loop

Direct return
++++++++++++++++++++++++

Tested code :
*************

.. code::

   return res*u

Result
******

>>> %timeit test_prox_l21(u, 0.5, n, p)
1000 loops, best of 3: 266 us per loop

FINAL TESTS
-----------

Version 1
+++++++++


.. code::

   def prox_l21(u, l, n_samples, n_kernels):
       """
       proximity operator l(2, 1, 2) norm, see prox_l11
       """
       res = np.zeros(n_samples*n_kernels)
       for i in range(n_kernels):
           res[i*n_samples:(i+1)*n_samples] =\
                   max(1. - l/norm(u[i*n_samples:(i+1)*n_samples], 2), 0.)
       res = res*u
       return res

Version 2
+++++++++

.. code:: python

   def test_prox_l21(u, l, n_samples, n_kernels):
       """
       proximity operator l(2, 1, 2) norm, see prox_l11
       """
       for i in u.reshape(n_kernels, n_samples):
           i * =  max(1. - l/norm(i, 2), 0.)
       return u


Results
+++++++

>>> %timeit prox_l21(u, 0.5, n, p)
1000 loops, best of 3: 1.01 ms per loop

>>> %timeit test_prox_l21(u, 0.5, n, p)
1000 loops, best of 3: 617 us per loop



Improving prox p=1 and q=2
==========================

.. code::

   def prox_l12(u, l, n_samples, n_kernels):
       """
       proximity operator for l(1, 2, 2) norm, see prox_l11
       """
       u = u.reshape(n_kernels, n_samples)
       for i in u:
           Ml, sum_Ml = compute_M(i, l, n_samples)
           i = np.sign(i)*np.maximum(np.abs(i)-(l*sum_Ml)/((1+l*Ml)*norm(i, 2)), 0)
       return u.reshape(n_kernels*n_samples)


.. code::

   def prox_l12_test(u, l, n_samples, n_kernels):
       """
       proximity operator for l(1, 2, 2) norm, see prox_l11
       """
       for i in u.reshape(n_kernels, n_samples):
           Ml, sum_Ml = compute_M(i, l, n_samples)
           i = np.sign(i)*np.maximum(np.abs(i)-(l*sum_Ml)/((1+l*Ml)*norm(i, 2)), 0)
       return u

Results
-------



>>> %timeit prox_l12_test(u, 0.5, 5000, 10)
100 loops, best of 3: 3.17 ms per loop

>>> u = np.arange(5000*10)

>>> %timeit prox_l12(u, 0.5, 5000, 10)
100 loops, best of 3: 3.18 ms per loop

>>> u = np.arange(50000*10)

>>> %timeit prox_l12(u, 0.5, 50000, 10)
10 loops, best of 3: 28.2 ms per loop

>>> u = np.arange(50000*10)

>>> %timeit prox_l12_test(u, 0.5, 50000, 10)
10 loops, best of 3: 23.4 ms per loop

So we chose the second (test) version


More advanced test
------------------

.. code::

   def prox_l12(u, l, n_samples, n_kernels):
       """
       proximity operator for l(1, 2, 2) norm, see prox_l11
       """
       for i in u.reshape(n_kernels, n_samples):
           Ml, sum_Ml = compute_M(i, l, n_samples)
           i = np.sign(i)*np.maximum(np.abs(i)-(l*sum_Ml)/((1+l*Ml)*norm(i, 2)), 0)
       return u

.. code::

   def test_prox_l12(u, l, n_samples, n_kernels):
       """
       proximity operator for l(1, 2, 2) norm, see prox_l11
       """
       res = np.zeros(n_samples*n_kernels)
       for i in range(n_kernels):
           Ml, sum_Ml = compute_M(
                   res[i*n_samples:(i+1)*n_samples], l, n_samples)
           res[i*n_samples:(i+1)*n_samples] =\
               np.sign(res[i*n_samples:(i+1)*n_samples])*\
               np.maximum(np.abs(res[i*n_samples:(i+1)*n_samples]) -\
                           (l*sum_Ml)/((1+l*Ml)*\
                           norm(res[i*n_samples:(i+1)*n_samples], 2)), 0)
       return res

We take, like before, n = 5000, p = 8
u = np.arange(n*p)

>>> %timeit prox_l12(u, 0.5, n, p)
100 loops, best of 3: 2.52 ms per loop

>>> u = np.arange(n*p)

>>> %timeit test_prox_l12(u, 0.5, n, p)
100 loops, best of 3: 3.11 ms per loop

Why this time the "sliced" version (ie test_ version) is slower ??
