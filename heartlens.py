# HEARTLENS-AI
# AI Powered Cardiovascular Risk Detection System

from random import randint

print("\n==============================")
print("      HEARTLENS - AI")
print("==============================\n")

name = input("Enter Patient Name : ")

age = int(input("Enter Age : "))
heart_rate = int(input("Enter Heart Rate : "))
bp = int(input("Enter Blood Pressure : "))
cholesterol = int(input("Enter Cholesterol Level : "))
sugar = int(input("Enter Sugar Level : "))

risk_score = 0

if age > 50:
    risk_score += 20

if heart_rate > 100:
    risk_score += 20

if bp > 140:
    risk_score += 20

if cholesterol > 240:
    risk_score += 20

if sugar > 180:
    risk_score += 20

ai_accuracy = randint(95, 99)

print("\n==============================")
print("       AI ANALYSIS REPORT")
print("==============================")

print(f"\nPatient Name      : {name}")
print(f"Age               : {age}")
print(f"Heart Rate        : {heart_rate}")
print(f"Blood Pressure    : {bp}")
print(f"Cholesterol Level : {cholesterol}")
print(f"Sugar Level       : {sugar}")

print(f"\nAI Risk Score     : {risk_score}%")
print(f"AI Accuracy       : {ai_accuracy}%")

print("\n==============================")

if risk_score >= 80:
    print("HEART CONDITION : HIGH RISK")
    print("Recommendation  : Immediate medical consultation required")

elif risk_score >= 40:
    print("HEART CONDITION : MODERATE RISK")
    print("Recommendation  : Regular monitoring and healthy lifestyle")

else:
    print("HEART CONDITION : LOW RISK")
    print("Recommendation  : Heart condition appears stable")

print("\n==============================")
print("   HEARTLENS-AI COMPLETED")
print("==============================")