#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.

med=input("Do u have a medical cause? TYPE Y OR N")
attend= int(input("Enter attendance level"))

if med=="Y":
    print("U R ALLOWED BECAUSE OF MEDICAL CAUSE")
else:
    if attend>=75:
        print("U R ALLOWED")
    else:
        print("U R NOT ALLOWED")