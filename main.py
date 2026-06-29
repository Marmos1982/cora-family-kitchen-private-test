import streamlit as st
from datetime import datetime

# =========================================================
# CORA FAMILY KITCHEN — BUTTON SAFE VERSION
# =========================================================

st.set_page_config(
    page_title="Cora Family Kitchen",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# STYLE
# =========================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #fff8ef 0%, #f3e6d4 100%);
        color: #2b1a10;
    }

    .cora-title {
        font-size: 34px;
        font-weight: 900;
        color: #3a2416;
        margin-bottom: 0px;
    }

    .cora-subtitle {
        font-size: 17px;
        color: #7a563c;
        margin-bottom: 20px;
    }

    .cora-card {
        background: rgba(255,255,255,0.86);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #ead8c4;
        box-shadow: 0 4px 16px rgba(0,0,0,0.06);
        margin-bottom: 16px;
    }

    .cora-box {
        background: #fff1d8;
        padding: 15px;
        border-radius: 15px;
        border-left: 6px solid #d28a35;
        color: #3a2416;
        margin: 12px 0px;
    }

    div.stButton > button {
        width: 100%;
        min-height: 48px;
        border-radius: 14px;
        border: 1px solid #d8b993;
        background: #fffaf3;
        color: #3a2416;
        font-weight: 800;
    }

    div.stButton > button:hover {
        background: #f1d6ae;
        border: 1px solid #b9782f;
        color: #2a160c;
    }

    .small {
        font-size: 13px;
        color: #7a563c;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# STATE HELPERS
# =========================================================

def init_state(key, value):
    if key not in st.session_state:
        st.session_state[key] = value


def set_view(view_name):
    st.session_state.active_view = view_name
    st.session_state.menu_open = False


def toggle_menu():
    st.session_state.menu_open = not st.session_state.menu_open


def set_message(text):
    st.session_state.message = text


# =========================================================
# INIT SESSION STATE
# =========================================================

init_state("active_view", "home")
init_state("menu_open", False)
init_state("shopping_items", [])
init_state("message", "")
init_state("recipe_result", "")
init_state("family_note_saved", "")

# =========================================================
# HEADER
# =========================================================

st.markdown('<div class="cora-title">🍳 Cora Family Kitchen</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="cora-subtitle">Ruhig kochen. Klar einkaufen. Weniger Stress im Kopf.</div>',
    unsafe_allow_html=True,
)

# =========================================================
# TOP BUTTONS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Start", key="btn_home"):
        set_view("home")

with col2:
    if st.button("🧰 Menü", key="btn_menu"):
        toggle_menu()

with col3:
    if st.button("🛒 Einkauf", key="btn_shopping_top"):
        set_view("shopping")

with col4:
    if st.button("🍽️ Kochen", key="btn_cooking_top"):
        set_view("cooking")

# =========================================================
# MENU
# =========================================================

if st.session_state.menu_open:
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🧰 Cora Werkzeugkiste")
    st.caption("Nicht alles auf einmal. Nur das, was du gerade brauchst.")

    m1, m2, m3 = st.columns(3)

    with m1:
        if st.button("🍳 Rezept", key="menu_recipe"):
            set_view("recipe")

    with m2:
        if st.button("🛒 Einkaufsliste", key="menu_shopping"):
            set_view("shopping")

    with m3:
        if st.button("🥘 Kochhilfe", key="menu_cooking"):
            set_view("cooking")

    m4, m5, m6 = st.columns(3)

    with m4:
        if st.button("👨‍👧 Familie", key="menu_family"):
            set_view("family")

    with m5:
        if st.button("🧠 Planen", key="menu_plan"):
            set_view("plan")

    with m6:
        if st.button("❌ Schließen", key="menu_close"):
            st.session_state.menu_open = False

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HOME
# =========================================================

if st.session_state.active_view == "home":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### Willkommen ❤️")
    st.write("Heute machen wir es einfach. Kein Küchen-Chaos. Kein Einkaufs-Stress.")

    st.markdown(
        """
        <div class="cora-box">
        <b>Cora sagt:</b><br>
        Erst schauen, was da ist. Dann entscheiden. Nicht alles im Kopf tragen.
        </div>
        """,
        unsafe_allow_html=True,
    )

    h1, h2, h3 = st.columns(3)

    with h1:
        if st.button("🍳 Rezept starten", key="home_recipe"):
            set_view("recipe")

    with h2:
        if st.button("🛒 Einkauf starten", key="home_shopping"):
            set_view("shopping")

    with h3:
        if st.button("🥘 Kochhilfe starten", key="home_cooking"):
            set_view("cooking")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RECIPE
# =========================================================

elif st.session_state.active_view == "recipe":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🍳 Rezept finden")

    ingredients = st.text_area(
        "Was hast du zuhause?",
        placeholder="z.B. Reis, Eier, Paprika, Nudeln, Käse, Huhn ...",
        key="recipe_ingredients",
    )

    mode = st.selectbox(
        "Was brauchst du heute?",
        [
            "Schnell & einfach",
            "Familienessen",
            "Resteverwertung",
            "Billig kochen",
            "Warm & gemütlich",
        ],
        key="recipe_mode",
    )

    r1, r2 = st.columns(2)

    with r1:
        if st.button("✨ Cora Vorschlag", key="recipe_generate"):
            if ingredients.strip():
                st.session_state.recipe_result = (
                    f"Modus: {mode}\n\n"
                    f"Zutaten: {ingredients}\n\n"
                    "Cora Idee:\n"
                    "Mach daraus eine einfache Pfanne.\n\n"
                    "1. Basis kochen: Reis, Nudeln oder Kartoffeln.\n"
                    "2. Gemüse oder Reste klein schneiden.\n"
                    "3. Alles anbraten.\n"
                    "4. Ei, Fleisch, Käse oder Bohnen dazu.\n"
                    "5. Würzen mit Salz, Paprika, Knoblauch, Kräutern oder Sojasauce.\n\n"
                    "Nicht perfekt. Nur warm, gut und machbar."
                )
                set_message("Rezeptvorschlag erstellt.")
            else:
                st.session_state.recipe_result = "Bitte zuerst eintragen, was zuhause ist."
                set_message("Keine Zutaten eingetragen.")

    with r2:
        if st.button("🧹 Ergebnis leeren", key="recipe_clear"):
            st.session_state.recipe_result = ""
            set_message("Rezeptfeld geleert.")

    if st.session_state.recipe_result:
        st.markdown("#### Ergebnis")
        st.info(st.session_state.recipe_result)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# SHOPPING
# =========================================================

elif st.session_state.active_view == "shopping":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🛒 Einkaufsliste")

    new_item = st.text_input(
        "Artikel hinzufügen",
        placeholder="z.B. Milch, Haferflocken, Ketchup ...",
        key="new_shopping_item",
    )

    s1, s2 = st.columns(2)

    with s1:
        if st.button("➕ Hinzufügen", key="shopping_add"):
            item = new_item.strip()
            if item:
                st.session_state.shopping_items.append(
                    {
                        "name": item,
                        "done": False,
                        "time": datetime.now().strftime("%H:%M"),
                    }
                )
                set_message(f"{item} hinzugefügt.")
            else:
                set_message("Kein Artikel eingegeben.")

    with s2:
        if st.button("🧹 Liste leeren", key="shopping_clear"):
            st.session_state.shopping_items = []
            set_message("Einkaufsliste geleert.")

    st.markdown("#### Liste")

    if not st.session_state.shopping_items:
        st.caption("Noch keine Artikel in der Liste.")
    else:
        delete_index = None

        for i, item in enumerate(st.session_state.shopping_items):
            row1, row2 = st.columns([5, 1])

            with row1:
                checked = st.checkbox(
                    item["name"],
                    value=item["done"],
                    key=f"shopping_item_check_{i}_{item['name']}",
                )
                st.session_state.shopping_items[i]["done"] = checked

            with row2:
                if st.button("❌", key=f"shopping_delete_{i}_{item['name']}"):
                    delete_index = i

        if delete_index is not None:
            removed = st.session_state.shopping_items.pop(delete_index)
            set_message(f"{removed['name']} entfernt.")
            st.rerun()

        done_count = sum(1 for item in st.session_state.shopping_items if item["done"])
        total_count = len(st.session_state.shopping_items)

        st.success(f"Erledigt: {done_count} / {total_count}")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# COOKING
# =========================================================

elif st.session_state.active_view == "cooking":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🍽️ Kochmodus")

    energy = st.radio(
        "Wie viel Energie ist heute da?",
        ["Sehr wenig", "Normal", "Heute geht mehr"],
        key="cooking_energy",
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("⚡ 10 Minuten", key="cook_fast"):
            st.info("Eierbrot, Nudeln mit Butter/Käse, Reis mit Ei, Suppe oder Toast.")
            set_message("Schnelle Kochidee gewählt.")

    with c2:
        if st.button("🍚 Basis + Reste", key="cook_base"):
            st.info("Reis/Nudeln/Kartoffeln als Basis. Reste anbraten. Würzen. Fertig.")
            set_message("Basis-Idee gewählt.")

    with c3:
        if st.button("🥶 Kühlschrank leer?", key="cook_empty"):
            st.info("Dann einfach halten: Nudeln, Ei, Brot, Suppe, Reis, Tiefkühlgemüse.")
            set_message("Notfall-Idee gewählt.")

    st.markdown(
        f"""
        <div class="cora-box">
        <b>Heute Modus:</b> {energy}<br>
        <b>Cora:</b> Mach es kleiner, nicht schwerer.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FAMILY
# =========================================================

elif st.session_state.active_view == "family":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 👨‍👧 Familienmodus")

    family_note = st.text_area(
        "Was ist heute wichtig?",
        placeholder="z.B. Schule, Training, Essen, Termine, Einkauf ...",
        key="family_note_input",
    )

    f1, f2 = st.columns(2)

    with f1:
        if st.button("💾 Merken", key="family_save"):
            st.session_state.family_note_saved = family_note
            set_message("Familiennotiz gespeichert.")

    with f2:
        if st.button("🧹 Löschen", key="family_delete"):
            st.session_state.family_note_saved = ""
            set_message("Familiennotiz gelöscht.")

    if st.session_state.family_note_saved:
        st.success(st.session_state.family_note_saved)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# PLAN
# =========================================================

elif st.session_state.active_view == "plan":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🧠 Stressfrei planen")

    st.write("Nicht alles gleichzeitig. Cora macht daraus drei kleine Schritte.")

    p1, p2, p3 = st.columns(3)

    with p1:
        if st.button("1️⃣ Essen wählen", key="plan_food"):
            st.info("Ein einfaches Essen wählen. Nicht zehn Ideen gleichzeitig.")
            set_message("Plan Schritt 1.")

    with p2:
        if st.button("2️⃣ Was fehlt?", key="plan_missing"):
            st.info("Nur aufschreiben, was wirklich fehlt.")
            set_message("Plan Schritt 2.")

    with p3:
        if st.button("3️⃣ Ruhig einkaufen", key="plan_shop"):
            st.info("Im Geschäft nur abhaken. Keine neue Baustelle im Kopf.")
            set_message("Plan Schritt 3.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

if st.session_state.message:
    st.caption(f"Letzte Aktion: {st.session_state.message}")

with st.expander("🔧 Debug"):
    st.write("Aktive Ansicht:", st.session_state.active_view)
    st.write("Menü offen:", st.session_state.menu_open)
    st.write("Einkaufsliste:", st.session_state.shopping_items)
