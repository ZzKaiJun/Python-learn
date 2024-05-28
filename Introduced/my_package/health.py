#健康計算機模組 module

#bmi計算function
def get_bmi(height,weight):
    height = height/100
    bmi = weight/height**2
    bmi = round(bmi,1)
    return bmi

#bmr計算function
def get_bmr(sex,height,weight,age):
    if sex == "男":
        bmr = 66 + (13.7*weight + 5*height - 6.8*age)
        bmr = round(bmr, 2)
        return bmr
    else:
        bmr = 655 + (9.6 * weight + 1.8 * height - 4.7 * age)
        bmr = round(bmr, 2)
        return bmr

#tdee計算function
def get_tdee(sex,height,weight,age,times):
    if sex == "男":
        bmr = 66 + (13.7*weight + 5*height - 6.8*age)
        bmr = round(bmr, 2)
    else:
        bmr = 655 + (9.6 * weight + 1.8 * height - 4.7 * age)
        bmr = round(bmr, 2)

    if times == 1:
        tdee = bmr * 1.2
    elif times == 2:
        tdee = bmr * 1.375
    elif times == 3:
        tdee = bmr * 1.55
    elif times == 4:
        tdee = bmr * 1.725
    else:
        tdee = bmr * 1.9
    tdee = round(tdee, 2)
    return tdee