print("Food_deleivery app")
print("What you want to do?")
print("1.Order_Food\n2.Cancel_Order\n3.Exit")
order=[]

while True:
    try:
        n=int(input("Enter the choice: "))
        if n==3:
            print("Exit is done")
            break
        if 0<n<=2:
            if n==1:
                print("Which food would you like to order?")
                print("1.Indian\n2.Chinese\n3.Italian")
                m=int(input("Enter: "))
                if m==1:
                    order="Indian"
                    order.append(m)
                    print("Indian is ordered")
                elif m==2:
                    order="Chinese"
                    order.append(m)
                    print("Chinese is ordered")
                elif m==3:
                    order="Italian"
                    order.append(m)
                    print("Italilan is ordered")
                elif m==4:
                    print(order)
                else:
                    print("Syllabus is out of conetxt")
            elif n==2:
                if order:
                    print(order,"is cancelled")
                    order=None
                    
                else:
                    print("Nothing to cancel")
        else:
            print("error")
    except:
        print("error")
