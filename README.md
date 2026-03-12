
# Multi-Label Confusion Matrix (Corrected Implementation)

This repository provides a corrected implementation of the multilabel confusion matrix described in the original paper.

The original repository contains two issues:
- deprecated `np.int` usage which breaks with modern NumPy versions
- small inconsistencies between the implementation and the procedure described in the paper

Since the original repository does not appear to be actively maintained, this implementation fixes these issues and aims to provide a working and faithful reference implementation.



This repository is based on the original implementation provided by the authors.

The original work is licensed under the Creative Commons Attribution 4.0 License (CC BY 4.0).
This repository includes modifications and fixes to the original implementation.


# Functionality
To retrieve a confusion matrix, run cm(true_labels, predicted_labels).

The labels are lists where each entry corresponds to instance i. Each instance is a list of length num_classes with hot encoded classes. An example:

True Labels: A,D,E  
Predicted Labels: A,C,D

cm then expencts the hot encoded labels as:
true_labels = [1,0,0,1,1]
predicted_labels = [1,0,1,1,0]

## 1. CM


## 2. Case distinction
The paper distinguishes three cases of how true and predicted labels are related. Those are:
### I. 



# Correction Case
The original repository failes e.g. in the following case:
pred_labels = [1,0,0,1]
true_labels = [1,1,1,0]

where it yields:
```
[[1 0 1 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 1 1 0 0]
 [0 0 0 0 0]]
```

But according to the paper, the algorithm should yield:


```
[[1 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 1 1 0 0]
 [0 0 0 0 0]]
 ```




