from pathlib import Path

path = Path("main.py")
text = path.read_text(encoding="utf-8")

start = text.index('st.markdown("""\n<style>')
end = text.index('</style>\n""", unsafe_allow_html=True)', start) + len('</style>\n""", unsafe_allow_html=True)')

new_css = '''st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background:
        radial-gradient(circle at top center, rgba(255, 110, 20, 0.20), transparent 32%),
        radial-gradient(circle at bottom right, rgba(255, 60, 20, 0.10), transparent 30%),
        linear-gradient(180deg, #160600 0%, #070301 58%, #000000 100%);
    color: #f7efe7;
}

.block-container {
    max-width: 780px;
    padding-top: 90px !important;
    padding-bottom: 360px !important;
}

p, div, span, label {
    color: #f1e7dc !important;
}

[data-testid="stImage"] {
    max-width: 720px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 18px;
}

[data-testid="stImage"] img {
    border-radius: 22px;
    border: 1px solid rgba(255, 160, 55, 0.38);
    box-shadow: 0 0 30px rgba(255, 110, 20, 0.18);
}

.cora-header,
.cora-card,
.stRadio {
    background: rgba(0, 0, 0, 0.72);
    border: 1px solid rgba(255, 160, 55, 0.35);
    border-radius: 22px;
    box-shadow: 0 0 24px rgba(255, 110, 20, 0.10);
}

.cora-header {
    padding: 20px 18px 24px 18px;
    margin-bottom: 22px;
}

.cora-card {
    padding: 18px;
    margin-bottom: 18px;
}

.cora-title {
    font-size: 2.05rem;
    font-weight: 950;
    color: #ff9f2f !important;
    margin-bottom: 8px;
}

.cora-subtitle,
.card-text {
    font-size: 1.05rem;
    line-height: 1.55;
    color: #ffe9d1 !important;
}

.card-title,
.section-title,
.shopping-category-title {
    color: #ff9f2f !important;
    font-weight: 950;
}

.card-title { font-size: 1.42rem; margin-bottom: 10px; }
.section-title { font-size: 1.42rem; margin-top: 34px; margin-bottom: 12px; }
.shopping-category-title { font-size: 1.22rem; margin-top: 24px; margin-bottom: 8px; }

.info-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
}

.info-grid div,
.list-item,
.stCheckbox {
    background: rgba(255, 255, 255, 0.060);
    border: 1px solid rgba(255, 160, 55, 0.18);
    border-radius: 13px;
}

.info-grid div {
    padding: 12px;
    font-size: 0.98rem;
    line-height: 1.4;
}

.list-item {
    padding: 9px 12px;
    margin-bottom: 8px;
    font-size: 1.04rem;
    font-weight: 600;
    line-height: 1.45;
}

.stRadio {
    padding: 12px 14px;
    margin-bottom: 16px;
}

.stRadio label,
.stCheckbox label {
    color: #f7efe7 !important;
    font-weight: 700 !important;
}

.stRadio div[role="radiogroup"] label {
    background: rgba(255, 255, 255, 0.060);
    border-radius: 12px;
    padding: 8px 10px;
    margin-bottom: 6px;
}

.stCheckbox {
    padding: 6px 10px;
    margin-bottom: 8px;
}

.stCheckbox label {
    font-size: 1.05rem !important;
}

.stCheckbox input {
    accent-color: #ff9f2f;
}

.streamlit-expanderHeader {
    color: #ffb14a !important;
    font-weight: 850 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #ff9f2f, #ff4d1a);
    color: #160600 !important;
    border: none;
    border-radius: 18px;
    font-weight: 950;
    width: 100%;
    min-height: 72px;
    padding: 0.9rem 1rem;
    font-size: 1.08rem;
    box-shadow: 0 0 20px rgba(255, 120, 20, 0.24);
    white-space: normal;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #ffb34d, #ff6b2a);
    color: #000000 !important;
}

@media (max-width: 600px) {
    .block-container {
        padding-top: 120px !important;
        padding-bottom: 430px !important;
        padding-left: 1.15rem !important;
        padding-right: 1.15rem !important;
    }

    [data-testid="stImage"] {
        max-width: 100%;
        margin-bottom: 18px;
    }

    .cora-title { font-size: 1.65rem; }
    .cora-subtitle, .card-text { font-size: 1rem; }
    .section-title { font-size: 1.28rem; margin-top: 36px; }
    .shopping-category-title { font-size: 1.12rem; }

    .info-grid {
        grid-template-columns: 1fr;
    }

    .list-item {
        font-size: 1rem;
    }

    .stButton > button {
        min-height: 74px;
        font-size: 1.08rem;
        border-radius: 18px;
    }
}
</style>
""", unsafe_allow_html=True)'''

text = text[:start] + new_css + text[end:]

old_nav = '''for row_start in range(0, len(nav_items), 2):
    cols = st.columns(2)
    for idx, item in enumerate(nav_items[row_start:row_start + 2]):
        with cols[idx]:
            is_active = st.session_state.view == item
            label = f"✅ {item}" if is_active else item
            if st.button(label, key=f"nav_{row_start}_{idx}_{item}"):
                set_view(item)
                st.rerun()'''

new_nav = '''for item in nav_items:
    is_active = st.session_state.view == item
    label = f"✅ {item}" if is_active else item
    if st.button(label, key=f"nav_{item}"):
        set_view(item)
        st.rerun()'''

text = text.replace(old_nav, new_nav)

if "cora-mobile-bottom-spacer" not in text:
    text += '''

# =========================================================
# MOBILE SAFE BOTTOM SPACER
# =========================================================
st.markdown('<div class="cora-mobile-bottom-spacer" style="height:260px;"></div>', unsafe_allow_html=True)
'''

path.write_text(text, encoding="utf-8")
print("✅ main.py mobile fixed: oben frei, unten frei, Navigation sauber.")
