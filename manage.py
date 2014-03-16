import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
	print os.path.abspath(root)
	os.system ("cp /Users/anuj/projects/boardwatch/template/template.md "+os.path.abspath(root)+"/index.md")
	#print startpath+os.path.basename(root)

list_files("./")
