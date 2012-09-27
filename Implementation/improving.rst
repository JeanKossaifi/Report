Improving prox p=2, q=1
=======================

First implementation
--------------------

The fist implementation consisted of creating a new numpy array of the correct shape and then filling it with the corresponding values :

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

The second implementation was modifying inplace the array argument: 

.. code-block:: python

   def prox_l21(u, l, n_samples, n_kernels):
       """
       proximity operator l(2, 1, 2) norm, see prox_l11
       """
       for i in range(n_kernels):
           u[i*n_samples:(i-1)*n_samples] * =\
                   max(1. - l/norm(u[i*n_samples:(i-1)*n_samples], 2), 0.)
       return u


Memory use
----------

Test program
++++++++++++

We used memory_profiler for the tests. This is a tool that monitors, for every line of the program, the amount of memory (RAM) used.

.. code-block:: python
   :linenos:

   from fista import prox_l21, test_prox_l21
   import numpy as np

   u = np.arange(5000*10)

   @profile
   def profile(u):
     for i in range(1500):
         u = prox_l21(u, 0.5, 5000, 10)

   profile(u)

To test the other program, we replace *prox_l21* by *test_prox_l21*.

Results
+++++++

The results are summarised in the following tables.

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

The second criterion to consider is execution speed. 

To monitor it we use an IPython *magic*, %timeit, that indicates the execution time of a given piece of code by executing it several times and taking the average.

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

In this new version we reshape u, so that the new vector has as many lines as there are kernels, to be able to process kernel by kernel:

.. code::

    def test_prox_l21(u, l, n_samples, n_kernels):
        for i in u.reshape(n_kernels, n_samples):
            u = u * max(1. - l/norm(u, 2), 0)
        return u

Execution_time
++++++++++++++

We compare the execution time of this new version compared to the former one.

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

Here, we check if the way in which we return the result has any influence.

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

.. code-block:: python

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

Version that creates a new array and fill it :

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


Version that modifies the given array inplace:

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
We ran different tests with different data

>>> %timeit prox_l12_test(u, 0.5, 5000, 10)
100 loops, best of 3: 3.17 ms per loop

>>> u = np.arange(5000*10)

>>> %timeit prox_l12(u, 0.5, 5000, 10)
100 loops, best of 3: 3.18 ms per loop

Creating a new test array :

>>> u = np.arange(50000*10)

>>> %timeit prox_l12(u, 0.5, 50000, 10)
10 loops, best of 3: 28.2 ms per loop

>>> u = np.arange(50000*10)

>>> %timeit prox_l12_test(u, 0.5, 50000, 10)
10 loops, best of 3: 23.4 ms per loop

So we chose the second (test) version, the faster one.


More advanced test
------------------

Simple inplace modification version :

.. code::

   def prox_l12(u, l, n_samples, n_kernels):
       """
       proximity operator for l(1, 2, 2) norm, see prox_l11
       """
       for i in u.reshape(n_kernels, n_samples):
           Ml, sum_Ml = compute_M(i, l, n_samples)
           i = np.sign(i)*np.maximum(np.abs(i)-(l*sum_Ml)/((1+l*Ml)*norm(i, 2)), 0)
       return u

Complex version creating a new array and filling it appropriately:

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
