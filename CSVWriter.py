from OSWorker import OSWorker
from TableParser import TableParser

class CSVWriter:
	def __init__(self, folderPath):
		self.PARENT_FOLDER = folderPath

	def writeTableToCSV(self, table):
		tableObj = TableParser(table)
		tableObj.parseTable()
		tableTitle = tableObj.getTableTitle()
		tableString = tableObj.getTableString()

		newFile = self.PARENT_FOLDER+"/"+tableTitle
		print(newFile)
		if OSWorker.isExistingPath(newFile):
			OSWorker.deleteFile(newFile)
		OSWorker.createFile(newFile)
		OSWorker.appendToFile(newFile,tableString)
