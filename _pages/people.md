---
title: "People"
permalink: /people/
author_profile: false
---

<style>
.people-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 24px;
  margin: 18px 0 30px 0;
}

.person-card {
  border-radius: 16px;
  padding: 20px;
  text-align: center;
  background: rgba(128,128,128,0.14);
  border: 1px solid rgba(128,128,128,0.28);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}

.person-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.15);
}

.person-card img {
  width: 180px;
  aspect-ratio: 3 / 4;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 14px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}

.person-name {
  margin: 6px 0 2px 0;
  font-size: 1.05rem;
  line-height: 1.25;
}

.person-name-ko {
  display: block;
  margin: 0 0 6px 0;
  font-size: 0.82rem;
  opacity: 0.78;
  line-height: 1.2;
  font-family: "Pretendard", "Noto Sans KR", sans-serif;
  color: inherit;
}

.person-role {
  margin: 0;
  font-size: 0.95rem;
  opacity: 0.82;
  line-height: 1.35;
}

/* --- Alumni (horizontal card) --- */
.alumni-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 12px;
}

@media (max-width: 1100px) {
  .alumni-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 650px) {
  .alumni-grid {
    grid-template-columns: 1fr;
  }
}

.alumni-card {
  border: 1px solid rgba(128,128,128,0.18);
  background: rgba(128,128,128,0.06);
  border-radius: 14px;
  padding: 16px 18px;
  display: flex;
  align-items: center;
  gap: 18px;
  transition: transform 0.16s ease, box-shadow 0.16s ease;
}

.alumni-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.14);
}

.alumni-photo {
  width: 80px;
  height: 100px;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid rgba(128,128,128,0.22);
  background: rgba(128,128,128,0.10);
  flex-shrink: 0;
}

.alumni-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  gap: 2px;
  min-width: 0;
}

.alumni-name {
  font-weight: 800;
  margin: 0;
  font-size: 0.98rem;
  line-height: 1.2;
}

.alumni-name-ko {
  display: block;
  margin: 0 0 4px 0;
  font-size: 0.78rem;
  opacity: 0.76;
  line-height: 1.15;
  font-family: "Pretendard", "Noto Sans KR", sans-serif;
  color: inherit;
}

.alumni-affil {
  margin: 0;
  font-size: 0.70rem;
  opacity: 0.85;
  line-height: 1.25;
  word-break: keep-all;
}

.alumni-affil-ko {
  display: block;
  margin: 2px 0 0 0;
  font-size: 0.70rem;
  opacity: 0.74;
  line-height: 1.2;
  font-family: "Pretendard", "Noto Sans KR", sans-serif;
  color: inherit;
  word-break: keep-all;
}

.alumni-tag {
  margin-top: 8px;
  font-size: 0.80rem;
  opacity: 0.75;
}
</style>

## Current Members

{% for group in site.data.people.current %}
### {{ group.heading }}

<div class="people-grid">
{% for person in group.members %}
  <div class="person-card">
    <img src="{{ person.image | relative_url }}" alt="{{ person.name }}">
    <div class="person-name"><strong>{{ person.name }}</strong></div>
    {% if person.name_ko %}<div class="person-name-ko">{{ person.name_ko }}</div>{% endif %}
    <div class="person-role">{{ person.role }}</div>
  </div>
{% endfor %}
</div>

{% unless forloop.last %}---{% endunless %}

{% endfor %}

## Alumni

<div class="alumni-grid">
{% for person in site.data.people.alumni %}
  <div class="alumni-card">
    <img class="alumni-photo" src="{{ person.image | relative_url }}" alt="{{ person.name }}">
    <div class="alumni-info">
      <div class="alumni-name">{{ person.name }}</div>
      {% if person.name_ko %}<div class="alumni-name-ko">{{ person.name_ko }}</div>{% endif %}
      {% if person.affiliation %}<div class="alumni-affil">{{ person.affiliation }}</div>{% endif %}
      {% if person.affiliation_ko %}<div class="alumni-affil-ko">{{ person.affiliation_ko }}</div>{% endif %}
      {% if person.tag %}<div class="alumni-tag">{{ person.tag }}</div>{% endif %}
    </div>
  </div>
{% endfor %}
</div>
