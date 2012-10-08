Experiment of Yeast_SW_5-7
==========================

:math:`l_2` norm
----------------

Reducing lambda range
+++++++++++++++++++++

We first reduced the range of possible lambdas by fitting FISTA with many different possible values. 

.. code:: python

    infos = lambda_choice('l22', lambdas, 4, Ksw, y, n_iter=10000, n_jobs=4)

Result 
******

======================= ======================  ===================== ====================
Lambda                  Dual gap                aux score             classification score
======================= ======================  ===================== ====================
Lambda = 0.001000       dual gap = 0.062820     auc_score = 1.000000  score = 100.000000
Lambda = 0.010000       dual gap = 0.615903     auc_score = 1.000000  score = 100.000000
Lambda = 0.100000       dual gap = 5.091619     auc_score = 1.000000  score = 100.000000
Lambda = 1.000000       dual gap = 10.217634    auc_score = 1.000000  score = 100.000000
Lambda = 10.000000      dual gap = 56.041059    auc_score = 0.980000  score = 98.000000
Lambda = 100.000000     dual gap = 132.912672   auc_score = 0.950000  score = 95.000000
Lambda = 1000.000000    dual gap = 149.936520   auc_score = 0.945000  score = 94.500000
Lambda = 10000.000000   dual gap = 151.853605   auc_score = 0.945000  score = 94.500000
Lambda = 100000.000000  dual gap = 152.047744   auc_score = 0.945000  score = 94.500000
======================= ======================  ===================== ====================


More precise range
++++++++++++++++++

Based on this first experiment we chose a more precise range.

.. code:: python

    lambdas = [1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]


Result
******

=================== ===================== =============== ====================
Lambda                  Dual gap              aux score   classification score
=================== ===================== =============== ====================
Lambda = 1.000000   dual gap = 10.217634  auc = 1.000000  score = 100.000000
Lambda = 2.000000   dual gap = 0.000001   auc = 1.000000  score = 100.000000
Lambda = 3.000000   dual gap = 10.401112  auc = 1.000000  score = 100.000000
Lambda = 4.000000   dual gap = 19.591883  auc = 1.000000  score = 100.000000
Lambda = 5.000000   dual gap = 27.599890  auc = 1.000000  score = 100.000000
Lambda = 6.000000   dual gap = 34.610895  auc = 0.995000  score = 99.500000
Lambda = 7.000000   dual gap = 40.825269  auc = 0.990000  score = 99.000000
Lambda = 8.000000   dual gap = 46.427253  auc = 0.985000  score = 98.500000
Lambda = 8.500000   dual gap = 49.013493  auc = 0.985000  score = 98.500000
Lambda = 9.000000   dual gap = 51.471548  auc = 0.980000  score = 98.000000
Lambda = 9.500000   dual gap = 53.811158  auc = 0.980000  score = 98.000000
Lambda = 10.000000  dual gap = 56.041059  auc = 0.980000  score = 98.000000
=================== ===================== =============== ====================

Thus we chose the higher lambda raising the maximal score: we take :math:`\lambda = 5`.

Cross-validation
++++++++++++++++

We use cross-validation to estimate the performance of our algorithm.


Result
******

.. parsed-literal::

    mean score : 84.000000, score std : 5.830952, mean auc : 0.840000

Detailed results by fold
************************

.. parsed-literal::

    ***** FOLD 1  *********
    
    objective_function  :  12.7693383531
    lambda_  :  0.1
    gap  :  11.7321925328
    nulled_coefs_per_kernel  :  [21]
    score  :  85.0
    norms  :  [121.83457709021104]
    nulled_kernels  :  0
    nulled_coefs  :  21
    auc_score  :  0.85
    dual_objective_function  :  1.03714582038
    
    
    
    ***** FOLD 2  *********
    
    objective_function  :  12.6649694244
    lambda_  :  0.1
    gap  :  11.6331045205
    nulled_coefs_per_kernel  :  [22]
    score  :  90.0
    norms  :  [120.81971695411008]
    nulled_kernels  :  0
    nulled_coefs  :  22
    auc_score  :  0.9
    dual_objective_function  :  1.03186490389
    
    
    
    ***** FOLD 3  *********
    
    objective_function  :  12.6383749217
    lambda_  :  0.1
    gap  :  11.5995836482
    nulled_coefs_per_kernel  :  [26]
    score  :  90.0
    norms  :  [120.52941405053399]
    nulled_kernels  :  0
    nulled_coefs  :  26
    auc_score  :  0.9
    dual_objective_function  :  1.03879127349
    
    
    
    ***** FOLD 4  *********
    
    objective_function  :  12.6304869888
    lambda_  :  0.1
    gap  :  11.594977658
    nulled_coefs_per_kernel  :  [27]
    score  :  85.0
    norms  :  [120.44574708901398]
    nulled_kernels  :  0
    nulled_coefs  :  27
    auc_score  :  0.85
    dual_objective_function  :  1.03550933087
    
    
    
    ***** FOLD 5  *********
    
    objective_function  :  12.8908535799
    lambda_  :  0.1
    gap  :  11.8454498191
    nulled_coefs_per_kernel  :  [20]
    score  :  90.0
    norms  :  [122.93799476466741]
    nulled_kernels  :  0
    nulled_coefs  :  20
    auc_score  :  0.9
    dual_objective_function  :  1.04540376085
    
    
    
    ***** FOLD 6  *********
    
    objective_function  :  12.8767344714
    lambda_  :  0.1
    gap  :  11.8286523183
    nulled_coefs_per_kernel  :  [24]
    score  :  85.0
    norms  :  [122.82120840763614]
    nulled_kernels  :  0
    nulled_coefs  :  24
    auc_score  :  0.85
    dual_objective_function  :  1.04808215313
    
    
    
    ***** FOLD 7  *********
    
    objective_function  :  12.8168814567
    lambda_  :  0.1
    gap  :  11.7726388721
    nulled_coefs_per_kernel  :  [23]
    score  :  80.0
    norms  :  [122.2446330351401]
    nulled_kernels  :  0
    nulled_coefs  :  23
    auc_score  :  0.8
    dual_objective_function  :  1.04424258459
    
    
    
    ***** FOLD 8  *********
    
    objective_function  :  12.6894865642
    lambda_  :  0.1
    gap  :  11.6507225359
    nulled_coefs_per_kernel  :  [25]
    score  :  85.0
    norms  :  [121.01319599152858]
    nulled_kernels  :  0
    nulled_coefs  :  25
    auc_score  :  0.85
    dual_objective_function  :  1.03876402832
    
    
    
    ***** FOLD 9  *********
    
    objective_function  :  12.7055328011
    lambda_  :  0.1
    gap  :  11.6679464382
    nulled_coefs_per_kernel  :  [23]
    score  :  80.0
    norms  :  [121.19949236488191]
    nulled_kernels  :  0
    nulled_coefs  :  23
    auc_score  :  0.8
    dual_objective_function  :  1.03758636295
    
    
    
    ***** FOLD 10  *********
    
    objective_function  :  12.9282530532
    lambda_  :  0.1
    gap  :  11.9244237222
    nulled_coefs_per_kernel  :  [4]
    score  :  70.0
    norms  :  [123.62351056512924]
    nulled_kernels  :  0
    nulled_coefs  :  4
    auc_score  :  0.7
    dual_objective_function  :  1.00382933107
    
    
    


:math:`l_1` norm
----------------

Reducing lambda range
+++++++++++++++++++++

We used the same protocol here

======================= ===================== ===================== ====================
Lambda                  Dual gap              auc score             classification score
======================= ===================== ===================== ====================
Lambda = 0.001000       dual gap = 0.133421   auc_score = 1.000000  score = 100.000000
Lambda = 0.010000       dual gap = 1.328398   auc_score = 1.000000  score = 100.000000
Lambda = 0.100000       dual gap = 12.715437  auc_score = 1.000000  score = 100.000000
Lambda = 1.000000       dual gap = 72.643917  auc_score = 0.945000  score = 94.500000
Lambda = 10.000000      dual gap = 35.347653  auc_score = 0.500000  score = 50.000000
Lambda = 100.000000     dual gap = 0.000000   auc_score = 0.500000  score = 50.000000
Lambda = 1000.000000    dual gap = 0.000000   auc_score = 0.500000  score = 50.000000
Lambda = 10000.000000   dual gap = 0.000000   auc_score = 0.500000  score = 50.000000
Lambda = 100000.000000  dual gap = 0.000000   auc_score = 0.500000  score = 50.000000
======================= ===================== ===================== ====================


Double-cross-validation
+++++++++++++++++++++++

.. code:: python

    lambdas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3]

We use double cross validation with 100,000 iterations

.. code:: python

    result = double_cross_val('l11', lambdas, 4, 4, Ksw, y, n_iter=100000)

Results by external cross validation
************************************
================================ =========== ============== ===================
External cross validation number Best lambda external score internal mean score
================================ =========== ============== ===================
1                                0.1         80.0           83.5
1                                0.1         80.0           83.5
1                                0.1         80.0           83.5
1                                0.1         80.0           83.5
================================ =========== ============== ===================

Cross-validation
++++++++++++++++

Result
******
.. parsed-literal::

    mean score : 84.000000, score std : 5.830952, mean auc : 0.840000


Detailed results by fold
************************

.. code:: python

    for i, e in enumerate(res_SW_l1.infos):
        print "***** FOLD %d  *********\n" % (i+1) 
        for j in e:
            print j, " : ", e[j]
        print "\n\n"

.. parsed-literal::

    ***** FOLD 1  *********
    
    objective_function  :  12.7693383531
    lambda_  :  0.1
    gap  :  11.7321925328
    nulled_coefs_per_kernel  :  [21]
    score  :  85.0
    norms  :  [121.83457709021104]
    nulled_kernels  :  0
    nulled_coefs  :  21
    auc_score  :  0.85
    dual_objective_function  :  1.03714582038
    
    
    
    ***** FOLD 2  *********
    
    objective_function  :  12.6649694244
    lambda_  :  0.1
    gap  :  11.6331045205
    nulled_coefs_per_kernel  :  [22]
    score  :  90.0
    norms  :  [120.81971695411008]
    nulled_kernels  :  0
    nulled_coefs  :  22
    auc_score  :  0.9
    dual_objective_function  :  1.03186490389
    
    
    
    ***** FOLD 3  *********
    
    objective_function  :  12.6383749217
    lambda_  :  0.1
    gap  :  11.5995836482
    nulled_coefs_per_kernel  :  [26]
    score  :  90.0
    norms  :  [120.52941405053399]
    nulled_kernels  :  0
    nulled_coefs  :  26
    auc_score  :  0.9
    dual_objective_function  :  1.03879127349
    
    
    
    ***** FOLD 4  *********
    
    objective_function  :  12.6304869888
    lambda_  :  0.1
    gap  :  11.594977658
    nulled_coefs_per_kernel  :  [27]
    score  :  85.0
    norms  :  [120.44574708901398]
    nulled_kernels  :  0
    nulled_coefs  :  27
    auc_score  :  0.85
    dual_objective_function  :  1.03550933087
    
    
    
    ***** FOLD 5  *********
    
    objective_function  :  12.8908535799
    lambda_  :  0.1
    gap  :  11.8454498191
    nulled_coefs_per_kernel  :  [20]
    score  :  90.0
    norms  :  [122.93799476466741]
    nulled_kernels  :  0
    nulled_coefs  :  20
    auc_score  :  0.9
    dual_objective_function  :  1.04540376085
    
    
    
    ***** FOLD 6  *********
    
    objective_function  :  12.8767344714
    lambda_  :  0.1
    gap  :  11.8286523183
    nulled_coefs_per_kernel  :  [24]
    score  :  85.0
    norms  :  [122.82120840763614]
    nulled_kernels  :  0
    nulled_coefs  :  24
    auc_score  :  0.85
    dual_objective_function  :  1.04808215313
    
    
    
    ***** FOLD 7  *********
    
    objective_function  :  12.8168814567
    lambda_  :  0.1
    gap  :  11.7726388721
    nulled_coefs_per_kernel  :  [23]
    score  :  80.0
    norms  :  [122.2446330351401]
    nulled_kernels  :  0
    nulled_coefs  :  23
    auc_score  :  0.8
    dual_objective_function  :  1.04424258459
    
    
    
    ***** FOLD 8  *********
    
    objective_function  :  12.6894865642
    lambda_  :  0.1
    gap  :  11.6507225359
    nulled_coefs_per_kernel  :  [25]
    score  :  85.0
    norms  :  [121.01319599152858]
    nulled_kernels  :  0
    nulled_coefs  :  25
    auc_score  :  0.85
    dual_objective_function  :  1.03876402832
    
    
    
    ***** FOLD 9  *********
    
    objective_function  :  12.7055328011
    lambda_  :  0.1
    gap  :  11.6679464382
    nulled_coefs_per_kernel  :  [23]
    score  :  80.0
    norms  :  [121.19949236488191]
    nulled_kernels  :  0
    nulled_coefs  :  23
    auc_score  :  0.8
    dual_objective_function  :  1.03758636295
    
    
    
    ***** FOLD 10  *********
    
    objective_function  :  12.9282530532
    lambda_  :  0.1
    gap  :  11.9244237222
    nulled_coefs_per_kernel  :  [4]
    score  :  70.0
    norms  :  [123.62351056512924]
    nulled_kernels  :  0
    nulled_coefs  :  4
    auc_score  :  0.7
    dual_objective_function  :  1.00382933107
    
    
    


Yeast all kernels
=================

:math:`l_{21}` penalty
---------------------

Reducing lambda range
+++++++++++++++++++++

.. parsed-literal::

======================= ===================== =============== ====================
Lambda                  Dual gap              auc score       classification score
======================= ===================== =============== ====================
Lambda = 0.001000       dual gap = 0.004605   auc = 1.000000  score = 100.000000
Lambda = 0.010000       dual gap = 0.046025   auc = 1.000000  score = 100.000000
Lambda = 0.100000       dual gap = 0.457173   auc = 1.000000  score = 100.000000
Lambda = 1.000000       dual gap = 4.271293   auc = 1.000000  score = 100.000000
Lambda = 10.000000      dual gap = 22.613612  auc = 0.970000  score = 97.000000
Lambda = 100.000000     dual gap = 22.252123  auc = 0.630000  score = 63.000000
Lambda = 1000.000000    dual gap = 0.000000   auc = 0.500000  score = 50.000000
Lambda = 10000.000000   dual gap = 0.000000   auc = 0.500000  score = 50.000000
Lambda = 100000.000000  dual gap = 0.000000   auc = 0.500000  score = 50.000000
======================= ===================== =============== ====================


Cross validation
++++++++++++++++

Results
*******

.. parsed-literal::

    mean score : 91.000000, score std : 6.244998, mean auc : 0.910000

Detailed results by fold
************************

.. parsed-literal::

    ***** FOLD 1  *********
    
    objective_function  :  7.31638866847
    lambda_  :  1
    gap  :  4.21072706327
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  95.0
    norms  :  [0.069358930492743248, 2.2346040693158251, 1.0138934098337098, 1.0922049674625633, 2.5169693216194844, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  0.95
    dual_objective_function  :  3.1056616052
    
    
    
    ***** FOLD 2  *********
    
    objective_function  :  7.33710535909
    lambda_  :  1
    gap  :  4.22627353304
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  100.0
    norms  :  [0.088156495245877181, 2.2797507364901208, 1.1513614431783308, 1.1808039751539641, 2.2443100329746724, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  1.0
    dual_objective_function  :  3.11083182606
    
    
    
    ***** FOLD 3  *********
    
    objective_function  :  7.21470291437
    lambda_  :  1
    gap  :  4.15369067782
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  95.0
    norms  :  [0.077251791898294703, 2.09717429854209, 1.0211914698976265, 1.3366981558814146, 2.2806077034471786, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  0.95
    dual_objective_function  :  3.06101223655
    
    
    
    ***** FOLD 4  *********
    
    objective_function  :  7.29748624516
    lambda_  :  1
    gap  :  4.20144170353
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  90.0
    norms  :  [0.079319920754422693, 2.2893223819064397, 1.0304632014041444, 1.3076296178472779, 2.2063670940267004, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  0.9
    dual_objective_function  :  3.09604454163
    
    
    
    ***** FOLD 5  *********
    
    objective_function  :  7.17804561669
    lambda_  :  1
    gap  :  4.12548637613
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  85.0
    norms  :  [0.082543706494261126, 2.1561365528564398, 1.0764973471473775, 1.3990404882147052, 2.0840837584965661, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  0.85
    dual_objective_function  :  3.05255924056
    
    
    
    ***** FOLD 6  *********
    
    objective_function  :  7.17540923357
    lambda_  :  1
    gap  :  4.12333555316
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  90.0
    norms  :  [0.076451319569985521, 2.3660559555043239, 0.91329341039119694, 1.1046861268156427, 2.3232979926965407, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  0.9
    dual_objective_function  :  3.05207368041
    
    
    
    ***** FOLD 7  *********
    
    objective_function  :  7.16916389716
    lambda_  :  1
    gap  :  4.12352021597
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  90.0
    norms  :  [0.077827144986862898, 1.8512610325064831, 0.89268312388691051, 1.5212478917075714, 2.4385367048316176, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  0.9
    dual_objective_function  :  3.04564368118
    
    
    
    ***** FOLD 8  *********
    
    objective_function  :  7.04945755057
    lambda_  :  1
    gap  :  4.0560556737
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  85.0
    norms  :  [0.094744072448544311, 2.3757696151912189, 1.0128973601260873, 1.3276810886284689, 1.851847561907171, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  0.85
    dual_objective_function  :  2.99340187687
    
    
    
    ***** FOLD 9  *********
    
    objective_function  :  7.40402974875
    lambda_  :  1
    gap  :  4.26343864692
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  100.0
    norms  :  [0.096736689082981581, 2.1828953873900905, 0.99544252892389429, 1.2026777665689832, 2.5326489192680475, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  1.0
    dual_objective_function  :  3.14059110183
    
    
    
    ***** FOLD 10  *********
    
    objective_function  :  6.75727684425
    lambda_  :  1
    gap  :  3.87128026415
    nulled_coefs_per_kernel  :  [0, 0, 0, 0, 0, 180]
    score  :  80.0
    norms  :  [0.076962140910571686, 1.7775819493223635, 0.62364834536544966, 1.2507859189807888, 2.6672573722837525, 0.0]
    nulled_kernels  :  1
    nulled_coefs  :  180
    auc_score  :  0.8
    dual_objective_function  :  2.8859965801
    
    
    


:math:`l_{12}` penalty
----------------------

================== ======================= =============== ====================
Lambda             Duality gap             auc score       classification score
================== ======================= =============== ====================
Lambda = 0.100000  dual gap = 17.734493    auc = 1.000000  score = 100.000000
Lambda = 0.200000  dual gap = 47.085330    auc = 1.000000  score = 100.000000
Lambda = 0.300000  dual gap = 85.135761    auc = 1.000000  score = 100.000000
Lambda = 0.400000  dual gap = 130.122003   auc = 0.970000  score = 97.000000
Lambda = 0.500000  dual gap = 189.450062   auc = 0.945000  score = 94.500000
Lambda = 0.600000  dual gap = 213.578780   auc = 0.935000  score = 93.500000
Lambda = 0.700000  dual gap = 295.887021   auc = 0.915000  score = 91.500000
Lambda = 0.800000  dual gap = 350.908773   auc = 0.905000  score = 90.500000
Lambda = 0.900000  dual gap = 412.421888   auc = 0.890000  score = 89.000000
Lambda = 1.000000  dual gap = 480.042919   auc = 0.885000  score = 88.500000
Lambda = 1.100000  dual gap = 557.725337   auc = 0.885000  score = 88.500000
Lambda = 1.200000  dual gap = 1333.846705  auc = 0.855000  score = 85.500000
Lambda = 1.300000  dual gap = 1390.406934  auc = 0.845000  score = 84.500000
================== ======================= =============== ====================


Cross-validation
----------------

Results
*******

.. parsed-literal::

    mean score : 91.000000, score std : 6.244998, mean auc : 0.910000

Detailed results by fold
************************

.. parsed-literal::

    ***** FOLD 1  *********
    
    objective_function  :  35.323999886
    lambda_  :  0.3
    gap  :  76.3107278465
    nulled_coefs_per_kernel  :  [160, 160, 160, 158, 163, 165]
    score  :  95.0
    norms  :  [1.6173134785985877, 5.4273051465913404, 4.2539837168544885, 7.794780513819455, 4.624535824563857, 3.633387840050061]
    nulled_kernels  :  0
    nulled_coefs  :  966
    auc_score  :  0.95
    dual_objective_function  :  -40.9867279605
    
    
    
    ***** FOLD 2  *********
    
    objective_function  :  35.0164018575
    lambda_  :  0.3
    gap  :  73.2322968804
    nulled_coefs_per_kernel  :  [164, 163, 161, 157, 163, 161]
    score  :  95.0
    norms  :  [2.4429343136826134, 5.648566317512443, 4.343796087918384, 7.807658571321594, 4.292366601210854, 3.3262410000432303]
    nulled_kernels  :  0
    nulled_coefs  :  969
    auc_score  :  0.95
    dual_objective_function  :  -38.2158950229
    
    
    
    ***** FOLD 3  *********
    
    objective_function  :  33.4123153958
    lambda_  :  0.3
    gap  :  67.025822206
    nulled_coefs_per_kernel  :  [164, 160, 168, 164, 166, 164]
    score  :  85.0
    norms  :  [2.7465373003150053, 4.717620774243243, 4.689215802097662, 7.521851267008401, 5.128051663250463, 3.1155972853863054]
    nulled_kernels  :  0
    nulled_coefs  :  986
    auc_score  :  0.85
    dual_objective_function  :  -33.6135068102
    
    
    
    ***** FOLD 4  *********
    
    objective_function  :  33.2826472464
    lambda_  :  0.3
    gap  :  76.2573528059
    nulled_coefs_per_kernel  :  [166, 163, 166, 154, 164, 168]
    score  :  90.0
    norms  :  [2.2368668445281017, 5.635285705836582, 4.433943132412762, 5.987270732867844, 4.963858488352576, 4.12246219659647]
    nulled_kernels  :  0
    nulled_coefs  :  981
    auc_score  :  0.9
    dual_objective_function  :  -42.9747055595
    
    
    
    ***** FOLD 5  *********
    
    objective_function  :  34.1122903497
    lambda_  :  0.3
    gap  :  72.4301414597
    nulled_coefs_per_kernel  :  [166, 162, 166, 154, 164, 166]
    score  :  90.0
    norms  :  [1.8802667404055349, 5.886924025688008, 4.7171724256047805, 7.084191778691791, 5.240821645137548, 2.994170871276404]
    nulled_kernels  :  0
    nulled_coefs  :  978
    auc_score  :  0.9
    dual_objective_function  :  -38.31785111
    
    
    
    ***** FOLD 6  *********
    
    objective_function  :  32.4694491391
    lambda_  :  0.3
    gap  :  64.8538318113
    nulled_coefs_per_kernel  :  [153, 160, 156, 159, 163, 166]
    score  :  85.0
    norms  :  [4.019957348759387, 5.412894660935292, 3.734054402561677, 6.632148400871322, 5.00449250976388, 3.617125780331545]
    nulled_kernels  :  0
    nulled_coefs  :  957
    auc_score  :  0.85
    dual_objective_function  :  -32.3843826722
    
    
    
    ***** FOLD 7  *********
    
    objective_function  :  34.0982909233
    lambda_  :  0.3
    gap  :  70.1032192671
    nulled_coefs_per_kernel  :  [160, 154, 164, 158, 163, 169]
    score  :  85.0
    norms  :  [2.5587355822364493, 5.775101495127533, 4.167072709390902, 7.677352101177551, 4.956073036752995, 2.844344924174483]
    nulled_kernels  :  0
    nulled_coefs  :  968
    auc_score  :  0.85
    dual_objective_function  :  -36.0049283438
    
    
    
    ***** FOLD 8  *********
    
    objective_function  :  31.3240952814
    lambda_  :  0.3
    gap  :  66.6753776678
    nulled_coefs_per_kernel  :  [162, 167, 169, 164, 165, 169]
    score  :  75.0
    norms  :  [2.388948282925996, 5.691615244102296, 4.114707201082938, 6.556561843855067, 4.53512916742091, 3.953236077965818]
    nulled_kernels  :  0
    nulled_coefs  :  996
    auc_score  :  0.75
    dual_objective_function  :  -35.3512823864
    
    
    
    ***** FOLD 9  *********
    
    objective_function  :  35.1401228789
    lambda_  :  0.3
    gap  :  73.5694073467
    nulled_coefs_per_kernel  :  [164, 167, 167, 156, 164, 168]
    score  :  95.0
    norms  :  [3.0291694429229183, 6.097307387545399, 4.677334778123896, 7.230726154679853, 4.403479916203015, 3.025281194982475]
    nulled_kernels  :  0
    nulled_coefs  :  986
    auc_score  :  0.95
    dual_objective_function  :  -38.4292844678
    
    
    
    ***** FOLD 10  *********
    
    objective_function  :  31.2075780044
    lambda_  :  0.3
    gap  :  67.4045632859
    nulled_coefs_per_kernel  :  [163, 161, 170, 166, 168, 167]
    score  :  75.0
    norms  :  [3.9985694106527947, 4.220939983073274, 3.427573545306402, 7.571500492876156, 4.633664317507462, 3.1598777413096957]
    nulled_kernels  :  0
    nulled_coefs  :  995
    auc_score  :  0.75
    dual_objective_function  :  -36.1969852815

Conclusion
-----------

Here, not only did we get a very hight good classification rate (>90%), we also confirmed that mixed norms were more adapted when prior knowledge is available. Thus, while we only have a score of 84 % with norms :math:`l_1` and :math:`l_2`, this increases to 91% when using :math:`l_{12}` and :math:`l_{21}` norms.
