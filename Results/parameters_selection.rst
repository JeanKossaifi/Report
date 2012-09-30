Parameter selection
===================

An important aspect of this work is the selection of the best regularisation parameter ( :math:`\lambda` ).

For this purpose we use double cross validation. This consists of evaluating the test error with a learning test, with cross validation. The optimal regularisation hyper-parameters are chosen during this step using cross-validation as well.

Thus, we evaluate by cross validation :

 * The optimal regularisation parameter, in an intern loop
 * The test error, in an extern loop

.. math::
   :nowrap:

   \begin{algorithm}[H]
     \caption{\small Double cross validation}
     \label{alg:double_cross_val} 
     \begin{algorithmic}
       \STATE \begin{tabular}{@{\hspace{0cm}}p{1.4cm}l}
       \textbf{Parameters}  & $(K, y)$ : observation matrix and the vector of associated labels.\\
           & $C$ : hyper-parameters vector\\
           & $K_{ext}$ : number of folds for the outer loop\\
           & $K_{int}$ : number of folds for the inner loop\\
       \end{tabular}
       \STATE $KFold_{ext} \leftarrow \text{ divide K into } K_{ext} \text{ folds}$\\
     \FOR{i \textbf{from} 1 \TO $K_{ext}$}
         \STATE $\text{train}_{ext}[i] \leftarrow 1 \text{ bloc of } KFold_{ext}$
         \STATE $\text{valid}_{ext}[i] \leftarrow \text{ the other blocks of } KFold_{ext}$
         \STATE $KFold_{int} \leftarrow \text{ divide train}_{ext}[i] \text{ into } K_{int} \text{ folds}$\\
         \FOR{j \textbf{from} 1 \TO $K_{int}$}
            \STATE $\text{train}_{int}[j] \leftarrow 1 \text{ bloc of } KFold_{int}$
            \STATE $\text{valid}_{int}[j] \leftarrow \text{ the other blocks of } KFold_{int}$
            \FOR{k \textbf{from} 1 \TO size(C)}
               \STATE $\text{model}_{int}$[j, k] $\leftarrow$ fit-algorithm($\text{train}_{int}[j]$)
               \STATE $\text{error}_{int}$[j, k] $\leftarrow$ compute-error($\text{model}_{int}[j]$, $\text{valid}_{int}[j]$))
            \ENDFOR
         \ENDFOR
         \STATE $\text{error}_{int}$[i]$ \leftarrow  \text{mean}_j( \text{error}_{int}$[j,k])
         \STATE $\text{C}_{opt}$[i]$     \leftarrow  \text{min}( \text{error}_{int}$[i])
         \STATE $\text{model}_{ext}$[i]$ \leftarrow  \text{fit-algorithm}( \text{train}_{ext}$[i], $\text{C}_{opt}$[i])
         \STATE $\text{error}_{ext}$[i]$ \leftarrow  \text{compute-error}( \text{model}_{ext}$[i], $\text{valid}_{ext}$[i])
     \ENDFOR 
     \STATE $\text{error}_{test} \leftarrow  \text{mean}_i( \text{error}_{ext}$[i])
     \RETURN $\text{error}_{test}$ 
     \end{algorithmic}
   \end{algorithm}

