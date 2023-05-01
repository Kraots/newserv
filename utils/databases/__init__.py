from .dbs import (  # noqa
    database1,
    database2,
    database3,
    database4,
    database5,
    database6,
    database7,
    database8,
    database9,
    database10,
    database11,
    database12,
    database13
)


class GetDoc:
    @classmethod
    async def get(cls, id=745298049567424623):
        """|coro|

        This method is a shortcut for ``await .find_one({'_id': id})``
        If the ``id`` isn't given, then it will use the owner's id by default (745298049567424623)
        """

        return await cls.find_one({'_id': id})


from .db_intros import Intro
from .db_rules import Rules
from .db_mutes import Mutes
from .db_levels import Level
from .db_invalid_names import InvalidName
from .db_marriage import Marriage
from .db_tickets import Ticket
from .db_afks import AFK
from .db_game import Game, Characters
from .db_giveaways import GiveAway
from .db_bdays import Birthday
from .db_bad_words import BadWords
from .db_constants import Constants
from .db_reminders import Reminder
from .db_todos import ToDo
from .db_sober import Sober
from .db_bdsm import BDSM
from .db_polls import Poll
from .db_stats import Stats
from .db_warns import Warns
from .db_tags import Tags
from .db_restrictions import Restrictions

__all__ = (
    'Intro',
    'Rules',
    'Mutes',
    'Level',
    'InvalidName',
    'Marriage',
    'Ticket',
    'AFK',
    'Game',
    'Characters',
    'GiveAway',
    'Birthday',
    'BadWords',
    'Constants',
    'Reminder',
    'ToDo',
    'Sober',
    'BDSM',
    'Poll',
    'Stats',
    'Warns',
    'Tags',
    'Restrictions'
)

from .objects import Database  # noqa
