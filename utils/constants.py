from typing import NamedTuple

import string as st
from datetime import datetime

__all__ = (
    'FIRST_JANUARY_1970',
    'ALLOWED_CHARACTERS',
    'EDGE_CHARACTERS_CASES',
    'EDGE_CHARACTERS_TABLE',
    'PUNCTUATIONS_AND_DIGITS',
    'PAD_TABLE',
    'LETTERS_EMOJI',
    'LETTERS_TABLE',
    'EMOJIS_TABLE',
    'NUMBERS_EMOJI',
    'NUMBERS_TABLE',
    'Channels',
    'Categories',
    'StaffRoles',
    'ExtraRoles'
)

FIRST_JANUARY_1970 = datetime(1970, 1, 1, 0, 0, 0, 0)
ALLOWED_CHARACTERS = tuple(st.printable)
EDGE_CHARACTERS_CASES = {
    '@': 'a',
    '0': 'o',
    '1': 'i',
    '$': 's',
    '!': 'i',
    '9': 'g',
    '5': 's',
}
EDGE_CHARACTERS_TABLE = str.maketrans(EDGE_CHARACTERS_CASES)
PUNCTUATIONS_AND_DIGITS = tuple(list(st.punctuation) + list(st.digits))
PAD_TABLE = str.maketrans({k: '' for k in PUNCTUATIONS_AND_DIGITS})

LETTERS_EMOJI = {
    'a': '🇦', 'b': '🇧', 'c': '🇨', 'd': '🇩',
    'e': '🇪', 'f': '🇫', 'g': '🇬', 'h': '🇭',
    'i': '🇮', 'j': '🇯', 'k': '🇰', 'l': '🇱',
    'm': '🇲', 'n': '🇳', 'o': '🇴', 'p': '🇵',
    'q': '🇶', 'r': '🇷', 's': '🇸', 't': '🇹',
    'u': '🇺', 'v': '🇻', 'w': '🇼', 'x': '🇽',
    'y': '🇾', 'z': '🇿'
}
NUMBERS_EMOJI = {
    '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣',
    '4': '4️⃣', '5': '5️⃣', '6': '6️⃣', '7': '7️⃣',
    '8': '8️⃣', '9': '9️⃣'
}
LETTERS_TABLE = str.maketrans(LETTERS_EMOJI)
NUMBERS_TABLE = str.maketrans(NUMBERS_EMOJI)

EMOJIS_TABLE = str.maketrans({v: k for k, v in LETTERS_EMOJI.items()})


class Channels(NamedTuple):
    verify = 1102654728774623365

    tickets = 1102654728774623367
    news = 1102660519736901632
    boosts = 1102654728774623368
    rules = 1102654728774623369
    welcome = 1102654728774623370
    roles = 1102654728774623371
    colours = 1102654729194045450
    intros = 1102654729194045451
    birthdays = 1102654729194045452
    polls = 1102654729194045453
    activity_reports = 1102654729194045454

    general = 1102654729194045456
    venting = 1102654729194045458
    nsfw = 1102654729387004045

    bots = 1102654729387004047
    memes = 1102654729387004049
    anime = 1102654729387004050
    animals = 1102654729387004051
    gaming = 1102654729387004052

    selfies = 1102654729387004054
    artwork = 1102654729626067024
    photos = 1102654729626067025
    videos = 1102654729626067026
    outfit_showcase = 1102654729626067027

    recommendations = 1102654729626067032
    # confessions = 1089494283863736320
    quotes = 1102654729626067033
    self_ad = 1102654729890299984

    no_mic_chat = 1102654729890299986
    music_commands = 1102654729890299987
    music = 1102654729890299988
    lobby_1 = 1102654729890299989
    lobby_2 = 1102654729890299990
    sleep = 1102654729890299991

    staff_chat = 1102654730313945168
    bot_commands = 1102654730313945169

    logs = 1102654730313945171
    messages_logs = 1102654730313945172
    moderation_logs = 1102654730313945173
    github = 1102654730313945174
    discord_news = 1102654730313945175
    discord_safety = 1102654730313945176

    all = (
        tickets, news, boosts, rules, welcome, intros,
        roles, colours, birthdays, general, venting,
        nsfw, bots, memes, anime, animals,
        gaming, selfies, artwork, photos, videos,
        no_mic_chat, music_commands, music,
        lobby_1, lobby_2, sleep, staff_chat, logs,
        messages_logs, moderation_logs, github, bot_commands, verify,
        recommendations, self_ad, polls, activity_reports, outfit_showcase,
        discord_news, discord_safety
    )


class Categories(NamedTuple):
    server = 1102654728774623366
    general = 1102654729194045455
    fun = 1102654729387004046
    media = 1102654729387004053
    extra = 1102654729626067029
    music = 1102654729890299985
    staff = 1102654729890299992
    tickets = 1102654730313945177

    all = (server, general, fun, media, extra, music, staff, tickets)


class StaffRoles(NamedTuple):
    owner = 1102654728774623362
    admin = 1102654728757858383
    moderator = 1102654728757858382

    all = (owner, admin, moderator)


class ExtraRoles(NamedTuple):
    muted = 1102654728757858380
    blocked = 1102654728757858381
    unverified = 1102654728350998546
    bot = 1102654728350998545
    server_booster = 1078313465392943125
    special_booster = 1078368293297066074

    all = (muted, blocked, unverified, bot)
