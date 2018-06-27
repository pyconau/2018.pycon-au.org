---
layout: talk
type: track
snake: rainbow

talkid: 1001
track: security
title: Security and Privacy Track
permalink: /security-and-privacy-track/
card: security.png

speakers: 
    - name: Eliza Sorensen
      thumbnailUrl: eliza.png
      twitter: zemmiph0bia
      company: Co-founder of Assembly Four
    - name: Chris Watt
      thumbnailUrl: chris.png
      company: Head of Product, Environexus
      twitter: teknetia


abstract: |
    In today's world, digital security and personal privacy are two extremely cruicial and valued aspets of our existance. The Security and Privacy track hopes to share knowledge about both of these concepts, both in sharing information about how to ensure security, and detailing ways we can protect our own privacy. 
---
Talks in this track:

{% for talk in site.talks %}{% if talk.type == "talk" and talk.track == page.track %}* [{{ talk.title }}]({{talk.url}}) {% for speaker in talk.speakers %}{{ speaker.name }}{% endfor %}
{% endif %}{% endfor %}

<hr>
<p align="center">The Security and Privacy Track is seeking a Track Sponsor to help make their event happen.<br>Is that you? <a href="/news/call-for-sponsorship/">Get in touch!</a></p>
