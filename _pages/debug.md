---
layout: page
title: Debug
snake: grey
permalink: /debug/
---

### Talks

Total Count: {{ site.talks | size }}

*Talks*

{% assign talkcount = 0 %}
{% assign seccount = 0 %}
{% assign djangocount = 0 %}
{% assign educount = 0 %}
{% assign iotcount = 0 %}
{% for session in site.talks %}{% if session.type == "talk" %}
{% assign talkcount = talkcount | plus: 1 %}
{% if session.track == "security" %}{% assign seccount = seccount | plus: 1 %}{% endif %}
{% if session.track == "django" %}{% assign djangocount = djangocount | plus: 1 %}{% endif %}
{% if session.track == "education" %}{% assign educount = educount | plus: 1 %}{% endif %}
{% if session.track == "iot" %}{% assign iotcount = iotcount | plus: 1 %}{% endif %}
{%endif%}{% endfor %}

Total Talks: {{ talkcount }}

Security: {{seccount}}

Django: {{djangocount }}

Education: {{ educount }}

IoT: {{iotcount}}

*Unassigned Talks*

{% assign untalk = 0 %}

{% for session in site.talks %}
    {% assign found = "No" %}
    {% for d in site.data.schedule %}
        {% for t in d.timeslots %}
            {% for s in t.talkIds %}
                {% if s == session.talkid %}{% assign found = "Yes" %}{%endif%}
            {%endfor%}
        {%endfor%}
    {%endfor%}
    {% if found == "No" %}{% assign untalk = untalk | plus: 1 %} {{session.title}}{%endif%}
{%endfor%}

Talks left unassigned: {{untalk}}

*Duplicate talks*


{% assign duptalk-count = 0%}
{%- for session in site.talks -%}
    {%- assign duptalk = 0 -%}
    {%- for d in site.data.schedule -%}
        {% for t in d.timeslots %}
            {% for s in t.talkIds %}
                {% if s == session.talkid %}{% assign duptalk = duptalk | plus: 1 %}{%endif%}
            {%endfor%}
        {%endfor%}
    {%-endfor-%}
    {%- if duptalk > 1 %}{% assign duptalk-count = duptalk-count | plus: 1 %} {{session.title}}, {%- endif-%}
{%-endfor%}

Talks running multiple times: {{duptalk-count}}



*Tracks*

{% for session in site.talks %}{% if session.type == "track" %}
- {{session.talkid | default: 'None' }} --  {{ session.title }}
{%endif%}{% endfor %}

*keynotes*

{% for session in site.talks %}{% if session.type == "keynote" %}
- {{session.talkid | default: 'None' }} --  {{ session.title }}
{%endif%}{% endfor %}

### Sponsors

Count: 
{% for l in site.data.sponsors %}
    {{ l.title }}: {{ l.sponsors | size}}
{% endfor %}

