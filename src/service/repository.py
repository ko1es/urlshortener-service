from settings.db import db
from bson import ObjectId
from bson.errors import InvalidId
from settings import CONFIG
from pymongo.collection import Collection
from service.models import Source
from service.types import ShortCode, SourceId
from typing import Dict
import secrets
from service.exceptions import ShortCodeNotFound, AlreadyExistsInRepositoryException, InvalidParamException


class SourceRepository:

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

    def get_by_code(self, short_code: ShortCode) -> Source:
        try:
            result = self.collection.find_one({'short_code': short_code})
        except InvalidId:
            raise InvalidParamException()
        if not result:
            raise ShortCodeNotFound()
        return self.to_service_instance(db_instance=result)

    def get_by_id(self, identifier: SourceId) -> Source:
        try:
            result = self.collection.find_one({'_id': ObjectId(identifier)})
        except InvalidId:
            raise InvalidParamException()
        if not result:
            raise ShortCodeNotFound()
        return self.to_service_instance(db_instance=result)

    def insert(self, instance: Source) -> SourceId:
        result = self.collection.insert_one(self.to_db_instance(instance))
        return SourceId(result.inserted_id)

    def delete_by_short_code(self, short_code: ShortCode) -> None:
        self.collection.delete_one({'short_code': short_code})
    
    def update_url(self, short_code: ShortCode, url: str) -> None:
        self.collection.update_one(
            {'short_code': short_code}, {'$set':{'origin': url}}
        )
    
    def update_touch_count(self, short_code: ShortCode, touch_count: int) -> None:
        self.collection.update_one(
            {'short_code': short_code}, {'$set':{'touch_count': touch_count}}
        )