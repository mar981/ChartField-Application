import csv

def empty(csv_part,row): #needs to have a parameter for a specific part of the CSV to check it because if there is a blank in one part doesnt mean theres blank in every part
    if csv_part == 'fund':
        if row[3] == '' or row[4] == '':
            return True
        else:
            return False
    elif csv_part == 'deptid':
        if row[5] == '' or row[6] == '':
            return True
        else:
            return False
    elif csv_part == 'program':
        if row[7] == '' or row[8] == '':
            return True
        else:
            return False
    elif csv_part == 'project':
        if row[9] == '' or row[10] == '':
            return True
        else:
            return False
    elif csv_part == 'account':
        if row[11] == '' or row[12] == '':
            return True
        else:
            return False
        
def part_len(a,row):
    if a == 'fund':
        if len(row[3]) > 2 or len(row[4]) > 2 or len(row[3]) < 2 or len(row[4]) < 2:
            return True
        else:
            return False
    elif a == 'deptid':
        if len(row[5]) > 5 or len(row[6]) > 5 or  len(row[5]) < 5 or len(row[6]) < 5:
            return True
        else:
            return False
    elif a =='deptiD':
        if len(row[6]) > 5 or  len(row[6]) < 5:
            return True
        else:
            return False
    elif a == 'program':
        if len(row[7]) > 5 or len(row[8]) > 5 or  len(row[7]) < 5 or len(row[8]) < 5:
            return True
        else:
            return False
    elif a == 'project':
        if len(row[9]) > 5 or len(row[10]) > 5 or  len(row[9]) < 5 or len(row[10]) < 5:
            return True
        else:
            return False
    elif a == 'account':
        if len(row[11]) > 5 or len(row[12]) > 5 or  len(row[11]) < 5 or len(row[12]) < 5:
            return True
        else:
            return False
    elif a == 'accounT':
        if len(row[12]) > 5 or len(row[12]) < 5:
            return True
        else:
            return False

def list_4_original(Original):
    
    data = Original.read()
    
    data2 = data.split('\n')

    hold = []

    skip = 0 
    for line in data2:
        skip += 1
        if skip == 1: 
            pass
        else:
            datasplit = line.split('\t')
            hold.append(datasplit)
    return hold
            
def list_compare(cleandoc):
    cleanread = cleandoc.read()
    
    cleansplit = cleanread.split('\n')

    cleanlist = []

    skip = 0 
    for line in cleansplit:
        skip += 1
        if skip == 1:
            pass
        else:
            datasplit = line.split('\t') 
            cleanlist.append(datasplit)
    return cleanlist
    
def find_errors():
    import csv
    import os
    
    ###ANALYSIS WITH MONTHS
    print('-----------------------------------------------------------------\n')
    file = input("Enter the file name you want to analyze for errors: \n (HAS TO INCLUDE THE END: '.csv.txt')(press enter when ready): ")
    date = input("\nEnter today's date (MM-DD-YY), it will be added to the end of the files created. (press enter when ready): ")
    print("\nResults:")

    try:
        os.makedirs('J:\FSM\Maria Restrepo\PROGRAMS\\ERRORS')
    except:
        pass
    try:
        os.makedirs('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN')
    except:
        pass

    Original = open(file)
    
    hold = list_4_original(Original)
        

    #CVS with months'+date+'.csv.txt'
    monthdoc = open('J:\FSM\Maria Restrepo\PROGRAMS\\ERRORS\\CVS with months'+date+'.csv.txt','w',encoding='utf8')

    #CVS clean w.o MONTHS'+date+'.csv.txt'
    cleandoc = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS'+date+'.csv.txt', 'w',encoding='utf8')

    ##iterating over every row in the document for the monthss
    for row in hold:
    
        NETID_IS_JAN = row[2].startswith('Jan')
        NETID_IS_FEB = row[2].startswith('Feb')
        NETID_IS_MAR = row[2].startswith('Mar')
        NETID_IS_APR = row[2].startswith('Apr')
        NETID_IS_MAY = row[2].startswith('May')
        NETID_IS_JUN = row[2].startswith('Jun')
        NETID_IS_JUL = row[2].startswith('Jul')
        NETID_IS_AUG = row[2].startswith('Aug')
        NETID_IS_SEP = row[2].startswith('Sep')
        NETID_IS_OCT = row[2].startswith('Oct')
        NETID_IS_NOV = row[2].startswith('Nov')
        NETID_IS_DEC = row[2].startswith('Dec')

        PROG_IS_JAN = row[7].startswith('Jan') or row[8].startswith('Jan')
        PROG_IS_FEB = row[7].startswith('Feb') or row[8].startswith('Feb')
        PROG_IS_MAR = row[7].startswith('Mar') or row[8].startswith('Mar')
        PROG_IS_APR = row[7].startswith('Apr') or row[8].startswith('Apr')
        PROG_IS_MAY = row[7].startswith('May') or row[8].startswith('May')
        PROG_IS_JUN = row[7].startswith('Jun') or row[8].startswith('Jun')
        PROG_IS_JUL = row[7].startswith('Jul') or row[8].startswith('Jul')
        PROG_IS_AUG = row[7].startswith('Aug') or row[8].startswith('Aug')
        PROG_IS_SEP = row[7].startswith('Sep') or row[8].startswith('Sep')
        PROG_IS_OCT = row[7].startswith('Oct') or row[8].startswith('Oct')
        PROG_IS_NOV = row[7].startswith('Nov') or row[8].startswith('Nov')
        PROG_IS_DEC = row[7].startswith('Dec') or row[8].startswith('Dec')

        
        netid = NETID_IS_JAN or NETID_IS_FEB or NETID_IS_MAR or NETID_IS_APR or NETID_IS_MAY or NETID_IS_JUN or NETID_IS_JUL or NETID_IS_AUG or NETID_IS_SEP or NETID_IS_OCT or NETID_IS_NOV or NETID_IS_DEC 
        prog = PROG_IS_JAN or PROG_IS_FEB or PROG_IS_MAR or PROG_IS_APR or PROG_IS_MAY or PROG_IS_JUN or PROG_IS_JUL or PROG_IS_AUG or PROG_IS_SEP or PROG_IS_OCT or PROG_IS_NOV or PROG_IS_DEC

        if netid or prog: 
            monthdoc.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n') 

        else:
            cleandoc.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')

    
    print("All done with CVS with months"+date+'.csv.txt')
    monthdoc.close()
    Original.close()
    cleandoc.close()


    #-----------------------------------------------------------------------------------------#

    #FUND ERRORS
    ##opening the file
    
    Original = open(file)
    
    hold = list_4_original(Original)

    fund_doc = open('J:\FSM\Maria Restrepo\PROGRAMS\\ERRORS\\CVS with FUND errors'+date+'.csv.txt','w')
    #fund_doc.write(''+'\t'+''+'\t'+''+'\t'+'FUND'+'\t'+'FUND'+'\n')


    cleandoc = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS'+date+'.csv.txt')

    newclean = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS.FUNDS ERR'+date+'.csv.txt','w')

    
    for row in hold:
        FUNDFROM__ = row[3].startswith('-')
        FUND_LEN = part_len('fund',row)
        FUND_EMPTY = empty('fund',row)
        FUNDTO__ = row[4].startswith('-')

        fund_errors = FUNDFROM__ or FUND_LEN or FUND_EMPTY or FUNDTO__
    
        if fund_errors:
            fund_doc.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')

    print("All done with CVS with FUND errors" + date+'.csv.txt')    
    fund_doc.close()
    Original.close()

    cleanlist = list_compare(cleandoc)
    
    try:    
        for row in cleanlist:
            FUNDFROM__ = row[3].startswith('-')
            FUND_LEN = part_len('fund',row)
            FUND_EMPTY = empty('fund',row)
            FUNDTO__ = row[4].startswith('-')

            fund_errors = FUNDFROM__ or FUND_LEN or FUND_EMPTY or FUNDTO__
        
            if fund_errors:
                lol = 'lol'
            
            else:
                newclean.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')
    except:
        if row != ['']:
           print('An exception was raised and not because it is an empty line at the end of the text document.')

    #YOU CANT USE AN ELSE STATEMENT BECAUSE AN EXCEPTION WILL ALWAYS BE RAISED BECAUSE NOTEPAD WILL ALWAYS ADD A BLANK LINE TO THE END
    #OF THE FILE AND THEREFORE THE ERROR OF 'INDEX OUT OF RANGE' WILL ALWAYS OCCUR
    #print('''All done with CVS with "w.o MONTHS.FUNDS ERR"''' + date+'.csv.txt')       
    cleandoc.close()
    newclean.close()
    
    ##DEPTID ERRORS
    ##opening the file

    Original = open(file)
    
    hold = list_4_original(Original)
    
    deptid_doc = open('J:\FSM\Maria Restrepo\PROGRAMS\\ERRORS\\CVS with DEPTID errors'+date+'.csv.txt','w')
    #deptid_doc.write(''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+'DEPTID'+'\t'+'DEPTID'+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\n')

    
    cleandoc = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS.FUNDS ERR'+date+'.csv.txt')
    
    newclean = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS.FUNDS.DEPTID ERR'+date+'.csv.txt','w')
    
    
    for row in hold:

        DEPTIDFROM__ = row[5].startswith('-')
        DEPTIDFROM_ALPHA = row[5].isnumeric()
        DEPTIDFROM_IS_NA = row[5] is ('NA')
        DEPTIDTO_IS_NA = row[6] is ('NA')
        DEPTIDTO_ALPHA = row[6].isnumeric()
        DEPTIDTO__ = row[6].startswith('-')
        DEPTID_LEN = part_len('deptid',row)
        DEPTID_LEN_COND = part_len('deptiD',row) #FOR THOSE WHO HAVE 0 AS THE BEGINNING PART OF THE RANGE AND WE ONLY WANT TO LOOK AT THE END PART OF THE RANGE FOR ERRORS
        DEPTID_EMPTY = empty('deptid',row)

        deptid_errors = DEPTIDFROM__ or not DEPTIDFROM_ALPHA or DEPTIDFROM_IS_NA or DEPTIDTO_IS_NA or not DEPTIDTO_ALPHA or DEPTIDTO__ or DEPTID_LEN or DEPTID_EMPTY
        flag_for_row6 = not DEPTIDTO_IS_NA and DEPTIDTO_ALPHA and not DEPTIDTO__ and not DEPTID_LEN_COND and not DEPTID_EMPTY
        
        if deptid_errors:
            if row[5] == '0' and flag_for_row6: #THE FLAG IS TO MAKE SURE THE CVS THAT HAVE 0 AS THE BEGINNING PART OF THE RANGE DONT HAVE AN ERROR IN THE END PART OF THE RANGE
                lol = 'lol'
            else:
                deptid_doc.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')

    print('All done with CVS with DEPTID errors'+date+'.csv.txt')      
    deptid_doc.close()
    Original.close()

    cleanlist = list_compare(cleandoc)
    counter = 0 
    try:
        ##iterating over every row in the document for the monthss
        for row in cleanlist:
            counter += 1
            DEPTIDFROM__ = row[5].startswith('-')
            DEPTIDFROM_ALPHA = row[5].isnumeric()
            DEPTIDFROM_IS_NA = row[5] is ('NA')
            DEPTIDTO_IS_NA = row[6] is ('NA')
            DEPTIDTO_ALPHA = row[6].isnumeric()
            DEPTIDTO__ = row[6].startswith('-')
            DEPTID_LEN = part_len('deptid',row)
            DEPTID_LEN_COND = part_len('deptiD',row)
            DEPTID_EMPTY = empty('deptid',row)

            deptid_errors = DEPTIDFROM__ or not DEPTIDFROM_ALPHA or DEPTIDFROM_IS_NA or DEPTIDTO_IS_NA or not DEPTIDTO_ALPHA or DEPTIDTO__ or DEPTID_LEN or DEPTID_EMPTY
            flag_for_row6 = not DEPTIDTO_IS_NA and DEPTIDTO_ALPHA and not DEPTIDTO__ and not DEPTID_LEN_COND and not DEPTID_EMPTY
            
            if deptid_errors:
                if row[5] == '0' and flag_for_row6:
                    newclean.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')
                else:
                    lol = 'lol'
            else:
                newclean.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')
    except:
        if row != ['']:
            print(row)
            print('An exception was raised and not because it is an empty line at the end of the text document.')

    #print('''All done with CVS with "w.o MONTHS.FUNDS.DEPTID ERR"''' + date+'.csv.txt')       
    cleandoc.close()
    newclean.close()

    ##PROG ERRORS
    ##opening the file
    Original = open(file)

    hold = list_4_original(Original)
    
    prog_doc = open('J:\FSM\Maria Restrepo\PROGRAMS\\ERRORS\\CVS with PROG errors'+date+'.csv.txt','w')
    #prog_doc.write(''+''+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+'PROGRAM'+'\t'+'PROGRAM'+'\t'+''+'\t'+''+'\t'+''+'\n')

    cleandoc = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS.FUNDS.DEPTID ERR'+date+'.csv.txt')

    newclean = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS.FUNDS.DEPTID.PROG ERR'+date+'.csv.txt','w')
    
    for row in hold:

        #PROGFROM_NUM = row[7].isnumeric()
        PROGFROM__ = row[7].startswith('-')
        PROGTO_Z999 = row[8] is ('Z999')
        PROGTO_ZZZZ = row[8] is ('ZZZZ')
        #PROGTO_ZZZZZ = row[8] is ('ZZZZZ')
        PROGTO_NUM = row[8].isnumeric()
        PROGTO__ = row[8].startswith('-')
        PROG_LEN = part_len('program',row)
        PROG_EMPTY = empty('program',row) 

        prog_errors =  PROGFROM__ or PROGTO_Z999 or PROGTO_ZZZZ or PROGTO__ or PROG_LEN or PROG_EMPTY or PROGTO_NUM
        #PROGFROM_NUM or PROGTO_ZZZZZ
        if prog_errors:
            prog_doc.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')

    print("All done with CVS with PROG errors" + date+ ".csv.txt")      
    prog_doc.close()
    Original.close()

    cleanlist = list_compare(cleandoc)
    try:
        for row in cleanlist:
            #PROGFROM_NUM = row[7].isnumeric()
            PROGFROM__ = row[7].startswith('-')
            PROGTO_Z999 = row[8] is ('Z999')
            PROGTO_ZZZZ = row[8] is ('ZZZZ')
            #PROGTO_ZZZZZ = row[8] is ('ZZZZZ')
            #PROGTO_NUM = row[8].isnumeric()
            PROGTO__ = row[8].startswith('-')
            PROG_LEN = part_len('program',row)
            PROG_EMPTY = empty('program',row) 

            prog_errors = PROGFROM__ or PROGTO_Z999 or PROGTO_ZZZZ or PROGTO__ or PROG_LEN or PROG_EMPTY
            #PROGFROM_NUM or  PROGTO_NUM or PROGTO_ZZZZZ      
            if prog_errors:
                lol = 'lol' 
            else:
                newclean.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')
    except:
        if row != ['']:
            print('An exception was raised and not because it is an empty line at the end of the text document.')
      
    #print('''All done with CVS with "w.o MONTHS.FUNDS.DEPTID.PROG ERR"''' + date+'.csv.txt')       
    cleandoc.close()
    newclean.close()
  
    ##PROJ ERRORS
    ##opening the file
    Original = open(file)

    hold = list_4_original(Original)
    
    proj_doc = open('J:\FSM\Maria Restrepo\PROGRAMS\\ERRORS\\CVS with PROJ errors'+date+'.csv.txt','w')
    #proj_doc.write(''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+'PROJECT'+'\t'+'PROJECT'+'\t'+''+'\n')

    cleandoc = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS.FUNDS.DEPTID.PROG ERR'+date+'.csv.txt')

    newclean = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS.FUNDS.DEPTID.PROG.PROJ ERR'+date+'.csv.txt','w')
    
    for row in hold:

        PROJFROM__ = row[9].startswith('-')
        PROJFROM_A00000 = row[9] is ('A00000')
        PROJTO_99999 = row[10] is ('99999')
        PROJTO_Z999 = row[10] is ('Z999')
        PROJTO__ = row[10].startswith('-')
        PROJ_LEN = part_len('project',row)
        PROJ_EMPTY = empty('project',row) 

        proj_errors = PROJFROM__  or PROJFROM_A00000 or PROJTO_99999 or PROJTO_Z999 or PROJTO__ or PROJ_LEN or PROJ_EMPTY 
    
        if proj_errors:
            proj_doc.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')

    
    print("All done with CVS with PROJ errors"+ date+ ".csv.txt")      
    proj_doc.close()
    Original.close()

    cleanlist = list_compare(cleandoc)
    try:
        for row in cleanlist:

            PROJFROM__ = row[9].startswith('-')
            PROJFROM_A00000 = row[9] is ('A00000')
            PROJTO_99999 = row[10] is ('99999')
            PROJTO_Z999 = row[10] is ('Z999')
            PROJTO__ = row[10].startswith('-')
            PROJ_LEN = part_len('project',row)
            PROJ_EMPTY = empty('project',row) 

            proj_errors = PROJFROM__ or PROJFROM_A00000 or PROJTO_99999 or PROJTO_Z999 or PROJTO__ or PROJ_LEN or PROJ_EMPTY 
        
            if proj_errors:
                lol = 'lol'
            else:
                newclean.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')

    except:
       if row != ['']:
           print('An exception was raised and not because it is an empty line at the end of the text document.')
    
    #print('''All done with CVS with "w.o MONTHS.FUNDS.DEPTID.PROG.PROJ ERR"''' + date+'.csv.txt')       
    cleandoc.close()
    newclean.close()
  
    ##ACC ERRORS
    ##opening the file
    Original = open(file)

    hold = list_4_original(Original)
    
    acc_doc = open('J:\FSM\Maria Restrepo\PROGRAMS\\ERRORS\\CVS with ACC errors'+date+'.csv.txt','w')
    #acc_doc.write(''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+'ACCOUNT'+'\t'+'ACCOUNT'+'\n')

    cleandoc = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean w.o MONTHS.FUNDS.DEPTID.PROG.PROJ ERR'+date+'.csv.txt')

    newclean = open('J:\FSM\Maria Restrepo\PROGRAMS\\CLEAN\\CVS clean USE THIS ONE'+date+'.csv.txt','w')
    #CVS clean w.o MONTHS.FUNDS.DEPTID.PROG.PROJ.ACC ERR

    for row in hold:

        ACCFROM__ = row[11].startswith('-')
        ACCFROM_ALPHA = row[11].isnumeric()
        ACCFROM_A0000 = row[11].startswith('A0000')
        ACCFROM_00000_dash = row[11].startswith("00000'")
        ACCTO_Z999 = row[11] is ('Z999')
        ACCTO_Z9999 = row[11].startswith('Z9999')
        ACCTO_ZZZZZ = row[11].startswith('ZZZZZ')
        ACCTO__ = row[12].startswith('-')
        ACCTO_ALPHA = row[12].isnumeric()
        ACC_LEN = part_len('account',row)
        ACC_LEN_COND = part_len('accounT',row)
        ACC_EMPTY = empty('account',row) 

        acc_errors = ACCFROM__ or not ACCFROM_ALPHA or ACCFROM_A0000 or ACCFROM_00000_dash or ACCTO_Z999  or ACCTO_Z9999 or ACCTO_ZZZZZ or ACCTO__ or not ACCTO_ALPHA or ACC_LEN or ACC_EMPTY
        flag_for_row12 = not ACCTO__ and ACCTO_ALPHA and not ACC_LEN_COND and not ACC_EMPTY

        if acc_errors:
            if row[11] == '0' and flag_for_row12:
                lol = 'lol'
            else:
                acc_doc.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')

    print("All done with CVS with ACC errors"+date+'.csv.txt')      
    acc_doc.close()
    Original.close()

    cleanlist = list_compare(cleandoc)

    try:
        for row in cleanlist:

            ACCFROM__ = row[11].startswith('-')
            ACCFROM_ALPHA = row[11].isnumeric()
            ACCFROM_A0000 = row[11].startswith('A0000')
            ACCFROM_00000_dash = row[11].startswith("00000'")
            ACCTO_Z999 = row[11] is ('Z999')
            ACCTO_Z9999 = row[11].startswith('Z9999')
            ACCTO_ZZZZZ = row[11].startswith('ZZZZZ')
            ACCTO__ = row[12].startswith('-')
            ACCTO_ALPHA = row[12].isnumeric()
            ACC_LEN = part_len('account',row)
            ACC_LEN_COND = part_len('accounT',row)
            ACC_EMPTY = empty('account',row) 

            acc_errors = ACCFROM__ or not ACCFROM_ALPHA or ACCFROM_A0000 or ACCFROM_00000_dash or ACCTO_Z999  or ACCTO_Z9999 or ACCTO_ZZZZZ or ACCTO__ or not ACCTO_ALPHA or ACC_LEN or ACC_EMPTY
            flag_for_row12 = not ACCTO__ and ACCTO_ALPHA and not ACC_LEN_COND and not ACC_EMPTY

        
            if acc_errors:
                if row[11] == '0' and flag_for_row12:
                    newclean.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')
                else:
                    lol = 'lol'
            else:
                newclean.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\t'+row[4]+'\t'+row[5]+'\t'+row[6]+'\t'+row[7]+'\t'+row[8]+'\t'+row[9]+'\t'+row[10]+'\t'+row[11]+'\t'+row[12]+'\n')
    except:
       if row != ['']:
           print('An exception was raised and not because it is an empty line at the end of the text document.')
                 
    print('''All done with CVS with "USE THIS ONE"''' + date+'.csv.txt')       
    cleandoc.close()
    newclean.close()
    print('All done!')
find_errors()


'''
###ANALYSIS WITH LETTERS A -E

##opening the file
Original = open('Chartfield analysis3-28-18 - Copy.csv')

##reading the data
csvdoc = csv.reader(Original)

#creating new file for NETDs with letter A-E
A_Edoc = open('Chartfield analysis with A-E.csv','w')

for row in csvdoc:
    ##iterating over every row in the document for letter A - letter E
    
    #variable for isolating the NETIDS with the letter A-E
    beg_with_A = row[2].startswith('A')
    beg_with_B = row[2].startswith('B')
    beg_with_C = row[2].startswith('C')
    beg_with_D = row[2].startswith('D') 
    beg_with_E = row[2].startswith('E')

    #variable for isolating the NETIDS with months
    NETID_IS_JAN = row[2].startswith('Jan')
    NETID_IS_FEB = row[2].startswith('Feb')
    NETID_IS_MAR = row[2].startswith('Mar')
    NETID_IS_APR = row[2].startswith('Apr')
    NETID_IS_MAY = row[2].startswith('May')
    NETID_IS_JUN = row[2].startswith('Jun')
    NETID_IS_JUL = row[2].startswith('Jul')
    NETID_IS_AUG = row[2].startswith('Aug')
    NETID_IS_SEP = row[2].startswith('Sep')
    NETID_IS_OCT = row[2].startswith('Oct')
    NETID_IS_NOV = row[2].startswith('Nov')
    NETID_IS_DEC = row[2].startswith('Dec')

    month_identification = NETID_IS_JAN or NETID_IS_FEB or NETID_IS_MAR or NETID_IS_APR or NETID_IS_MAY or NETID_IS_JUN or NETID_IS_JUL or NETID_IS_AUG or NETID_IS_SEP or NETID_IS_OCT or NETID_IS_NOV or NETID_IS_DEC
    

    if (beg_with_A or beg_with_B or beg_with_C or beg_with_D or beg_with_E):

        if month_identification:
           continue

        if row[4] == 'XX' or row[4] == 'ZZ':
            row[4] = '99'

        if row[6] == 'ZZZZZ':
            row[6] = 'Z9999'
            
        if row[8] == 'ZZZZZ':
            row[8] = 'Z9999'

        if row[10] == 'ZZZZZ':
            row[10] = 'Z9999'


        A_Edoc.write(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+row[7]+','+row[8]+','+row[9]+','+row[10]+','+row[11]+','+row[12]+'\n') 
        

print("All done with Chartfield analysis with A-E.csv.")
A_Edoc.close()
Original.close()


###ANALYSIS WITH LETTERS F -L

##opening the file
Original = open('Chartfield analysis3-28-18 - Copy.csv')

##reading the data
csvdoc = csv.reader(Original)

#creating new file for NETDs with letter F-L
F_Ldoc = open('Chartfield analysis with F-L.csv','w')

for row in csvdoc:
    ##iterating over every row in the document for letter F - letter L
    
    #variable for isolating the NETIDS with the letter F-L
    beg_with_F = row[2].startswith('F')
    beg_with_G = row[2].startswith('G')
    beg_with_H = row[2].startswith('H')
    beg_with_I = row[2].startswith('I') 
    beg_with_J = row[2].startswith('J')
    beg_with_K = row[2].startswith('K')
    beg_with_L = row[2].startswith('L')

    #variable for isolating the NETIDS with months
    NETID_IS_JAN = row[2].startswith('Jan')
    NETID_IS_FEB = row[2].startswith('Feb')
    NETID_IS_MAR = row[2].startswith('Mar')
    NETID_IS_APR = row[2].startswith('Apr')
    NETID_IS_MAY = row[2].startswith('May')
    NETID_IS_JUN = row[2].startswith('Jun')
    NETID_IS_JUL = row[2].startswith('Jul')
    NETID_IS_AUG = row[2].startswith('Aug')
    NETID_IS_SEP = row[2].startswith('Sep')
    NETID_IS_OCT = row[2].startswith('Oct')
    NETID_IS_NOV = row[2].startswith('Nov')
    NETID_IS_DEC = row[2].startswith('Dec')

    month_identification = NETID_IS_JAN or NETID_IS_FEB or NETID_IS_MAR or NETID_IS_APR or NETID_IS_MAY or NETID_IS_JUN or NETID_IS_JUL or NETID_IS_AUG or NETID_IS_SEP or NETID_IS_OCT or NETID_IS_NOV or NETID_IS_DEC
    

    if (beg_with_F or beg_with_G or beg_with_H or beg_with_I or beg_with_J or beg_with_K or beg_with_L):

        if month_identification:
           continue

        if row[4] == 'XX' or row[4] == 'ZZ':
            row[4] = '99'

        F_Ldoc.write(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+row[7]+','+row[8]+','+row[9]+','+row[10]+','+row[11]+','+row[12]+'\n') 
        

print("All done with Chartfield analysis with F-L.csv.")
F_Ldoc.close()
Original.close()


###ANALYSIS WITH LETTERS M -S

##opening the file
Original = open('Chartfield analysis3-28-18 - Copy.csv')

##reading the data
csvdoc = csv.reader(Original)

#creating new file for NETDs with letter M-S
M_Sdoc = open('Chartfield analysis with M-S.csv','w')

for row in csvdoc:
    ##iterating over every row in the document for letter M - letter S
    
    #variable for isolating the NETIDS with the letter M-S
    beg_with_M = row[2].startswith('M')
    beg_with_N = row[2].startswith('N')
    beg_with_O = row[2].startswith('O')
    beg_with_P = row[2].startswith('P') 
    beg_with_Q = row[2].startswith('Q')
    beg_with_R = row[2].startswith('R')
    beg_with_S = row[2].startswith('S')

    #variable for isolating the NETIDS with months
    NETID_IS_JAN = row[2].startswith('Jan')
    NETID_IS_FEB = row[2].startswith('Feb')
    NETID_IS_MAR = row[2].startswith('Mar')
    NETID_IS_APR = row[2].startswith('Apr')
    NETID_IS_MAY = row[2].startswith('May')
    NETID_IS_JUN = row[2].startswith('Jun')
    NETID_IS_JUL = row[2].startswith('Jul')
    NETID_IS_AUG = row[2].startswith('Aug')
    NETID_IS_SEP = row[2].startswith('Sep')
    NETID_IS_OCT = row[2].startswith('Oct')
    NETID_IS_NOV = row[2].startswith('Nov')
    NETID_IS_DEC = row[2].startswith('Dec')

    month_identification = NETID_IS_JAN or NETID_IS_FEB or NETID_IS_MAR or NETID_IS_APR or NETID_IS_MAY or NETID_IS_JUN or NETID_IS_JUL or NETID_IS_AUG or NETID_IS_SEP or NETID_IS_OCT or NETID_IS_NOV or NETID_IS_DEC
    

    if (beg_with_M or beg_with_N or beg_with_O or beg_with_P or beg_with_Q or beg_with_R or beg_with_S):

        if month_identification:
           continue
        if row[4] == 'XX' or row[4] == 'ZZ':
            row[4] = '99'

        M_Sdoc.write(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+row[7]+','+row[8]+','+row[9]+','+row[10]+','+row[11]+','+row[12]+'\n') 
        

print("All done with Chartfield analysis with M-S.csv.")
M_Sdoc.close()
Original.close()


###ANALYSIS WITH LETTERS T -Z

##opening the file
Original = open('Chartfield analysis3-28-18 - Copy.csv')

##reading the data
csvdoc = csv.reader(Original)

#creating new file for NETDs with letter T-Z
T_Zdoc = open('Chartfield analysis with T-Z.csv','w')

for row in csvdoc:
    ##iterating over every row in the document for letter T - letter Z
    
    #variable for isolating the NETIDS with the letter T-Z
    beg_with_T = row[2].startswith('T')
    beg_with_U = row[2].startswith('U')
    beg_with_V = row[2].startswith('V')
    beg_with_W = row[2].startswith('W') 
    beg_with_X = row[2].startswith('X')
    beg_with_Y = row[2].startswith('Y')
    beg_with_Z = row[2].startswith('Z')

    #variable for isolating the NETIDS with months
    NETID_IS_JAN = row[2].startswith('Jan')
    NETID_IS_FEB = row[2].startswith('Feb')
    NETID_IS_MAR = row[2].startswith('Mar')
    NETID_IS_APR = row[2].startswith('Apr')
    NETID_IS_MAY = row[2].startswith('May')
    NETID_IS_JUN = row[2].startswith('Jun')
    NETID_IS_JUL = row[2].startswith('Jul')
    NETID_IS_AUG = row[2].startswith('Aug')
    NETID_IS_SEP = row[2].startswith('Sep')
    NETID_IS_OCT = row[2].startswith('Oct')
    NETID_IS_NOV = row[2].startswith('Nov')
    NETID_IS_DEC = row[2].startswith('Dec')

    month_identification = NETID_IS_JAN or NETID_IS_FEB or NETID_IS_MAR or NETID_IS_APR or NETID_IS_MAY or NETID_IS_JUN or NETID_IS_JUL or NETID_IS_AUG or NETID_IS_SEP or NETID_IS_OCT or NETID_IS_NOV or NETID_IS_DEC
    

    if (beg_with_T or beg_with_U or beg_with_V or beg_with_W or beg_with_X or beg_with_Y or beg_with_Z):

        if month_identification:
           continue
        if row[4] == 'XX' or row[4] == 'ZZ':
            row[4] = '99'

        T_Zdoc.write(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+row[7]+','+row[8]+','+row[9]+','+row[10]+','+row[11]+','+row[12]+'\n') 
        

print("All done with Chartfield analysis with T-Z.csv.")
T_Zdoc.close()
Original.close()
'''
