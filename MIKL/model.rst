Model
=====

Here we consider multiple kernel classifiers where the kernel used are not necessary positive definite.

We want to combine information from different sources, each one being represented by one or more kernels, and to integrate prior knowledge.

Thus, the goal is to find a vector :math:`\alpha` that yields the lowest generalisation error. 

Finally, this problems comes to solving the following penalised optimisation problem : 

.. math::
   :label: objective_function_general

   \min_{\bfalpha\in\realset^{n\kappa}}\sum_{i=1}^n\left|1-y_i\bfk_i^{\top}\bfalpha\right|_+^2+f_2(\alpha)

Where :math:`f_2` is the regularisation term which integrates any prior knowledge, :math:`|x|_+ = max(x, 0)` and :math:`k_i \text{ is the } i^{th} \text{ column of the kernel } K`.
