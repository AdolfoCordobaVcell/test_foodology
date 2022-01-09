import pandas as pd
import matplotlib.pyplot as plt

# Read .csv file
df = pd.read_csv("StudentsPerformance.csv")

# description of the variables
# column names
print(df.columns)

# data size
print(df.shape)

# null values in the data
print(df.info())

# distribution of numerical variables
print(df.describe())

# distribution of categorical variables
print(df.describe(include=['O']))

# filter blanks
df_filter = df.fillna(0)
print(df_filter)

# add the general score column
def score(row):
    general_score = (row["math score"] + row["reading score"] + row["writing score"]) / 3
    return general_score

df_filter["general score"] = df_filter.apply(score, axis=1)

print(df_filter)

# number of students according to their gender
gender = df_filter["gender"].value_counts()
print(gender)

gender.plot(kind="bar")
plt.show()

# number of students according to the ethnicity
ethnicity = df_filter["race/ethnicity"].value_counts().sort_index(ascending=True)
print(ethnicity)

ethnicity.plot(kind="bar")
plt.show()

# academic grade of the students' parents
parents = df_filter["parental level of education"].value_counts()
print(parents)

parents.plot(kind="bar")
plt.show()

# number of students according to the lunch
lunch = df_filter["lunch"].value_counts()
print(lunch)

lunch.plot(kind="bar")
plt.show()

# number of students who completed the test preparation course and those who did not
test = df_filter["test preparation course"].value_counts()
print(test)

test.plot(kind="bar")
plt.show()

# students who passed math
aprobatory_math = df_filter[df_filter["math score"] > 70]

print(aprobatory_math)

# students who passed reading
aprobatory_reading = df_filter[df_filter["reading score"] > 70]

print(aprobatory_reading)

# students who passed writing
aprobatory_writing = df_filter[df_filter["writing score"] > 70]

print(aprobatory_writing)

# mean for general and subject score according to gender
gender_mean = df_filter.groupby("gender").agg({
    "math score": "mean",
    "reading score": "mean",
    "writing score": "mean",
    "general score": "mean"
})

print(gender_mean)

# grafics according to the scores to gender
gender_mean["math score"].plot(kind="bar")
plt.show()

gender_mean["reading score"].plot(kind="bar")
plt.show()

gender_mean["writing score"].plot(kind="bar")
plt.show()

gender_mean["general score"].plot(kind="bar")
plt.show()