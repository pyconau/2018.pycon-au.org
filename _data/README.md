### Schedule and Talks

The schedule file contains multiple days

Each day has a number of tracks defined. This is the expected number of rooms that will be defined in the list of talkIds

The talkIds map to a talkid in the `_talks/` folder

This allows us to define talks multiple times (e.g. Lunch, Lightning Talks) and keep talk data away from schedule data (useful for edits of talk information)

Some talk IDs are special. For example: 
    - '404' is an empty slot
    - '403' is a talk continuation (where the talk runs over one slot)

Special talk types: 
    - `service` have two types: long and short. Mostly, they are one id per slot (except in continuations)
    - `keynote` has small display differences

### Sponsors

`link` is the display name. `href` is the URL to display

Place new sponsors in their tier, based on existing content 
