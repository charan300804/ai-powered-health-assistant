import sys

def calculate_bmi(weight, height):
    # height in meters, weight in kg
    bmi = weight / (height ** 2) if height > 0 else 0
    if bmi < 18.5:
        category = "Underweight"
        advice = "Consider speaking to a doctor about healthy weight gain strategies."
    elif bmi < 25:
        category = "Normal Weight"
        advice = "Great job! Maintain a balanced diet and regular physical activity."
    elif bmi < 30:
        category = "Overweight"
        advice = "Aim to incorporate more daily movement and focus on whole foods."
    else:
        category = "Obesity"
        advice = "We recommend consulting a healthcare provider or nutritionist for tailored advice."
    return bmi, category, advice

def main():
    print("--- FitBuddy AI Health Assistant ---")
    print("-" * 40)
    try:
        weight = float(input("Enter weight in kilograms (kg): "))
        height = float(input("Enter height in meters (e.g. 1.75): "))
    except ValueError:
        print("Invalid input values. Exiting.")
        return

    bmi, cat, advice = calculate_bmi(weight, height)

    print("
================ HEALTH DIAGNOSIS ================")
    print(f"BMI Score          : {bmi:.1f}")
    print(f"Weight Category    : {cat}")
    print("-------------------------------------------------")
    print("Recommendations:")
    print(f" {advice}")
    print("=================================================
")

if __name__ == "__main__":
    main()
