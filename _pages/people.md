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

/* --- Alumni (vertical, compact) --- */
.alumni-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 12px;
}

@media (max-width: 1100px) {
  .alumni-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 650px) {
  .alumni-grid { grid-template-columns: 1fr; }
}

.alumni-card {
  border: 1px solid rgba(128,128,128,0.18);
  background: rgba(128,128,128,0.06);
  border-radius: 14px;
  padding: 14px 14px 12px 14px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  min-height: 220px;
  transition: transform 0.16s ease, box-shadow 0.16s ease;
}

.alumni-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.14);
}

.alumni-photo {
  width: 60px;
  height: 76px;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid rgba(128,128,128,0.22);
  background: rgba(128,128,128,0.10);
  margin-bottom: 10px;
}

.alumni-name {
  font-weight: 800;
  margin: 0 0 2px 0;
  font-size: 0.92rem;
  line-height: 1.15;
}

.alumni-name-ko {
  display: block;
  margin: 0 0 6px 0;
  font-size: 0.75rem;
  opacity: 0.76;
  line-height: 1.15;
  font-family: "Pretendard", "Noto Sans KR", sans-serif;
  color: inherit;
}

.alumni-affil {
  margin: 0;
  font-size: 0.82rem;
  opacity: 0.85;
  line-height: 1.25;
}

.alumni-affil-ko {
  display: block;
  margin: 4px 0 0 0;
  font-size: 0.74rem;
  opacity: 0.74;
  line-height: 1.2;
  font-family: "Pretendard", "Noto Sans KR", sans-serif;
  color: inherit;
}

.alumni-tag {
  margin-top: auto;
  padding-top: 10px;
  font-size: 0.72rem;
  opacity: 0.75;
}
</style>

## Current Members

### Doctoral Researchers

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/heesu.jpeg' | relative_url }}" alt="Heesoo Yang">
    <div class="person-name"><strong>Heesoo Yang</strong></div>
    <div class="person-name-ko">양희수</div>
    <div class="person-role">Ph.D. Candidate</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/minwook.png' | relative_url }}" alt="Minwook Lee">
    <div class="person-name"><strong>Minwook Lee</strong></div>
    <div class="person-name-ko">이민욱</div>
    <div class="person-role">Ph.D. Candidate</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/yen.png' | relative_url }}" alt="Le Hai Yen">
    <div class="person-name"><strong>Le Hai Yen</strong></div>
    <div class="person-name-ko">옌</div>
    <div class="person-role">Ph.D. Candidate</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/seyoung.jpeg' | relative_url }}" alt="Seyoung Cho">
    <div class="person-name"><strong>Seyoung Cho</strong></div>
    <div class="person-name-ko">조세영</div>
    <div class="person-role">Ph.D. Student</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/juwon.jpeg' | relative_url }}" alt="Juwon Park">
    <div class="person-name"><strong>Juwon Park</strong></div>
    <div class="person-name-ko">박주원</div>
    <div class="person-role">Ph.D. Student</div>
  </div>

</div>

---

### Master’s Student

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/ryul.jpeg' | relative_url }}" alt="Ryul Heo">
    <div class="person-name"><strong>Ryul Heo</strong></div>
    <div class="person-name-ko">허률</div>
    <div class="person-role">Master's Student</div>
  </div>

</div>

---

### Part-time Student

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/woman.png' | relative_url }}" alt="Sula Kim">
    <div class="person-name"><strong>Sula Kim</strong></div>
    <div class="person-name-ko">김슬아</div>
    <div class="person-role">Ph.D. Student<br>SK DND</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/man.png' | relative_url }}" alt="Gohun Kim">
    <div class="person-name"><strong>Gohun Kim</strong></div>
    <div class="person-name-ko">김고헌</div>
    <div class="person-role">Ph.D. Student<br>Dahawa Farm</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/woman.png' | relative_url }}" alt="Jieun Park">
    <div class="person-name"><strong>Jieun Park</strong></div>
    <div class="person-name-ko">박지은</div>
    <div class="person-role">Master's Student<br>농림수산식품교육문화정보원</div>
  </div>
  

  <div class="person-card">
    <img src="{{ '/images/man.png' | relative_url }}" alt="Dongju Kim">
    <div class="person-name"><strong>Dongju Kim</strong></div>
    <div class="person-name-ko">김동주</div>
    <div class="person-role">Master's Student</div>
  </div>
</div>

---

### Project Staff

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/man.png' | relative_url }}" alt="Jiyong Yun">
    <div class="person-name"><strong>Jiyong Yun</strong></div>
    <div class="person-name-ko">윤지용</div>
    <div class="person-role">Field Manager</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/eunji.jpeg' | relative_url }}" alt="Eunji Jang">
    <div class="person-name"><strong>Eunji Jang</strong></div>
    <div class="person-name-ko">장은지</div>
    <div class="person-role">Project Staff</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/youngjoo.jpeg' | relative_url }}" alt="Youngju Kwon">
    <div class="person-name"><strong>Youngju Kwon</strong></div>
    <div class="person-name-ko">권영주</div>
    <div class="person-role">Project Staff</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/hyunkyung.jpeg' | relative_url }}" alt="Hyunkyung Shin">
    <div class="person-name"><strong>Hyunkyung Shin</strong></div>
    <div class="person-name-ko">신현경</div>
    <div class="person-role">Project Staff</div>
  </div>

  <div class="person-card">
    <img src="{{ '/images/jinseon.png' | relative_url }}" alt="Jinseon Jeon">
    <div class="person-name"><strong>Jinseon Jeon</strong></div>
    <div class="person-name-ko">전진선</div>
    <div class="person-role">Project Staff</div>
  </div>

</div>

---

## Alumni

<div class="alumni-grid">

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Suhyun Bae">
    <div class="alumni-name">Suhyun Bae</div>
    <div class="alumni-name-ko">배수현</div>
    <div class="alumni-affil">Samsung Electronics</div>
    <div class="alumni-affil-ko">삼성전자</div>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Jagyeong Park">
    <div class="alumni-name">Jagyeong Park</div>
    <div class="alumni-name-ko">박자경</div>
    <div class="alumni-affil">Jeonbuk Research Institute</div>
    <div class="alumni-affil-ko">전북연구원</div>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Seongji Jeong">
    <div class="alumni-name">Seongji Jeong</div>
    <div class="alumni-name-ko">정성지</div>
    <div class="alumni-affil">Pennsylvania State University</div>
    <div class="alumni-affil-ko">펜실베니아 주립대학교</div>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/man.png' | relative_url }}" alt="Jisik Min">
    <div class="alumni-name">Jisik Min</div>
    <div class="alumni-name-ko">민지식</div>
    <div class="alumni-affil">Soonchunhyang University</div>
    <div class="alumni-affil-ko">순천향대학교</div>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Gwiyeong Ko">
    <div class="alumni-name">Gwiyeong Ko</div>
    <div class="alumni-name-ko">고귀영</div>
    <div class="alumni-affil">Korea Foundation for Local Educational Administration</div>
    <div class="alumni-affil-ko">한국지방교육행정연구재단</div>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/woman.png' | relative_url }}" alt="Hyunju Yoo">
    <div class="alumni-name">Hyunju Yoo</div>
    <div class="alumni-name-ko">유현주</div>
    <div class="alumni-affil">Inha University</div>
    <div class="alumni-affil-ko">인하대학교</div>
    <div class="alumni-tag">Ph.D.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/man.png' | relative_url }}" alt="Seokho Hong">
    <div class="alumni-name">Seokho Hong</div>
    <div class="alumni-name-ko">홍석호</div>
    <div class="alumni-affil">—</div>
    <div class="alumni-tag">M.A.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/jihyeon.jpeg' | relative_url }}" alt="Jihyeon An">
    <div class="alumni-name">Jihyeon An</div>
    <div class="alumni-name-ko">안지현</div>
    <div class="alumni-affil">Konkuk University</div>
    <div class="alumni-affil-ko">건국대학교</div>
    <div class="alumni-tag">M.A.</div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/jiyeon1.jpeg' | relative_url }}" alt="Jiyeon Kim">
    <div class="alumni-name">Jiyeon Kim</div>
    <div class="alumni-name-ko">김지연</div>
    <div class="alumni-affil">Ph.D. Student</div>
    <div class="alumni-tag">M.A.</div>
  </div>

</div>
