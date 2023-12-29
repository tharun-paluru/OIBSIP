#python program to calculate BMI
'''BODY MASS INDEX (BMI) = RATIO OF WEIGHT IN KGS TO THE SQUARE OF HEIGHT IN METERS

                           BMI = weight(in kgs)/height square(in meters)
                           units = kg per meter square

BMI < 18.5 ---> Under Weight
18.5 <= BMI <= 24.9  ---> Healthy Weight
25 <= BMI <= 29.9 ---> Over Weight
BMI >= 30 ---> obese'''

def details():                                                           #taking the inputs
    name = input("Please!,enter your name:")
    W = float(input(f"{name} please! ENTER YOUR WEIGHT IN KILOGRANS:")) 
    h = float(input(f"{name} please! ENTER YOUR HEIGHT IN FEETS:"))
    H = round(h*0.305,2) #height in meters
    return (name,W,H)

def show(name,W,H):                                                     #displaying the inputs
    print(f"{name},your weight is {W} kgs")
    print(f"{name},your height in meters is {H} mts")
    
def BMI_CAL(name,W,H):                                                  #calculating the  BMI
    BMI = W/(H**2)
    BMI = round(BMI,2)

    if (BMI < 18.50):
        print(f"hi!{name},your BMI value is {BMI} kg/m.sq which concludes your are in 'UNDER WEIGHT' section so you should eat healthy food buddy...")
    elif(18.50 <= BMI <= 24.99):
        print(f"hi!{name},your BMI value is {BMI} kg/m.sq which concludes your are in 'HEALTHY WEIGHT' section so keep going on buddy...")
    elif(25 <= BMI <= 29.99):
        print(f"hi!{name},your BMI value is {BMI} kg/m.sq which concludes your are in 'OVER WEIGHT' section so you should eat less food buddy...")
    elif(BMI >= 30):
        print(f"hi!{name},your BMI value is {BMI} kg/m.sq which concludes your are in 'OBESE' section so you be very carefull buddy...")
    
    
#main 
print("hey! this is an BMI calculater so be ready with your weight(in kgs) and height(in feets)")
name,W,H = details()
show(name,W,H)
BMI_CAL(name,W,H)
