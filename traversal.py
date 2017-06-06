#import os

#def ListDir(path):
#    flist = os.listdir(path)
#    all_file = []
    
#    for fname in flist:
#        file_path = os.path.join(path, fname)

#        if os.path.isdir(file_path):
#            ListDir(file_path)
#        #print(file_path)  
#        all_file.append(file_path)

#    return all_file

#all_files = ListDir('D:\\python\\test_dir')

#print(all_files)

# traversal the given path

def find_last(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)
        if position==-1:
            return last_position
        last_position=position


def IsSpace(string):
    s = ""
    for i in string:
        if i.isspace():
            continue
        s += i
    return s
            
def Replace(string):
    import re
    s = re.findall(r'foreach\s*\(\D+\)', string) # find all strings according to the regex
    if s:
        print(s)

        p = re.split(r'\(', string, 1) #split by '(' and ')', we can get the midddle part of the string
        p[0] = IsSpace(p[0])

        p[1] = p[1].replace(',', ' :')
        
        final = ""

        for index in range(len(p)):
            final += p[index]

        final = final.replace('foreach', 'for (')
        print(final)
        return final
    else:
        return string  

def Traversal(path): 
    import os

    file_absolute_path = []

    for path,d,flist in os.walk(path):
        
        for fname in flist:
            p = os.path.join(path, fname)
            file_absolute_path.append(p)
    print("Total File:", len(file_absolute_path))      
    return file_absolute_path

def ReadFile(path):
    import re    
    fo = open(path, 'r', encoding = 'ANSI')
    
    content = fo.readlines()
    fo.close()
    return content

def WriteFile(path,ls):
    fw = open(path, 'w', encoding = 'ANSI')
    fw.writelines(ls)
    fw.close()

  #  
  #  'E:\\python\\test_dir'

List = []
for i in Traversal('E:\\git_code\\CS_Imaging\\2DViewer\\src'):
    content = ReadFile(i)
    
    for line in content:
        l = Replace(line)
        List.append(l)      
    if List == content:
        List.clear()
        continue
    
    WriteFile(i, List)
    List.clear()
        
    
#print(Traversal('D:\\Python\\test_dir'))
#print(Replace('foreach(f*, h)'))

