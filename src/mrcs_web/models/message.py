"""
Created on 3 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

A structured representation of a message - received via the API
"""

from pydantic import BaseModel

from mrcs_core.messaging.message import Message


# --------------------------------------------------------------------------------------------------------------------

class APIMessage(Message):

    # ----------------------------------------------------------------------------------------------------------------

    class Model(BaseModel):
        routing: str
        body: dict


    # ----------------------------------------------------------------------------------------------------------------


    @classmethod
    def construct_from_model(cls, model: Model):
        return cls.construct_from_jdict(model.model_dump())

