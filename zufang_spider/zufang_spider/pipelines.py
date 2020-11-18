# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
# 1.7版本以下导入settings的方法
# from scrapy.conf import settings
# 1.7版本以上引入settings的方法
from scrapy.utils.project import get_project_settings


class ZufangSpiderPipeline:
    """
    # 存入mongodb
    import pymongo

    collection_name = 'scrapy_items'

    def __init__(self):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client(self.mongo_db)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item

    """
    """
    # 存入mysql
class MysqlPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user 
        self.password = password
        self.port = port
    
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            database = crawler.settings.get('MYSQL_DATABASE'),
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            port = crawler.settings.get('MYSQL_PORT')     
        )
    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port):
        self.cursor = self.db.cursor()
    
    def close_spider(self, spider):
        self.db.close()
    
    def process_item(self, item, spider):
        print(item['title'])
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (itme.table, keys, values)
        self.cursor.excute(sql,tuple(data.values()))
        self.db.commit()
        return item
            
    """
    """
    # 去重
from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()
    
    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found:%s" % item)
        else:
        self.ids_seen.add(item['id'])
        return item
    
    """

    def __init__(self):
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[settings['MONGODB_DOCNAME']]

    # 数据持久化的操作
    def process_item(self, item, spider):
        zufang = dict(item)
        self.post.insert(zufang)
        return item
