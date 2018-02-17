# !/usr/local/bin/python3

import os
import json
import tarfile
import glob

cwd = os.getcwd()
print (cwd)
fname2 = ""
# Deleting existing files
for fname2 in os.listdir(cwd):
    if fname2.startswith("sample"):
        os.remove(os.path.join(cwd, fname2))


with open("test.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content] 
contentDir =[]
contentGZ =[]
i=0

print (content)

while content:
    e=content.pop()
#print e
    e1,e2=e.split(":")
	#print e1,e2
    for root, dirs, files in os.walk("/random/universe/repo/packages", topdown=False):
    	for name in files:
    		fname=os.path.join(root, name)
	    	if fname.endswith('package.json'):
	    		data = json.load(open(fname,encoding="utf-8"))
	    		if (e2 == data["version"] and e1 == data["name"]):
	    			contentDir.append(os.path.join(root))

					#for root1,dirs1,files1 in os.walk(root,topdown=False):
					#		print(os.path.join(root1,files1))
					#print(os.listdir(root))
					#with tarfile.open("sample.tar", "w") as tar:
					#for name1 in os.listdir(root):
					#tar.add(os.path.join(root,name))
	          
						

print (contentDir)

for x in contentDir:
	i = i+1
	with tarfile.open("sample_" + str(i) + ".tar.gz","w:gz") as tar:
		for name1 in os.listdir(x):
			tar.add(os.path.join(x,name1))
		tar.close()
	contentGZ.append(os.path.join(cwd,str(i)+"_sample.tar.gz"))	
	

print (contentGZ)

with tarfile.open("sample_packages.tar.gz","w:gz") as tar:
	for name2 in os.listdir(cwd):
		if name2.startswith("sample"):
			tar.add(os.path.join(cwd,name2))
	tar.close()





  		#for name in dirs:
     		#	print(os.path.join(root, name))


