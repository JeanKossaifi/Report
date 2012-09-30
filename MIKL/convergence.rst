Convergence
===========

First idea
----------

The first idea to check the convergence of the algorithm is to test

.. math::

  || Z^k - Z^{k+1}|| < \epsilon

However, this quantity can become very small whereas convergence is not reached yet.

Another, better, idea is to consider the normalised quantity : 

.. math::

  \frac{|| Z^k - Z^{k+1}||}{ || Z^k ||} < \epsilon

This criterion is also biased.

Eventually, the best solution is to consider the dual gap.


Dual gap
--------

We have to introduce the dual problem :math:`F_d`, and, to a variable :math:`X^{(k)}` we have to associate a dual variable :math:`Y^{(k)}`

Then the dual gap is defined as :

.. math::

   \eta^{(k)} = F_p(X^{(k)}) - F_d(Y^{(k)}) \ge 0

When optimality is reached, the duality gap is equal to zero.

Thus, a good convergence criterion is :

.. math::
   
   F_p(X^{(k)}) - F_d(Y^{(k)}) < \epsilon

Dual problem
++++++++++++

We remind the reader that the primal problem is :

.. math::
   :label: objective_function

   F_p(\alpha) = arg \min_{\bfalpha\in\realset^{n\kappa}}\sum_{i=1}^n\left|1-y_i\bfk_i^{\top}\bfalpha\right|_+^2+\frac{\lambda}{q}\|\bfalpha\|_{pq;r}^q


The dual problem is the following :

.. math::
   :label: dual_objective_function

   \max_{Y} -\frac{1}{2} \|Y\|_2^2 + Tr(Y^T M) - f_2^* (G^* Y)

where :math:`f_2^*` is the Fenchel conjugate of :math:`\frac{\lambda}{q} f_2` and Y is the dual variable, :math:`Y = y - K \alpha`.

Fenchel conjugate of a mixed norm
+++++++++++++++++++++++++++++++++++

The Fenchel conjugate of a mixed norm is the function :

.. math::
   :nowrap:
   
   \begin{equation}
   v(x) = 
   \left\{
       \begin{aligned}
         & 0 \text{ if } \|x\|_{p', q'} \le 1 \\
         & +\infty \text{ otherwise}.
       \end{aligned}
     \right.
   \end{equation} 

where :math:`\|.\|_{p', q'}` is the dual mixed norm of the original mixed norm ( :math:`\|.\|_{p', q'}` ).


In practice, if we are in the second case, (ie :math:`\|x\|_{p', q'} > 1`), we will normalise the dual variable to fall back to the first case.


Fenchel conjugate of a squared mixed norm
+++++++++++++++++++++++++++++++++++++++++

The Fenchel conjugate of a squared mixed norm is the function :

.. math::

   v(x) = \frac{1}{2} \|x\|_{p',q'}^2


where :math:`\|.\|_{p', q'}` is the dual mixed norm of the original mixed norm ( :math:`\|.\|_{p', q'}` ).

Dual norm
+++++++++

The dual norm of :math:`\|.\|_{p,q}` is the norm

.. math::
   
   \|.\|_{p',q'} \text{ such as } : & \text{ if } p>1, \frac{1}{p} + \frac{1}{p} \text{ ( same for q)}\\
                                    & \text{ if } p=1, p'=+\infty \text{( same for q)}


Dual variable
+++++++++++++

For a variable :math:`\alpha`, the dual variable associated is :math:`Y = \|y - K\alpha\|_+ = \|1 - K_y \alpha\|_+`

