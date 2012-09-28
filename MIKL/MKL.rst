MKL
====

Kernels
-------
Assuming each element of the training sample :math:`S = \{(x_1, y_1), ..., (x_N,\; y_N)\}_{i=1}^n` is an element of :math:`\RR^p * Y`, a kernel is simply an element of :math:`\RR^{p*p}`.

From now on, we will assume that we have a set of :math:`\kernels=\{k_1,\ldots,k_\tau\}` of :math:`\tau` kernels and multiple kernel classifiers are the signed versions of functions :math:`f` from the sample-dependent family :math:`\family_S` defined for a training set :math:`S=\{(\bfx_i,y_i)\}_{i=1}^n` as 

.. math::
   
   \family_S=\left\{\bfx\mapsto\sum_{i,t=1}^{n,\tau}\alpha_{it}k_t(\bfx_i,\bfx):\bfalpha\in\realset^{n\tau},k_t\in\kernels\right\}.

Thus, the  output predicted for :math:`\bfx` by  :math:`f\in\family_S` is :math:`\sign(f(\bfx))`.


MKL principle
--------------
The global idea of Multiple Kernel Learning is to combine information from different sources, each one being represented by a kernel.

The first idea is to consider a linear combination of all the kernels ie 

.. math::

   K(x, x') = \sum_{m} K_m(x, x').

The kernels are usually positive definite.
