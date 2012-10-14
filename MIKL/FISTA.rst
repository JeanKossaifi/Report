Algorithm used
==============

The main idea was to use a well-established and robust algorithm. Standing for Iterative Shrinkage Thresholding Algorithm, ISTA was the first choice as it was proved to converge [Fu, 1998 ; Daubechies et coll., 2004].
   
We will use an iterative projected gradient algorithm. The point in which we project is based on the last point and obtained by using the proximity operator.

The proximity operator associated to a proper convex function :math:`\phi : \RR^p \rightarrow \RR`  and to :math:`\lambda > 0` is denoted by :math:`prox_{\lambda, \phi} : \RR^p \rightarrow \RR` and defined as follows :

.. math::

   prox_{\lambda, \phi}(y) = \argmin_{\bfalpha\in\RR^p} \frac{1}{2} \|y - \bfalpha\|_2^2 + \lambda \phi(\bfalpha).
 
ISTA
----

ISTA
   is an iterative projected gradient algorithm. 

Algorithm
++++++++++

.. math::
   :nowrap:

   \begin{algorithm}[H]
     \caption{\small ISTA (squared hinge loss)}
     \label{alg:fb} 
     \begin{algorithmic}
       \STATE \begin{tabular}{@{\hspace{0cm}}p{1.1cm}l}
       \textbf{initialize}  & $\bfalpha^{(0)}\in\RR^{n\tau}$ (for
       instance $\mathbf{0}$) \\
                            & $ K_y $ = diag(y)$K$\\
     \end{tabular}
     % \STATE
     \REPEAT
       \STATE $\bfalpha^{(k+1)} = \prox\nolimits_{\mu, \lambda, f_2}
       \left(\bfalpha^{(k)} 
         - \lambda K_y^T \|1 - K_y \bfalpha^{(k+1)}\|_+ \right)$
       , with $\lambda < \frac{2}{\|K K^T\|_2}$ (Lipschitz constant)
       \UNTIL{convergence}
     \end{algorithmic}
   \end{algorithm}

Convergence
------------


The problem is 

.. math::
   
   \min_{\alpha} f_1(\alpha) + f_2(\alpha)

As previously said, ISTA is an iterative projected gradient algorithm. Therefore it converges if :

* :math:`f_1` is a proper convex function whose gradient is Lipschitz continuous: :math:`\exists L \in \RR_+` such that :math:`\|\nabla f_1 (x) - \nabla f_2(y)\| \le L \|x - y\|` for all :math:`x \text{ and }  y \text{ in } \RR^p \text{. } L` is called the Lipschitz constant.

* :math:`f_2` is a proper convex function (not necessarily differentiable).

As previouslty mentionned, we use the hinge loss :math:`f_1(\bfalpha) = \sum_{i=1}^n\left|1-y_i\bfk_i^{\top}\bfalpha\right|_+` and the mixed norm penalty :math:`f_2(\bfalpha)  = \lambda/q \|\bfalpha\|_{pq}^q`, with :math:`p,q \geq   1`, which are both convex lower semicontinuous functions, nondifferentiable when their arguments are :math:`0`. In addition, :math:`\nabla_{\bfalpha} f_2(\bfalpha)` is only :math:`\beta`-Lipschtiz when :math:`p, q \in  \{1, 2\}`. We therefore limit the study of proximity operators to `\ell_1`, :math:`\ell_2`, :math:`\ell_{12}`, :math:`\ell_{21}` norms.

Hence the convergence of ISTA with the previously mentioned characteristics.

However the convergence rate is only in :math:`O(\frac{1}{N})` where :math:`N` is the number of iteration.  

For this reason, we prefer using a another version of ISTA, which is faster, although more complicated. Hence its name, FISTA, standing for Fast ISTA.

FISTA
-----

Algorithm
+++++++++

.. math::
   :nowrap:

   \begin{algorithm}[H]
     \caption{\small Fast-ISTA (squared hinge loss)}
     \label{alg:fb} 
     \begin{algorithmic}
       \STATE \begin{tabular}{@{\hspace{0cm}}p{1.1cm}l}
       \textbf{initialize}  & $\beta^{(0)} \in \RR^{n\tau}$\\
                           & $ Z^{(1)} = \beta^{(0)}$\\
         & $\tau^{(1)} = 1$\\
         & $ k = 1$\\
         & $\mu = \frac{1}{|| K^* K ||} < \frac{2}{\|K K^T\|_2}$ (Lipschitz constant)\\
         & $K_y = \text{diag}(y) K$\\
         & $\lambda =$ penalisation coefficient\\
     \end{tabular}
     % \STATE
     \REPEAT
       \STATE $\beta^{(k)} = \prox_{\mu \lambda f_2} ( Z^{(k)} + K_y^{*} \|1 - K_y Z^{(k)} \|_+) $\\
      $ \tau^{(k+1)} = \frac{1 + \sqrt{1 + 4 \tau^{k^2}}}{2} $\\
      $ Z^{(k+1)} = \beta^{(k)} + \frac{\tau^{(k)} - 1}{\tau^{(k+1)}} ( \beta^{(k)} - \beta^{(k - 1)}) $\\
       \UNTIL{convergence}
     \end{algorithmic}
   \end{algorithm}

The result is the p-vector :math:`Z^{(k+1)}`, corresponding to the coefficients vector associated to each sample.

Mixed norms
-----------

For p=q=1
+++++++++

.. math::
   
   \hat{\alpha}_{l,m} = \sign(u_{l,m}) \left| |u_{l,m}| - \lambda \right|_+


which is also know as the soft-thresholding operator.

For p=2 and q=1
+++++++++++++++

.. math::

   \hat{\alpha}_{l,m} = u_{l,m} \left| 1 - \frac{ \lambda}{ \|u_{l \bullet }\|_{2}} \right|_+

where l is in range(0, n_kernels) and m is in range(0, n_samples) so :math:`u_{l \bullet }` = [u(l, m) for l in n_samples]

This operator is detailed later on in the `Implementation` part.


For p=1 and q=2
+++++++++++++++

.. math::

   \hat{\alpha}_{l,m} = sign(u_{l,m})\left||u_{l,m}| - \frac{\lambda \sum\limits_{m_l=1}^{M_l} u2_{l,m_l}}{(1+\lambda M_l) \|u_{l \bullet }\|_{2}} \right|_+

where  :math:`u2_{l,m_l}`  denotes the :math:`|u_{l,m_l}|` ordered  by descending  order for fixed  :math:`l`,  and the quantity :math:`M_l` is the number computed in compute_M


For p=q=2
+++++++++

.. math::

   \hat{\alpha}_{l,m} = \frac{1}{1 + \lambda} \, u_{l,m}

