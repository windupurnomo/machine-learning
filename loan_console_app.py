import pickle

# minta input dari user (ini berdasarkan kolom yg kita gunakan waktu pembuatan model)
# ['Married', 'Dependents', 'ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

print("==================")
print("Selamat datang di aplikasi LOAN APP")
print("==================")
print("Silakan masukan data berikut")

# mendapatkan input parameter dari user
married = int(input("Apakah Anda sudah menikah? Tidak (0); Ya (1); Lainnya (2): "))
dependents = int(input("Jumlah tanggungan: "))
income = int(input("Pendapatan Bulanan Anda (Rp dalam ribuan): "))
loanAmount = int(input("Pinjaman yang diajukan (Rp dalam ribuan): "))
term = int(input("Termin pembayaran (hari): "))

# panggil model
with open('loan-classifier.pkl', 'rb') as file:
    model = pickle.load(file)

# lakukan prediksi berdasarkan data
param = [[married, dependents, income, loanAmount, term]]
prediction = model.predict(param)

# keluarkan output
# yes ===> 0
# no ===> 1
res = prediction[0]
print("-----------")
if res == 0:
    print("Selamat Anda akan mendapatkan PINJAMAN")
else:
    print("Maaf Anda tidak akan mendapat PINJAMAN")
