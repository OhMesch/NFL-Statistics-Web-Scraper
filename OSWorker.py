import os

class OSWorker:
	#Should be using os.getpath...?
	#If it is all static how will I pass in logger object
	#If it is nonstatic, we can give it a reference of where to write
	#Leave static and give CSVWriter access to logger
	#What happens if somebody passes in a full file path?

	def appendToFile(filePath, contentToAdd):
		fullFilePath = os.path.join(os.getcwd(),filePath)
		file = open(fullFilePath, "a")
		file.write(contentToAdd)
		file.close()

	def createFile(filePath):
		fullFilePath = os.path.join(os.getcwd(),filePath)
		file = open(fullFilePath,"w+")
		file.close()

	def createFolder(folderPath):
		fullFolderPath = os.path.join(os.getcwd(),folderPath)
		os.makedirs(fullFolderPath)

	def deleteFile(filePath):
		fullFilePath = os.path.join(os.getcwd(),filePath)
		os.remove(fullFilePath)

	def deleteFolder(filePath):
		fullFilePath = os.path.join(os.getcwd(),filePath)
		os.rmdir(fullFilePath)

	def isExistingPath(path):
		fullFilePath = os.path.join(os.getcwd(),path)
		return(os.path.exists(fullFilePath))