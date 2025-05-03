### ✅ Machine learning models can be grouped into **three main types**, based on what they're used for:

### 1. **Supervised Learning (Predictive Models)**

These models **learn from labeled data** — meaning each example in the data has a known output (target or label).
They try to **predict** the label for new data.

* 🔸 **Classification** (predicting categories):

  * Example: Will a customer buy? (Yes/No)
  * Models: Logistic Regression, Random Forest, SVM, Neural Networks

* 🔸 **Regression** (predicting numbers):

  * Example: What will the price of a house be?
  * Models: Linear Regression, Gradient Boosting Regressor

**→ These are what we often call *predictive models*.**

---

### 2. **Unsupervised Learning**

These models **don’t have labeled data** — they find patterns or structure in the data without knowing the "right" answers.

* 🔸 **Clustering**: Grouping similar items

  * Example: Customer segmentation
  * Models: K-Means, DBSCAN

* 🔸 **Dimensionality Reduction**: Simplifying data

  * Example: Visualizing high-dimensional data
  * Models: PCA, t-SNE, UMAP

---

### 3. **Semi-Supervised / Self-Supervised / Reinforcement Learning** (More advanced types)

* These are **less common** in basic ML workflows but important in advanced systems.
* Example: Chatbots learning from interactions (reinforcement), or models trained on data with few labels.

---

### ✅ So in short:

| Category              | Needs Labels?    | Goal                    | Example Models               |
| --------------------- | ---------------- | ----------------------- | ---------------------------- |
| **Supervised**        | ✅ Yes            | Predict outcomes        | Logistic Regression, SVM     |
| **Unsupervised**      | ❌ No             | Find structure/patterns | K-Means, PCA                 |
| **Others (Advanced)** | Mixed or special | Depends                 | Reinforcement Learning, etc. |

---

### 1. **Constant Variable**

A **constant variable** is a feature (column) where **every value is the same** for all rows.

#### 🧾 Example:

| Feature A |
| --------- |
| 1         |
| 1         |
| 1         |
| 1         |

🔍 **Why it’s a problem:**
It gives **no useful information** — since it doesn’t vary, it can’t help the model make decisions.

---

### 2. **Quasi-Constant Variable**

A **quasi-constant variable** is a feature where **almost all the values are the same**, but **a few are different**.

#### 🧾 Example:

| Feature B |
| --------- |
| 0         |
| 0         |
| 0         |
| 1         |

🔍 **Why it’s a problem:**
It might still carry **very little information**, and can often be removed unless those rare values are meaningful (like a rare disease flag in medical data).

---

### 3. **Duplicated Variable**

A **duplicated variable** is a feature that is an **exact copy** of another feature.

#### 🧾 Example:

| Feature C | Feature D |
| --------- | --------- |
| 10        | 10        |
| 20        | 20        |
| 30        | 30        |

🔍 **Why it’s a problem:**
It causes **redundancy** in the data and can confuse the model or make it slower, especially with high-dimensional data.

---

### ✅ Why remove these?

Removing constant, quasi-constant, and duplicated variables:

* **Reduces noise**
* **Improves model performance**
* **Speeds up training**
* **Simplifies the dataset**

Great! Here's a **simple Python example** using **pandas** to detect and remove **constant**, **quasi-constant**, and **duplicated** variables from a dataset.

Let’s say you have a DataFrame called `df`.

---

### ✅ 1. Remove **constant features**

```python
# Remove columns where all values are the same
constant_columns = [col for col in df.columns if df[col].nunique() == 1]
df = df.drop(columns=constant_columns)

print("Removed constant columns:", constant_columns)
```

---

### ✅ 2. Remove **quasi-constant features**

```python
# Threshold: 99% of the values are the same
quasi_constant_columns = []

for col in df.columns:
    top_freq = df[col].value_counts(normalize=True).max()
    if top_freq > 0.99:
        quasi_constant_columns.append(col)

df = df.drop(columns=quasi_constant_columns)

print("Removed quasi-constant columns:", quasi_constant_columns)
```

---

### ✅ 3. Remove **duplicated features**

```python
# Transpose the DataFrame to compare columns, then drop duplicates
df_T = df.T
duplicated_columns = df_T[df_T.duplicated()].index
df = df.drop(columns=duplicated_columns)

print("Removed duplicated columns:", duplicated_columns.tolist())
```

---

### 📌 Full process wrapped together:

```python
def remove_constant_quasi_constant_duplicated(df, quasi_thresh=0.99):
    # Constant
    constant_cols = [col for col in df.columns if df[col].nunique() == 1]
    df = df.drop(columns=constant_cols)

    # Quasi-constant
    quasi_constant_cols = []
    for col in df.columns:
        if df[col].value_counts(normalize=True).max() > quasi_thresh:
            quasi_constant_cols.append(col)
    df = df.drop(columns=quasi_constant_cols)

    # Duplicated
    duplicated_cols = df.T[df.T.duplicated()].index
    df = df.drop(columns=duplicated_cols)

    print("Removed:")
    print("- Constant:", constant_cols)
    print("- Quasi-constant:", quasi_constant_cols)
    print("- Duplicated:", duplicated_cols.tolist())

    return df
```

You can use this function by calling:

```python
df_cleaned = remove_constant_quasi_constant_duplicated(df)
```

 
