#!/usr/bin/python
from bs4 import BeautifulSoup


class parseIndex(object):
    def __init__(self):
        self.soup = BeautifulSoup(open("facebook/index.htm"))

    def printLayout(self):
        print(self.soup.prettify())

    def parseFacebookTable(self):
        allTr = self.soup.table
        for tr in allTr:
            print unicode(tr.th.string) + ":" + unicode(tr.td.string) + '\n',


        
def main():
    p = parseIndex()
    p.parseFacebookTable()

if __name__ == '__main__':
    main()
