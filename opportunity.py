import uuid
import datetime
from database import Database

class Opportunities(object):
    def __init__(self, creator, title, description, creator_id, _id=None):
        self.creator = creator
        self.creator_id = creator_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='opportunities',
                        data=self.json())
    
    def remove_from_mongo(self):
        Database.delete(collection='opportunities',
                        data=self.json())

    def json(self):
        return {
            'creator': self.creator,
            'creator_id': self.creator_id,
            'title': self.title,
            'description': self.description,
            '_id': self._id
        }

    @classmethod
    def from_mongo(cls, id):
        opportunities_data = Database.find_one(collection='opportunities',
                                      query={'_id': id})
        return cls(**opportunities_data)

    @classmethod
    def find_by_creator_id(cls, creator_id):
        opportunities = Database.find(collection='opportunities',
                              query={'creator_id': creator_id})
        return [cls(**opportunity) for opportunity in opportunities]


