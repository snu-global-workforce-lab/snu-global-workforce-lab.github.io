---
title: "Publications"
permalink: /publications/
author_profile: false
---

<style>
.pub-top{
  display:flex; flex-wrap:wrap; gap:10px; align-items:center;
  margin: 10px 0 16px 0;
}
.pub-btn{
  display:inline-block;
  padding:10px 14px;
  border-radius:12px;
  border:1px solid rgba(128,128,128,0.22);
  background: rgba(128,128,128,0.10);
  text-decoration:none;
  font-weight:800;
}
.pub-btn:hover{ background: rgba(128,128,128,0.16); }

.pub-note{
  opacity:0.85;
  font-size:0.95rem;
  line-height:1.55;
  margin: 8px 0 18px 0;
}

.pub-section{ margin-top:22px; }
.pub-section h2{ margin-bottom:12px; }

.pub-list{ margin:0; padding-left: 18px; }
.pub-item{ margin: 0 0 14px 0; line-height:1.35; }

.pub-title{ font-weight:800; }
.pub-venue{ opacity:0.85; }
.pub-authors{ opacity:0.85; margin-top:3px; }

.pub-links a{
  margin-left:8px;
  font-weight:700;
  text-decoration:none;
}
.pub-links a:hover{ text-decoration:underline; }

.pub-empty{ opacity:0.7; margin: 0 0 10px 0; }
</style>

<div class="pub-top">
  <a class="pub-btn" href="{{ '/files/CV_SuJungChoi.pdf' | relative_url }}" target="_blank" rel="noopener">Download CV (PDF)</a>
  <a class="pub-btn" href="#" target="_blank" rel="noopener">Google Scholar</a>
</div>

{% assign pubs = site.publications | sort: "date" | reverse %}
{% assign journal = pubs | where: "type", "Journal Article" %}
{% assign chapters = pubs | where: "type", "Book Chapter" %}
{% assign reports = pubs | where: "type", "Report" %}
{% assign wps = pubs | where: "type", "Working Paper" %}

{% assign sections = 
  "Journal Articles|journal,Book Chapters|chapters,Reports & Policy Outputs|reports,Working Papers|wps" | split: "," %}

{% for sec in sections %}
  {% assign pair = sec | split: "|" %}
  {% assign label = pair[0] %}
  {% assign key = pair[1] %}

  <div class="pub-section">
    <h2>{{ label }}</h2>

    {% assign list = "" %}
    {% if key == "journal" %}{% assign list = journal %}{% endif %}
    {% if key == "chapters" %}{% assign list = chapters %}{% endif %}
    {% if key == "reports" %}{% assign list = reports %}{% endif %}
    {% if key == "wps" %}{% assign list = wps %}{% endif %}

    {% if list.size == 0 %}
      <p class="pub-empty">No items found.</p>
    {% else %}
      <ol class="pub-list">
      {% for p in list %}
        <li class="pub-item">
          <span class="pub-title">{{ p.title }}</span>
          {% if p.venue %}<span class="pub-venue"> — <em>{{ p.venue }}</em></span>{% endif %}
          {% if p.authors and p.authors != "" %}
            <div class="pub-authors">{{ p.authors }} ({{ p.date | date: "%Y" }})</div>
          {% else %}
            <div class="pub-authors">({{ p.date | date: "%Y" }})</div>
          {% endif %}
          <div class="pub-links">
            <a href="{{ p.url | relative_url }}">Details</a>
            {% if p.paperurl and p.paperurl != "" %}
              <a href="{{ p.paperurl }}" target="_blank" rel="noopener">Link</a>
            {% endif %}
          </div>
        </li>
      {% endfor %}
      </ol>
    {% endif %}
  </div>
{% endfor %}
