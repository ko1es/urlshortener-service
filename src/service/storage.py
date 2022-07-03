from settings.db import db
from settings import CONFIG
from pymongo.collection import Collection
from service.models import Source
from service.types import ShortCode
from typing import Dict
from service.exceptions import ShortCodeNotFound, AlreadyExistsInRepositoryException

class SourceStorage:

    def __init__(self) -> None:
        self._db = db
        self.collection_name = 'shortcodes'
    
    @property
    def collection(self) -> Collection:
        return self._db[self.collection_name]

    def to_service_instance(self, db_instance: Dict) -> Source:
        return Source(**db_instance)
    
    def to_db_instance(self, instance: Source) -> Dict:
        return instance.dict()

    def get_by_code(self, code: ShortCode) -> Source:
        try:
            result = self.collection.find_one({'short_code': code})
        except:
            raise
        if not result:
            raise ShortCodeNotFound()
        return self.to_service_instance(db_instance=result)

    def insert(self, instance: Source) -> ShortCode:
        # try:
        result = self.collection.insert_one(self.to_db_instance(instance))
        return result.inserted_id
        # except DuplicateKeyError:
            # raise AlreadyExistsInRepositoryException()
