#Selenium
    find_element(By.ID, "id")
    find_element(By.NAME, "name")
    find_element(By.XPATH, "xpath")
    find_element(By.LINK_TEXT, "link text")
    find_element(By.PARTIAL_LINK_TEXT, "partial link text")
    find_element(By.TAG_NAME, "tag name")
    find_element(By.CLASS_NAME, "class name")
    find_element(By.CSS_SELECTOR, "css selector")



#os
    import os

    os.remove('sample.txt') # removes file from directory if exists. if not exissts then error
    os.rename('oldname.txt','newname.txt')
    os.path.exists('filename.txt') #returns true or false
    os.path.getsize('filename.txt')
    os.path.getmtime('filename.txt')
    os.path.abspath('filename.txt') # returns absolute path of the file
    os.getcwd() #see default path
    os.mkdir('folder') # creates new path
    os.chdir('folder') #change defaul location ex. \\folder\\folder\\
    os.rmdir('folder') #removes folder, if the folder is empty
    os.listdir('documents')
    os.isdir() # true/false if it is folder or not
    os.path.join(dir,name) #valid relative path



#datetime
    import datetime as dt
    x = os.path.getmtime('filename.txt')
    dt.datetime.fromtimestamp(x)



#csv
    import csv
    step1 = open('filename.csv')
    step2 = csv.reader(step1)
    for step3 in step2:
        name, phone, role = row
        print(name,phone,role)


    #create new file
    list  = [['Sarkhan','Xiamoi'],['Jafar','Iphone']]
    with open ('excel.csv','w') as file:
        y = csv.writer(file)
        y.writerows(list)


    #if multiple columns exists and you need only some of them
    with open('excel.csv', 'w') as file:
        reader = csv.DictReader(file)
        for x in reader:
            print(('{} has {} users'),format(row['NAME'],row['CIF']))


    with open('comments.csv') as software:
        reader = csv.DictReader(software)
        for row in reader:
            print(('{} has {} users').format(row['name'],row['users']));


    users = [{'name':'Sarxan','surname':'Shirinov','fathername':'Firidun'}]
    keys = ['name','surname','fathername']
    with open('comments.csv','w') as file:
        writer = csv.DictWriter(file, fieldnames = keys)
        writer.writeheader()
        writer.wrtierows(users)



#Pandas
pd.read_csv('path', sep|delimeter = ',', header = None | 0, usecols = all | ['Col1','Col2'] , index_col = None | 0, names = ['CIF','FIN','Full_Name'])
df.to_csv('path', index = True|False, header = True|False | 0, sep|delimeter = ',',  usecols = all | ['Col1','Col2'] , index_col = None | 0, names = ['CIF','FIN','Full_Name'])

