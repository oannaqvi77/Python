#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('Hello, World!')=


# In[3]:


a=1
b=-1
c=a+b


# In[4]:


print(c)


# In[1]:


Maths = input("Marks obtained in Maths = ")
Physics = input("Marks obtained in Physics = ")
Chemistry = input("Marks obtained in Chemistry = ")
Total_Marks = 300
sum = int(Maths)+int(Physics)+int(Chemistry)
Percentage=int((sum/Total_Marks)*100)
print(f"Your percentage is {Percentage}%")


# In[12]:


Student_name= "Aun"
#obtained marks
maths=float(input("Marks obtained in Maths = "))
chem=float(input("Marks obtained in Chem = "))
phy=float(input("Marks obtained in Physics = "))
eng=float(input("Marks obtained in English = "))
#max marks
maths_max= 100
chem_max=  100
phy_max=100
eng_max=100
total_obtained=maths+chem+phy+eng
total_max=maths_max+chem_max+phy_max+eng_max
percentage=total_obtained/total_max*100
print("Percentage =",percentage,"%")
if (percentage<50 or maths<50 or chem<50 or phy<50 or eng<50):
    print("You are Fail!")
elif(50<=percentage<60):
    print("You got C Grade, Bad work!")
elif(60<=percentage<70):
    print("You got B Grade, Average!")
elif(70<=percentage<80):
    print("You got A Grade, Good work!")
else:
    print("You got A-1 Grade, Excellent work!")


# In[23]:


height=int(input("Height in cm = "))
mass=int(input("Mass in Kg = "))
height_in_meters=height/100
BMI=round(mass/height_in_meters**2,2)
print("Your BMI is",BMI) 
if (BMI<18.5):
    print("You are Underweight")
elif (18.5<=BMI<24.9):
    print("You are Fit")
else:
    print("You are Overweight")


# In[20]:


type(BMI)


# In[12]:


print('Calculator for Converting Centigrade to Fahrenheit & Kelvin')
Centigrade=float(input('Insert Temperature in Centigrade = '))
Fahrenheit=round((1.8*Centigrade+32),2)
Kelvin=Centigrade+273
print('The Value in Fahrenheit is',Fahrenheit,'F')
print('The Value in Kelvin is',Kelvin,'K')


# In[16]:


n=int(input("Enter the value of n:"))
for i in range(1,n+1,2):
    print(str(i)+". "+"Hello")


# In[30]:


start=1
end=20
while(start<=end):
    
    print(start,"Aun")
    start=int(start+1)
    


# In[ ]:


Integer=int(input("Enter the value of integer"))
while(Integer>=0):
    print(Integer)
    Integer=int(input("Enter the value of integer: "))


# In[1]:


Integer=int(input("Enter the value of integer: "))
while(Integer>=0):
    if (Integer>=0):
        print("Integer is Positive")
    else:
        print("Integer is Negative, The End")
    Integer=int(input("Enter the value of integer: "))
          


# 

# In[2]:


a="Aun"*5
print(a)


# In[13]:


Table=int(input("Enter the Table number: "))
n=int(input("Enter the range of table: "))

for i in range(1,n+1):
   print(Table,"x",str(i)," = ",i*Table)


# In[8]:


n=int(input("Enter the number upto which even Sum is required: "))
s=0
for i in range(2,n+1):
    if (i%2==0):
        s=s+i
print(s)


# In[9]:


def is_leap(year):
    leap = True
    
    if (year%4==0 and year%100!=0 or year%400==0):
        return leap
    else:
        return False
year = int(input())
print(is_leap(year))


# In[4]:


n=float(input("Enter the value of n :"))
if (n>2 and n<4):
    print("n is in range of (2,4) exclusively")
else:
    print("n is not in the range of (2,4) exclusively")


# In[6]:


n=float(input("Enter the value of n :"))
if (n>2 or n<4):
    print(n>2 or n<4)
else:
    print("n is not greater than 2 or less than 4 exclusively")


# In[9]:


n=float(input("Enter the value of n :"))
print(not(n>2 or n<4))


# In[17]:


n=int(input("Enter the no. of rows: "))
for i in range (1,n+1):
    print(i*"*")
for i in range (n+1,0,-1):
    print(i*"*")


# In[23]:


n=int(input("Enter the no. of rows: "))
for i in range (n+1,0,-1):
    print(i*"*")
for i in range (0,n+1,1):
    print(i*"*")


# In[4]:


i=1
n=int(input("Enter the number of rows: "))
while (i<=n):
    j=1
    while (j<=i):
        print('*',end='')
        j=j+1
    print()
    i=i+1


# In[18]:


i=1
n=int(input("Enter the number of rows: "))
while (i<=n):
    j=1
    while (j<=i):
        l=n
        print(l*" ",'*',end='')
        j=j+1
        l=l-1
    print()
    i=i+1


# In[5]:


# datatypes are two
# primitive data types (includes str,bool,int,float)
# object oriented datatype
for i in range(5):
    print('\t'*i,'HELLO')


#  

# In[24]:


for i in range(5):
    print('\n'*i,'HELLO')
pattern_lines=5
for i in range(pattern_lines):
    print('-'*i+' '+ (pattern_lines-(i+1))*'-')


# In[42]:


n=int(input("Enter an integer: "))
if (((n/2)-int(n/2))==0):
    print('The number is even')
else:
    print('The number is odd')


# In[27]:


import winsound
for i in range(10):
    winsound.Beep(1000,500)
    winsound.Beep(1500,500)


# In[29]:


def say_hello():
    print("Hello")
    
say_hello()


# In[58]:


def is_even(n,m):
    result=n%2==0
    result_1=m%2==0
    return(result,result_1)

is_even(19,6)


# In[38]:


is_even(12)


# In[51]:


print(x)


# In[167]:


def generate_report(name,phys,chem,math,cs):
    per_math=str(math)+"% out of 100%"
    per_phy=str(phys)+"% out of 100%"
    per_chem=str(chem)+"out of 100%"
    per_CS=str(cs)+"% out of 100%"
    overall_per=(phys+chem+math+cs)/4
    msg = 'Student:'+name+'\n'+ per_math +'\n'+ per_chem +'\n' + per_phy +'\n' + per_CS
    return msg, overall_per


def show_report(overall_per):
    import winsound
    if(overall_per>=50):
        winsound.Beep(500,500)
        print ("passed")
    else:
        winsound.Beep(2000,500)
        print ("fail")


# In[168]:


m, p = generate_report("ali",54,67,65,87)
print(m,'\n',p)
h=show_report(34)




# In[180]:


def generate_report(name,phys,chem,math,cs):
    per_math=str(math)+"% out of 100%"
    per_phy=str(phys)+"% out of 100%"
    per_chem=str(chem)+"out of 100%"
    per_CS=str(cs)+"% out of 100%"
    overall_per=(phys+chem+math+cs)/4
    msg = 'Student:'+name+'\n'+ per_math +'\n'+ per_chem +'\n' + per_phy +'\n' + per_CS
    import winsound

    if(overall_per>=50):
        winsound.Beep(500,500)
        print ("passed")
    else:
        winsound.Beep(2000,500)
        print ("fail")
    return msg, overall_per


# In[182]:


m, p = generate_report("ali",90,76,65,87)
print(m,'\n',p)


# In[5]:


a=[2,4,5,6,8]
for i in range(5):
    print(a[i],end=' ')
    print(a[i]**2)


# In[18]:


a=[2,4,5,6,8]
b=[1,2,4,5,6]
for i in range(0,len(a)):
    print(a[i]+b[i])


# In[30]:


a=[2,4,5,6,8]
b=[1,2,4,5,6]
x=[]
for i in range(0,len(b)):
    x.append(a[i]+b[i])
print(x)


# In[33]:


a=[2,4,5,6,8]
b=[1,2,4,5,6]
for i in range(0,len(a)):
    v=(a[i]+b[i])
    for i in range(0,len(a)):
        print(v)


# In[27]:


y=[2,4,7,9,32,5]
y.sort()
print(y[-2])


# In[12]:


a=[1,4,10,2,9]
for i in range(0,len(a)):
    j=i
    for j in range(len(a)):
        if (a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        print(a)


# In[46]:


a=[1,4,10,2,9]
x=[]
for i in range(len(a)):
    x.append(a[-i-1])
print(x)


# In[6]:


def factorial(b):
    a=b-1
    while a>0:
        b=b*a
        a=a-1
    return(b)
factorial(5)


# In[2]:


print("Concrete Mix Design Quantities Calculator [Metric Units] (In Accordance with American Concrete Institute)")
print(" For for 5 MPa Concrete, Use 1:5:10 "+"\n"+" For for 7.5 MPa Concrete, Use 1:4:8 "+"\n"+" For for 10 MPa Concrete, Use 1:3:6 "+"\n"+" For for 15 MPa Concrete, Use 1:2:4 "+"\n"+" For for 20 MPa Concrete, Use 1:1.5:3 "+"\n"+" For for 25 MPa Concrete, Use 1:1:2 "+"\n"+" For for 30 MPa Concrete, Use 1:0.75:1.5 "+"\n"+" For for 35 MPa Concrete, Use 1:0.5:1 "+"\n"+" For for 40 MPa Concrete, Use 1:0.25:0.5 ")
Concrete_strength=float(input("Enter Concrete strength from above options: "))
f_agg=float(input("Enter the proportion of Fine Aggregates: "))
c_agg=float(input("Enter the proportion of Coarse Aggregates: "))
fm=float(input("Enter the Finess Modulus of Fine Aggregates, (Options are 2.4,2.6,2.8,3) : "))
max_agg_size=float(input("Enter the Max. Aggregates Size(mm)"+"Options are 9.5mm,12.5mm,19mm,25mm,37.5mm,50mm,75mm,100mm"+": "))
wa_c=float(input("Enter the Water Absorption of Coarse Aggregates (Enter (-ve)value in case of free surface moisture)(%): "))
wa_f=float(input("Enter the Water Absorption of Fine Aggregates (Enter (-ve)value in case of free surface moisture)(%): "))
ad_per=float(input("Enter the Percentage of Admixture: "))
slump=float(input("Value of Slump"+"\n"+"For slump 25-50mm, Enter 1"+"\n"+"For slump 75-100mm, Enter 2"+"\n"+"For slump 150-175mm, Enter 3"+": "))
if (slump==1):
    if(max_agg_size==9.5):
        water=207
        air=0.03
    elif(max_agg_size==12.5):
        water=199
        air=0.025
    elif(max_agg_size==19):
        water=190
        air=0.02
    elif(max_agg_size==25):
        water=179
        air=0.015
    elif(max_agg_size==37.5):
        water=166
        air=0.01
    elif(max_agg_size==50):
        water=154
        air=0.005
    elif(max_agg_size==75):
        water=130
        air=0.003
    elif(max_agg_size==100):
        water=113
        air=0.002
    else:
        print("Enter a valid number from the options")
elif (slump==2):
    if(max_agg_size==9.5):
        water=288
        air=0.03
    elif(max_agg_size==12.5):
        water=216
        air=0.025
    elif(max_agg_size==19):
        water=205
        air=0.02
    elif(max_agg_size==25):
        water=193
        air=0.015
    elif(max_agg_size==37.5):
        water=181
        air=0.01
    elif(max_agg_size==50):
        water=169
        air=0.005
    elif(max_agg_size==75):
        water=145
        air=0.003
    elif(max_agg_size==100):
        water=124
        air=0.002
    else:
        print("Enter a valid number from the options")
elif (slump==3):
    if(max_agg_size==9.5):
        water=243
        air=0.03
    elif(max_agg_size==12.5):
        water=228
        air=0.025
    elif(max_agg_size==19):
        water=216
        air=0.02
    elif(max_agg_size==25):
        water=202
        air=0.015
    elif(max_agg_size==37.5):
        water=190
        air=0.01
    elif(max_agg_size==50):
        water=178
        air=0.005
    elif(max_agg_size==75):
        water=160
        air=0.003
    elif(max_agg_size==100):
        water=148
        air=0.002
    else:
        print("Enter a valid number from the options")
else:
    print("Enter a valid value of slump from the options above")
water_v_per_m3=(water/1000)
if (Concrete_strength==45):
    wc=0.37
elif (Concrete_strength==40):
    wc=0.42
elif (Concrete_strength==35):
    wc=0.47
elif (Concrete_strength==30):
    wc=0.54
elif (Concrete_strength==25):
    wc=0.61
elif (Concrete_strength==20):
    wc=0.69
elif (Concrete_strength==15 or Concrete_strength==10 or Concrete_strength==5 ):
    wc=0.79
else:
    print("Enter a valid value from the options above")
cement_wt=water/wc
cement_v=cement_wt/3150
if (fm==2.4):
    if(max_agg_size==9.5):
        ca_wt=0.5
    elif(max_agg_size==12.5):
        ca_wt=0.59
    elif(max_agg_size==19):
        ca_wt=0.66
    elif(max_agg_size==25):
        ca_wt=0.71
    elif(max_agg_size==37.5):
        ca_wt=0.75
    elif(max_agg_size==50):
        ca_wt=0.78
    elif(max_agg_size==75):
        ca_wt=0.82
    elif(max_agg_size==100):
        ca_wt=0.84
    else:
        print("Enter a valid number")
if (fm==2.6):
    if(max_agg_size==9.5):
        ca_wt=0.48
    elif(max_agg_size==12.5):
        ca_wt=0.57
    elif(max_agg_size==19):
        ca_wt=0.64
    elif(max_agg_size==25):
        ca_wt=0.69
    elif(max_agg_size==37.5):
        ca_wt=0.73
    elif(max_agg_size==50):
        ca_wt=0.76
    elif(max_agg_size==75):
        ca_wt=0.8
    elif(max_agg_size==100):
        ca_wt=0.82
    else:
        print("Enter a valid number")
if (fm==2.8):
    if(max_agg_size==9.5):
        ca_wt=0.46
    elif(max_agg_size==12.5):
        ca_wt=0.55
    elif(max_agg_size==19):
        ca_wt=0.62
    elif(max_agg_size==25):
        ca_wt=0.67
    elif(max_agg_size==37.5):
        ca_wt=0.71
    elif(max_agg_size==50):
        ca_wt=0.74
    elif(max_agg_size==75):
        ca_wt=0.78
    elif(max_agg_size==100):
        ca_wt=0.8
    else:
        print("Enter a valid number")
if (fm==3):
    if(max_agg_size==9.5):
        ca_wt=0.44
    elif(max_agg_size==12.5):
        ca_wt=0.53
    elif(max_agg_size==19):
        ca_wt=0.6
    elif(max_agg_size==25):
        ca_wt=0.65
    elif(max_agg_size==37.5):
        ca_wt=0.69
    elif(max_agg_size==50):
        ca_wt=0.72
    elif(max_agg_size==75):
        ca_wt=0.76
    elif(max_agg_size==100):
        ca_wt=0.78
    else:
        print("Enter a valid number")
ca_wt_kg=ca_wt*1600
ca_v=ca_wt_kg/2700
admixture=ad_per/100
fine_aggregate=(1-(water_v_per_m3+ca_v+air+admixture+cement_v))
fine_wt=fine_aggregate*2650
water_ab=ca_v*wa_c/100+fine_aggregate*wa_f/100


print("Cement Weight in KG: ",round(cement_wt,1))
print("Fine Aggregates Weight in KG: ",round(fine_wt,1))
print("Coarse Aggregates Weight in KG: ",round(ca_wt_kg,1))
print("Admixture Volume in m3: ",admixture)
print("Water Volume in litres: ",round((water/1000+water_ab)*1000),1)
import winsound 
winsound.Beep(1000,1500)


# 
# cement=float(input('Enter the quantity of cement in KG: '))
# fine_agg=float(input('Enter the quantiy')

# In[26]:


a="2468"
for i in range(0,len(a)):
    b=a[-i-1]
    print(b,end="")


# In[ ]:


a=2468
b=0
while a>0:
    b=a/10
    c=b-int(b)
    d=c*10
    print(d)


# In[ ]:




