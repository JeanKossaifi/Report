Motivation
==========


The main goal of this is to work with a set of information from different sources and to highlight the most significant ones for a given problem.

For this purpose, we will use supervised binary classification. This means that we have in hand a set of examples we want to classify into two different classes.

In other words, we use a set of examples for which we already know the corresponding class. The objective is to use an algorithm to understand the underlying logic in the data in order to be able to generalise this knowledge to classify new examples into the correct class.


To make it simple, we want to combine the information from different sources in the best possible way, by using Multiple Kernel Learning. Each kernel (we will introduce this notion later) represent one source of information. It is basically represented by a squared matrix.

One of the challenges of this project is to integrate prior knowledge on the data. In other word, we want to take into account an expert knowledge in the way in which we combine the information together. For example, a prior knowledge can inform us that only part of the information is useful. An important part of the learning algorithm will thus be to discard the non useful ones.

Although the techniques developed can be applied in many fields, we will be interested mostly into a biology one.

Using yeast data (*William Noble, Professor of Genome Sciences and of Computer Science, http://noble.gs.washington.edu/yeast/*), we will try to combine information of different types and from different sources to predict the function of a number of proteins.

These different functions can be divided into 13 categories :

=================================   ==================
Category                            Number of examples
=================================   ==================
metabolism                           1048
energy                               242
cell cycle & DNA processing          600
transcription                        753
protein synthesis                    335
protein fate                         578
cellular transp. & transp. mech.     479
cell rescue, defense & virulence     264
interaction w/ cell. envt.           193
cell fate                            411
control of cell. organization        192
transport facilitation               306
others                               81
=================================   ==================

We considered two cases : 

* First all the data where used to predict.

* Second, we focused on a smaller amount of information.

  For that purpose we considered only the first 100 elements that belongs *only* to class 5 and the first 100 elements that belongs *only* to class 7. Eventually we obtained 200*200 kernels, and a vector of the 200 associated labels.
