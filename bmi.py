# Calculate that if you are overweight
a=float(input('Enter your height(m): \n'))
b=float(input('Enter your weight(kg): \n'))
BMI=(b/a/a)
print('Your BMI equals to:'+'%.1f' % BMI) #浮点数保留小数点: ‘%.Xf'%f 
if BMI <=18.5:
    print('Too skinny, baby.')
elif BMI <=25:
    print('Quite normal.')
else :
print('Overweight.')		