#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[ ]:




