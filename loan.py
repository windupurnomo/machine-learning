import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import r2_score

model = SVC(gamma='scale')

# read data from csv
loan = pd.read_csv("kaggle_loan_training.csv")

# kolom yg ingin dihapus
to_drop = ["Loan_ID", "Gender", "Self_Employed", "Credit_History", "Property_Area"]
loan.drop(columns=to_drop, inplace=True)


# ubah data menjadi numeric
def to_numeric(dt, dt_num, c):
    uniques = pd.unique(dt[c]).tolist()
    col_index = dt.columns.tolist().index(c)
    for index in dt_num.index:
        val = dt_num.iloc[index, col_index]
        dt_num.iloc[index, col_index] = int(uniques.index(val))


categories = loan.columns.tolist()
loan_num = loan.copy()
num_columns = []
for i in loan_num.columns:
    v = loan_num.loc[0, i]
    if isinstance(v, str):
        num_columns.append(i)

for col in num_columns:
    to_numeric(loan, loan_num, col)

# data cleaning
loan_num.dropna(inplace=True)
loan_num.reset_index(inplace=True, drop=True)

# memisahkan data
n = len(loan_num.columns.tolist()) - 1
splitNum = 0.7
indexMax = int(len(loan_num) * splitNum)
dt = loan_num.iloc[:, :n]
lb = loan_num.iloc[:, n:]
dt_training = dt.iloc[:indexMax, :]
lb_training = lb.iloc[:indexMax, :]["Loan_Status"]
dt_testing = dt.iloc[indexMax:, :]
lb_testing = lb.iloc[indexMax:, :]["Loan_Status"]
lb_training = lb_training.astype('int')
lb_testing = lb_testing.astype("int")

# proses TRAINING
model.fit(dt_training, lb_training)
prediction = model.predict(dt_testing)

n = len(lb_testing)
truePredict = 0
for i in range(n):
    a = prediction[i]
    b = lb_testing.tolist()[i]
    if a == b:
        truePredict += 1

# print("Prediksi benar: {} dari {}".format(truePredict, n))

predictionScore = r2_score(lb_testing, prediction)
modelScore = model.score(dt_testing, lb_testing)

print("r2score: ", predictionScore)
print("model score: ", modelScore)
print("Manual Accuracy {:.4f}".format(truePredict / n))
