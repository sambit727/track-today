# TO COMPILE UI FILE RUN THIS COMMAND
# python -m PyQt5.uic.pyuic -x filename.ui -o filename-py

# TO CREATE .EXE
# pyinstaller -i logo.ico -n TrackToday -w -F main.py

import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from diaryUI import Ui_MainWindow

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class Entry(Base):
    '''SQLite table for each all diary entries, handled by SQLAlchemy'''
    __tablename__ = 'diary'
    date = Column(String, primary_key=True)
    title = Column(String(1000))
    text = Column(String(4000))


engine = create_engine('sqlite:///diary.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        '''When calendar is clicked, call method checkEntry()'''

        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.startingEntry()
        self.calendarWidget.clicked.connect(self.checkEntry)

    def startingEntry(self):
        current_date = str(self.calendarWidget.selectedDate().toString('dd.MM.yyyy'))
        self.entry = session.query(Entry).filter_by(date=current_date).first()
        if self.entry:
            self.loadTitle()
            self.loadEntry()

    def checkEntry(self):
        '''Search for date in database, if found/not found, load accordingly
        into the textEdit'''

        current_date = str(self.calendarWidget.selectedDate().toString('dd.MM.yyyy'))
        self.entry = session.query(Entry).filter_by(date=current_date).first()

        if self.entry:     # if there is already an entry there
            self.loadTitle()
            self.loadEntry()
        else:              # if there is no entry
            self.entry = Entry(date=current_date)
            self.loadTitle()
            self.loadEntry()
            session.add(self.entry)

        self.textEdit_2.textChanged.connect(self.saveTitle)
        self.textEdit.textChanged.connect(self.saveEntry)


    def loadTitle(self):
        '''Loads the title of the entry'''
        self.textEdit_2.setHtml(self.entry.title)

    def loadEntry(self):
        '''Loads the text of the entry'''
        self.textEdit.setHtml(self.entry.text)

    def saveTitle(self):
        '''Saves the title of the entry'''
        self.entry.title = self.textEdit_2.toHtml()
        session.commit()

    def saveEntry(self):
        '''Saves the text of the entry'''
        self.entry.text = self.textEdit.toHtml()
        session.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Interesting Things')

    m = MainWindow()
    m.show()

    app.exec_()
