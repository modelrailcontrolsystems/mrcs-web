"""
Created on 6 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

A structured representation of a user - received via the API
"""

from pydantic import BaseModel

from mrcs_core.admin.user.user import User


# --------------------------------------------------------------------------------------------------------------------

class APIUser(User):

    # ----------------------------------------------------------------------------------------------------------------

    class InsertModel(BaseModel):
        class Config:
            extra = 'allow'

        email: str
        password: str
        role: str
        must_set_password: bool
        given_name: str
        family_name: str


    class UpdateModel(BaseModel):
        class Config:
            extra = 'allow'

        uid: str
        email: str
        role: str
        given_name: str
        family_name: str


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_insert_model(cls, model: InsertModel):
        return cls.construct_from_jdict(model.model_dump())


    @classmethod
    def construct_from_update_model(cls, model: UpdateModel):
        return cls.construct_from_jdict(model.model_dump())
