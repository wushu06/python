# Ptyhon program to organize contents of directory
import os
import sys
import shutil



# This function organizes contents of sourcePath in to multiple
# directories using the file types provided in extensionToDir
def OrganizeDirectory(sourcePath, extensionToDir):
    if not os.path.exists(sourcePath):
        print ("The source folder '" + sourcePath +
              "' does not exist!!\n")
    else:
        for file in os.listdir(sourcePath):
            file = os.path.join(sourcePath, file)

            # Ignore if its a directory
            if os.path.isdir(file):
                continue

            filename, fileExtension = os.path.splitext(file)
            fileExtension = fileExtension[1:]

            # If the file extension is present in the mapping
            if fileExtension in extensionToDir:

                # Store the corresponding directory name
                destinationName = extensionToDir[fileExtension]
                destinationPath = os.path.join(sourcePath, destinationName)

                # If the directory does not exist
                if not os.path.exists(destinationPath):
                    print ("Creating new directory for `" + fileExtension +
                          "` files, named - `" + destinationName + "'!!")

                    # Create a new directory
                    os.makedirs(destinationPath)

                # Move the file
                try:
                    shutil.move(file, destinationPath)
                except:
                    shutil.move(file, destinationPath+'/'+os.path.basename(file)+'-copy.'+fileExtension)
                    continue
                

def main():
    '''
    if len(sys.argv) != 2:
        print "Usage: <program> <source path directory>"
        return
    '''
    #sourcePath = sys.argv[1]
    sourcePath = os.getcwd()

    extenstions = {
        "svg":"img",
        "png":"img",
        "jpg":"img",
        "jpeg":"img",
        "gif":"img",
        "txt":"text",
        "md":"text",
        "zip":"Zip",
        "gzip":"Zip",
        "html":"Web/html",
        "json":"Web/json",
        "css":"Web/css",
        "php":"Web/php",
        #"py":"Web/py",
        "js":"Web/js",
        "mp4":"Media/videos",
        "mp3":"Media/audios",
        "pdf": "Documents",
        "csv": "Documents",
        "docx": "Documents"
    }

    for ex, folder in extenstions.iteritems() :
        extensionToDir = {}
        extensionToDir[ex]  = folder
        print("")
        OrganizeDirectory(sourcePath, extensionToDir)

if __name__ == "__main__":
        main()
       # print "Press Enter to continue ..." 
       # raw_input() 

