---
layout: page
title: About 
snake: rainbow
permalink: /about/
sponsors: true


team: 
    - name: Katie McLaughlin
      thumbnailUrl: katie-mclaughlin.png
      twitter: glasnt 
      track: general
      title: Site Chair
    - name: Katie Bell
      thumbnailUrl: katie-bell.png
      twitter: notsolonecoder
      track: security
      title: Site Co-Chair
    - name: Lilly Ryan
      thumbnailUrl: lilly-ryan.png
      twitter: attacus_au
      track: django
      title: Papers Chair
    - name: Russell Keith-Magee
      thumbnailUrl: russell-keithmagee.png
      twitter: freakboy3742
      track: education
      title: Treasurer
    - name: Jack Skinner
      thumbnailUrl: jack-skinner.png
      twitter: developerjack
      track: iot
      title: Operations

---

## Important Information

PyCon AU 2018 will be held in Sydney, Australia, at the [International Convention Center, Sydney](https://www.iccsydney.com.au)

- August 24: Specialist Tracks
- August 25-26: Conference Main Track 
- August 27-28: Development Sprints

## Specialist Tracks

The first day of PyCon AU is dedicated to specialist tracks. These tracks, also known as 'mini-confs', are curated
by smaller specialist groups within Python community, and allow for more in-depth talks on the subject. 

In 2018, these tracks will be: [Django](/djangoconau), [Security and Privacy](/security-and-privacy), [Education](/education), and [Internet of Things](/internet-of-things).

## Conference Main Track

The weekend of PyCon AU, traditionally the Saturday and Sunday, is the main conference event. We invite speakers from all backgrounds and levels of knowledge to share their experience and knowledge with our audience. 

Our full schedule of talks for 2018 has been released for [Saturday](/schedule/saturday) and [Sunday](/schedule/sunday)

## Development Sprints

Following three days of talks, we hold space in our venue for two days of Development Sprints (sometimes shortened just to 'Sprints')

Since you've travelled all the way to Sydney for a Python event, why not stay an extra day or two and stretch your legs in the new things you've learnt, or dive into some interesting projects you've heard about over the weekend?

Development Sprints provide an unstructured location for projects and contributors to work in real time on their projects, or for people to hack about with various things with people with experts in their fields. 

The sprints are uncatered, but the conference will provide copious amounts of table space, power, and internet connectivity. 

Tickets to the sprints can be purchased [on top of the normal event tickets](/attend/ticket-tiers)

## About PyCon Australia

PyCon Australia ("PyCon AU") is the national conference for the Python
Programming Community, bringing together professional, student and enthusiast developers
with a love for developing with Python.

PyCon Australia informs the country’s Python developers with presentations,
tutorials and panel sessions by experts and core developers of Python, as well
as the libraries and frameworks that they rely on.

PyCon Australia is held in two year blocks at the same city.

- 2010, 2011: Sydney, NSW
- 2012, 2013: Hobart, TAS
- 2014, 2015: Brisbane, QLD
- 2016, 2017: Melbourne, VIC
- 2018, 2019: Sydney, NSW

Videos from previous years can be downloaded from the [Linux Australia mirror site](http://mirror.linux.org.au/pycon-au/) or the [PyConAU YouTube channel](https://www.youtube.com/user/PyConAU/playlists)


## Lead Organising Team

<div class="row">
<div class="offset-lg-1"></div>
{%- for speaker in page.team -%}
  <div class="col-12 col-lg-2">
    <img class="rounded-circle speaker-picture border-{{speaker.track}} mx-auto" style="max-height: 166px"  alt="{{speaker.name}}" src="{{ site.baseurl | append: '/static/img/people/' | append: speaker.thumbnailUrl }}">
    <p align="center" style="margin-bottom: -10px"><span class="speaker_name" style="white-space: nowrap">{{ speaker.name }}</span>
    <br>{{speaker.title}}
    <br><a href="https://twitter.com/{{ speaker.twitter}}">@{{speaker.twitter}}</a>
    </p>
  </div>
{%- endfor -%}
</div>

