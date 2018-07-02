import os
import time
from datetime import datetime

class Logger:
    def __init__(self):
        self.initTime = datetime.now()
        self.logsFolder = os.path.join(os.getcwd(), 'Logs')
        self.logPath = os.path.join(self.logsFolder,self.initTime.strftime('%m-%d_%H:%M:%S.txt'))

        self.createLogFolderIfDoesntExist()

    def createLogFolderIfDoesntExist(self):
        logsFolder = os.path.join(os.getcwd(), 'Logs')
        if(not os.path.isdir(logsFolder)):
            os.makedirs(logsFolder)

    def getLogPath(self):
        return(self.logPath)

    def printLn(self, logEntry):
        logPath = self.getLogPath()
        linePrefix = self.getLinePrefix()
        logFile = open(logPath, 'a+')
        logFile.write(linePrefix + logEntry+'\n')
        logFile.close()

    def getLinePrefix(self):
        runTime = datetime.now() - self.initTime
        runTimeH = runTime.seconds // 3600
        runTimeM = runTime.seconds // 60
        runTimeS = runTime.seconds % 3600
        return('[%02d:%02d:%02d] ' % (runTimeH, runTimeM, runTimeS))