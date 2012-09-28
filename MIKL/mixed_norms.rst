Mixed norms
===========

In this section, it is assumed we have prior knowledge on data structure.
Thus it is possible to define groups of variables using expert knowledge. When those groups are defined, the goal is to detect the useful ones by using a different penalty on each level of the structure.

For this purpose we introduce mixed norms.

The :math:`l_{p,q,r}` norm are defined by :

If r = 1: 

.. math::
   
   \|\bfalpha\|_{pq; 1}=\left[\sum_{i=1}^n\left[\sum_{t=1}^{\tau}|\alpha_{it}|^p\right]^{q/p}\right]^{1/q},

If r = 2:

.. math::

   \|\bfalpha\|_{pq;2}=\left[\sum_{t=1}^{\tau}\left[\sum_{i=1}^n|\alpha_{it}|^p\right]^{q/p}\right]^{1/q},


(note that the order of summation has changed).

We will mainly consider r=2. In the remaining of this report, when r is not specified, it is assumed to be equal to 2.

Parsimony
---------
It can be noted that, whereas the norm 2 selects all the parameters, the norm 1 induces a parsimony, meaning that it will only select some parameters, the other's coefficients being zero.

Group lasso
-----------
The :math:`l_{21}` (p=2, q=1, r=2)  norm is also known as group lasso, as, due to its parsimony it selects only certain kernels.

p=1 q=2 r=2
-----------
The :math:`l_{12}` norm selects some elements only for each kernel. Thus, its parsimony is on the elements, not on the kernels.

Use of mixed norm in our problem
--------------------------------

In the previous problem, the penalisation :math:`f_2` will be a mixed norm.

In other words, :math:`f_2(\alpha) = \frac{\lambda}{q}\|\bfalpha\|_{pq;r}^q`

Thus, the problem becomes :

.. math::
   :label: objective_function

   \min_{\bfalpha\in\realset^{n\kappa}}\sum_{i=1}^n\left|1-y_i\bfk_i^{\top}\bfalpha\right|_+^2+\frac{\lambda}{q}\|\bfalpha\|_{pq;r}^q

