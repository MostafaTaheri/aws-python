from typing import List, Dict, AnyStr

import pymongo

from config import LoadConfig
from modules import *
from .consts.user_prefix_const import UserPrefixConst


class UserPrefix:
    """Detects users and prefixes from mongoDB and validate that.

    Example:
        user_prefix = UserPrefix()
        response = user_prefix.user_prefix_validation(
            username='A', prefix='arvan12'
        )
    """
    def __init__(self) -> None:
        """Initialize the variables."""
        self.consts = UserPrefixConst()
        self.config = LoadConfig()
        self.logging = Logging()
        self.myclient = pymongo.MongoClient(self.config.mogo_db_info())
        self.mydb = self.myclient[self.config.mogo_db_name()]

    def _find_user(self, name: AnyStr) -> List:
        """Finds user information.

        Returns:
            A list of result query.
        """
        try:
            self.mycollection = self.mydb[self.consts.collection_name.get(
                "users")]
            return [
                x for x in self.mycollection.find({
                    "name": name
                }, {
                    "id": 1
                }).limit(1)
            ]
        except Exception as Ex:
            self.logging.error(Ex)
            error = CustomException(self.consts.exception_status,
                                    self.consts.exception_message)
            return Tools.packer(status=error.fault_code,
                                message=error.fault_message)

    def _find_prefix(self, prefix: AnyStr) -> List:
        """Finds prefix information.

        Returns:
            A list of result query.
        """
        try:
            self.mycollection = self.mydb[self.consts.collection_name.get(
                "prefixes")]
            return [
                x for x in self.mycollection.find({
                    "prefix": prefix
                }, {
                    "id": 1
                }).limit(1)
            ]
        except Exception as Ex:
            self.logging.error(Ex)
            error = CustomException(self.consts.exception_status,
                                    self.consts.exception_message)
            return Tools.packer(status=error.fault_code,
                                message=error.fault_message)

    def _find_user_prefix(self, query: Dict) -> List:
        """Finds user_prefix information.

        Returns:
            A list of result query.
        """
        try:
            self.mycollection = self.mydb[self.consts.collection_name.get(
                "user_prefixes")]
            return [
                x for x in self.mycollection.find(query, {
                    "user_id": 1,
                    "prefix_id": 1,
                    "is_allowed": 1
                })
            ]
        except Exception as Ex:
            self.logging.error(Ex)
            return [
                CustomException(self.consts.exception_status,
                                self.consts.exception_message)
            ]

    async def user_prefix_validation(self, user_name: AnyStr,
                                     prefix: AnyStr) -> bool:
        """Validates allowed prefix for user.

        Returns:
            True if allowed else False.
        """
        try:
            self.user_id = self._find_user(name=user_name)[0]["id"]
            self.prefix = self._find_prefix(prefix=prefix)
            self.prefix_id = 0

            if not self.prefix and user_name is UserPrefixConst.exception_users[
                    0]:
                return True
            else:
                self.prefix_id = self.prefix[0]["id"]

            self.query = dict({
                '$and': [{
                    'user_id': self.user_id
                }, {
                    'prefix_id': self.prefix_id
                }]
            })

            self.user_prefix = self._find_user_prefix(query=self.query)

            if user_name not in self.consts.exception_users and \
                    self.consts.Exception_prefix in prefix[0:5]:
                return False
            elif self.query is None and user_name is not \
                    self.consts.exception_users[0]:
                return False
            elif list(
                    filter(lambda x: x["is_allowed"] is False,
                           self.user_prefix)):
                return False
            else:
                return True
        except Exception as Ex:
            self.logging.error(Ex)
            return False
