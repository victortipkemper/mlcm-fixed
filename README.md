# Multi-Label Confusion Matrix

This repository provides a corrected implementation of the multilabel confusion matrix described in the original paper "MLCM: Multi-Label Confusion Matrix" by  Heydarian et al.

## Issues Fixed

The original repository contained:
- Deprecated `np.int` usage which breaks with modern NumPy versions
- Small inconsistencies between the implementation and the procedure described in the paper


This implementation fixes these issues and provides a working, faithful reference implementation.

## License

The original work is licensed under the Creative Commons Attribution 4.0 License (CC BY 4.0).
This repository is not affiliated with the original authors.
It is an independent implementation based on the algorithm described in the paper.

## References

This implementation is based on:

M. Heydarian, T. Doyle, and R. Samavi, "MLCM: Multi-Label Confusion Matrix," IEEE Access, Feb. 2022, DOI: 10.1109/ACCESS.2022.3151048



## Installation

Install the package using pip:

```bash
pip install -e .
```

## Usage

### Basic Usage

To compute a confusion matrix, use the `cm()` function:

```python
from mlcm_fixed import cm
import numpy as np

# Create binary encoded labels (one row per instance, one column per class)
true_labels = np.array([[1, 0, 1], [0, 1, 1]])      # 2 instances, 3 classes
predicted_labels = np.array([[1, 0, 0], [0, 1, 1]])

# Get raw and normalized confusion matrices
raw_cm, normalized_cm = cm(true_labels, predicted_labels)
print(raw_cm)
print(normalized_cm)
```

### Label Encoding Example

For instance with True Labels: A, D, E and Predicted Labels: A, C, D

```python
true_labels = [1, 0, 0, 1, 1]      # Classes: A, B, C, D, E
predicted_labels = [1, 0, 1, 1, 0] # Classes: A, B, C, D, E
```

## Case Distinction

The implementation distinguishes three cases based on how true and predicted labels relate:

### Case I: P ⊆ T (Predicted is subset of True)
All predicted labels are correct, but some true labels are missing.

### Case II: T ⊂ P (True is subset of Predicted)
All true labels are predicted, but some additional incorrect predictions exist.

### Case III: Neither P ⊆ T nor T ⊆ P
Some true labels are missing AND some incorrect predictions exist simultaneously.

The algorithms for handling each case are described in the original paper.

## Available Functions

- `cm(label_true, label_pred)` - Main function, returns raw and normalized confusion matrices
- `conf_mat_case_1(label_true, label_pred)` - Confusion matrix for Case I
- `conf_mat_case_2(label_true, label_pred)` - Confusion matrix for Case II
- `con_mat_case_3(label_true, label_pred)` - Confusion matrix for Case III
- `normalize_conf_matrix(matrix)` - Normalize confusion matrix row-wise
- `category_of_instance(label_instance_true, label_instance_pred)` - Determine which case an instance belongs to

## Example Correction

The original repository would fail on this case:

```python
pred_labels = [1, 0, 0, 1]
true_labels = [1, 1, 1, 0]
```

Original (incorrect) output:
```
[[1 0 1 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 1 1 0 0]
 [0 0 0 0 0]]
```

Corrected output:
```
[[1 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 1 1 0 0]
 [0 0 0 0 0]]
```

## Complete Example

Here's a complete example demonstrating all three cases:

```python
from mlcm_fixed import cm, conf_mat_case_1, conf_mat_case_2, con_mat_case_3
import numpy as np

# Example with 100 instances and 5 classes
num_instances = 100
num_classes = 5
true_labels = np.random.randint(2, size=(num_instances, num_classes))
pred_labels = np.random.randint(2, size=(num_instances, num_classes))

# Get confusion matrices
raw_cm, normalized_cm = cm(true_labels, pred_labels)

print("Raw Confusion Matrix:")
print(raw_cm)
print("\nNormalized Confusion Matrix:")
print(normalized_cm)

# You can also get individual case matrices
case1_cm = conf_mat_case_1(true_labels, pred_labels)
case2_cm = conf_mat_case_2(true_labels, pred_labels)
case3_cm = con_mat_case_3(true_labels, pred_labels)

print("\nCase I (P ⊆ T):")
print(case1_cm)
print("\nCase II (T ⊂ P):")
print(case2_cm)
print("\nCase III (neither):")
print(case3_cm)
```





