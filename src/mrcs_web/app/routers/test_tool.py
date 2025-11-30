"""
Created on 27 Nov 2025

@author: Bruno Beloff (bbeloff@me.com)

Test tool (TST) API

https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure
"""

from fastapi import APIRouter

from mrcs_core.messaging.message import Message
from mrcs_core.messaging.mqclient import Publisher
from mrcs_core.sys.environment import Environment
from mrcs_core.sys.logging import Logging


# --------------------------------------------------------------------------------------------------------------------

env = Environment.get()

Logging.config(env.log_name, level=env.log_level)
logger = Logging.getLogger()

logger.info(f'test_tool: {env}')

router = APIRouter()

publisher = Publisher.construct_pub(env.ops_mode.value.mq_mode)
publisher.connect()


# --------------------------------------------------------------------------------------------------------------------

@router.post("/tst/publish", tags=["messages"])
async def publish(message: Message):
    logger.info(f'publish:{message}')
    # TODO: implement publish(..)

    return None

