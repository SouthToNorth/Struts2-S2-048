import pymongo
from Config import ProductionConfig

db_conn = pymongo.MongoClient(ProductionConfig.DB,ProductionConfig.PORT)
ls_db = db_conn.wangzuxian
ls_Info = ls_db.Info
ls_WSPath = ls_db.WSPath