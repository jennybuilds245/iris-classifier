# Iris Classifier 

This is my first machine learning project. It trains a model to predict the species of an iris flower from four measurements of its petals and sepals, then compares two different algorithms to see which one does better.

I built it as part of an AI fundamentals course, so the code is kept simple and heavily commented. If you're also just starting out, I hope it's easy to follow.

## What it does

The script uses the classic Iris dataset that comes built into scikit-learn. It has 150 flowers across three species (setosa, versicolor and virginica), each described by four measurements: sepal length, sepal width, petal length and petal width.

Here's what happens when you run it:

1. The dataset is loaded and split so that 80% of the flowers are used for training and 20% are held back for testing. The split uses `random_state=42`, so you'll get the same results every time.
2. A **Decision Tree** classifier is trained on the training data.
3. It makes predictions on the test flowers and prints the first five next to the real answers, so you can compare them.
4. It prints the decision tree's accuracy.
5. A **K-Nearest Neighbours (KNN)** model with 5 neighbours is trained on the same data, and its accuracy is printed too, so the two approaches can be compared side by side.

## Project structure

```
iris-classifier/
├── src/
│   └── train.py          # the whole pipeline: load, split, train, evaluate
└── requirements.txt      # Python packages the project needs
```

## Setup

You'll need **Python 3.10 or newer** and **Git** installed.

### 1. Clone the repo

```bash
git clone https://github.com/jennybuilds245/iris-classifier.git
cd iris-classifier
```

### 2. Create a virtual environment

A virtual environment keeps this project's packages separate from everything else on your computer. I learned the hard way that skipping this step can cause some confusing errors!

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell complains that running scripts is disabled, run this once and then try activating again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

When it's active, you'll see `(venv)` at the start of your terminal prompt.

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` gives you any trouble, installing scikit-learn directly works too:

```bash
pip install scikit-learn
```

### 4. Run it

```bash
python src/train.py
```

**Using VS Code?** Press `Ctrl+Shift+P`, choose **Python: Select Interpreter**, and pick the one inside your `venv` folder. Otherwise the Run button might use a different Python that doesn't have scikit-learn installed.

## What you should see

First the feature names and the three species are printed, then a sample of predictions next to the actual labels, and finally the accuracy of each model. It'll look roughly like this:

```
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'] ['setosa' 'versicolor' 'virginica']
Predicted labels: [1 0 2 1 1]
Actual labels: [1 0 2 1 1]
Accuracy: ...
KNN Accuracy: ...
```

The labels are numbers: `0` is setosa, `1` is versicolor and `2` is virginica.

Both models tend to score very high on this dataset. That's partly because the iris species are quite easy to tell apart, and partly because the test set is small (only 30 flowers), so one or two mistakes make a big difference to the percentage.

## What I learned

- How to split data into training and test sets, and why you should never test a model on data it has already seen
- How to train and evaluate a model with scikit-learn's `fit` → `predict` → `accuracy_score` pattern
- That comparing more than one algorithm is a simple way to check whether your first choice is actually a good one
- How to set up a virtual environment properly (after a few false starts!)

## Ideas for next steps

- Try different values of `n_neighbors` for KNN and see how the accuracy changes
- Add a confusion matrix to see exactly which species get mixed up
- Use cross-validation for a more reliable accuracy score than a single split
- Visualise the decision tree to see the rules it learned

## Built with

- [Python](https://www.python.org/)
- [scikit-learn](https://scikit-learn.org/)
