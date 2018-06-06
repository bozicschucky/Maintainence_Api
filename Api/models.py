from Api import *
class Db:
    def __init__(self):
        con = pg.connect("dbname='posttest' user='postgres' host='localhost'  password='sudo'")