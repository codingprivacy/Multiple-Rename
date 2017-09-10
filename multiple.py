#this is a module which renames multiple files simultaneously.
#It renames the given files with the provided New name or with Giving Numbers
#It can even change the extension

# the syntax is   rename(src,new_name,numbering,extension)
#   if Dont want to specify new_name it can be given null (new_name='')
#   if want to do Numbering then (numbering=1) else by default(numbering=0)
#   if want to give extension then (extension='.jpg') else default is (extension='1') in which the extension dont change
#   if want to give no extension then (extension='0')   Make Sure it is a string


import os
def rename(path,new_name='',numbering=0,extension='1'):   #default arguments
    # print(numbering)
    # print(extension)
    # print(new_name)
    list=os.listdir(path)    #lists all the files in the path
    os.chdir(path)
#These below are the diffrent conditions based on which we rename the files
    try:
        if(new_name!='' and numbering==0 and extension=='0'):

            for i in list:                              #Taking each item of the folder

                f_name,f_ext=os.path.splitext(i)    #spliting of name and extension
                os.rename(i,new_name)               #renaming the file

        if(new_name!='' and numbering!=0 and extension=='0'):
            count=numbering
            for i in list:

                os.rename(i,new_name+str(count))
                count+=1
        if(new_name!='' and numbering!=0 and extension=='1'):
            count=numbering
            for i in list:

                f_name,f_ext=os.path.splitext(i)

                os.rename(i,new_name+str(count)+f_ext)
                count+=1
        if(new_name!='' and numbering==0 and extension=='1'):

            for i in list:
                f_name,f_ext=os.path.splitext(i)
                os.rename(i,new_name+f_ext)
        if(new_name!='' and numbering!=0 and (extension!='1' and extension!='0')):
            count=numbering
            for i in list:

                f_name,f_ext=os.path.splitext(i)
                os.rename(i,new_name+str(count)+extension)
                count+=1
        if(new_name!='' and numbering==0 and (extension!='1' and extension!='0')):

            for i in list:
                f_name,f_ext=os.path.splitext(i)
                os.rename(i,new_name+extension)



        if(new_name=='' and numbering!=0 and extension=='0'):
            count=numbering
            for i in list:

                f_name,f_ext=os.path.splitext(i)
                os.rename(i,f_name+str(count))
                count+=1
        if(new_name=='' and numbering!=0 and extension=='1'):
            count=numbering
            for i in list:

                f_name,f_ext=os.path.splitext(i)
                os.rename(i,f_name+str(count)+f_ext)
                count+=1
        if(new_name=='' and numbering==0 and extension=='1'):

            for i in list:
                f_name,f_ext=os.path.splitext(i)
                os.rename(i,f_name+f_ext)
        if(new_name=='' and numbering==0 and extension==0):

            for i in list:

                f_name,f_ext=os.path.splitext(i)
                os.rename(i,i)
        if(new_name=='' and numbering!=0 and (extension!='1' and extension!='0')):
            count=numbering
            for i in list:

                f_name,f_ext=os.path.splitext(i)
                os.rename(i,f_name+str(count)+extension)
                count+=1
        if(new_name=='' and numbering==0 and (extension!='1' and extension!='0')):

            for i in list:

                f_name,f_ext=os.path.splitext(i)
                os.rename(i,f_name+extension)
    except WindowsError:
        print("Something Went Wrong, Renaming is not Finished.")

#path='C:\Users\Harsh\PycharmProjects\color_detect-using-ML\data\input_data\NOT_RED'
#rename(path,'not_red',1,)
