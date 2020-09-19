# 定义函数
def HAc(pH,concentration,V):
    pKa=4.76
    c1=concentration/(10**(pH-pKa)+1)
    c2=concentration/(10**(pKa-pH)+1)
    array=[]
    mw1=60.05
    mw2=82.03
    m1=c1*mw1*V
    m2=c2*mw2*V
    array.append(m1)
    array.append(m2)
    return array

def NaHCO3(pH,concentration,V):
    pKa=10.32
    c1=concentration/(10**(pH-pKa)+1)
    c2=concentration/(10**(pKa-pH)+1)
    array=[]
    mw1=84.0
    mw2=106.0
    m1=c1*mw1*V
    m2=c2*mw2*V
    array.append(m1)
    array.append(m2)
    return array

def NaH2PO4(pH,concentration,V):
    pKa=7.21
    c1=concentration/(10**(pH-pKa)+1)
    c2=concentration/(10**(pKa-pH)+1)
    array=[]
    mw1=119.98
    mw2=141.96
    m1=c1*mw1*V
    m2=c2*mw2*V
    array.append(m1)
    array.append(m2)
    return array
def Citric(pH,concentration,V):
    pKa=7.21
    c1=concentration/(10**(pH-pKa)+1)
    c2=concentration/(10**(pKa-pH)+1)
    array=[]
    mw1=210.14
    mw2=294.12
    m1=c1*mw1*V
    m2=c2*mw2*V
    array.append(m1)
    array.append(m2)
    return array
 
# 展示说明
print("本体系的浓度单位为mol/L，本体系固体无说明均为无水合")
print("选择体系：")
print("1-HAc-NaAc缓冲体系")
print("2-NaHCO3-Na2CO3缓冲体系")
print("3-NaH2PO4-Na2HPO4缓冲体系")
print("4-Citric-SodiumCitate（柠檬酸-柠檬酸钠）缓冲体系")

# 用户输入
choice = input("输入你的选择(1/2/3/4):")
 
num1 = float(input("输入pH: "))
num2 = float(input("输入浓度: "))
num3 = float(input("输入体积： "))
if choice == '1':
    gHAc=HAc(num1,num2,num3)[0]
    gNaAc=HAc(num1,num2,num3)[1]
    print("pH为",num1,"，浓度为",num2,"mol/L的",num3,"L的HAc-NaAc缓冲体系：")
    print("称取HAc",gHAc,"g，称取NaAc",gNaAc,"g")
    
 
elif choice == '2':
    gNaHCO3=NaHCO3(num1,num2,num3)[0]
    gNa2CO3=NaHCO3(num1,num2,num3)[1]
    print("pH为",num1,"，浓度为",num2,"mol/L的",num3,"L的NaHCO3-Na2CO3缓冲体系：")
    print("称取NaHCO3",gNaHCO3,"g，称取Na2CO3",gNa2CO3,"g")
 
elif choice == '3':
    gNaH2PO4=NaH2PO4(num1,num2,num3)[0]
    gNa2HPO4=NaH2PO4(num1,num2,num3)[1]
    print("pH为",num1,"，浓度为",num2,"mol/L的",num3,"L的NaH2PO4-Na2HPO4缓冲体系：")
    print("称取NaH2PO4",gNaH2PO4,"g，称取Na2HPO4",gNa2HPO4,"g")
 
elif choice == '4':
    gCitric=Citric(num1,num2,num3)[0]
    gSodiumCitate=Citric(num1,num2,num3)[1]
    print("pH为",num1,"，浓度为",num2,"mol/L的",num3,"L的Citric-SodiumCitate缓冲体系：")
    print("称取CitricAcid-H2O",gCitric,"g，称取SodiumCitate-2H2O",gSodiumCitate,"g")
else:
    print("非法输入")
