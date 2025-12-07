"""
Created on 3 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

A structured representation of a message - received via the API
"""

from pydantic import BaseModel

from mrcs_core.messaging.message import Message


# --------------------------------------------------------------------------------------------------------------------

class MessageModel(BaseModel):
    routing: str
    body: dict


# --------------------------------------------------------------------------------------------------------------------

class APIMessage(Message):

    @classmethod
    def construct_from_payload(cls, payload: MessageModel):
        return cls.construct_from_jdict(payload.model_dump())

