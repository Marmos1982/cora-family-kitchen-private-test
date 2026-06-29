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
    max-width: 780px;
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
    border-radius: 16px;
    font-weight: 950;
    padding: 0.82rem 1rem;
    width: 100%;
    min-height: 48px;
    box-shadow: 0 0 20px rgba(255, 120, 20, 0.24);
    white-space: normal;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #ffb34d, #ff6b2a);
    color: #000000 !important;
}

/* Navigation: bigger touch targets, stable on desktop and mobile */
div[data-testid="column"] .stButton > button {
    min-height: 52px;
    padding: 0.70rem 0.55rem;
    font-size: 0.96rem;
    white-space: normal;
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
# DATA — FAMILIEN-BASICS / VORRAT
# =========================================================
family_recipes = {
    "11. Nudeln mit schneller Tomatensauce": {
        "info": {"time": "15–20 Min", "budget": "Sehr günstig", "level": "Sehr einfach", "family": "Kinderklassiker"},
        "description": clean_text("""
            Der Familienretter, wenn wenig Energie da ist.
            Nudeln, Tomatensauce, Gewürze — warm, schnell, ehrlich.
        """),
        "ingredients": ["Nudeln", "Passierte Tomaten oder Tomatensauce", "Zwiebel", "Knoblauch", "Öl", "Salz", "Optional: Käse", "Optional: Kräuter"],
        "shopping": {
            "🍚 Trockenware": ["Nudeln"],
            "🛒 Obst & Gemüse": ["Zwiebel", "Knoblauch"],
            "🥫 Vorrat / Dosen": ["Passierte Tomaten oder Tomatensauce"],
            "🥢 Saucen & Gewürze": ["Öl", "Salz", "Optional: Kräuter"],
            "🥛 Kühlung": ["Optional: Käse"]
        },
        "steps": ["Nudeln kochen.", "Zwiebel und Knoblauch klein schneiden und in Öl anbraten.", "Tomatensauce dazugeben und würzen.", "Kurz köcheln lassen.", "Nudeln mit Sauce mischen.", "Optional Käse darüber."]
    },
    "12. Kartoffelpfanne mit Ei": {
        "info": {"time": "25 Min", "budget": "Sehr günstig", "level": "Einfach", "family": "Sättigend / Vorrat"},
        "description": clean_text("""
            Kartoffeln da? Eier da? Dann ist Essen fast fertig.
            Wenig Zutaten, viel Sättigung, perfekt für Resteküche.
        """),
        "ingredients": ["Kartoffeln", "Eier", "Zwiebel", "Öl oder Butter", "Salz", "Optional: Speck, Käse oder Gemüse"],
        "shopping": {
            "🥔 Basis": ["Kartoffeln"],
            "🥛 Kühlung / Ei": ["Eier", "Optional: Käse"],
            "🛒 Obst & Gemüse": ["Zwiebel", "Optional: Gemüse"],
            "🥢 Basics": ["Öl oder Butter", "Salz"],
            "🥩 Optional Fleisch": ["Optional: Speck"]
        },
        "steps": ["Kartoffeln kochen oder vorhandene Kartoffeln verwenden.", "Kartoffeln in Scheiben schneiden.", "Zwiebel in Öl oder Butter anbraten.", "Kartoffeln dazugeben und goldbraun braten.", "Eier darüber geben und stocken lassen.", "Würzen und servieren."]
    },
    "13. Reis mit Ei und Gemüse": {
        "info": {"time": "15–20 Min", "budget": "Sehr günstig", "level": "Sehr einfach", "family": "Reste-Retter"},
        "description": clean_text("""
            Reis ist da, Eier sind da, Gemüse ist egal ob frisch oder TK.
            Das ist genau Cora: aus wenig ein Essen machen.
        """),
        "ingredients": ["Reis oder Reisreste", "Eier", "TK-Gemüse oder Karotten", "Zwiebel", "Öl", "Salz", "Optional: Sojasauce"],
        "shopping": {
            "🍚 Basis": ["Reis"],
            "🥛 Kühlung / Ei": ["Eier"],
            "🛒 Gemüse": ["TK-Gemüse oder Karotten", "Zwiebel"],
            "🥢 Basics": ["Öl", "Salz", "Optional: Sojasauce"]
        },
        "steps": ["Reis kochen oder Reisreste verwenden.", "Zwiebel und Gemüse in Öl anbraten.", "Reis dazugeben und anrösten.", "Eier einrühren.", "Mit Salz oder Sojasauce abschmecken."]
    },
    "14. Schneller Nudelauflauf": {
        "info": {"time": "35–40 Min", "budget": "Günstig", "level": "Einfach", "family": "Ofen / satt"},
        "description": clean_text("""
            Wenn Nudeln, Milch und Käse da sind, wird daraus ein Auflauf.
            Gut, wenn alle satt werden sollen und der Ofen den Rest macht.
        """),
        "ingredients": ["Nudeln", "Milch oder Obers", "Käse", "Eier", "Salz", "Optional: Schinken, Gemüse oder Tomatensauce"],
        "shopping": {
            "🍚 Trockenware": ["Nudeln"],
            "🥛 Kühlung / Ei": ["Milch oder Obers", "Käse", "Eier"],
            "🥩 Optional": ["Optional: Schinken"],
            "🛒 Gemüse / Sauce": ["Optional: Gemüse oder Tomatensauce"],
            "🥢 Gewürze": ["Salz"]
        },
        "steps": ["Nudeln vorkochen.", "Milch/Obers mit Ei und Salz verrühren.", "Optional Gemüse oder Schinken dazugeben.", "Alles in eine Form geben.", "Käse darüber.", "Bei 180 °C ca. 25 Minuten backen."]
    },
    "15. Reste-Suppe aus Kartoffeln und Gemüse": {
        "info": {"time": "25–30 Min", "budget": "Sehr günstig", "level": "Einfach", "family": "Warm / ruhig"},
        "description": clean_text("""
            Suppe ist perfekt, wenn Reste weg müssen.
            Kartoffeln, Gemüse, Brühe — fertig ist ein ruhiges Essen.
        """),
        "ingredients": ["Kartoffeln", "Gemüse oder TK-Gemüse", "Zwiebel", "Brühe", "Öl", "Optional: Würstel, Brot oder Obers"],
        "shopping": {
            "🥔 Basis": ["Kartoffeln"],
            "🛒 Gemüse": ["Gemüse oder TK-Gemüse", "Zwiebel"],
            "🥢 Gewürze": ["Brühe", "Öl"],
            "🥩 Optional": ["Optional: Würstel"],
            "🍞 Optional": ["Optional: Brot"],
            "🥛 Optional": ["Optional: Obers"]
        },
        "steps": ["Zwiebel in Öl anbraten.", "Kartoffeln und Gemüse klein schneiden.", "Alles mit Brühe aufgießen.", "20 Minuten kochen.", "Optional pürieren.", "Optional Würstel, Brot oder Obers dazu."]
    },
    "16. Palatschinken pikant gefüllt": {
        "info": {"time": "25 Min", "budget": "Günstig", "level": "Einfach", "family": "Kinder mögen es"},
        "description": clean_text("""
            Wenn Mehl, Milch und Eier da sind, geht immer etwas.
            Pikant gefüllt wird daraus ein richtiges Essen.
        """),
        "ingredients": ["Mehl", "Milch", "Eier", "Salz", "Öl", "Optional: Käse, Schinken, Gemüse oder Reste"],
        "shopping": {
            "🍚 Vorrat": ["Mehl"],
            "🥛 Kühlung / Ei": ["Milch", "Eier", "Optional: Käse"],
            "🥩 Optional": ["Optional: Schinken"],
            "🛒 Optional": ["Optional: Gemüse oder Reste"],
            "🥢 Basics": ["Salz", "Öl"]
        },
        "steps": ["Mehl, Milch, Eier und Salz zu Teig rühren.", "Palatschinken dünn ausbacken.", "Mit Käse, Schinken, Gemüse oder Resten füllen.", "Kurz einklappen oder überbacken."]
    },
    "17. Ofenkartoffeln mit Dip": {
        "info": {"time": "40 Min", "budget": "Sehr günstig", "level": "Sehr einfach", "family": "Wenig Arbeit"},
        "description": clean_text("""
            Kartoffeln in den Ofen, Dip dazu, fertig.
            Wenig Kopf, wenig Chaos, trotzdem warm und sättigend.
        """),
        "ingredients": ["Kartoffeln", "Öl", "Salz", "Joghurt oder Sauerrahm", "Knoblauch", "Optional: Käse oder Gemüse"],
        "shopping": {
            "🥔 Basis": ["Kartoffeln"],
            "🥛 Kühlung": ["Joghurt oder Sauerrahm", "Optional: Käse"],
            "🛒 Gemüse": ["Knoblauch", "Optional: Gemüse"],
            "🥢 Basics": ["Öl", "Salz"]
        },
        "steps": ["Kartoffeln waschen und schneiden.", "Mit Öl und Salz mischen.", "Bei 200 °C ca. 30–35 Minuten backen.", "Dip aus Joghurt/Sauerrahm, Knoblauch und Salz rühren.", "Servieren."]
    },
    "18. Schnelle Grießnockerl- oder Nudelsuppe": {
        "info": {"time": "15–25 Min", "budget": "Sehr günstig", "level": "Einfach", "family": "Krank / müde / warm"},
        "description": clean_text("""
            Wenn der Tag schwer ist, ist Suppe oft genug.
            Warm, schnell, kein Drama.
        """),
        "ingredients": ["Brühe", "Suppennudeln oder Grießnockerl", "Karotten", "Optional: Ei", "Optional: Schnittlauch"],
        "shopping": {
            "🥢 Gewürze": ["Brühe"],
            "🍚 Trockenware": ["Suppennudeln oder Grießnockerl"],
            "🛒 Gemüse": ["Karotten", "Optional: Schnittlauch"],
            "🥛 Optional": ["Optional: Ei"]
        },
        "steps": ["Brühe erhitzen.", "Karotten klein schneiden und mitkochen.", "Suppennudeln oder Nockerl dazugeben.", "Kochen bis alles weich ist.", "Optional Ei oder Schnittlauch dazu."]
    },
    "19. Toast-Pizza Familienrettung": {
        "info": {"time": "10–15 Min", "budget": "Günstig", "level": "Sehr einfach", "family": "Kinder / schnell"},
        "description": clean_text("""
            Toast, Tomatensauce, Käse — mehr braucht es oft nicht.
            Perfekt, wenn wirklich keine Energie mehr da ist.
        """),
        "ingredients": ["Toast oder Brot", "Tomatensauce oder Ketchup", "Käse", "Optional: Schinken, Mais, Paprika oder Reste"],
        "shopping": {
            "🍞 Brot": ["Toast oder Brot"],
            "🥫 Sauce": ["Tomatensauce oder Ketchup"],
            "🥛 Kühlung": ["Käse"],
            "🥩 Optional": ["Optional: Schinken"],
            "🛒 Optional": ["Optional: Mais, Paprika oder Reste"]
        },
        "steps": ["Toast oder Brot auf ein Blech legen.", "Mit Sauce bestreichen.", "Käse und Belag darauf.", "Bei 200 °C ca. 8–10 Minuten backen."]
    },
    "20. Milchreis / süßer Reis": {
        "info": {"time": "30 Min", "budget": "Sehr günstig", "level": "Einfach", "family": "Süß / sättigend"},
        "description": clean_text("""
            Wenn Reis und Milch da sind, wird daraus ein warmes süßes Essen.
            Gut für Kinder, Abendessen oder Restetag.
        """),
        "ingredients": ["Reis oder Milchreis", "Milch", "Zucker", "Zimt", "Optional: Apfelmus oder Obst"],
        "shopping": {
            "🍚 Basis": ["Reis oder Milchreis"],
            "🥛 Kühlung": ["Milch"],
            "🍚 Vorrat / Süß": ["Zucker", "Zimt"],
            "🛒 Optional": ["Optional: Apfelmus oder Obst"]
        },
        "steps": ["Milch erhitzen.", "Reis dazugeben und langsam weich kochen.", "Regelmäßig rühren.", "Mit Zucker und Zimt abschmecken.", "Optional mit Apfelmus oder Obst servieren."]
    }
}

recipes.update(family_recipes)





# =========================================================
# DATA — CORA BACKSTUBE
# =========================================================
baking_recipes = {
    "1. Schneller Kakao-Blechkuchen": {
        "info": {"time": "25–30 Min", "budget": "Günstig", "level": "Einfach", "family": "Kinderfreundlich"},
        "description": clean_text("""
            Einfacher Familienkuchen aus Standard-Zutaten.
            Perfekt, wenn Kinder etwas Süßes wollen und kein Extra-Einkauf passieren soll.
        """),
        "ingredients": ["250 g Mehl", "180 g Zucker", "3 Eier", "150 ml Milch", "100 ml Öl", "3 EL Kakao", "1 Pkg Backpulver"],
        "shopping": {
            "🍚 Vorrat / Backen": ["Mehl", "Zucker", "Kakao", "Backpulver"],
            "🥛 Kühlung / Ei": ["Eier", "Milch"],
            "🥢 Basics": ["Öl oder Butter"]
        },
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
        "info": {"time": "20 Min", "budget": "Sehr günstig", "level": "Einfach", "family": "Perfekt mit Kindern"},
        "description": clean_text("""
            Waffeln retten viele Nachmittage.
            Mehl, Milch, Eier, Zucker — fertig.
        """),
        "ingredients": ["250 g Mehl", "2 Eier", "300 ml Milch", "2 EL Zucker", "1 Prise Salz", "1 TL Backpulver", "Öl oder Butter fürs Waffeleisen"],
        "shopping": {
            "🍚 Vorrat / Backen": ["Mehl", "Zucker", "Backpulver", "Salz"],
            "🥛 Kühlung / Ei": ["Eier", "Milch"],
            "🥢 Basics": ["Öl oder Butter"]
        },
        "steps": [
            "Alle Zutaten zu einem glatten Teig rühren.",
            "Waffeleisen vorheizen.",
            "Leicht einfetten.",
            "Waffeln portionsweise backen.",
            "Mit Zucker, Obst oder Marmelade servieren."
        ]
    },
    "3. Bananen-Pancakes": {
        "info": {"time": "15–20 Min", "budget": "Günstig", "level": "Sehr einfach", "family": "Gut für reife Bananen"},
        "description": clean_text("""
            Gut, wenn Bananen weg müssen.
            Schnell, weich, familientauglich.
        """),
        "ingredients": ["2 reife Bananen", "2 Eier", "120 g Mehl", "120 ml Milch", "1 TL Backpulver", "Öl oder Butter"],
        "shopping": {
            "🛒 Obst": ["Bananen"],
            "🍚 Vorrat / Backen": ["Mehl", "Backpulver"],
            "🥛 Kühlung / Ei": ["Eier", "Milch"],
            "🥢 Basics": ["Öl oder Butter"]
        },
        "steps": [
            "Bananen zerdrücken.",
            "Eier, Mehl, Milch und Backpulver einrühren.",
            "Pfanne erhitzen und etwas Öl oder Butter verwenden.",
            "Kleine Pancakes ausbacken.",
            "Warm servieren."
        ]
    },
    "4. Apfel-Zimt-Blechkuchen": {
        "info": {"time": "35–40 Min", "budget": "Günstig", "level": "Einfach", "family": "Wochenende / Besuch"},
        "description": clean_text("""
            Ein einfacher Kuchen, wenn Äpfel da sind.
            Warm, weich, familientauglich und ohne komplizierte Schritte.
        """),
        "ingredients": ["3 Äpfel", "250 g Mehl", "150 g Zucker", "3 Eier", "120 ml Milch", "100 ml Öl", "1 Pkg Backpulver", "Zimt"],
        "shopping": {
            "🛒 Obst": ["Äpfel"],
            "🍚 Vorrat / Backen": ["Mehl", "Zucker", "Backpulver", "Zimt"],
            "🥛 Kühlung / Ei": ["Eier", "Milch"],
            "🥢 Basics": ["Öl oder Butter"]
        },
        "steps": [
            "Backofen auf 180 °C vorheizen.",
            "Äpfel schälen oder gut waschen und klein schneiden.",
            "Mehl, Zucker, Backpulver und Zimt mischen.",
            "Eier, Milch und Öl dazugeben und rühren.",
            "Äpfel unterheben.",
            "In Form oder Blech geben und ca. 30–35 Minuten backen."
        ]
    },
    "5. Schoko-Muffins schnell": {
        "info": {"time": "20–25 Min", "budget": "Günstig", "level": "Einfach", "family": "Kinder / Schule"},
        "description": clean_text("""
            Kleine Portionen, schnell fertig.
            Gut für Kinder, Besuch oder wenn etwas Süßes gebraucht wird.
        """),
        "ingredients": ["200 g Mehl", "120 g Zucker", "2 Eier", "120 ml Milch", "80 ml Öl", "2 EL Kakao", "1/2 Pkg Backpulver", "Optional: Schokostücke"],
        "shopping": {
            "🍚 Vorrat / Backen": ["Mehl", "Zucker", "Kakao", "Backpulver", "Optional: Schokostücke"],
            "🥛 Kühlung / Ei": ["Eier", "Milch"],
            "🥢 Basics": ["Öl oder Butter"]
        },
        "steps": [
            "Backofen auf 180 °C vorheizen.",
            "Trockene Zutaten mischen.",
            "Eier, Milch und Öl dazugeben.",
            "Kurz rühren, nicht übertreiben.",
            "In Muffinformen füllen.",
            "Ca. 18–22 Minuten backen."
        ]
    },
    "6. Arme Ritter süß": {
        "info": {"time": "10–15 Min", "budget": "Sehr günstig", "level": "Sehr einfach", "family": "Reste retten"},
        "description": clean_text("""
            Perfekt für altes Brot oder Toast.
            Süß, schnell und fast immer mit Dingen möglich, die daheim sind.
        """),
        "ingredients": ["Altes Brot oder Toast", "2 Eier", "150 ml Milch", "Zucker", "Zimt", "Butter oder Öl"],
        "shopping": {
            "🍞 Brot / Vorrat": ["Altes Brot oder Toast"],
            "🥛 Kühlung / Ei": ["Eier", "Milch"],
            "🍚 Vorrat / Backen": ["Zucker", "Zimt"],
            "🥢 Basics": ["Butter oder Öl"]
        },
        "steps": [
            "Eier, Milch, Zucker und Zimt verquirlen.",
            "Brot oder Toast kurz darin wenden.",
            "In Butter oder Öl goldbraun braten.",
            "Warm servieren."
        ]
    },
    "7. Joghurt-Becherkuchen": {
        "info": {"time": "30–35 Min", "budget": "Günstig", "level": "Einfach", "family": "Ohne Waage möglich"},
        "description": clean_text("""
            Becherkuchen ist perfekt, wenn man nicht lang messen will.
            Joghurtbecher als Maß, fertig.
        """),
        "ingredients": ["1 Becher Joghurt", "2 Becher Mehl", "1 Becher Zucker", "1/2 Becher Öl", "3 Eier", "1 Pkg Backpulver", "Optional: Kakao oder Obst"],
        "shopping": {
            "🥛 Kühlung / Ei": ["Joghurt", "Eier"],
            "🍚 Vorrat / Backen": ["Mehl", "Zucker", "Backpulver", "Optional: Kakao"],
            "🥢 Basics": ["Öl"],
            "🛒 Obst": ["Optional: Obst"]
        },
        "steps": [
            "Backofen auf 180 °C vorheizen.",
            "Joghurt in eine Schüssel geben und Becher als Maß behalten.",
            "Alle Zutaten dazugeben und glatt rühren.",
            "Optional Kakao oder Obst unterheben.",
            "In eine Form geben und ca. 30 Minuten backen."
        ]
    },
    "8. Schnelle Zimtschnecken aus Blätterteig": {
        "info": {"time": "20 Min", "budget": "Günstig bis mittel", "level": "Sehr einfach", "family": "Schnell / Besuch"},
        "description": clean_text("""
            Wenn Blätterteig da ist, geht das fast ohne Denken.
            Aufrollen, schneiden, backen.
        """),
        "ingredients": ["1 Rolle Blätterteig", "Butter", "Zucker", "Zimt", "Optional: Glasur aus Staubzucker und wenig Wasser"],
        "shopping": {
            "🥛 Kühlung": ["Blätterteig", "Butter"],
            "🍚 Vorrat / Backen": ["Zucker", "Zimt", "Optional: Staubzucker"]
        },
        "steps": [
            "Backofen nach Packung vorheizen.",
            "Blätterteig ausrollen.",
            "Mit Butter bestreichen und Zucker/Zimt darüber streuen.",
            "Einrollen und in Scheiben schneiden.",
            "Ca. 12–15 Minuten backen.",
            "Optional mit Glasur beträufeln."
        ]
    },
    "9. Kinder-Kekse einfach": {
        "info": {"time": "30 Min", "budget": "Günstig", "level": "Einfach", "family": "Kinder helfen mit"},
        "description": clean_text("""
            Einfache Kekse zum Ausstechen oder Formen.
            Gut, wenn Kinder mithelfen wollen.
        """),
        "ingredients": ["250 g Mehl", "100 g Zucker", "125 g Butter", "1 Ei", "1 Prise Salz", "Optional: Vanillezucker"],
        "shopping": {
            "🍚 Vorrat / Backen": ["Mehl", "Zucker", "Salz", "Optional: Vanillezucker"],
            "🥛 Kühlung / Ei": ["Butter", "Ei"]
        },
        "steps": [
            "Alle Zutaten zu einem Teig kneten.",
            "Kurz kalt stellen, wenn Zeit ist.",
            "Ausrollen oder kleine Kugeln formen.",
            "Bei 180 °C ca. 10–12 Minuten backen.",
            "Abkühlen lassen."
        ]
    },
    "10. Palatschinken / Pancakes Basis": {
        "info": {"time": "15–20 Min", "budget": "Sehr günstig", "level": "Einfach", "family": "Süß oder herzhaft"},
        "description": clean_text("""
            Kein klassisches Backrohr-Rezept, aber ein Familienretter.
            Mehl, Milch, Eier — daraus wird immer etwas.
        """),
        "ingredients": ["200 g Mehl", "2 Eier", "350 ml Milch", "1 Prise Salz", "Öl oder Butter für die Pfanne", "Optional: Marmelade, Nutella, Apfelmus"],
        "shopping": {
            "🍚 Vorrat / Backen": ["Mehl", "Salz", "Optional: Marmelade / Nutella / Apfelmus"],
            "🥛 Kühlung / Ei": ["Eier", "Milch"],
            "🥢 Basics": ["Öl oder Butter"]
        },
        "steps": [
            "Mehl, Eier, Milch und Salz glatt rühren.",
            "Pfanne erhitzen und leicht fetten.",
            "Dünne Palatschinken ausbacken.",
            "Süß oder herzhaft füllen.",
            "Sofort servieren."
        ]
    }
}


# =========================================================
# SESSION STATE
# =========================================================
if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = list(recipes.keys())[0]

if "selected_baking" not in st.session_state:
    st.session_state.selected_baking = list(baking_recipes.keys())[0]

if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

if "view" not in st.session_state:
    st.session_state.view = "🏠 Start"

if "photos_checked" not in st.session_state:
    st.session_state.photos_checked = False

if "recipe_history" not in st.session_state:
    st.session_state.recipe_history = []

if "favorite_recipes" not in st.session_state:
    st.session_state.favorite_recipes = []


# =========================================================
# EXTRA HELPERS
# =========================================================
def set_view(view_name):
    st.session_state.view = view_name


def add_history(kind, name):
    """Keep a small local session history without duplicates."""
    entry = {"kind": kind, "name": name}
    current = st.session_state.get("recipe_history", [])
    current = [item for item in current if not (item.get("kind") == kind and item.get("name") == name)]
    current.insert(0, entry)
    st.session_state.recipe_history = current[:8]


def toggle_favorite(kind, name):
    key = f"{kind}|{name}"
    favorites = st.session_state.get("favorite_recipes", [])
    if key in favorites:
        favorites.remove(key)
    else:
        favorites.insert(0, key)
    st.session_state.favorite_recipes = favorites[:12]


def is_favorite(kind, name):
    return f"{kind}|{name}" in st.session_state.get("favorite_recipes", [])


def open_history_item(kind, name):
    if kind == "cook" and name in recipes:
        st.session_state.selected_recipe = name
        set_view("🍲 Kochen")
    elif kind == "bake" and name in baking_recipes:
        st.session_state.selected_baking = name
        set_view("🍰 Backen")


def render_history():
    st.markdown('<div class="section-title">🕘 Verlauf & Favoriten</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="cora-card">
        <div class="card-title">🕘 Zuletzt geöffnet</div>
        <div class="card-text">
            Cora merkt sich in dieser Sitzung, was du zuletzt gekocht oder gebacken hast.<br>
            Schnell wiederfinden. Liste nochmal öffnen. Favorit markieren.
        </div>
    </div>
    """, unsafe_allow_html=True)

    history = st.session_state.get("recipe_history", [])
    if not history:
        st.markdown('<div class="list-item">Noch kein Verlauf. Öffne ein Rezept oder eine Backidee, dann erscheint es hier.</div>', unsafe_allow_html=True)
    else:
        for idx, item in enumerate(history):
            kind = item.get("kind")
            name = item.get("name")
            icon = "🍲" if kind == "cook" else "🍰"
            fav = "⭐" if is_favorite(kind, name) else "☆"
            st.markdown(f'<div class="list-item">{icon} {fav} {name}</div>', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("🔁 Öffnen", key=f"hist_open_{idx}_{kind}"):
                    open_history_item(kind, name)
                    st.rerun()
            with c2:
                if st.button("⭐ Favorit", key=f"hist_fav_{idx}_{kind}"):
                    toggle_favorite(kind, name)
                    st.rerun()
            with c3:
                if kind == "cook":
                    if st.button("🛒 Liste", key=f"hist_shop_{idx}_{kind}"):
                        st.session_state.selected_recipe = name
                        set_view("🛒 Einkauf")
                        st.rerun()
                else:
                    if st.button("🛒 Back-Liste", key=f"hist_bakeshop_{idx}_{kind}"):
                        st.session_state.selected_baking = name
                        set_view("🍰 Backen")
                        st.rerun()

    favorites = st.session_state.get("favorite_recipes", [])
    if favorites:
        st.markdown('<div class="section-title">⭐ Familienfavoriten</div>', unsafe_allow_html=True)
        for idx, fav_key in enumerate(favorites[:8]):
            try:
                kind, name = fav_key.split("|", 1)
            except ValueError:
                continue
            icon = "🍲" if kind == "cook" else "🍰"
            st.markdown(f'<div class="list-item">{icon} ⭐ {name}</div>', unsafe_allow_html=True)

    c_clear, c_home = st.columns(2)
    with c_clear:
        if st.button("🧹 Verlauf löschen", key="clear_history"):
            st.session_state.recipe_history = []
            st.rerun()
    with c_home:
        if st.button("🏠 Zur Hauptansicht", key="history_home"):
            set_view("🏠 Start")
            st.rerun()


def show_found_items_card(items_by_category):
    st.markdown('<div class="section-title">✨ Cora hat sortiert</div>', unsafe_allow_html=True)
    for category, items in items_by_category.items():
        st.markdown(f'<div class="shopping-category-title">{category}</div>', unsafe_allow_html=True)
        for item in items:
            st.markdown(f'<div class="list-item">✅ {item}</div>', unsafe_allow_html=True)


def build_export_text(title, name, shopping, prefix="shop"):
    open_lines = []
    done_lines = []
    total_count = 0
    done_count = 0

    for category, items in shopping.items():
        category_open = []
        category_done = []
        for item in items:
            key = f"{prefix}_{st.session_state.reset_counter}_{name}_{category}_{item}"
            is_done = bool(st.session_state.get(key, False))
            total_count += 1
            if is_done:
                done_count += 1
                category_done.append(f"✅ {item}")
            else:
                category_open.append(f"☐ {item}")

        if category_open:
            open_lines.append(category)
            open_lines.extend(category_open)
            open_lines.append("")
        if category_done:
            done_lines.append(category)
            done_lines.extend(category_done)
            done_lines.append("")

    open_count = total_count - done_count
    lines = [
        "🛒 Cora Einkaufsliste",
        "",
        f"{title}: {name}",
        "",
        "NOCH KAUFEN",
    ]
    lines.extend(open_lines if open_lines else ["Alles erledigt ✅", ""])
    lines.append("ERLEDIGT")
    lines.extend(done_lines if done_lines else ["Noch nichts abgehakt.", ""])
    lines.extend([
        "STATUS",
        f"✅ Erledigt: {done_count} / {total_count}",
        f"☐ Noch offen: {open_count}",
    ])
    return "\n".join(lines), done_count, open_count, total_count


def render_shopping_mode(title, name, shopping, prefix="shop"):
    st.markdown('<div class="section-title">🛒 Cora Einkaufsmodus — abhaken fertig</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="cora-card">
        <div class="card-title">🛒 Entspannt einkaufen</div>
        <div class="card-text">
            Im Geschäft musst du Cora nicht alles erzählen.<br>
            Liste öffnen. Artikel abhaken. Weitergehen.<br><br>
            Wenn du festhängst: Cora fragen.<br>
            Beispiel: ausverkauft, Budget knapp oder Aktion unsicher.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for category, items in shopping.items():
        st.markdown(f'<div class="shopping-category-title">{category}</div>', unsafe_allow_html=True)
        for item in items:
            key = f"{prefix}_{st.session_state.reset_counter}_{name}_{category}_{item}"
            st.checkbox(item, key=key)

    shopping_text, done_count, open_count, total_count = build_export_text(title, name, shopping, prefix=prefix)

    st.markdown(f"""
    <div class="cora-card">
        <div class="card-title">📌 Einkaufsstand</div>
        <div class="card-text">
            ✅ Erledigt: <b>{done_count}</b> / {total_count}<br>
            ⏳ Noch offen: <b>{open_count}</b><br><br>
            Cora sagt: Nicht reden. Nicht denken. Nur abhaken.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📋 Fertige Liste anzeigen / kopieren"):
        st.text_area("Cora Einkaufsliste", shopping_text, height=300, label_visibility="collapsed")

    st.download_button(
        label="⬇️ Einkaufsliste als TXT speichern",
        data=shopping_text,
        file_name="cora_einkaufsliste.txt",
        mime="text/plain"
    )

    col_reset, col_done = st.columns(2)
    with col_reset:
        if st.button("🔄 Liste zurücksetzen", key=f"reset_{prefix}"):
            st.session_state.reset_counter += 1
            st.rerun()
    with col_done:
        if st.button("✅ Einkauf fertig", key=f"done_{prefix}"):
            st.success("Einkauf erledigt. Cora sagt: Stark. Heim, kochen, fertig.")


def render_recipe(recipe_name):
    add_history("cook", recipe_name)
    recipe = recipes[recipe_name]
    description_html = recipe["description"].replace("\n", "<br>")
    st.markdown(f"""
    <div class="cora-card">
        <div class="card-title">{recipe_name}</div>
        <div class="card-text">{description_html}</div>
    </div>
    """, unsafe_allow_html=True)
    show_info_card(recipe)
    show_simple_list("Zutaten", recipe["ingredients"], icon="🧾")
    render_shopping_mode("Gericht", recipe_name, recipe["shopping"], prefix="cook")
    st.markdown('<div class="section-title">👨‍🍳 Kochschritte</div>', unsafe_allow_html=True)
    for i, step in enumerate(recipe["steps"], start=1):
        st.markdown(f'<div class="list-item"><b>{i}.</b> {step}</div>', unsafe_allow_html=True)


def render_baking(bake_name):
    add_history("bake", bake_name)
    bake = baking_recipes[bake_name]
    description_html = bake["description"].replace("\n", "<br>")
    st.markdown(f"""
    <div class="cora-card">
        <div class="card-title">{bake_name}</div>
        <div class="card-text">{description_html}</div>
    </div>
    """, unsafe_allow_html=True)
    show_info_card(bake)
    show_simple_list("Back-Zutaten", bake["ingredients"], icon="🧾")
    render_shopping_mode("Backidee", bake_name, bake["shopping"], prefix="bake")
    st.markdown('<div class="section-title">👩‍🍳 Backschritte</div>', unsafe_allow_html=True)
    for i, step in enumerate(bake["steps"], start=1):
        st.markdown(f'<div class="list-item"><b>{i}.</b> {step}</div>', unsafe_allow_html=True)




def home_button(key_suffix=""):
    """Small safe back button used in all sub pages."""
    if st.button("🏠 Zur Startseite", key=f"home_{key_suffix}"):
        st.session_state.view = "🏠 Start"
        st.rerun()

# =========================================================
# CORA IMAGE
# =========================================================
if CORA_IMAGE is not None and CORA_IMAGE.exists():
    st.image(str(CORA_IMAGE), use_container_width=True)
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
# NAVIGATION — MOBILE FIRST / DESKTOP SAFE
# =========================================================
st.markdown("""
<div class="cora-card">
    <div class="card-title">🧭 Schnell finden</div>
    <div class="card-text">Ein Bereich wählen. Kein Suchen. Kein Scroll-Chaos.</div>
</div>
""", unsafe_allow_html=True)

nav_items = [
    "🏠 Start",
    "📸 Was ist da?",
    "🍲 Kochen",
    "🍰 Backen",
    "🛒 Einkauf",
    "🕘 Verlauf",
    "🎙️ Cora Hilfe",
]

for row_start in range(0, len(nav_items), 2):
    cols = st.columns(2)
    for idx, item in enumerate(nav_items[row_start:row_start + 2]):
        with cols[idx]:
            is_active = st.session_state.view == item
            label = f"✅ {item}" if is_active else item
            if st.button(label, key=f"nav_{row_start}_{idx}_{item}"):
                set_view(item)
                st.rerun()


# =========================================================
# START / PHOTO FLOW
# =========================================================
if st.session_state.view in ["🏠 Start", "📸 Was ist da?"]:
    st.markdown('<div class="section-title">📸 Was ist da?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="cora-card">
        <div class="card-title">📸 3 Bilder reichen</div>
        <div class="card-text">
            Keine Lust alles zu checken?<br>
            Mach 3 Bilder: Kühlschrank, Vorrat, Tiefkühl / Reste.<br><br>
            Cora sortiert. Cora zaubert Ideen. Was fehlt, kommt auf die Einkaufsliste.
        </div>
    </div>
    """, unsafe_allow_html=True)

    uploaded_photos = st.file_uploader(
        "3 Bilder hochladen",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    if uploaded_photos:
        st.markdown(f'<div class="list-item">✅ {len(uploaded_photos)} Bild(er) geladen. Für V1 reicht das als Foto-Flow.</div>', unsafe_allow_html=True)
        cols = st.columns(3)
        for idx, photo in enumerate(uploaded_photos[:3]):
            with cols[idx % 3]:
                st.image(photo, use_container_width=True)
        if st.button("✨ Cora prüfen und sortieren"):
            st.session_state.photos_checked = True
            st.rerun()

    if st.session_state.photos_checked:
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

    st.markdown('<div class="section-title">🧭 Was brauchst du jetzt?</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🍲 Koch mir was", key="go_cook_from_start"):
            set_view("🍲 Kochen")
            st.rerun()
    with c2:
        if st.button("🍰 Back mir was", key="go_bake_from_start"):
            set_view("🍰 Backen")
            st.rerun()
    with c3:
        if st.button("🛒 Was fehlt?", key="go_shop_from_start"):
            set_view("🛒 Einkauf")
            st.rerun()


# =========================================================
# COOKING VIEW
# =========================================================
if st.session_state.view == "🍲 Kochen":
    st.markdown('<div class="section-title">🍳 Kochen — Asia & Familien-Basics</div>', unsafe_allow_html=True)
    recipe_names = list(recipes.keys())
    selected_recipe = st.radio(
        "Gericht auswählen",
        recipe_names,
        index=recipe_names.index(st.session_state.selected_recipe),
        label_visibility="collapsed"
    )
    st.session_state.selected_recipe = selected_recipe
    render_recipe(selected_recipe)
    home_button("cook")


# =========================================================
# BAKING VIEW
# =========================================================
if st.session_state.view == "🍰 Backen":
    st.markdown('<div class="section-title">🍰 Cora Backstube — Top 10 einfach aus Vorrat</div>', unsafe_allow_html=True)
    baking_names = list(baking_recipes.keys())
    selected_baking = st.radio(
        "Backidee auswählen",
        baking_names,
        index=baking_names.index(st.session_state.selected_baking),
        label_visibility="collapsed"
    )
    st.session_state.selected_baking = selected_baking
    render_baking(selected_baking)
    home_button("bake")


# =========================================================
# SHOPPING VIEW
# =========================================================
if st.session_state.view == "🛒 Einkauf":
    st.markdown('<div class="section-title">🛒 Einkauf — entspannt abhaken</div>', unsafe_allow_html=True)
    recipe_names = list(recipes.keys())
    selected_recipe = st.radio(
        "Liste für Gericht auswählen",
        recipe_names,
        index=recipe_names.index(st.session_state.selected_recipe),
        label_visibility="collapsed"
    )
    st.session_state.selected_recipe = selected_recipe
    recipe = recipes[selected_recipe]
    render_shopping_mode("Gericht", selected_recipe, recipe["shopping"], prefix="shopview")

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
    home_button("shop")


# =========================================================
# HISTORY VIEW
# =========================================================
if st.session_state.view == "🕘 Verlauf":
    render_history()


# =========================================================
# HELP VIEW
# =========================================================
if st.session_state.view == "🎙️ Cora Hilfe":
    st.markdown('<div class="section-title">🎙️ Wann Cora fragen?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="cora-card">
        <div class="card-title">Im Geschäft hakst du nur ab.</div>
        <div class="card-text">
            Wenn du festhängst, fragst du Cora.<br><br>
            ✅ Ersatz finden: „Brokkoli ist ausverkauft.“<br>
            ✅ Aktion prüfen: „Lohnt sich Butter auf Vorrat?“<br>
            ✅ Budget retten: „Was kann ich streichen?“<br>
            ✅ Nach dem Einkauf: „Was koche ich zuerst?“<br><br>
            Nicht reden müssen. Nur Hilfe, wenn du sie brauchst.
        </div>
    </div>
    """, unsafe_allow_html=True)
    home_button("help")


# =========================================================
# CORA TIP
# =========================================================
st.markdown("""
<div class="cora-card">
    <div class="card-title">💡 Cora Tipp</div>
    <div class="card-text">
        Du brauchst keine 100 Rezepte.<br>
        Du brauchst eine klare Richtung.<br><br>
        Was ist da? Cora prüft.<br>
        Cora zaubert Ideen.<br>
        Was fehlt, kommt auf die Einkaufsliste.<br>
        Verlauf merkt, was funktioniert hat.
    </div>
</div>
""", unsafe_allow_html=True)
