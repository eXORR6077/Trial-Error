#BMI-Rechner

def body_mass_index(körpergewicht, m):
    bmi = körpergewicht/(m*m)
    return bmi

def bmi_scale(age, bmi):
    if age >= 19 and age <= 24:
        if bmi <= 18:
            bmi_scale_result = "Untergewicht"
        elif bmi > 18 and bmi <= 24:
            bmi_scale_result = "Normalgewicht"
        elif bmi > 24 and bmi <= 29:
            bmi_scale_result = "Übergewicht"
        elif bmi > 29 and bmi <= 39:
            bmi_scale_result = "starkes Übergewicht"
        elif bmi > 39:
            bmi_scale_result = "extrem starkes Übergewicht"
    elif age >= 25 and age <= 34:
        if bmi <= 19:
            bmi_scale_result = "Untergewicht"
        elif bmi > 19 and bmi <= 25:
            bmi_scale_result = "Normalgewicht"
        elif bmi > 25 and bmi <= 30:
            bmi_scale_result = "Übergewicht"
        elif bmi > 30 and bmi <= 40:
            bmi_scale_result = "starkes Übergewicht"
        elif bmi > 40:
            bmi_scale_result = "extrem starkes Übergewicht"
    elif age >= 35 and age <= 44:
        if bmi <= 20:
            bmi_scale_result = "Untergewicht"
        elif bmi > 20 and bmi <= 26:
            bmi_scale_result = "Normalgewicht"
        elif bmi > 26 and bmi <= 31:
            bmi_scale_result = "Übergewicht"
        elif bmi > 31 and bmi <= 41:
            bmi_scale_result = "starkes Übergewicht"
        elif bmi > 41:
            bmi_scale_result = "extrem starkes Übergewicht"
    elif age >= 45 and age <= 54:
        if bmi <= 21:
            bmi_scale_result = "Untergewicht"
        elif bmi > 21 and bmi <= 27:
            bmi_scale_result = "Normalgewicht"
        elif bmi > 27 and bmi <= 32:
            bmi_scale_result = "Übergewicht"
        elif bmi > 32 and bmi <= 42:
            bmi_scale_result = "starkes Übergewicht"
        elif bmi > 42:
            bmi_scale_result = "extrem starkes Übergewicht"
    elif age >= 55 and age <= 64:
        if bmi <= 22:
            bmi_scale_result = "Untergewicht"
        elif bmi > 22 and bmi <= 28:
            bmi_scale_result = "Normalgewicht"
        elif bmi > 28 and bmi <= 33:
            bmi_scale_result = "Übergewicht"
        elif bmi > 33 and bmi <= 43:
            bmi_scale_result = "starkes Übergewicht"
        elif bmi > 43:
            bmi_scale_result = "extrem starkes Übergewicht"
    elif age > 64:
        if bmi <= 23:
            bmi_scale_result = "Untergewicht"
        elif bmi > 23 and bmi <= 29:
            bmi_scale_result = "Normalgewicht"
        elif bmi > 29 and bmi <= 34:
            bmi_scale_result = "Übergewicht"
        elif bmi > 34 and bmi <= 44:
            bmi_scale_result = "starkes Übergewicht"
        elif bmi > 44:
            bmi_scale_result = "extrem starkes Übergewicht"
    return bmi_scale_result

kg = float(input("Wie viel wiegst du?(kg):\n "))
m = float(input("Wie groß bist du?(m)(statt ',' bitte '.' eingeben):\n "))
age = int(input("Wie alt bist du?(Jahre):\n "))

while True:                                                 
    ask_for_BMI_scale = input("Möchtest du wissen, ob dein Gewicht in Ordnung ist?(ja/nein):\n").lower()
    if ask_for_BMI_scale == "ja" or ask_for_BMI_scale == "nein":
        if ask_for_BMI_scale == "ja":
            bmi_wert = body_mass_index(kg, m)
            result = bmi_scale(age, bmi_wert)
            print(f"Laut BMI-Skala hast du {result} & dein BMI-Wert beträgt {round(bmi_wert, 2)}")
        elif ask_for_BMI_scale == "nein":
            bmi_wert = body_mass_index(kg, m)
            print(f"okay - dein BMI-Wert beträgt {round(bmi_wert, 2)}")
        break
    else:
        print("Bitte gib 'ja' oder 'nein' ein!")




