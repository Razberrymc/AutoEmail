import pandas as pd
import smtplib

prop=pd.read_csv(r'\Users\mclark\Desktop\python\email\fakeEmailData_mclarkTests.csv')

for index, row in prop.iterrows():
    Name_of_Field = ""
    write_email = False
    if (Name_of_Field == "") and (row['Owner_ID_Flag']) == 1:
        Name_of_Field = "Owner ID"
        Field1Value = (row['Owner_ID1']).strip()
        Field2Value = (row['Owner_ID2']).strip()
        write_email = True
    elif (Name_of_Field == "") and (row['Owner_Name_Flag']) == 1:
        Name_of_Field = "Owner Name"
        Field1Value = (row['Owner_Name1']).strip()
        Field2Value = (row['Owner_Name2']).strip()
        write_email = True
    elif (Name_of_Field == "") and (row['Owner_Mail_Addr_Flag']) == 1:
        Name_of_Field = "Owner Mailing Address"
        Field1Value = (row['Owner_Mail_Addr1']).strip()
        Field2Value = (row['Owner_Mail_Addr2']).strip()
        write_email = True
    elif (Name_of_Field == "") and (row['Legal_Desc_Flag']) == 1:
        Name_of_Field = "Legal Description"
        Field1Value = (row['Legal_Desc1']).strip()
        Field2Value = (row['Legal_Desc2']).strip()
        write_email = True
    elif (Name_of_Field == "") and (row['Exemptions_Flag']) == 1:
        Name_of_Field = "Exemptions"
        Field1Value = (row['Exemptions1']).strip()
        Field2Value = (row['Exemptions2']).strip()
        write_email = True
    elif (Name_of_Field == "") and (row['Ag_Classification_Flag']) == 1:
        Name_of_Field = "Ag Classification"
        Field1Value = (row['Ag_Classification1']).strip()
        Field2Value = (row['Ag_Classification2']).strip()
        write_email = True



    if ((row['Owner_ID_Flag']) == 1) and (Field1Value != (row['Owner_ID1']) and (str(row['Owner_ID1']).strip() == "nan")):
        addOn1 = "- A change in Owner ID was also detected. It was NO OWNER ID, now it is " + str(row['Owner_ID2']).strip() + ".\n\n"
    elif ((row['Owner_ID_Flag']) == 1) and (Field1Value != (row['Owner_ID1']) and (str(row['Owner_ID2']).strip() == "nan")):
        addOn1 = "- A change in Owner ID was also detected. It was " + str(row['Owner_ID1']).strip() + ", now it is NO OWNER ID" + ".\n\n"
    elif ((row['Owner_ID_Flag']) == 1) and (Field1Value != (row['Owner_ID1'])):
        addOn1 = "- A change in Owner ID was also detected. It was " + str(row['Owner_ID1']).strip() + ", now it is " + str(row['Owner_ID2']).strip() + ".\n\n"
    else:
        addOn1 = ""

    if ((row['Owner_Name_Flag']) == 1) and (Field1Value != (row['Owner_Name1']) and (str(row['Owner_Name1']).strip() == "nan")):
        addOn2 = "- A change in Owner Name was also detected. It was NO OWNER NAME, now it is " + str(row['Owner_Name2']).strip() + ".\n\n"
    elif ((row['Owner_Name_Flag']) == 1) and (Field1Value != (row['Owner_Name1']) and (str(row['Owner_Name2']).strip() == "nan")):
        addOn2 = "- A change in Owner Name was also detected. It was " + str(row['Owner_Name1']).strip() + ", now it is NO OWNER NAME" + ".\n\n"
    elif ((row['Owner_Name_Flag']) == 1) and (Field1Value != (row['Owner_Name1'])):
        addOn2 = "- A change in Owner Name was also detected. It was " + str(row['Owner_Name1']).strip() + ", now it is " + str(row['Owner_Name2']).strip() + ".\n\n"
    else:
        addOn2 = ""

    if ((row['Owner_Mail_Addr_Flag']) == 1) and (Field1Value != (row['Owner_Mail_Addr1']) and (str(row['Owner_Mail_Addr1']).strip() == "nan")):
        addOn3 = "- A change in Owner Mailing Address was also detected. It was NO OWNER MAILING ADDRESS, now it is " + str(row['Owner_Mail_Addr2']).strip() + ".\n\n"
    elif ((row['Owner_Mail_Addr_Flag']) == 1) and (Field1Value != (row['Owner_Mail_Addr1']) and (str(row['Owner_Mail_Addr2']).strip() == "nan")):
        addOn3 = "- A change in Owner Mailing Address was also detected. It was " + str(row['Owner_Mail_Addr1']).strip() + ", now it is NO OWNER MAILING ADDRESS" + ".\n\n"
    elif ((row['Owner_Mail_Addr_Flag']) == 1) and (Field1Value != (row['Owner_Mail_Addr1'])):
        addOn3 = "- A change in Owner Mailing Address was also detected. It was " + str(row['Owner_Mail_Addr1']).strip() + ", now it is " + str(row['Owner_Mail_Addr2']).strip() + ".\n\n"
    else:
        addOn3 = ""

    if ((row['Legal_Desc_Flag']) == 1) and (Field1Value != (row['Legal_Desc1']) and (str(row['Legal_Desc1']).strip() == "nan")):
        addOn4 = "- A change in Legal Description was also detected. It was NO LEGAL DESCRIPTION, now it is " + str(row['Legal_Desc2']).strip() + ".\n\n"
    elif ((row['Legal_Desc_Flag']) == 1) and (Field1Value != (row['Legal_Desc1']) and (str(row['Legal_Desc2']).strip() == "nan")):
        addOn4 = "- A change in Legal Description was also detected. It was " + str(row['Legal_Desc1']).strip() + ", now it is NO LEGAL DESCRIPTION" + ".\n\n"
    elif ((row['Legal_Desc_Flag']) == 1) and (Field1Value != (row['Legal_Desc1'])):
        addOn4 = "- A change in Legal Description was also detected. It was " + str(row['Legal_Desc1']).strip() + ", now it is " + str(row['Legal_Desc2']).strip() + ".\n\n"
    else:
        addOn4 = ""

    if ((row['Exemptions_Flag']) == 1) and (Field1Value != (row['Exemptions1']) and (str(row['Exemptions1']).strip() == "nan")):
        addOn5 = "- A change in Exemptions was also detected. It was NO EXEMPTIONS, now it is " + str(row['Exemptions2']).strip() + ".\n\n"
        #addOn5 = "- A change in Exemptions was also detected. It was NO EXEMPTIONS, now it is " + str(masterExemptionList) + ".\n\n"
    elif ((row['Exemptions_Flag']) == 1) and (Field1Value != (row['Exemptions1']) and (str(row['Exemptions2']).strip() == "nan")):
        addOn5 = "- A change in Exemptions was also detected. It was " + str(row['Exemptions1']).strip() + ", now it is NO EXEMPTIONS" + ".\n\n"
        #addOn5 = "- A change in Exemptions was also detected. It was " + str(masterExemptionList) + ", now it is NO EXEMPTIONS" + ".\n\n"
    elif ((row['Exemptions_Flag']) == 1) and (Field1Value != (row['Exemptions1'])):
        addOn5 = "- A change in Exemptions was also detected. It was " + str(row['Exemptions1']).strip() + ", now it is " + str(row['Exemptions2']).strip() + ".\n\n"
        #addOn5 = "- A change in Exemptions was also detected. It was " + str(masterExemptionList) + ", now it is " + str(masterExemptionList2) + ".\n\n"
    else:
        addOn5 = ""

    if ((row['Ag_Classification_Flag']) == 1) and (Field1Value != (row['Ag_Classification1']) and (str(row['Ag_Classification1']).strip() == "nan")):
        addOn6 = "- A change in Ag Classification was also detected. It was NO AG CLASSIFICATION, now it is " + str(row['Ag_Classification2']).strip() + ".\n\n"
    elif ((row['Ag_Classification_Flag']) == 1) and (Field1Value != (row['Ag_Classification1']) and (str(row['Ag_Classification2']).strip() == "nan")):
        addOn6 = "- A change in Ag Classification was also detected. It was " + str(row['Ag_Classification1']).strip() + ", now it is NO AG CLASSIFICATION" + ".\n\n"
    elif ((row['Ag_Classification_Flag']) == 1) and (Field1Value != (row['Ag_Classification1'])):
        addOn6 = "- A change in Ag Classification was also detected. It was " + str(row['Ag_Classification1']).strip() + ", now it is " + str(row['Ag_Classification2']).strip() + ".\n\n"
    else:
        addOn6 = ""



    if write_email == True:

        FirstName = (row['first_name'])
        LastName = (row['last_name'])
        ParcelNumber = (row['geo_id'])
        changeDate = (row['Date_Changed'])
        SitusAddress = (row['SitusAddress'])

        smtpObj = smtplib.SMTP('smtp.office365.com', 587)

        type(smtpObj)

        smtpObj.ehlo()

        smtpObj.starttls()

        #print("Please enter your password:")

        cred = open("launchCodes.txt", "r")
        credList = cred.readlines()
        username = (credList[0]).rstrip('\n')
        password = (credList[1]).rstrip('\n')

        smtpObj.login(username, password) #PW can be subbed w/ input() but using actual PW to speed up process

        sender=username
        receiver='mclarkacpa@gmail.com'
        subject='Information Change Alert on Alachua County Parcel: ' + ParcelNumber
        content= "Dear " + FirstName + " " + LastName + ",\n\nOur system has detected that your property information at " + ParcelNumber + ", " + SitusAddress + " has changed." + " At the time of you voluntarily signing up for our owner alert system, our system showed " + Name_of_Field + ". Our system indicates that on " + changeDate + " " + str(Field1Value) + " has been changed to " + str(Field2Value) + ".\n\n" + addOn1 + addOn2 + addOn3 + addOn4 + addOn5 + addOn6 + "If this change was initiated by you, the owner, this will serve as a receipt that the above changes were made.\nIf this change WAS NOT initiated by you, the owner, please contact us immediately at 352-374-5230 or reply to this email to acpa@acpafl.org.\nIf ownership of a parcel was changed over to another owner altogether, this will be the last email alert you will receive on this particular parcel. You must sign up again for any new parcels you would like to be notified about.\n\nThe information reflected in this free service that you, the owner, signed up for is for informational purposes only. This information cannot be used in any legal matters as official documentation. It is strictly for your general knowledge only. You should contact us immediately with any questions or concerns."
        mailtext='Subject:'+subject+'\n\n'+content


        smtpObj.sendmail(sender, receiver, mailtext)

        cred.close()

        smtpObj.quit()
