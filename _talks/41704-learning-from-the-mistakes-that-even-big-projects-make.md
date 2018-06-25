---
layout: talk
recordingconsent: true
talkid: 41704
title: Learning from the mistakes that even big projects make
track: security
type: talk

speakers:
- bio: | 
    Michael is a Principal Architect at Aptira where he spends most of his time
    helping telcos understand cloud, network function virtualization, and service
    orchestration. He’s an active OpenStack Compute developer, and has previously
    served as the Compute Project Technical Lead, a Compute and Olso Core Reviewer,
    as well as serving on the OpenStack-wide Technical Committee. Michael has
    previously held a series of development and devops jobs, mostly for large
    American corporations in the “web” space.
  company: Aptira
  name: Michael Still
  thumbnailUrl: michael-still.png
  twitter: mikal
  url: http://www.madebymikal.com

abstract: Since 2011, I've worked on a large Open Source project in python. It kind
  of got out of hand -- 1000s of developers and millions of lines of code. Yet despite
  being well resourced, we made the same mistakes that those tiny scripts you whip
  up to solve a small problem make. Come learn from our fail.
---
This talk will use the privilege separation daemon that the project wrote to tell the story of decisions that were expedient at the time, and how we regretted them later. In a universe in which you can only run commands as root via sudo, dd'ing from one file on the filesystem to another seems almost reasonable. Especially if you ignore that the filenames are defined by the user. Heck, we shell out to "mv" to move files around, even when we don't need escalated permissions to move the file in question.

While we'll focus mainly on the security apparatus because it is the gift that keeps on giving, we'll bump into other examples along the way as well. For example how we had pluggable drivers, but you have to turn them on by passing in python module paths. So what happens when we change the interface the driver is required to implement and you have a third party driver? The answer isn't good. Or how we refused to use existing Open Source code from other projects through a mixture of hubris and licensing religion.

On a strictly technical front, this is a talk about how to do user space privilege separation sensibly. Although we should probably discuss why we also chose in the last six months to not do it as safely as we could.

For a softer technical take, the talk will cover how doing things right was less well documented than doing things the wrong way. Code reviewers didn't know the anti-patterns, which were common in the code base, so made weird assumptions about what was ok or not.

On a human front, this is about herding cats. Developers with external pressures from their various employers, skipping steps because it was expedient, and how throwing automation in front of developers because having a conversation as adults is hard. Ultimately we ended up being close to stalled before we were "saved" from an unexpected direction.

In the end I think we're in a reasonable place now, so I certainly don't intend to give a lecture about doom and gloom. Think of us more as a light hearted object lesson.
