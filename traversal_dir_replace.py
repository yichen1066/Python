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

def write_log(content):
    fw = open("E:\\python\\modify_log.txt",'a')
    fw.write(content)
    fw.close()

    
def find_last(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)
        if position==-1:
            return last_position
        last_position=position


def IsSpace(string):
    for i in string:
        if i.isspace():
            return True
    return False
            
def Replace(string):
    import re
    s = re.findall(r'\D+foreach\s*\(\D+\)\D+', string) # find all strings according to the regex
    if s:
        print("Find:",len(s))
        print("Original:",s[0])
        
        string = string.replace(',', ' :')
        
        t = re.findall(r'foreach\s*\(', string)

        if IsSpace(t[0]):
            string = string.replace('foreach', 'for')
        else:
            string = string.replace('foreach', 'for ')
        print("Modify  :",string)
        print('~~~~~~~~~~~\n')
    return string  

def Traversal(path): 
    import os

    file_absolute_path = []

    for path,d,flist in os.walk(path):
        
        for fname in flist:
            p = os.path.join(path, fname)
            file_absolute_path.append(p)
            
    print("Total files:", len(file_absolute_path))
    print("Record:\n")
    
    return file_absolute_path

def read_file(path):
    import re    
    fo = open(path, 'r', encoding = 'ANSI')
    
    content = fo.readlines()
    fo.close()
    return content

def write_file(path,ls):
    fw = open(path, 'w', encoding = 'ANSI')
    fw.writelines(ls)
    fw.close()

  #  
  #  'E:\\python\\test_dir'

List = []
modify_file_num = 0

for i in Traversal('E:\\git_code\\CS_Imaging\\2DViewer\\src'):
    content = read_file(i)
    
    for line in content:
        l = Replace(line)
        List.append(l)      
    if List == content:
        List.clear()
        continue
    
    write_file(i, List)
    print("File Name:", i)
    print("-------------------------------------------------------\n")
    
    modify_file_num += 1
    List.clear()
print("Modified Files:",modify_file_num)          

