FISTA
=====

Big picture
-----------

Fista was implemented as a class.
This has 3 main methods, namely fit, predict and score.

As indicated by its name, fit *fits* the data, ie have the algorithm learn from the data. 

Predict computes the output for the given data using the coefficients computed while fitting the data.

Finally, score computes the score of the predicted output, the score being the percentage of good classification.

All the parameters of the __init__ method are optional, meaning that it is possible to instantiate an object without any argument.

In addition, several convenient features have been implemented.

Generic class
-------------

The class can be used either with a squared hinge loss (by default) or with a least square.

For the latter, the score and some additional features have not been implanted yet for the latter, however.

The main difference between the two losses is the step determining where to apply the gradient descent.
This is store as a function, chosen at the beginning of the algorithm, depending on the loss.

Computation of the Lipschitz constant
-------------------------------------

Computing the Lipschitz constant can be time and memory consuming for big data. Therefore, the user is provided with the opportunity to pass it as an argument of the fit method, to recompute it every time, or, finally, to save it.

In this last case, the sha1 hash of the data is computed, and used to identify this uniquely. This allows computing the corresponding Lipschitz constant and storing it, in a convenient way, along with the hash.

Thus, each time new data are fitted, their hash is computed and compared to the existing ones. Eventually, if the Lipschitz constant have already been computed, it is directly loaded. In the other case, the calculus is done and the result store like previously described.

Info
----

The `info` method can only be used after the instance has been fitter and is only here for test purpose. It returns a Bunch of useful information.

A Bunch is a dictionary that exposes its methods as attributes.
This is far more convenient when seeking for information.

Prox for the l122 norm (p=1, q=2 and r=2)
=========================================


The proximity operator for this norm is 

.. math::

   \hat{\alpha}_{l,m} = \sign(u_{l,m})\left||u_{l,m}| -
      \frac{\lambda \sum\limits_{m_l=1}^{M_l} \check
        u_{l,m_l}}{(1+\lambda M_l) \|u_{l \bullet }\|_{2}} 
    \right|_+ ,

where  :math:`\check  u_{l,m_l}`  denotes the  :math:`|u_{l,m_l}|` ordered  by descending  order for fixed  :math:`l`,  and the quantity :math:`M_l` is the number such that
    
.. math::

   \check u_{l,M_l+1} \leq  \lambda \sum_{m_l=1}^{M_l+1}
   \left(\check u_{l,m_l} - \check u_{l,M_l+1}\right) \ ,
    
and

.. math::

   \check     u_{l,M_l}    >    \lambda\sum_{m_l=1}^{M_l}
   \left(\check u_{l,m_l} - \check u_{k,M_l}\right) .
       
Let us first remember that :math:`\check u`, :math:`u` and :math:`\alpha` have the same dimension.
:math:`\alpha` is of dimension (n_kernels * n_samples) ( where n_kernels is the number of kernels and n_samples the number of observations).

The reader is reminded that :math:`X` is of dimension (ie shape) (n_samples, n_samples*n_kernels)

It can be observed that :math:`X * \alpha` is effectively of shape (n_samples, 1) as :math:`y` the labels vector to be predicted.

We are here computing the proximity operator with p=1, q=2, r=2 of :math:`\check u`, which can be rewritten as follows.


.. math::

   \mathbf{\check u} = 
    \begin{pmatrix}
    \check u_{1,1}  &  \check u_{1,2}   &  \check u_{1,3}   & \cdots &  \check u_{1,n_{samples}}\\
    \check u_{2,1}  &  \check u_{2, 2}  &  \check u_{2, 3}  & \cdots &  \check u_{2, n_{samples}}\\
    \vdots & \vdots & \vdots & \ddots & \vdots\\
    \check u_{n_{kernels}, 1}  &  \check u_{n_{kernels},2 }  &  \check u_{n_{kernels},3} & \cdots & \check u_{n_{kernels}, n_{samples}}\\
    \end{pmatrix}


Computing :math:`M_l`
---------------------

The quantity :math:`M_l` is the number such that
    
.. math::
   :label: Ml1

   \check u_{l,M_l+1} \leq  \lambda \sum_{m_l=0}^{M_l+1}
   \left(\check u_{l,m_l} - \check u_{l,M_l+1}\right) \ ,
    
and

.. math::
   :label: Ml2

   \check     u_{l,M_l}    >    \lambda\sum_{m_l=0}^{M_l}
   \left(\check u_{l,m_l} - \check u_{k,M_l}\right) .

.. warning::
   
   In the above formula, we have started indexing at zero instead of 1 to be coherent with python indexing. Therefore, we will have to add one to the final result.

Let us fix :math:`k = M_l`.

Let :math:`\check u_l` be the considered kernel (ie a line of :math:`\check u`).

We can define

.. math:: 
   :label: g_k
   
   g_{M_l + 1} = g_{k+1} = \sum_{m_l=0}^{M_l+1} \left(\check u_{l,i} - \check u_{l,M_l+1}\right)\\

and 

.. math::
   :label: h_k

   h_{M_l} = h_k = \sum_{m_l=0}^{M_l} \left(\check u_{l,i} - \check u_{k,M_l}\right)


Thus, g and h will be vectors of :math:`\RR^{n_kernels}` and we have: 

.. math::

   g_k & = \lambda\sum_{i=0}^{k+1} \left(\check u_{l,i} - \check u_{l,k+1}\right)\\
       & = \lambda\sum_{i=0}^{k} \left(\check u_{l,i} - \check u_{l,k+1}\right)\\
       & = \lambda \left[ ( \sum_{i=0}^{k} \check u_{l,i}) - (k+1) \check u_{l, k+1} \right] \\


Hence the vector g : 

.. math::
       g = \lambda 
             \begin{pmatrix}
             \check u_0  \\
             \vdots \\
             \check u_0 + \cdots +  \check u_{n-1} \\
             \end{pmatrix}
         - \begin{pmatrix}
             1  \\
             \vdots \\
             n \\
             \end{pmatrix}
          \cdot \begin{pmatrix}
             \check u_1  \\
             \vdots \\
             \check u_n \\
             \end{pmatrix}

Finally, in "pseudo"-Python :

.. math::

   g = \lambda * (np.cumsum( \check u [:-1] - (np.arange(len(\check u) -1 ) +1 ) * \check u [1:]

Similarly, we have: 

.. math::

   h_k & = \lambda\sum_{i=0}^{k} \left(\check u_{l,i} - \check u_{l,k}\right)\\
       & = \lambda \left[ ( \sum_{i=0}^{k} \check u_{l,i}) - (k+1) \check u_{l, k} \right] \\

Hence the vector h : 

.. math::
       h = \lambda 
             \begin{pmatrix}
             \check u_0  \\
             \vdots \\
             \check u_0 + \cdots +  \check u_{n-1} \\
             \end{pmatrix}
         - \begin{pmatrix}
             1  \\
             \vdots \\
             n \\
             \end{pmatrix}
          \cdot \begin{pmatrix}
             \check u_0  \\
             \vdots \\
             \check u_{n+1} \\
             \end{pmatrix}

Finally, in "pseudo"-Python :

.. math::

   h = \lambda * (np.cumsum( \check u [:-1] - (np.arange(len(\check u) -1 ) +1 ) * \check u [:-1]


It can be noted that if :math:`u_l` is of size :math:`(n+1)` then :math:`M_l \in [O, \cdots, n-1]` because we also consider :math:`M_{l+1}` and begin indexing at zero in python.

Finding the good indice
------------------------

Assuming that g and h are already computed, :math:`M_l` is such that:

.. math::
   
   u_{M_{l+1}} - g \le 0\\
   \text{and } u_{M_l} - h > 0

ie such that :math:`[ (g(M_l) \leq O)` & :math:`(h(M_l) > 0) ]`

In other words, :math:`M_l = argmax((g(M_l) \leq O.)` & :math:`(h(M_l) > 0.)) + 1` where & is the logical element wise operator on arrays.

.. warning::

   We have to add 1 because in Python indexing starts at 0, as mentioned at the beginning.

Mixed norms
===========

The mixed norms were computed very easily by remembering that :math:`|v|_{p, q} = \left||v|_p\right|_q`

The basic norms are computed using the scipy `norm` function.

Dual mixed norms
================

Again, the dual mixed normed are computed in an easy way by applying the mathematical definition, and applying the right norm.

For example, computing the dual mixed norm l11 of v is computing its infinite norm.

Cross-validation
================

Both the cross validation and the double cross-validation use parallel computing.

Thus, the results on the different folds are computed at the same time on different CPUs.

For that purpose, we used the `Joblib` library.

Last, all the information returned are packed in a Bunch which is a dictionary that exposes its elements as attributes.

Data
====

Simulated data
--------------

For test purpose we generated seeded random data.

The seed is here to ensure reproducibility of the experiment.

Thus, we generated a random kernel (ie a random matrix of size ( :math:`n_{samples}`, :math:`n_{samples}*n_{kernels}` ) and random associated labels. For these, we took the sign of the normal random data (which is 1 or -1).

For the random data generator we used a normal generator, based on a Mercen-Twister uniform one.


Yeast_data
----------

Original data
+++++++++++++

We wrote a function that loads automatically the data in the memory. If needed, it downloads the files from the internet, save it on the disk, pre-process it to be more convenient and convert it in a more efficient way, before saving it to the disk, and removing the original.

Using 200 samples
+++++++++++++++++

To use only the first 200 samples, we wrote a function that loads only the needed data.
   
We first use our previous function to load the data and create the list of the names.

.. code-block:: python

   data = fetch_data()

   data_names = [#'kernel_matrix_pfamdom_cn_3588',
            'kernel_matrix_tap_n_3588',
             'kernel_matrix_mpi_n_3588',
             'kernel_matrix_mgi_n_3588',
             #'kernel_matrix_exp_diff_n_3588',
             'kernel_matrix_exp_gauss_n_3588',
             'kernel_matrix_pfamdom_exp_cn_3588',
             'kernel_matrix_sw_cn_3588']o

We then create a function that returns *only* the first 100 elements belonging to the class number `column1`, and the 100 belonging only to the class `column2`.

For that we create an appropriate mask that we will apply to the data.

.. code-block:: python

   def unique_indices(y, column1, column2, n_indices):
    """
    Returns a list of indices of the n_indices first elements belonging ONLY to column1 or column2
    """
    n_samples = len(y[:, 0])
    mask1 = (y[:, column1] == 1) & np.logical_not((np.delete(y, [11, 12, column1], 1)==1).any(axis=1))
    mask2 = (y[:, column2] == 1) & np.logical_not((np.delete(y, [11, 12, column2], 1)==1).any(axis=1))
    # We want a mask of indices, not of Booleans
    mask1 = set(np.arange(n_samples)[mask1==True])
    mask2 = set(np.arange(n_samples)[mask2==True])
    # We consider only the 100 first in column1 who are not in column2
    mask1 = list(set.difference(mask1, mask2))[:n_indices]
    mask2 = list(mask2)[:n_indices]
    # We create the full list indices
    indices = mask1
    indices.extend(mask2)
    return indices

We then verify that every kernel has the right size :

.. code-blocks:: python

   new_data = Bunch()
indices = unique_indices(data.y, 5, 7, 100)
for i in data_names:
    new_data[i] = data.kernels[i][indices, :][:, indices]
    print new_data[i].shape

>>>
(200, 200)
(200, 200)
(200, 200)
(200, 200)
(200, 200)
(200, 200)

And that the kernel is composed as wanted : 

.. code-blocks:: python

   # y is the label of class 5 : 1 if the element belongs to class 5
   # -1 if it doesn't (ie it belongs to class 7)
   new_data['y'] = data.y[indices, 5]
   print new_data.y.shape
   print len(new_data.y[new_data.y==1])
   print len(new_data.y[new_data.y==-1])

>>>
(200,)
100
100

We verify that the kernel has 200 elements, 100 belonging only to the first class, and 100 to the second one.


