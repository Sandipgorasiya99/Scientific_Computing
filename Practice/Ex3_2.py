xh = input ('Enter the Number of Hours ')
xr = input('Enter your hourly rate ')
try:
    fxh = float(xh)
    fxr = float(xr)
except:
    print('*'*25)
    print('Error, please enter numeric number')
    quit()
print(fxh,fxr)
if fxh > 40.0:
    #Overtime dispaly and ask for overtime rate
    exrh= fxh - 40.0
    print('You worked', exrh , 'Hours overtime!, NO worries, you will be paid for that.')
    xotr=input('What is your overtime rate ')
    fxotr = float (xotr)
    #Calculate regular and overtime pay and print
    regp=fxr*40.0
    otp=exrh*fxr*fxotr
    print('Your regular pay is ', regp, '€')
    print('Your overtime pay is ', otp, '€')
    print('In total, You will be paid with' , regp+otp, '€')
else:
    print('You will be paid with' , fxh*fxr, '€')
