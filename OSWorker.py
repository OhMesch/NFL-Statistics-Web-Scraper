import os

class OSWorker:
	#Should be using os.getpath...?
	#If it is all static how will I pass in logger object
	#If it is nonstatic, we can give it a reference of where to write
	#Leave static and give CSVWriter access to logger
	#What happens if somebody passes in a full file path?

	def appendToFile(filePath, contentToAdd):
		fullFilePath = OSWorker.getAbsolutePath(filePath)
		file = open(fullFilePath, "a")
		file.write(contentToAdd)
		file.close()

	def createFile(filePath):
		fullFilePath = OSWorker.getAbsolutePath(filePath)
		file = open(fullFilePath,"w+")
		file.close()

	def createFolder(folderPath):
		fullFolderPath = OSWorker.getAbsolutePath(folderPath)
		os.makedirs(fullFolderPath)

	def deleteFile(filePath):
		fullFilePath = OSWorker.getAbsolutePath(filePath)
		os.remove(fullFilePath)

	def deleteFolder(filePath):
		fullFilePath = OSWorker.getAbsolutePath(filePath)
		os.rmdir(fullFilePath)

	def getAbsolutePath(local):
		return(os.path.join(os.getcwd(),local))

	def isExistingPath(path):
		fullFilePath = OSWorker.getAbsolutePath(path)
		return(os.path.exists(fullFilePath))

	def joinPath(basePath, additionPath):
		return(os.path.join(basePath,additionPath))