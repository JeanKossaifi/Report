Mixed norms
===========

In this section, it is assumed we have prior knowledge on data structure.
Thus it is possible to define groups of variables using expert knowledge. When those groups are defined, the goal is to detect the useful ones by using a different penalty on each level of the structure.

For this purpose we introduce mixed norms.

The :math:`l_{p,q}` norm are defined by :

.. math::

   \|\bfalpha\|_{pq;2}=\left[\sum_{t=1}^{\tau}\left[\sum_{i=1}^n|\alpha_{it}|^p\right]^{q/p}\right]^{1/q},


Sparsity
--------

Sparsity
   A solution is said to be sparse is one or more of its coefficients are zeroed.

It can be noted that, whereas the norm 2 selects all the parameters, the norm 1 induces a sparsity, meaning that it will only select some parameters, the other's coefficients being zero.

More generally, every norm :math:`p` with :math:`p \le 1` induces a sparse structure. However, a norm :math:`p` is convex only if :math:`p \ge 1:math:`p`. Therefore, the only sparse norm considered will be for :math:`p=1`.

Some norms
----------

:math:`l_p` norms
+++++++++++++++++

Let :math:`\boldsymbol{X}=(x_1,\cdots,x_n)^T` be a vector and :math:`p \in \mathbb{N}, p \ge 1`, the associated norm :math:`l_p` is defined by:

.. math::

     \textrm{For } 1 \leq p<\infty, \quad & \|\boldsymbol{X}\|_p =  \left( \sum_{i=1}^n |x_i|^p \right)^{\frac{1}{p}} \\
     \textrm{For } p=\infty, \quad & \|\boldsymbol{X}\|_{\infty}=  \max \left( |x_1|, \cdots,|x_n| \right).

:math:`l_1` norm
++++++++++++++++

As previously said, the :math:`l_1` norm induces a sparse structure, meaning that it zeroes some of the coefficients.

:math:`l_2` norm
++++++++++++++++

The mixed norm :math:`l_2` equivalent to the simple norm :math:`l_2`.

Group lasso
+++++++++++

The :math:`l_{12}` (p=1, q=2, r=2)  norm is also known as group lasso, as, due to its parsimony it selects only certain kernels.
It was first introduced by Yuan et Lin [2006] in order to select the set of variables associated with relevant groups.

Elitist lasso
++++++++++++++

The :math:`l_{21}` (p=2, q=1, r=2) norm selects some elements only for each kernel. Thus, its parsimony is on the elements of each kernel, not on the kernels themselves.

Use of mixed norm in our problem
--------------------------------

In the previous problem, the penalisation :math:`f_2` will be a mixed norm.

In other words, :math:`f_2(\alpha) = \frac{\lambda}{q}\|\bfalpha\|_{pq}^q`

Thus, the problem becomes :

.. math::
   :label: objective_function

   \min_{\bfalpha\in\realset^{n\kappa}}\sum_{i=1}^n\left|1-y_i\bfk_i^{\top}\bfalpha\right|_+^2+\frac{\lambda}{q}\|\bfalpha\|_{pq}^q

