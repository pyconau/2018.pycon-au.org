---
layout: talk
recordingconsent: true
talkid: 41797
title: Taking Django Async
track: django
type: talk

speakers:
- bio: "Andrew is a member of the Django core team, and has been working with Django\
    \ since 2007, on projects such as South, Django Migrations, and Channels. He works\
    \ at Eventbrite as a Senior Software Engineer.\r\n\r\nWhen he\u2019s not writing\
    \ open source or travelling around the world speaking about it, he enjoys flying\
    \ light aircraft, archery, electronics, and developing games."
  company: ''
  name: Andrew Godwin
  thumbnailUrl: andrew-godwin.png
  twitter: andrewgodwin
  url: http://www.aeracode.org

abstract: We take a look at Django and Channels 2.0 and the changes it brings by going
  fully async - Examining not only why the change makes things better, but also how
  it's managed to bridge between Django's synchronous world and the async world. Plus,
  what might the future hold for Django and Channels?
---
The Channels project has taken a major turn with version 2.0, embracing Python's async functionality and building applications around an async event loop rather than worker processes. But why the big change? And what does it mean for Django?

We'll look at the progress Channels is making in turning more of the request/response cycle into native async code - how far can we get down the stack before making APIs async becomes hard? Can we make it as far as the ORM? How do we bridge between Django's synchronous world and the async world when we do reach that boundary?

We also take a look at how it's changed both Channels consumers, opening up the possibility of mixing async calls in with your synchronous code, and how it's changed what the ASGI spec looks like and what that might mean for adoption.

And, finally, we'll look what's next for Django and Channels, and maybe how it will affect the Python web world as a whole.
