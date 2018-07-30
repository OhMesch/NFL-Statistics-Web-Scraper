from OSWorker import OSWorker

class CSVWriter:
	def __init__():
		self.PARENT_FOLDER = "PlayerStats"

	def createNewPlayerFolder(folderName):
		newFolder = self.PARENT_FOLDER + "/" + folderName
		if OSWorker.isExistingPath(newFolder):
			OSWorker.deleteFolder(newFolder)
		OSWorker.createFolder(newFolder)

	def createNewPlayerCSV(self, fileName, contents):
		pass