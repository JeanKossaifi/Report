Setting
=======

We are interested in classification problems. More precisely supervised binary classification. This can be generalised to multiple classification by using *one against all* for example.

We first consider a set of training examples (a samples) :math:`S = \{(x_1, y_1), ..., (x_N,\; y_N)\}_{i=1}^n` of :math:`n_{samples}` labeled pairs :math:`(x_i, y_i) \in \RR^p * Y, \forall i \in \mathbb{N}` where :math:`Y = {-1, +1}` is the sets of labels, and assuming that every observation :math:`x_i` is a p-vector. These pairs are the realisations of :math:`n` independant copies :math:`(X_1, Y_1), \cdots, (X_n, Y_n)` of a random labeled variable (X, Y) distributed according to an unknown distribution on :math:`\RR^p * Y`.

Let :math:`X` be the input data, we want to find a function :math:`F` so that :math:`F(X) = Y` with the best possible accuracy.
