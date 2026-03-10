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
  margin: 0 0 6px 0;
  font-size: 0.83rem;
  opacity: 0.78;
  line-height: 1.2;
}

.person-role {
  margin: 0;
  font-size: 0.95rem;
  opacity: 0.82;
  line-height: 1.35;
}

.person-role-ko {
  margin: 4px 0 0 0;
  font-size: 0.82rem;
  opacity: 0.72;
  line-height: 1.3;
}

/* --- Alumni (vertical, compact) --- */
.alumni-grid{
  display:grid;
  grid-template-columns: repeat(4, 1fr);
  gap:16px;
  margin-top:12px;
}

@media (max-width: 1100px){
  .alumni-grid{ grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 650px){
  .alumni-grid{ grid-template-columns: 1fr; }
}

.alumni-card{
  border:1px solid rgba(128,128,128,0.18);
  background: rgba(128,128,128,0.06);
  border-radius:14px;
  padding:14px 14px 12px 14px;
  display:flex;
  flex-direction:column;
  align-items:center;
  text-align:center;
  min-height: 220px;
  transition: transform 0.16s ease, box-shadow 0.16s ease;
}

.alumni-card:hover{
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.14);
}

.alumni-photo{
  width:60px;
  height:76px;
  object-fit:cover;
  border-radius:8px;
  border:1px solid rgba(128,128,128,0.22);
  background: rgba(128,128,128,0.10);
  margin-bottom:10px;
}

.alumni-name{
  font-weight:800;
  margin:0 0 2px 0;
  font-size:0.92rem;
  line-height:1.15;
}

.alumni-name-ko{
  margin:0 0 6px 0;
  font-size:0.75rem;
  opacity:0.76;
  line-height:1.15;
}

.alumni-affil{
  margin:0;
  font-size:0.82rem;
  opacity:0.85;
  line-height:1.25;
}

.alumni-affil-ko{
  margin:4px 0 0 0;
  font-size:0.74rem;
  opacity:0.74;
  line-height:1.2;
}

.alumni-tag{
  margin-top:auto;
  padding-top:10px;
  font-size:0.72rem;
  opacity:0.75;
}

.section-ko{
  font-size: 0.82rem;
  opacity: 0.72;
  font-weight: 500;
}
</style>

## Current Members  
---

### Doctoral Researchers  

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/heesu.jpeg' | relative_url }}" alt="Heesoo Yang">
    <p class="person-name"><strong>Heesoo Yang</strong></p>
    <p class="person-name-ko">양희수</p>
    <p class="person-role">Ph.D. Candidate</p>
  </div>

  <div class="person-card">   
    <img src="{{ '/images/minwook.png' | relative_url }}" alt="Minwook Lee">
    <p class="person-name"><strong>Minwook Lee</strong></p>
    <p class="person-name-ko">이민욱</p>
    <p class="person-role">Ph.D. Candidate</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/yen.png' | relative_url }}" alt="Le Hai Yen">
    <p class="person-name"><strong>Le Hai Yen</strong></p>
    <p class="person-name-ko">옌</p>
    <p class="person-role-ko">박사수료</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/seyoung.jpeg' | relative_url }}" alt="Seyoung Cho">
    <p class="person-name"><strong>Seyoung Cho</strong></p>
    <p class="person-name-ko">조세영</p>
    <p class="person-role">Ph.D. Student</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/juwon.jpeg' | relative_url }}" alt="Juwon Park">
    <p class="person-name"><strong>Juwon Park</strong></p>
    <p class="person-name-ko">박주원</p>
    <p class="person-role">Ph.D. Student</p>
  </div>

</div>

---

### Master’s Student  

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/ryul.jpeg' | relative_url }}" alt="Ryul Heo">
    <p class="person-name"><strong>Ryul Heo</strong></p>
    <p class="person-name-ko">허률</p>
    <p class="person-role">M.A. Student</p>
  </div>

</div>

---

### Part-time Ph.D. Student  

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/heesu.png' | relative_url }}" alt="Gohun Kim">
    <p class="person-name"><strong>Gohun Kim</strong></p>
    <p class="person-name-ko">김고헌</p>
    <p class="person-role">Ph.D. Student (Part-time)<br>Dahawa Farm</p>
    <p class="person-role-ko">다하와농장</p>
  </div>

</div>

---

### Project Team  
<div class="section-ko">사업단</div>

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/fm.png' | relative_url }}" alt="TBD">
    <p class="person-name"><strong>Jiyong Yun</strong></p>
    <p class="person-name-ko">윤지용</p>
    <p class="person-role">Field Manager</p>
    <p class="person-role-ko">Field Manager</p>
  </div>

</div>

---

### Project Staff  

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/eunji.jpeg' | relative_url }}" alt="Eunji Jang">
    <p class="person-name"><strong>Eunji Jang</strong></p>
    <p class="person-name-ko">장은지</p>
    <p class="person-role">Project Staff</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/youngjoo.jpeg' | relative_url }}" alt="Youngju Kwon">
    <p class="person-name"><strong>Youngju Kwon</strong></p>
    <p class="person-name-ko">권영주</p>
    <p class="person-role">Project Staff</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/hyunkyung.jpeg' | relative_url }}" alt="Hyunkyung Shin">
    <p class="person-name"><strong>Hyunkyung Shin</strong></p>
    <p class="person-name-ko">신현경</p>
    <p class="person-role">Project Staff</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/jinseon.png' | relative_url }}" alt="Jinseon Jeon">
    <p class="person-name"><strong>Jinseon Jeon</strong></p>
    <p class="person-name-ko">전진선</p>
    <p class="person-role">Project Staff</p>
  </div>

</div>

---

## Alumni  
<div class="section-ko">졸업생</div>

<div class="alumni-grid">

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Suhyun Bae">
    <p class="alumni-name">Suhyun Bae</p>
    <p class="alumni-name-ko">배수현</p>
    <p class="alumni-affil">Samsung Electronics</p>
    <p class="alumni-affil-ko">삼성전자</p>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Jagyeong Park">
    <p class="alumni-name">Jagyeong Park</p>
    <p class="alumni-name-ko">박자경</p>
    <p class="alumni-affil">Jeonbuk Research Institute</p>
    <p class="alumni-affil-ko">전북연구원</p>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Seongji Jeong">
    <p class="alumni-name">Seongji Jeong</p>
    <p class="alumni-name-ko">정성지</p>
    <p class="alumni-affil">Pennsylvania State University</p>
    <p class="alumni-affil-ko">펜실베니아 주립대학교</p>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/man.png' | relative_url }}" alt="Jisik Min">
    <p class="alumni-name">Jisik Min</p>
    <p class="alumni-name-ko">민지식</p>
    <p class="alumni-affil">Soonchunhyang University</p>
    <p class="alumni-affil-ko">순천향대학교</p>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Gwiyeong Ko">
    <p class="alumni-name">Gwiyeong Ko</p>
    <p class="alumni-name-ko">고귀영</p>
    <p class="alumni-affil">Korea Foundation for Local Educational Administration</p>
    <p class="alumni-affil-ko">한국지방교육행정연구재단</p>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Hyunju Yoo">
    <p class="alumni-name">Hyunju Yoo</p>
    <p class="alumni-name-ko">유현주</p>
    <p class="alumni-affil">Inha University</p>
    <p class="alumni-affil-ko">인하대학교</p>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/man.png' | relative_url }}" alt="Seokho Hong">
    <p class="alumni-name">Seokho Hong</p>
    <p class="alumni-name-ko">홍석호</p>
    <p class="alumni-affil">—</p>
    <p class="alumni-affil-ko">—</p>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/jihyeon.jpeg' | relative_url }}" alt="Jihyeon An">
    <p class="alumni-name">Jihyeon An</p>
    <p class="alumni-name-ko">안지현</p>
    <p class="alumni-affil">Konkuk University</p>
    <p class="alumni-affil-ko">건국대학교</p>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/jiyeon1.jpeg' | relative_url }}" alt="Jiyeon Kim">
    <p class="alumni-name">Jiyeon Kim</p>
    <p class="alumni-name-ko">김지연</p>
    <p class="alumni-affil">Ph.D. Student</p>
    <p class="alumni-affil-ko">박사과정 유학</p>
    <div class="alumni-tag">Alumni</div>
  </div>

</div>
