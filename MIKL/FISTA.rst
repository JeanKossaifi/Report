Algorithm used
==============

The main idea was to use a well-established and robust algorithm. Standing for Iterative Shrinkage Thresholding Algorithm, ISTA was the first choice.

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
       instance $\mathbf{0}$) % \vphantom{$\bigg \lfloor$}
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
   
As previously said, ISTA is an iterative projected gradient algorithm. Therefore it is proved to converge. However the convergence rate is only in :math:`O(\frac{1}{N})` where :math:`N` is the number of iteration.  

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

Note : 
