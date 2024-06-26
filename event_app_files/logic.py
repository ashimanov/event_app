from typing import List

import model, datetime
import db


TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass

class EventLogic:
    def __init__(self):
        self._event_db = db.EventDB()


    @staticmethod
    def _validate_event(event: model.Event):
        if event is None:
            raise LogicException("event is None")
        if event.date is None:
            raise LogicException('event date is None')
        if not datetime.date.fromisoformat(event.date):
            raise LogicException('event date is not in datetime format')
        if event.title is None or len(event.title) > TITLE_LIMIT:
            raise LogicException(f"title length > MAX: {TITLE_LIMIT}")
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text length > MAX: {TEXT_LIMIT}")

    def create(self, event: model.Event) -> str:
        self._validate_event(event)
        if self._event_db._check_duplicate_date(event.date):
            raise LogicException(f"event date already exists!")
        try:
            return self._event_db.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    # def create(self, event: model.Event) -> str:
    #     self._validate_event(event)
    #     for stored_event in self._event_db._storage.values():
    #         if event.date == stored_event.date:
    #             raise LogicException('event date already exists!')
    #     try:
    #         return self._event_db.create(event)
    #     except Exception as ex:
    #         raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Event]:
        try:
            return self._event_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._event_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: model.Event):
        self._validate_event(event)
        try:
            return self._event_db.update(_id, event)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._event_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")
