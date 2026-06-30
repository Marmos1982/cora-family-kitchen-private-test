import streamlit as st
from pathlib import Path
from textwrap import dedent

st.set_page_config(
    page_title="Cora Family Kitchen",
    page_icon="🔥",
    layout="centered"
)

# =========================================================
# PATHS
# =========================================================
APP_DIR = Path(__file__).parent


def find_cora_image():
    possible_names = [
        "cora.png",
        "cora.png.png",
        "Cora.png",
        "Cora.PNG",
        "cora.PNG",
        "cora.jpg",
        "cora.jpeg",
        "Cora.jpg",
        "Cora.jpeg",
        "cora.webp",
        "Cora.webp",
    ]

    for name in possible_names:
        path = APP_DIR / name
        if path.exists():
            return path

    for path in APP_DIR.iterdir():
        if path.is_file():
            name = path.name.lower()
            if "cora" in name and path.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
                return path

    return None


CORA_IMAGE = find_cora_image()


# =========================================================
# HELPERS
# =========================================================
def clean_text(text):
    return dedent(text).strip()


def show_info_card(recipe):
    info = recipe["info"]

    st.markdown(f"""
    <div class="cora-card">
        <div class="card-title">🔥 Kurzinfo</div>
        <div class="info-grid">
            <div><b>Zeit:</b><br>{info["time"]}</div>
            <div><b>Budget:</b><br>{info["budget"]}</div>
            <div><b>Level:</b><br>{info["level"]}</div>
            <div><b>Family:</b><br>{info["family"]}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_simple_list(title, items, icon="🧾"):
    st.markdown(f'<div class="section-title">{icon} {title}</div>', unsafe_allow_html=True)

    for item in items:
        st.markdown(f"""
        <div class="list-item">
            {item}
        </div>
        """, unsafe_allow_html=True)


def show_found_items_card(found_items):
    st.markdown("""
    <div class="cora-card">
        <div class="card-title">📦 Cora hat sortiert</div>
        <div class="card-text">
            Das ist der erste V1-Demo-Check. Später erkennt Cora die Zutaten direkt aus den Bildern.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for category, items in found_items.items():
        st.markdown(f'<div class="shopping-category-title">{category}</div>', unsafe_allow_html=True)
        for item in items:
            st.markdown(f"""
            <div class="list-item">
                ✅ {item}
            </div>
            """, unsafe_allow_html=True)


# =========================================================
# CSS / DESIGN
# =========================================================
st.markdown("""
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
    max-width: 820px;
    padding-top: 1.2rem;
    padding-bottom: 200px !important;
}

p, div, span, label {
    color: #f1e7dc !important;
}

/* Bild */
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

/* Header */
.cora-header {
    background: rgba(0, 0, 0, 0.72);
    border: 1px solid rgba(255, 160, 55, 0.40);
    border-radius: 24px;
    padding: 20px 18px 24px 18px;
    margin-top: 10px;
    margin-bottom: 22px;
    box-shadow: 0 0 30px rgba(255, 110, 20, 0.14);
}

.cora-title {
    font-size: 2.05rem;
    font-weight: 950;
    color: #ff9f2f !important;
    margin-bottom: 8px;
}

.cora-subtitle {
    font-size: 1.05rem;
    line-height: 1.5;
    color: #ffe9d1 !important;
}

/* Cards */
.cora-card {
    background: rgba(0, 0, 0, 0.72);
    border: 1px solid rgba(255, 160, 55, 0.35);
    border-radius: 22px;
    padding: 18px 18px;
    margin-bottom: 18px;
    box-shadow: 0 0 24px rgba(255, 110, 20, 0.10);
}

.card-title {
    color: #ff9f2f !important;
    font-size: 1.42rem;
    font-weight: 900;
    margin-bottom: 10px;
}

.card-text {
    color: #f8eadf !important;
    font-size: 1.03rem;
    line-height: 1.6;
}

/* Info Grid */
.info-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
}

.info-grid div {
    background: rgba(255, 255, 255, 0.055);
    border: 1px solid rgba(255, 160, 55, 0.22);
    border-radius: 14px;
    padding: 12px;
    font-size: 0.98rem;
    line-height: 1.4;
}

/* Section */
.section-title {
    color: #ff9f2f !important;
    font-size: 1.42rem;
    font-weight: 950;
    margin-top: 28px;
    margin-bottom: 12px;
}

.shopping-category-title {
    color: #ff9f2f !important;
    font-size: 1.22rem;
    font-weight: 950;
    margin-top: 24px;
    margin-bottom: 8px;
}

/* List Items */
.list-item {
    background: rgba(255, 255, 255, 0.060);
    border: 1px solid rgba(255, 160, 55, 0.18);
    border-radius: 13px;
    padding: 9px 12px;
    margin-bottom: 8px;
    font-size: 1.04rem;
    font-weight: 600;
    line-height: 1.45;
}

/* Radio Auswahl */
.stRadio {
    background: rgba(0, 0, 0, 0.58);
    border: 1px solid rgba(255, 160, 55, 0.32);
    border-radius: 18px;
    padding: 12px 14px;
    margin-bottom: 16px;
}

.stRadio label {
    color: #f7efe7 !important;
    font-size: 1.02rem !important;
    font-weight: 700 !important;
}

.stRadio div[role="radiogroup"] label {
    background: rgba(255, 255, 255, 0.060);
    border-radius: 12px;
    padding: 8px 10px;
    margin-bottom: 6px;
}

/* Checkbox */
.stCheckbox {
    background: rgba(255, 255, 255, 0.060);
    border-radius: 13px;
    padding: 6px 10px;
    margin-bottom: 8px;
}

.stCheckbox label {
    color: #f7efe7 !important;
    font-size: 1.05rem !important;
    font-weight: 650 !important;
}

.stCheckbox label span {
    color: #f7efe7 !important;
    opacity: 1 !important;
}

.stCheckbox input {
    accent-color: #ff9f2f;
}

/* Expander */
.streamlit-expanderHeader {
    color: #ffb14a !important;
    font-weight: 850 !important;
    font-size: 1.02rem !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #ff9f2f, #ff4d1a);
    color: #160600 !important;
    border: none;
    border-radius: 15px;
    font-weight: 950;
    padding: 0.75rem 1rem;
    width: 100%;
    box-shadow: 0 0 20px rgba(255, 120, 20, 0.24);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #ffb34d, #ff6b2a);
    color: #000000 !important;
}

/* Mobile */
@media (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-bottom: 220px !important;
    }

    [data-testid="stImage"] {
        max-width: 100%;
        margin-bottom: 16px;
    }

    .cora-title {
        font-size: 1.65rem;
    }

    .cora-subtitle {
        font-size: 0.98rem;
    }

    .section-title {
        font-size: 1.24rem;
    }

    .shopping-category-title {
        font-size: 1.12rem;
    }

    .info-grid {
        grid-template-columns: 1fr;
    }

    .list-item {
        font-size: 0.98rem;
    }

    .stCheckbox label {
        font-size: 0.98rem !important;
    }

    /* Am Handy: Desktop-Buttonleiste verstecken, Menü bleibt */
    .desktop-nav {
        display: none !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        min-height: 54px !important;
    }

    .stSelectbox div[data-baseweb="select"] span,
    .stSelectbox div[data-baseweb="select"] div {
        font-size: 1.08rem !important;
    }

    [data-testid="stFileUploader"] {
        padding: 10px;
        z-index: 50;
    }
}

/* Navigation Fix */
.nav-label {
    color: #ff9f2f !important;
    font-weight: 950;
    margin-bottom: 0.35rem;
}

[data-testid="stFileUploader"] {
    position: relative;
    z-index: 5;
    background: rgba(0, 0, 0, 0.58);
    border: 1px dashed rgba(255, 160, 55, 0.45);
    border-radius: 18px;
    padding: 12px;
    margin-bottom: 18px;
}

[data-testid="stFileUploader"] * {
    pointer-events: auto !important;
}

.stSelectbox {
    position: relative;
    z-index: 4;
}

div[data-testid="column"] {
    position: relative;
    z-index: 3;
}

.small-note {
    color: #ffe9d1 !important;
    opacity: 0.86;
    font-size: 0.92rem;
    margin-top: -8px;
    margin-bottom: 12px;
}

.cora-separator {
    height: 1px;
    background: rgba(255, 160, 55, 0.22);
    margin: 18px 0 22px 0;
}


/* Serious Mobile Menü / Upload Fix */
.stSelectbox label {
    color: #ffb14a !important;
    font-size: 1.05rem !important;
    font-weight: 950 !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(0, 0, 0, 0.88) !important;
    border: 1px solid rgba(255, 160, 55, 0.58) !important;
    border-radius: 15px !important;
    min-height: 52px !important;
    box-shadow: 0 0 18px rgba(255, 110, 20, 0.14);
}

.stSelectbox div[data-baseweb="select"] span,
.stSelectbox div[data-baseweb="select"] div {
    color: #fff3e4 !important;
    font-weight: 850 !important;
}

div[data-baseweb="popover"],
div[data-baseweb="menu"] {
    z-index: 999999 !important;
}

div[role="listbox"] {
    background: #090302 !important;
    border: 1px solid rgba(255, 160, 55, 0.58) !important;
}

div[role="option"] {
    color: #fff3e4 !important;
    background: #090302 !important;
    font-weight: 800 !important;
}

div[role="option"]:hover {
    background: rgba(255, 120, 20, 0.22) !important;
}

[data-testid="stFileUploader"] {
    position: relative !important;
    z-index: 20 !important;
    pointer-events: auto !important;
    background: rgba(0, 0, 0, 0.72) !important;
    border: 1px dashed rgba(255, 160, 55, 0.60) !important;
    border-radius: 18px !important;
    padding: 14px !important;
}

[data-testid="stFileUploader"] * {
    pointer-events: auto !important;
}

[data-testid="stFileUploader"] button {
    position: relative !important;
    z-index: 30 !important;
}

@media (max-width: 600px) {
    .desktop-nav {
        display: none !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        min-height: 56px !important;
    }
}


/* Product Polish v3: desktop clean line, mobile clean menu */
.block-container {
    max-width: 820px !important;
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
}

[data-testid="stImage"] {
    width: 100% !important;
    max-width: 820px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    margin-bottom: 22px !important;
}

[data-testid="stImage"] img {
    width: 100% !important;
    height: auto !important;
    display: block !important;
}

.cora-header,
.cora-card,
.list-item,
.stRadio,
[data-testid="stFileUploader"] {
    max-width: 820px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}

.nav-label {
    max-width: 820px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    margin-top: 4px !important;
}

.desktop-nav {
    max-width: 820px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    margin-bottom: 16px !important;
}

.desktop-nav [data-testid="stHorizontalBlock"] {
    gap: 0.7rem !important;
}

.desktop-nav .stButton > button {
    min-height: 46px !important;
    font-size: 0.92rem !important;
    white-space: nowrap !important;
}

.mobile-nav {
    display: none !important;
}

.cora-separator {
    margin-top: 16px !important;
    margin-bottom: 24px !important;
}

@media (max-width: 600px) {
    .block-container {
        max-width: 100% !important;
        padding-left: 0.95rem !important;
        padding-right: 0.95rem !important;
        padding-top: 0.75rem !important;
    }

    [data-testid="stImage"] {
        max-width: 100% !important;
        margin-bottom: 16px !important;
    }

    .cora-header {
        padding: 16px 14px 18px 14px !important;
        border-radius: 20px !important;
        margin-bottom: 16px !important;
    }

    .cora-title {
        font-size: 1.48rem !important;
        line-height: 1.15 !important;
    }

    .cora-subtitle {
        font-size: 0.92rem !important;
        line-height: 1.42 !important;
    }

    .desktop-nav {
        display: none !important;
    }

    .mobile-nav {
        display: block !important;
        max-width: 100% !important;
        margin-bottom: 14px !important;
    }

    .stSelectbox label {
        color: #ffb14a !important;
        font-size: 1.02rem !important;
        font-weight: 950 !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        min-height: 56px !important;
        background: rgba(0, 0, 0, 0.90) !important;
        border: 1px solid rgba(255, 160, 55, 0.62) !important;
        border-radius: 15px !important;
    }

    .stSelectbox div[data-baseweb="select"] span,
    .stSelectbox div[data-baseweb="select"] div {
        color: #fff3e4 !important;
        font-size: 1.02rem !important;
        font-weight: 850 !important;
    }

    .list-item {
        font-size: 0.96rem !important;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# DATA — TOP 10 ASIA
# =========================================================
recipes = {
    "1. Kraut-Karotten-Nudelpfanne": {
        "info": {
            "time": "20–25 Min",
            "budget": "Sehr günstig",
            "level": "Einfach",
            "family": "Mild / familientauglich"
        },
        "description": clean_text("""
            Schnell, günstig und perfekt für normale Familientage.
            Kraut, Karotten, Nudeln und eine einfache Asia-Sauce.
            Kein Stress. Keine 100 Zutaten. Pfanne heiß, Kopf ruhig.
        """),
        "ingredients": [
            "Nudeln oder Reisnudeln",
            "Weißkraut oder Chinakohl",
            "Karotten",
            "Zwiebel",
            "Knoblauch",
            "Sojasauce",
            "Honig oder Zucker",
            "Öl",
            "Optional: Huhn, Faschiertes oder Ei",
            "Optional: Sweet-Chili-Sauce"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Weißkraut oder Chinakohl",
                "Karotten",
                "Zwiebel",
                "Knoblauch"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Optional: Huhn, Faschiertes oder Eier"
            ],
            "🍚 Trockenware": [
                "Nudeln oder Reisnudeln"
            ],
            "🥢 Saucen & Gewürze": [
                "Sojasauce",
                "Honig oder Zucker",
                "Öl",
                "Optional: Sweet-Chili-Sauce"
            ]
        },
        "steps": [
            "Nudeln oder Reisnudeln kochen.",
            "Kraut fein schneiden, Karotten raspeln oder dünn schneiden.",
            "Zwiebel und Knoblauch in Öl anbraten.",
            "Kraut und Karotten dazugeben und weich braten.",
            "Optional Huhn, Faschiertes oder Ei dazugeben.",
            "Mit Sojasauce, Honig oder Zucker und etwas Wasser abschmecken.",
            "Nudeln dazugeben und alles gut vermischen.",
            "Optional mit Sweet-Chili-Sauce servieren."
        ]
    },

    "2. Asia-Huhn mit Brokkoli": {
        "info": {
            "time": "25 Min",
            "budget": "Mittel / Angebot nutzen",
            "level": "Einfach",
            "family": "Sehr familientauglich"
        },
        "description": clean_text("""
            Mildes Asia-Huhn mit Brokkoli und Reis.
            Einfach, warm, sättigend und besser als hektisch irgendwas bestellen.
        """),
        "ingredients": [
            "Huhn",
            "Brokkoli frisch oder TK",
            "Karotten",
            "Reis",
            "Knoblauch",
            "Sojasauce",
            "Honig oder Zucker",
            "Speisestärke",
            "Öl"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Brokkoli frisch oder TK",
                "Karotten",
                "Knoblauch"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Huhn"
            ],
            "🍚 Trockenware": [
                "Reis"
            ],
            "🥢 Saucen & Gewürze": [
                "Sojasauce",
                "Honig oder Zucker",
                "Speisestärke",
                "Öl"
            ]
        },
        "steps": [
            "Reis kochen.",
            "Huhn klein schneiden und in Öl scharf anbraten.",
            "Brokkoli und Karotten dazugeben.",
            "Sauce aus Sojasauce, Honig oder Zucker, Wasser und Speisestärke rühren.",
            "Sauce in die Pfanne geben und kurz eindicken lassen.",
            "Mit Reis servieren."
        ]
    },

    "3. Nasi Goreng Familienversion": {
        "info": {
            "time": "20 Min",
            "budget": "Günstig",
            "level": "Einfach",
            "family": "Mild / perfekt für Reste"
        },
        "description": clean_text("""
            Perfekt für Reisreste.
            Ei, Reis, Gemüse, Sojasauce — fertig.
            Wenig Aufwand, viel Nutzen.
        """),
        "ingredients": [
            "Reis oder Reisreste",
            "Eier",
            "Karotten",
            "TK-Gemüse oder Erbsen",
            "Zwiebel",
            "Knoblauch",
            "Sojasauce",
            "Öl",
            "Optional: Curry",
            "Optional: Sweet-Chili-Sauce"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Karotten",
                "TK-Gemüse oder Erbsen",
                "Zwiebel",
                "Knoblauch"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Eier",
                "Optional: Huhn"
            ],
            "🍚 Trockenware": [
                "Reis"
            ],
            "🥢 Saucen & Gewürze": [
                "Sojasauce",
                "Öl",
                "Optional: Curry",
                "Optional: Sweet-Chili-Sauce"
            ]
        },
        "steps": [
            "Reis vorkochen oder Reisreste verwenden.",
            "Zwiebel und Knoblauch anbraten.",
            "Gemüse dazugeben.",
            "Reis dazugeben und gut anrösten.",
            "Ei in die Pfanne geben und unterrühren.",
            "Mit Sojasauce und optional Curry abschmecken.",
            "Optional mit Sweet-Chili-Sauce servieren."
        ]
    },

    "4. Kokos-Curry mit Reis": {
        "info": {
            "time": "25–30 Min",
            "budget": "Günstig bis mittel",
            "level": "Einfach",
            "family": "Mild möglich"
        },
        "description": clean_text("""
            Warmes Kokos-Curry für stressige Tage.
            Reis, Gemüse, Kokosmilch und optional Huhn oder Tofu.
        """),
        "ingredients": [
            "Reis",
            "Kokosmilch",
            "Currypaste oder Currypulver",
            "Karotten",
            "Brokkoli oder TK-Gemüse",
            "Zwiebel",
            "Knoblauch",
            "Optional: Huhn oder Tofu",
            "Öl",
            "Sojasauce"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Karotten",
                "Brokkoli oder TK-Gemüse",
                "Zwiebel",
                "Knoblauch"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Optional: Huhn oder Tofu"
            ],
            "🍚 Trockenware": [
                "Reis"
            ],
            "🥢 Saucen & Gewürze": [
                "Kokosmilch",
                "Currypaste oder Currypulver",
                "Sojasauce",
                "Öl"
            ]
        },
        "steps": [
            "Reis kochen.",
            "Zwiebel und Knoblauch in Öl anbraten.",
            "Optional Huhn oder Tofu anbraten.",
            "Gemüse dazugeben.",
            "Kokosmilch und Curry dazugeben.",
            "10–15 Minuten köcheln lassen.",
            "Mit Sojasauce abschmecken und mit Reis servieren."
        ]
    },

    "5. Teriyaki-Nudelpfanne": {
        "info": {
            "time": "20–25 Min",
            "budget": "Günstig",
            "level": "Einfach",
            "family": "Süßlich / kinderfreundlich"
        },
        "description": clean_text("""
            Schnelle Nudelpfanne mit süß-salziger Teriyaki-Richtung.
            Gut für Tage, wo der Kopf keine Diskussion mehr will.
        """),
        "ingredients": [
            "Mie-Nudeln oder Spaghetti",
            "Karotten",
            "Paprika oder TK-Gemüse",
            "Zwiebel",
            "Knoblauch",
            "Sojasauce",
            "Honig oder Zucker",
            "Optional: Huhn",
            "Öl"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Karotten",
                "Paprika oder TK-Gemüse",
                "Zwiebel",
                "Knoblauch"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Optional: Huhn"
            ],
            "🍚 Trockenware": [
                "Mie-Nudeln oder Spaghetti"
            ],
            "🥢 Saucen & Gewürze": [
                "Sojasauce",
                "Honig oder Zucker",
                "Öl"
            ]
        },
        "steps": [
            "Nudeln kochen.",
            "Gemüse schneiden.",
            "Optional Huhn anbraten.",
            "Gemüse dazugeben und kurz braten.",
            "Sojasauce, Honig oder Zucker und etwas Wasser dazugeben.",
            "Nudeln untermischen und kurz ziehen lassen."
        ]
    },

    "6. Eierreis mit Gemüse": {
        "info": {
            "time": "15–20 Min",
            "budget": "Sehr günstig",
            "level": "Sehr einfach",
            "family": "Mild / schnell"
        },
        "description": clean_text("""
            Einer der besten Familienretter.
            Reis, Ei, Gemüse, Sojasauce.
            Schnell, günstig, warm.
        """),
        "ingredients": [
            "Reis",
            "Eier",
            "Karotten",
            "Erbsen oder TK-Gemüse",
            "Zwiebel",
            "Knoblauch",
            "Sojasauce",
            "Öl"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Karotten",
                "Erbsen oder TK-Gemüse",
                "Zwiebel",
                "Knoblauch"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Eier"
            ],
            "🍚 Trockenware": [
                "Reis"
            ],
            "🥢 Saucen & Gewürze": [
                "Sojasauce",
                "Öl"
            ]
        },
        "steps": [
            "Reis kochen oder Reisreste verwenden.",
            "Zwiebel und Knoblauch anbraten.",
            "Gemüse dazugeben.",
            "Reis dazugeben und anrösten.",
            "Eier dazugeben und unterrühren.",
            "Mit Sojasauce abschmecken."
        ]
    },

    "7. Erdnuss-Nudeln": {
        "info": {
            "time": "15–20 Min",
            "budget": "Günstig",
            "level": "Einfach",
            "family": "Cremig / mild"
        },
        "description": clean_text("""
            Cremige Erdnuss-Nudeln.
            Wenig Zutaten, viel Geschmack.
            Perfekt, wenn wenig Energie da ist.
        """),
        "ingredients": [
            "Nudeln",
            "Erdnussbutter",
            "Sojasauce",
            "Knoblauch",
            "Karotten",
            "Optional: Gurke",
            "Optional: Sweet-Chili-Sauce",
            "Wasser zum Verdünnen"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Karotten",
                "Knoblauch",
                "Optional: Gurke"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Optional: Huhn oder Tofu"
            ],
            "🍚 Trockenware": [
                "Nudeln"
            ],
            "🥢 Saucen & Gewürze": [
                "Erdnussbutter",
                "Sojasauce",
                "Optional: Sweet-Chili-Sauce"
            ]
        },
        "steps": [
            "Nudeln kochen.",
            "Erdnussbutter mit Sojasauce und warmem Wasser cremig rühren.",
            "Knoblauch kurz anbraten.",
            "Karotten dazugeben.",
            "Nudeln und Sauce untermischen.",
            "Optional mit Gurke oder Sweet-Chili servieren."
        ]
    },

    "8. Sweet-Chili-Huhn mit Reis": {
        "info": {
            "time": "25 Min",
            "budget": "Mittel",
            "level": "Einfach",
            "family": "Süß / mild scharf möglich"
        },
        "description": clean_text("""
            Sweet-Chili-Huhn ist schnell, einfach und sehr familientauglich.
            Reis dazu und fertig ist ein starkes Abendessen.
        """),
        "ingredients": [
            "Huhn",
            "Reis",
            "Karotten",
            "Paprika oder TK-Gemüse",
            "Knoblauch",
            "Sweet-Chili-Sauce",
            "Sojasauce",
            "Öl"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Karotten",
                "Paprika oder TK-Gemüse",
                "Knoblauch"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Huhn"
            ],
            "🍚 Trockenware": [
                "Reis"
            ],
            "🥢 Saucen & Gewürze": [
                "Sweet-Chili-Sauce",
                "Sojasauce",
                "Öl"
            ]
        },
        "steps": [
            "Reis kochen.",
            "Huhn klein schneiden und anbraten.",
            "Gemüse dazugeben.",
            "Sweet-Chili-Sauce und etwas Sojasauce dazugeben.",
            "Kurz einkochen lassen.",
            "Mit Reis servieren."
        ]
    },

    "9. Ramen mit Ei & Gemüse": {
        "info": {
            "time": "15–20 Min",
            "budget": "Günstig",
            "level": "Sehr einfach",
            "family": "Warm / schnell"
        },
        "description": clean_text("""
            Schnelle Ramen-Bowl für kalte oder müde Tage.
            Ei, Gemüse, Nudeln, Brühe.
            Kein Luxus, aber echte Entlastung.
        """),
        "ingredients": [
            "Ramen- oder Mie-Nudeln",
            "Eier",
            "Karotten",
            "Frühlingszwiebel oder normale Zwiebel",
            "Knoblauch",
            "Brühe",
            "Sojasauce",
            "Optional: TK-Gemüse"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Karotten",
                "Frühlingszwiebel oder normale Zwiebel",
                "Knoblauch",
                "Optional: TK-Gemüse"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Eier"
            ],
            "🍚 Trockenware": [
                "Ramen- oder Mie-Nudeln"
            ],
            "🥢 Saucen & Gewürze": [
                "Brühe",
                "Sojasauce"
            ]
        },
        "steps": [
            "Brühe erhitzen.",
            "Karotten und Gemüse kurz mitkochen.",
            "Nudeln dazugeben.",
            "Ei kochen oder direkt in die Suppe geben.",
            "Mit Sojasauce abschmecken.",
            "Warm servieren."
        ]
    },

    "10. Asia-Kraut-Wok mit Ei": {
        "info": {
            "time": "20 Min",
            "budget": "Sehr günstig",
            "level": "Einfach",
            "family": "Mild / gut für Resteküche"
        },
        "description": clean_text("""
            Kraut, Ei und Asia-Sauce.
            Einfach, günstig und überraschend gut.
            Cora sagt: kein Sidequest, nur Pfanne.
        """),
        "ingredients": [
            "Weißkraut oder Spitzkohl",
            "Eier",
            "Karotten",
            "Zwiebel",
            "Knoblauch",
            "Sojasauce",
            "Öl",
            "Optional: Reis oder Nudeln"
        ],
        "shopping": {
            "🛒 Obst & Gemüse": [
                "Weißkraut oder Spitzkohl",
                "Karotten",
                "Zwiebel",
                "Knoblauch"
            ],
            "🥩 Kühlung / Fleisch / Ei": [
                "Eier"
            ],
            "🍚 Trockenware": [
                "Optional: Reis oder Nudeln"
            ],
            "🥢 Saucen & Gewürze": [
                "Sojasauce",
                "Öl"
            ]
        },
        "steps": [
            "Kraut fein schneiden.",
            "Karotten, Zwiebel und Knoblauch vorbereiten.",
            "Zwiebel und Knoblauch in Öl anbraten.",
            "Kraut und Karotten dazugeben und braten.",
            "Eier dazugeben und unterrühren.",
            "Mit Sojasauce abschmecken.",
            "Optional mit Reis oder Nudeln servieren."
        ]
    }
}



# =========================================================
# DATA — CORA BACKSTUBE
# =========================================================
baking_recipes = {
    "1. Schneller Kakao-Blechkuchen": {
        "info": {
            "time": "25–30 Min Backzeit",
            "budget": "Günstig",
            "level": "Einfach",
            "family": "Kinderfreundlich"
        },
        "description": clean_text("""
            Einfacher Familienkuchen aus Standard-Zutaten.
            Perfekt, wenn Kinder etwas Süßes wollen und kein Extra-Einkauf passieren soll.
        """),
        "ingredients": [
            "250 g Mehl",
            "180 g Zucker",
            "3 Eier",
            "150 ml Milch",
            "100 ml Öl",
            "3 EL Kakao",
            "1 Pkg Backpulver"
        ],
        "missing_check": [
            "Mehl",
            "Zucker",
            "Eier",
            "Milch",
            "Öl oder Butter",
            "Kakao",
            "Backpulver"
        ],
        "steps": [
            "Backofen auf 180 °C Ober-/Unterhitze vorheizen.",
            "Mehl, Zucker, Kakao und Backpulver mischen.",
            "Eier, Milch und Öl dazugeben.",
            "Alles glatt rühren.",
            "Auf ein kleines Blech oder in eine Form geben.",
            "Ca. 25–30 Minuten backen.",
            "Abkühlen lassen und servieren."
        ]
    },
    "2. Cora Waffeln": {
        "info": {
            "time": "20 Min",
            "budget": "Sehr günstig",
            "level": "Einfach",
            "family": "Perfekt mit Kindern"
        },
        "description": clean_text("""
            Waffeln retten viele Nachmittage.
            Mehl, Milch, Eier, Zucker — fertig.
        """),
        "ingredients": [
            "250 g Mehl",
            "2 Eier",
            "300 ml Milch",
            "2 EL Zucker",
            "1 Prise Salz",
            "1 TL Backpulver",
            "Öl oder Butter fürs Waffeleisen"
        ],
        "missing_check": [
            "Mehl",
            "Eier",
            "Milch",
            "Zucker",
            "Backpulver",
            "Öl oder Butter"
        ],
        "steps": [
            "Alle Zutaten zu einem glatten Teig rühren.",
            "Waffeleisen vorheizen.",
            "Leicht einfetten.",
            "Waffeln portionsweise backen.",
            "Mit Zucker, Obst oder Marmelade servieren."
        ]
    },
    "3. Bananen-Pancakes": {
        "info": {
            "time": "15–20 Min",
            "budget": "Günstig",
            "level": "Sehr einfach",
            "family": "Gut für reife Bananen"
        },
        "description": clean_text("""
            Gut, wenn Bananen weg müssen.
            Schnell, weich, familientauglich.
        """),
        "ingredients": [
            "2 reife Bananen",
            "2 Eier",
            "120 g Mehl",
            "120 ml Milch",
            "1 TL Backpulver",
            "Öl oder Butter"
        ],
        "missing_check": [
            "Bananen",
            "Eier",
            "Mehl",
            "Milch",
            "Backpulver",
            "Öl oder Butter"
        ],
        "steps": [
            "Bananen zerdrücken.",
            "Eier, Mehl, Milch und Backpulver einrühren.",
            "Pfanne erhitzen und etwas Öl oder Butter verwenden.",
            "Kleine Pancakes ausbacken.",
            "Warm servieren."
        ]
    }
}


# =========================================================
# SESSION STATE
# =========================================================
if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = list(recipes.keys())[0]

if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

if "kitchen_mode" not in st.session_state:
    st.session_state.kitchen_mode = "🍲 Kochen"

if "page" not in st.session_state:
    st.session_state.page = "🏠 Start"

def go(page):
    st.session_state.page = page



# =========================================================
# CORA IMAGE
# =========================================================
if CORA_IMAGE is not None and CORA_IMAGE.exists():
    st.image(str(CORA_IMAGE), width="stretch")
else:
    st.error("Cora Bild nicht gefunden.")
    st.info(f"App-Ordner: {APP_DIR}")
    st.info("Lege ein Bild mit Cora im Namen in diesen Ordner. Beispiel: cora.png")


# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="cora-header">
    <div class="cora-title">🔥 Cora Family Kitchen</div>
    <div class="cora-subtitle">
        Schnell wählen. Schnell einkaufen. Schnell kochen.<br>
        Weniger Chaos im Kopf. Mehr Zeit zum Leben.
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION — DESKTOP BUTTONS + MOBILE DROPDOWN
# =========================================================
pages = ["🏠 Start", "🍳 Rezept", "🛒 Einkauf", "👨‍🍳 Kochen", "📸 Upload"]

st.markdown('<div class="nav-label">🧭 Schnellwahl</div>', unsafe_allow_html=True)

st.markdown('<div class="desktop-nav">', unsafe_allow_html=True)
nav_cols = st.columns(5)
for col, page_name in zip(nav_cols, pages):
    with col:
        st.button(page_name, key=f"nav_{page_name}", use_container_width=True, on_click=go, args=(page_name,))
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="mobile-nav">', unsafe_allow_html=True)
selected_page = st.selectbox(
    "Menü",
    pages,
    index=pages.index(st.session_state.page) if st.session_state.page in pages else 0,
    label_visibility="visible",
    key="mobile_menu"
)
st.markdown('</div>', unsafe_allow_html=True)

if selected_page != st.session_state.page:
    st.session_state.page = selected_page
    st.rerun()

st.markdown(
    f'<div class="list-item">📍 Aktuell offen: <b>{st.session_state.page}</b></div>',
    unsafe_allow_html=True
)

st.markdown('<div class="cora-separator"></div>', unsafe_allow_html=True)


# =========================================================
# SHARED RECIPE SELECTOR
# =========================================================
recipe_names = list(recipes.keys())
if st.session_state.selected_recipe not in recipe_names:
    st.session_state.selected_recipe = recipe_names[0]

def recipe_picker():
    st.markdown('<div class="section-title">🍳 Gericht wählen</div>', unsafe_allow_html=True)
    selected = st.radio(
        "Gericht auswählen",
        recipe_names,
        index=recipe_names.index(st.session_state.selected_recipe),
        label_visibility="collapsed",
        key="recipe_picker_radio"
    )
    st.session_state.selected_recipe = selected
    return recipes[selected], selected


def show_recipe_card(recipe, selected_recipe):
    description_html = recipe["description"].replace("\n", "<br>")
    st.markdown(f"""
    <div class="cora-card">
        <div class="card-title">{selected_recipe}</div>
        <div class="card-text">
            {description_html}
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# PAGE: START
# =========================================================
if st.session_state.page == "🏠 Start":
    st.markdown("""
    <div class="cora-card">
        <div class="card-title">Willkommen ❤️</div>
        <div class="card-text">
            Heute machen wir es einfach.<br>
            Kein Küchen-Chaos. Kein Einkaufs-Stress.<br><br>
            Cora sagt:<br>
            Erst schauen, was da ist. Dann entscheiden.
            Nicht alles im Kopf tragen.
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("🍳 Rezept starten", use_container_width=True, on_click=go, args=("🍳 Rezept",))
    with c2:
        st.button("🛒 Einkauf starten", use_container_width=True, on_click=go, args=("🛒 Einkauf",))
    with c3:
        st.button("📸 Bild hochladen", use_container_width=True, on_click=go, args=("📸 Upload",))

    st.markdown("""
    <div class="cora-card">
        <div class="card-title">💡 Cora Tipp</div>
        <div class="card-text">
            Ein Gericht. Eine Liste. Eine Route.<br>
            Schnell rein. Schnell raus.<br>
            Mehr Zeit zum Leben.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# PAGE: UPLOAD
# =========================================================
elif st.session_state.page == "📸 Upload":
    st.markdown("""
    <div class="cora-card">
        <div class="card-title">📸 Was ist da?</div>
        <div class="card-text">
            Keine Lust alles zu checken?<br>
            Mach 3 Bilder: Kühlschrank, Vorrat, Tiefkühl / Reste.<br><br>
            Cora sortiert. Cora zaubert Ideen. Was fehlt, kommt auf die Einkaufsliste.
        </div>
    </div>
    """, unsafe_allow_html=True)

    uploaded_photos = st.file_uploader(
        "📸 Bilder hochladen",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
        key="photo_upload",
        help="Kühlschrank, Vorrat oder Tiefkühl hochladen."
    )

    if uploaded_photos:
        st.markdown(f"""
        <div class="list-item">
            ✅ {len(uploaded_photos)} Bild(er) geladen. Für V1 reicht das als Foto-Flow.
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(3)
        for idx, photo in enumerate(uploaded_photos[:3]):
            with cols[idx % 3]:
                st.image(photo, width="stretch")

        if st.button("✨ Cora prüfen und sortieren", use_container_width=True):
            st.session_state["photos_checked"] = True

    if st.session_state.get("photos_checked"):
        demo_found_items = {
            "🍚 Basis": ["Reis", "Nudeln", "Kartoffeln"],
            "🥦 Gemüse / TK": ["TK Asia Gemüse", "Karotten", "Zwiebel"],
            "🥩 Eiweiß": ["Eier", "Putenfleisch oder Rest-Fleisch"],
            "🍰 Backen": ["Mehl", "Zucker", "Milch", "Kakao"]
        }
        show_found_items_card(demo_found_items)

        st.markdown("""
        <div class="cora-card">
            <div class="card-title">💡 Cora Ideen</div>
            <div class="card-text">
                🍲 Asia-Reis mit Gemüse und Ei<br>
                🍝 Nudelpfanne mit Karotten und Zwiebel<br>
                🥔 Kartoffelpfanne<br>
                🍰 Schneller Kakao-Blechkuchen
            </div>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# PAGE: RECIPE
# =========================================================
elif st.session_state.page == "🍳 Rezept":
    st.markdown('<div class="section-title">🧭 Was brauchst du jetzt?</div>', unsafe_allow_html=True)
    st.session_state.kitchen_mode = st.radio(
        "Modus wählen",
        ["🍲 Kochen", "🍰 Backen"],
        index=["🍲 Kochen", "🍰 Backen"].index(st.session_state.kitchen_mode) if st.session_state.kitchen_mode in ["🍲 Kochen", "🍰 Backen"] else 0,
        horizontal=True,
        label_visibility="collapsed",
        key="mode_recipe"
    )

    if st.session_state.kitchen_mode == "🍲 Kochen":
        st.markdown('<div class="section-title">🍳 Top 10 Asia — Was kochen wir heute?</div>', unsafe_allow_html=True)
        recipe, selected_recipe = recipe_picker()
        show_recipe_card(recipe, selected_recipe)
        show_info_card(recipe)
        show_simple_list("Zutaten", recipe["ingredients"], icon="🧾")

        c1, c2 = st.columns(2)
        with c1:
            st.button("🛒 Zur Einkaufsliste", use_container_width=True, on_click=go, args=("🛒 Einkauf",))
        with c2:
            st.button("👨‍🍳 Zu den Kochschritten", use_container_width=True, on_click=go, args=("👨‍🍳 Kochen",))

    else:
        st.markdown('<div class="section-title">🍰 Cora Backstube — einfach aus Vorrat</div>', unsafe_allow_html=True)
        baking_names = list(baking_recipes.keys())
        selected_baking = st.radio(
            "Backidee auswählen",
            baking_names,
            label_visibility="collapsed",
            key="baking_picker"
        )

        bake = baking_recipes[selected_baking]
        bake_description_html = bake["description"].replace("\n", "<br>")

        st.markdown(f"""
        <div class="cora-card">
            <div class="card-title">{selected_baking}</div>
            <div class="card-text">
                {bake_description_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

        show_info_card(bake)
        show_simple_list("Back-Zutaten", bake["ingredients"], icon="🧾")

        st.markdown('<div class="section-title">🛒 Fehlt etwas?</div>', unsafe_allow_html=True)
        for item in bake["missing_check"]:
            st.checkbox(item, key=f"bake_missing_{selected_baking}_{item}")

        st.markdown('<div class="section-title">👩‍🍳 Backschritte</div>', unsafe_allow_html=True)
        for i, step in enumerate(bake["steps"], start=1):
            st.markdown(f"""
            <div class="list-item">
                <b>{i}.</b> {step}
            </div>
            """, unsafe_allow_html=True)


# =========================================================
# PAGE: SHOPPING
# =========================================================
elif st.session_state.page == "🛒 Einkauf":
    recipe, selected_recipe = recipe_picker()
    st.markdown('<div class="section-title">🛒 Einkaufsliste nach Marktstruktur</div>', unsafe_allow_html=True)

    for category, items in recipe["shopping"].items():
        st.markdown(f'<div class="shopping-category-title">{category}</div>', unsafe_allow_html=True)

        for item in items:
            checkbox_key = f"{st.session_state.reset_counter}_{selected_recipe}_{category}_{item}"
            st.checkbox(item, key=checkbox_key)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("✅ Einkaufsliste zurücksetzen", use_container_width=True):
        st.session_state.reset_counter += 1
        st.rerun()

    st.markdown("""
    <div class="cora-card">
        <div class="card-title">💰 Lohnt sich das?</div>
        <div class="card-text">
            Später prüft Cora hier Aktionen, Benzin, Zeit und Stress.<br><br>
            Nicht jedes Angebot spart Geld.<br>
            Manchmal kostet der Weg mehr als die Aktion.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="shopping-category-title">Fehlt oft für Kochen / Backen</div>', unsafe_allow_html=True)
    for item in ["Sojasauce", "Backpulver", "Butter", "Eier", "Milch", "TK Gemüse", "Putenfleisch"]:
        st.checkbox(item, key=f"quick_shop_{item}")


# =========================================================
# PAGE: COOKING
# =========================================================
elif st.session_state.page == "👨‍🍳 Kochen":
    recipe, selected_recipe = recipe_picker()
    show_recipe_card(recipe, selected_recipe)

    st.markdown('<div class="section-title">👨‍🍳 Kochschritte</div>', unsafe_allow_html=True)

    for i, step in enumerate(recipe["steps"], start=1):
        st.markdown(f"""
        <div class="list-item">
            <b>{i}.</b> {step}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cora-card">
        <div class="card-title">🔥 Cora sagt</div>
        <div class="card-text">
            Pfanne heiß. Kopf ruhig.<br>
            Schritt für Schritt. Kein Küchen-Chaos.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# DEBUG
# =========================================================
with st.expander("🛠 Debug"):
    st.write("Aktuelle Seite:", st.session_state.page)
    st.write("Gewähltes Rezept:", st.session_state.selected_recipe)
    st.write("Modus:", st.session_state.kitchen_mode)
