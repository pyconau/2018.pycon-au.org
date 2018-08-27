---
video_url: https://youtu.be/MEba95kL0eo
layout: talk
recordingconsent: true
talkid: 45289
title: Creating Solid APIs
track: django
type: talk

speakers:
- bio: "Rivo Laks is an experienced software developer and systems architect.\r\n\r\n
      Django developer since 2011. Interested in React, Docker and many other technologies surrounding web development.\r\n\r\n
      Ex-Thorgate, currently on sabbatical and looking for new opportunities."
  company: Thorgate
  name: Rivo Laks
  thumbnailUrl: rivo-laks.png
  twitter: rivolaks
  url: https://rivolaks.com/

abstract: 'Increasingly, our apps are used not by humans but by other apps - via their
  APIs. Thus your APIs need to be well-designed and easy to consume for other developers.

  I will share tips and good practices on authentication, versioning, documentation,
  response structure, and why it all matters.'
---
Adding a few API endpoints to your application for internal consumption is easy. Creating APIs that other developers will love to use is a much harder problem.
You'll need to think about solving variety of topics such as response structure, documentation, versioning, authentication, and more. There are existing good practices for each of them, but often developers who haven't done a lot of API work aren't familiar with them.

My talk will show how to find reasonable solutions for those problems, building on top of Django and DRF.
I will talk about JSON API, OAuth2, and other technologies and show how they fit into the puzzle.
Importance of standardized response structure, as well as auto-generated documentation will also be discussed.

I'll talk about good documentation and why it matters a lot more than most developers want to admit.
We'll then look at why a standardized response structure such as JSON API makes lives of 3rd-party developers easier. Next I'll move on to authentication, introducing OAuth2 and discussing when it is a good choice and when not. Finally we'll think about versioning and how you can change your API without breaking all existing apps.
And the talk wouldn't be complete without looking at how those practices are used in the real world APIs.
