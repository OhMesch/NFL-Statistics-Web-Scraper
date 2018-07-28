import os
from Logger import Logger

class OSWorker:
	#Should be using os.getpath...?
	#If it is all static how will I pass in logger object
	#If it is nonstatic, we can give it a reference of where to write
	def appendToFile(filePath, contentToAdd):
		file = open(filePath, "a")
		file.write(contentToAdd)
		file.close()

	def createFile(filePath):
		file = open(filePath,"w+")
		file.close()

	def createFolder(folderPath):
		os.mkdirs(folderPath)

	def deleteFile(filePath):
		os.rmdir(filePath)

	def isExistingPath(path):
		return(os.path.exists(path))