class multipleFunctions():
    def Subfields():
            print("Subfields are in AI")
            mylists=["Machine Learning","Natural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
            for temp in mylists:
                print(temp)

    def OddEven():
            num=int(input("Enter a number:"))
            if((num%2)==0):
                print("is Even Number")
                GivenNum="Even Number"
            else:
                print(num,"is Odd Number")
                GivenNum="Odd Number"

    def Eligible():
            Gender=input("Your Gender:")
            Age=int(input("Your Age"))
            if(Age>=18 and Gender=="Female"):
                print("Eligible")
            elif(Age>=21 and Gender=="Male"):
                print("Eligible")
            else:
                print("Not Eligible")

    def percentage():
            Sub1=float(input("Subject1="))
            Sub2=float(input("Subject2="))
            Sub3=float(input("Subject3="))
            Sub4=float(input("Subject4="))
            Sub5=float(input("Subject5="))
            Total=Sub1+Sub2+Sub3+Sub4+Sub5
            print("Total :",Total)
            Percentage=Total/500.0*100
            print("Percentage : ",Percentage)

    def triangle():
            height=int(input("Height:"))
            breadth=int(input("Breadth:"))
            print("Area formula:(Height*Breadth)/2")
            Area=(height*breadth)/2 
            print("Area of a Triangle:",Area)
            height1=int(input("Height1:"))
            height2=int(input("Height2:"))
            breadth_1=int(input("Breadth:"))
            print("Perimeter formula:Height1+Height2+Breadth")
            Perimeter=height1+height2+breadth_1
            print("Perimeter of a Triangle:",Perimeter)