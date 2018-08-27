---
video_url: https://youtu.be/nopZ7ydl55k
layout: talk
recordingconsent: true
talkid: 45378
title: Write Perfect* Code First Time, Every Time
track: general
type: talk

speakers:
- bio: "As a child, Ishaan developed an unhealthy obsession with rolling down steep\
    \ roads on his tricycle. Since then, he\u2019s been looking to get adrenaline\
    \ rushes in the world of Python as his tricycle does not fit him anymore. Having\
    \ worked in predictive markets, financial systems, renewable energy and the construction\
    \ industries he\u2019s interested in solving problems people have described as\
    \ being 'strange' and 'cute'.  Ishaan has a bachelors in economics and computer\
    \ science  and a masters in artificial intelligence from the University of New\
    \ South Wales.  He also lectured the Design Computing course at the University\
    \ of New South Wales this year. "
  company: BVN
  name: Ishaan Varshney
  thumbnailUrl: ishaan-varshney.png
  twitter: ishaan_varshney
  url: https://ishaan.xyz

abstract: "Wouldn\u2019t it be nice to know if the line you just wrote actually works?\
  \ In this talk, we look at a Python development environment that is tuned for situations\
  \ where one has to explore a new code base, learn a new framework or is a new-comer\
  \ to the Python language.\n\n*No code is perfect."
---
The traditional method of writing programs has been:
- Write some code
- Execute it
- Print variables out to the console to verify the code is working as expected.
However, Python, being an interpreted language, has the benefit of being able to execute code on the fly. 

Taking advantage of this, we explore a workflow, using Visual Studio Code’s (VScode) Python Extension, to try-before-you-buy each line of code before we write it in a script. That is, one can execute and verify code in VScode's debug console without having to write-run-rewrite. This allows us to explore several options fast! 

This workflow not only cuts debugging time significantly but also provides visibility in libraries lacking comprehensive documentation (as often is the case).

The basic layout of the talk will be:
- Brief comparison of interpreted and dynamic languages
- Walkthrough of what a large percentage of workflows look like. Type code in editor, go to terminal, execute script, observe error, fix error, print variable, see that it’s incorrect, fix logic error, and finally verify again.
- Walkthrough–Visual Studio Code workflow:
    - Everything in one screen 
    - Integration of REPL, editor and debugger into a workflow
    - Ability to execute different code snippets while preserving the session, thus removing the need to re-execute the script.
    - Ability to inspect the attributes and methods of objects especially helpful when dealing with large libraries e.g. scikit-learn.
- Personal stories about how this workflow helped my students and friends solidify certain concepts about the Python language.




