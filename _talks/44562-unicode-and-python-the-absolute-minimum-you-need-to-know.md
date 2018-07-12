---
layout: talk
recordingconsent: true
talkid: 44562
title: 'Unicode and Python: the absolute minimum you need to know'
track: general
type: talk

speakers:
- bio: "Rapha\xEBl lives in Timor-Leste, where he works for Catalpa, a nonprofit that\
    \ builds software for international development. He currently works on Hamutuk,\
    \ a program that aims to reduce the prevalence of stunting in children under two.\
    \ In past lives, he worked for startups in the US and ate lots of chocolate in\
    \ France. He loves learning languages and dislikes air conditioning."
  company: Catalpa
  name: Raphaël Merx
  thumbnailUrl: raphael-merx.png
  twitter: raphaelmerx
  url: ''

abstract: "Born from parents who don't mind string encoding, my name has an \"\xEB\
  \". How can your code handle that character? How does Unicode handle it? If you\
  \ see \"\\u00EB\" in a stack trace, does that mean your encoding is broken?\n\n\
  Ignoring unicode often backfires. This talk is about preventing Unicode burns."
---
This presentation aims to give the audience a hands on approach to handling unicode. The first 10 minutes are about what unicode and utf-8 are. I'm leaving aside the history of unicode for the sake of brevity. Then we'll give a short overview of how Python handles unicode, and move to best practices and gotchas.

The goal is that by the end of the presentation, the audience feels comfortable with building applications that handle non-ASCII strings. Conceivably there will be some aha moments, where past mysterious errors that the audience ran into are now understandable.
