import os
#path = "/users/user/Desktop/cluster_files"
#path = raw_input("Enter path of the directory containing clusters:\n")
path = '/home/anurag/Downloads/cluster_files'
os.chdir(path)
temp = os.listdir(os.getcwd())
head = raw_input("Enter head of the hashtag:\n")
head = head.lower()
clusters = []
flag = False
for i in temp:
    clusters.append(i[:-4])
#print clusters
for i in clusters:
    i = i.lower()
    i = i[1:-1]  
    if head == i:
        flag = True
        print "Match found!"
listdir = []
'''if flag == False:
    for i in clusters:
        temp = i
        (x, y) = (temp, [])
        f = open(path+"/" + temp + '.txt', 'rU')
        for line in f:   
            y.append(line[1:-2])    
        y = ' '.join(y)
        f.close()
        listdir.append((x, y))'''

for i in clusters:
        temp = i
        (x, y) = (temp, [])
        f = open(path+"/" + temp + '.txt', 'rU')
        for line in f:   
            y.append(line[1:-2])    
        y = ' '.join(y)
        f.close()
        listdir.append((x, y))

hashtag = raw_input("Enter segmented hashtag: \n")
temp = hashtag.split()
nearness = []
for i in listdir:
 #   print i
    count = 0
    (x, y) = i
    title = x
    for j in temp:
        count =count + y.count(j)
    #print "count" + str(count)
    y = y.split()
    length = len(y)
    #print "length" + str(length)
    coeff = count/float(length)
    nearness.append((coeff, title))
    #print "coeff" + str(coeff)
b = sorted(nearness)
#print b
print b[-4:]
   
        
  
     
    
