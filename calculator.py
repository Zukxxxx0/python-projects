while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")


choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
print(choice)
if (select_op(choice) == -1):
    # program ends here
    print("Done. Terminating")
    exit()
