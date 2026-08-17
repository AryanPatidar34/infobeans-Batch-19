'''
=====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
'''


from collections import namedtuple
hospital=namedtuple("basic",["patient_id","patient_name","age","disease"])
n=int(input("Enter number of patient : "))
arr=[]
for i in range(n):
    id=input("Enter id of patient : ")
    n=input("Enter name of patient : ")
    age=int(input("Enter age of patient : "))
    d=input("Enter disease : ")
    arr.append(hospital(id,n,age,d))
for i in arr:
    print(i.patient_id,i.patient_name,i.age,i.disease)
ID=input("Enter Patient ID : ")
dis=input("Enter disease :")
c=0
for i in arr:
    if i.patient_id==ID and i.disease==dis:
        print("patient found")
        print(i.patient_id,i.patient_name,i.age,i.disease)
    if i.age>60:
        print(i.patient_id,i.patient_name,i.age,i.disease)
    if i.disease==dis:
        c+=1
print("patients with Diabetes :",c)
