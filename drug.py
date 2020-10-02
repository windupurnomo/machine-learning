import pandas as pd
from sklearn.svm import SVC

model = SVC(gamma='scale')

df = pd.read_csv("drug200.csv")
df_num = df.copy()

uniqueSex = pd.unique(df["Sex"]).tolist()
uniqueBP = pd.unique(df["BP"]).tolist()
uniqueCholesterol = pd.unique(df["Cholesterol"]).tolist()
uniqueDrug = pd.unique(df["Drug"]).tolist()


# ubah menjadi nilai numerik
def to_numeric(uniques, col_index):
    for index in df_num.index:
        val = df_num.iloc[index, col_index]
        df_num.iloc[index, col_index] = int(uniques.index(val))


to_numeric(uniqueSex, 1)
to_numeric(uniqueBP, 2)
to_numeric(uniqueCholesterol, 3)
to_numeric(uniqueDrug, 5)

# membagi data menjadi data TRAINING dan TESTING
training = df_num.iloc[:100, ]
testing = df_num.iloc[100:, ]

training_data = training.iloc[:, :5]
training_target = training.iloc[:, 5:]
testing_data = testing.iloc[:, :5]
testing_target = testing.iloc[:, 5:]

training_target = training_target["Drug"]
training_target = training_target.astype("int")

# proses TRAINING
model.fit(training_data, training_target)
prediction = model.predict(testing_data)

print(prediction)
print(prediction.shape)


