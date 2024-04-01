from typing import List

import model
import storage

class DBException(Exception):
    pass

class EventDB:
    def __init__(self):
        self._storage = storage.LocalStorage()
        # self.all_event_dates = storage.LocalStorage()

    # def get_all_events(self):
    #     try:
    #         return self._storage.get_all_events()
    #     except Exception as ex:
    #         raise DBException(f"failed get_all_events operation with: {ex}")

    def _check_duplicate_date(self, date: str) -> bool:
        try:
            return self._check_duplicate_date(date)
        except Exception as ex:
            raise DBException(f"failed to check date duplication")


    def create(self, event: model.Event) -> str:
        try:
            return self._storage.create(event)
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Event]:
        try:
            return self._storage.list()
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._storage.read(_id)
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: model.Event):
        try:
            return self._storage.update(_id, event)
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._storage.delete(_id)
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")

    @property
    def storage(self):
        return self._storage
