import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 포켓몬 이미지: PokeAPI의 공개 스프라이트 저장소에서 불러옵니다.
POKEMON = {
    "INTJ": {
        "name": "뮤츠", "english": "Mewtwo", "id": 150,
        "types": "에스퍼", "emoji": "🔮",
        "feature": "뛰어난 지능과 분석력으로 상황을 파악하는 전설의 포켓몬이에요.",
        "reason": "깊이 생각하고 큰 그림을 그리는 INTJ와 뮤츠는 전략을 세울 때 좋은 팀이 될 수 있어요. 서로의 독립성을 존중하면서 어려운 문제를 함께 해결하는 단짝이에요."
    },
    "INTP": {
        "name": "메타몽", "english": "Ditto", "id": 132,
        "types": "노말", "emoji": "🧩",
        "feature": "다른 포켓몬으로 변신할 수 있어 유연하고 호기심 많은 포켓몬이에요.",
        "reason": "새로운 가능성을 탐구하는 INTP와 메타몽은 엉뚱한 아이디어를 실험하는 콤비예요. 정해진 틀에 갇히지 않고 다양한 방법을 찾아가는 재미가 있어요."
    },
    "ENTJ": {
        "name": "리자몽", "english": "Charizard", "id": 6,
        "types": "불꽃 · 비행", "emoji": "🔥",
        "feature": "강한 자신감과 추진력을 가진 든든한 파트너예요.",
        "reason": "목표를 정하고 팀을 이끄는 ENTJ에게 리자몽의 당당한 에너지가 잘 어울려요. 큰 도전을 만났을 때 서로 용기를 북돋우며 앞으로 나아갈 수 있어요."
    },
    "ENTP": {
        "name": "겐가", "english": "Gengar", "id": 94,
        "types": "고스트 · 독", "emoji": "👻",
        "feature": "장난을 좋아하고 예측하기 어려운 재치가 매력인 포켓몬이에요.",
        "reason": "새로운 발상과 토론을 즐기는 ENTP와 겐가는 지루할 틈 없는 단짝이에요. 기발한 장난과 독특한 아이디어로 평범한 하루도 흥미진진하게 바꿔 줄 거예요."
    },
    "INFJ": {
        "name": "가디안", "english": "Gardevoir", "id": 282,
        "types": "에스퍼 · 페어리", "emoji": "🌙",
        "feature": "소중한 사람을 지키려는 마음이 강하고 섬세한 포켓몬이에요.",
        "reason": "다른 사람의 마음을 세심하게 살피는 INFJ와 가디안은 서로를 깊이 이해하는 조합이에요. 조용한 순간에도 마음을 나누고 서로에게 든든한 힘이 되어 줄 수 있어요."
    },
    "INFP": {
        "name": "이브이", "english": "Eevee", "id": 133,
        "types": "노말", "emoji": "🌼",
        "feature": "다양한 가능성을 품고 있으며 친근하고 사랑스러운 포켓몬이에요.",
        "reason": "자신만의 가치와 상상력을 소중히 여기는 INFP에게 이브이의 무한한 가능성이 잘 어울려요. 서로의 개성을 응원하며 각자의 방식으로 성장하는 따뜻한 단짝이 될 거예요."
    },
    "ENFJ": {
        "name": "피카츄", "english": "Pikachu", "id": 25,
        "types": "전기", "emoji": "⚡",
        "feature": "친구들과 마음을 나누고 힘을 합치는 데 익숙한 포켓몬이에요.",
        "reason": "사람들을 격려하고 함께하는 분위기를 만드는 ENFJ와 피카츄는 밝은 에너지가 닮았어요. 친구들이 힘들 때 서로 응원하며 팀을 하나로 모아 줄 수 있어요."
    },
    "ENFP": {
        "name": "푸린", "english": "Jigglypuff", "id": 39,
        "types": "노말 · 페어리", "emoji": "🎤",
        "feature": "노래와 표현을 좋아하며 주변을 즐겁게 만드는 포켓몬이에요.",
        "reason": "호기심이 많고 새로운 만남을 즐기는 ENFP와 푸린은 함께 있으면 웃음이 끊이지 않을 것 같아요. 신나는 아이디어와 따뜻한 표현으로 일상을 작은 모험으로 만들어 줘요."
    },
    "ISTJ": {
        "name": "꼬부기", "english": "Squirtle", "id": 7,
        "types": "물", "emoji": "💧",
        "feature": "차근차근 실력을 쌓아 가는 믿음직한 포켓몬이에요.",
        "reason": "책임감 있고 꾸준한 ISTJ와 꼬부기는 맡은 일을 성실하게 해내는 점이 잘 맞아요. 계획을 하나씩 실천하면서 서로 믿고 의지할 수 있는 안정적인 단짝이에요."
    },
    "ISFJ": {
        "name": "럭키", "english": "Chansey", "id": 113,
        "types": "노말", "emoji": "💗",
        "feature": "다친 포켓몬을 보살피는 것을 좋아하는 다정한 포켓몬이에요.",
        "reason": "주변 사람을 세심하게 챙기는 ISFJ와 럭키는 배려심이라는 공통점이 있어요. 말없이 곁을 지켜 주고 작은 필요도 알아채며 서로에게 편안한 안식처가 되어 줄 거예요."
    },
    "ESTJ": {
        "name": "윈디", "english": "Arcanine", "id": 59,
        "types": "불꽃", "emoji": "🦁",
        "feature": "용감하고 충성심이 강해 믿고 함께할 수 있는 포켓몬이에요.",
        "reason": "책임감 있게 일을 이끌고 질서를 중요하게 여기는 ESTJ에게 윈디의 믿음직함이 어울려요. 목표를 향해 힘차게 달리면서도 서로의 약속을 지키는 파트너가 될 수 있어요."
    },
    "ESFJ": {
        "name": "푸크린", "english": "Wigglytuff", "id": 40,
        "types": "노말 · 페어리", "emoji": "🎀",
        "feature": "사교적이고 포근한 분위기로 친구들을 편안하게 해 주는 포켓몬이에요.",
        "reason": "사람들과 어울리고 모두가 즐거운 분위기를 만드는 ESFJ와 푸크린은 환상의 팀이에요. 모임을 즐겁게 만들고 주변 친구들이 소외되지 않도록 함께 챙겨 줄 거예요."
    },
    "ISTP": {
        "name": "루카리오", "english": "Lucario", "id": 448,
        "types": "격투 · 강철", "emoji": "🥋",
        "feature": "상대의 기운을 감지하고 침착하게 움직이는 실력파 포켓몬이에요.",
        "reason": "직접 해 보며 방법을 찾고 위기에도 침착한 ISTP와 루카리오는 행동으로 호흡을 맞춰요. 말이 많지 않아도 서로의 실력을 믿으며 문제를 해결하는 든든한 조합이에요."
    },
    "ISFP": {
        "name": "치코리타", "english": "Chikorita", "id": 152,
        "types": "풀", "emoji": "🍃",
        "feature": "온화하고 다정하며 주변에 편안한 기운을 전하는 포켓몬이에요.",
        "reason": "자신만의 감각과 취향을 소중히 여기는 ISFP와 치코리타는 평화로운 시간을 함께 즐길 수 있어요. 자연 속을 산책하거나 작은 아름다움을 발견하며 마음을 충전하는 단짝이에요."
    },
    "ESTP": {
        "name": "갸라도스", "english": "Gyarados", "id": 130,
        "types": "물 · 비행", "emoji": "🌊",
        "feature": "강력한 힘과 대담함을 지닌 에너지 넘치는 포켓몬이에요.",
        "reason": "기회를 빠르게 잡고 직접 부딪쳐 보는 ESTP와 갸라도스는 모험심이 잘 맞아요. 예상 밖의 상황에서도 망설이기보다 재빠르게 움직이며 짜릿한 도전을 함께할 수 있어요."
    },
    "ESFP": {
        "name": "파치리스", "english": "Pachirisu", "id": 417,
        "types": "전기", "emoji": "✨",
        "feature": "활발하고 장난기 넘치며 주변에 생기를 더하는 포켓몬이에요.",
        "reason": "즐거운 경험을 함께 나누고 순간을 만끽하는 ESFP와 파치리스는 밝은 분위기가 닮았어요. 소소한 일도 신나는 추억으로 만들고 친구들에게 웃음을 전하는 단짝이 될 거예요."
    },
}

MBTI_GROUPS = {
    "🧠 분석가": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "💗 외교관": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "🛡️ 관리자": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "🎨 탐험가": ["ISTP", "ISFP", "ESTP", "ESFP"],
}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');
:root { --cream:#fff9e9; --yellow:#ffd85e; --gold:#f2b93b; --brown:#4f3b25; }
.stApp {
    background: radial-gradient(circle at 10% 0%, #fff0b8 0, transparent 30%),
                linear-gradient(180deg, #fffaf0 0%, #fff5d9 100%);
    color: var(--brown);
    font-family: 'Noto Sans KR', sans-serif;
}
.block-container { max-width: 900px; padding-top: 2rem; padding-bottom: 3rem; }
h1, h2, h3 { color: #513d25 !important; font-family: 'Jua', 'Noto Sans KR', sans-serif !important; }
.hero {
    text-align:center; padding: 1.6rem 1rem 1.2rem; border-radius: 28px;
    background: rgba(255,255,255,.72); border: 2px solid #ffe39a;
    box-shadow: 0 10px 28px rgba(160,112,32,.08); margin-bottom: 1.2rem;
}
.hero .eyebrow { font-size: 1rem; font-weight: 900; letter-spacing: .12em; color:#b77c12; }
.hero .headline { font-size: clamp(2.1rem, 6vw, 3.6rem); line-height:1.18; margin:.5rem 0; }
.hero .sub { font-size:1.08rem; line-height:1.7; color:#786345; }
.pill { display:inline-block; padding:.45rem .9rem; background:#fff0b5; border:1px solid #f7d875;
        border-radius:999px; font-weight:900; color:#785314; margin:.2rem; }
.result-card {
    background: rgba(255,255,255,.86); border: 2px solid #ffe39a;
    border-radius: 28px; padding: 1.4rem; box-shadow: 0 12px 30px rgba(130,90,25,.09);
}
.tip { background:#fff2c6; border-radius:18px; padding:1rem 1.1rem; line-height:1.8; }
.stButton > button {
    background: #fffdf5; color:#513d25; border:2px solid #f5d47a; border-radius:16px;
    min-height:3.2rem; font-size:1.05rem; font-weight:900; transition:all .18s ease;
}
.stButton > button:hover { background:#ffe28a; color:#513d25; border-color:#e8b83f; transform:translateY(-2px); }
.stButton > button:focus { box-shadow:0 0 0 .2rem #ffe9a8; }
div[data-testid="stImage"] img { border-radius:22px; }
footer {visibility:hidden;}
#MainMenu {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">✨ 나만의 포켓몬 파트너 찾기 ✨</div>
  <div class="headline">MBTI로 찾는<br>단짝 포켓몬</div>
  <div class="sub">나의 성격과 찰떡궁합인 포켓몬은 누구일까요?<br>MBTI를 선택하고 운명의 파트너를 만나 보세요!</div>
  <div><span class="pill">💛 16가지 유형</span><span class="pill">⚡ 나만의 단짝</span><span class="pill">🎉 축하 효과</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🌟 나의 MBTI를 골라 주세요")
st.write("아래에서 유형을 누르면 단짝 포켓몬을 바로 찾아드려요!")

if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

for group_name, types in MBTI_GROUPS.items():
    st.markdown(f"#### {group_name}")
    cols = st.columns(4)
    for col, mbti in zip(cols, types):
        with col:
            if st.button(mbti, key=f"mbti_{mbti}", use_container_width=True):
                st.session_state.selected_mbti = mbti
                st.rerun()

selected = st.session_state.selected_mbti

if selected:
    p = POKEMON[selected]
    st.markdown("---")
    st.markdown(
        f"<div style='text-align:center;padding:.6rem 0 1rem'>"
        f"<div style='font-size:1.1rem;color:#ad7918;font-weight:900'>🎊 축하해요! 🎊</div>"
        f"<h1 style='font-size:2.3rem;margin:.25rem 0'>당신의 단짝은 {p['name']}!</h1>"
        f"<div style='color:#826747;font-size:1.05rem'>MBTI <b>{selected}</b>에게 어울리는 포켓몬을 찾았어요.</div>"
        f"</div>",
        unsafe_allow_html=True,
    )
    components.html("""
    <div style="height:1px"></div>
    <script>
    (function(){
      const colors = ['#ffd84d','#ff9f68','#f58bc0','#91d8a5','#8ccfff','#d2a7ff'];
      const pieces = 90;
      for(let i=0;i<pieces;i++){
        const el=document.createElement('div');
        el.style.cssText='position:fixed;top:-14px;left:'+Math.random()*100+'%;width:9px;height:13px;z-index:99999;pointer-events:none;border-radius:2px;background:'+colors[i%colors.length]+';transform:rotate('+Math.random()*360+'deg);animation:fall '+(2.2+Math.random()*2.3)+'s linear forwards;animation-delay:'+Math.random()*.7+'s;';
        document.body.appendChild(el);
        setTimeout(()=>el.remove(),5200);
      }
      const style=document.createElement('style');
      style.textContent='@keyframes fall{to{transform:translateY(110vh) rotate(900deg);opacity:.2}}';
      document.head.appendChild(style);
    })();
    </script>
    """, height=5)
    st.balloons()

    left, right = st.columns([1, 1.15], gap="large")
    with left:
        image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{p['id']}.png"
        st.image(image_url, use_container_width=True)
        st.markdown(
            f"<div style='text-align:center'><span class='pill'>{p['emoji']} 타입: {p['types']}</span></div>",
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(f"## {p['name']} <span style='font-size:1rem;color:#98784d'>({p['english']})</span>", unsafe_allow_html=True)
        st.markdown("### 💫 어떤 포켓몬일까요?")
        st.write(p["feature"])
        st.markdown("### 💛 왜 나와 잘 맞을까요?")
        st.markdown(f"<div class='tip'>{p['reason']}</div>", unsafe_allow_html=True)
        st.markdown("")
        st.caption("이미지 출처: PokeAPI 공개 포켓몬 스프라이트 저장소")

    st.markdown("")
    if st.button("🔄 다른 MBTI도 찾아보기", use_container_width=True):
        st.session_state.selected_mbti = None
        st.rerun()
else:
    st.markdown("""
    <div class="tip">
    <b>💡 작은 안내</b><br>
    MBTI는 나를 알아보는 재미있는 참고 도구예요. 사람마다 성격은 다를 수 있으니,
    결과는 정답이라기보다 가볍게 즐기는 궁합 테스트로 봐 주세요!
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;color:#9b825d;font-size:.85rem;padding:2rem 0 .5rem">
  Made with 💛 · 포켓몬 이미지가 표시되려면 인터넷 연결이 필요해요.
</div>
""", unsafe_allow_html=True)
