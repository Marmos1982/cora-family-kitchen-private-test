import streamlit as st
from datetime import datetime

# =========================
# CORA FAMILY KITCHEN
# SAFE BUTTON FIX VERSION
# =========================

st.set_page_config(
    page_title="Cora Family Kitchen",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# BASIC CSS
# =========================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #fff8ef 0%, #f7efe2 100%);
    }

    .main-title {
        font-size: 34px;
        font-weight: 800;
        color: #3b2416;
        margin-bottom: 0px;
    }

    .sub-title {
        font-size: 17px;
        color: #6d4b35;
        margin-bottom: 22px;
    }

    .cora-card {
        background: #ffffffcc;
        padding: 18px;
        border-radius: 18px;
        border: 1px solid #ead8c4;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        margin-bottom: 14px;
    }

    .cora-box {
        background: #fff4df;
        padding: 14px;
        border-radius: 14px;
        border-left: 5px solid #d08a34;
        margin: 12px 0;
        color: #3b2416;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 14px;
        height: 48px;
        font-weight: 700;
        border: 1px solid #d8b993;
        background: #fffaf3;
        color: #3b2416;
    }

    div.stButton > button:hover {
        background: #f1d7b3;
        border: 1px solid #c4873c;
        color: #2a160c;
    }

    .small-note {
        font-size: 13px;
        color: #7a5a45;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# SESSION STATE HELPERS
# =========================

def init_state(key, default):
    if key not in st.session_state:
        st.session_state[key] = default


def toggle_state(key):
    if key not in st.session_state:
        st.session_state[key] = False
    st.session_state[key] = not st.session_state[key]


def set_state(key, value):
    st.session_state[key] = value


def reset_active_views():
    st.session_state.active_view = "home"


# =========================
# INIT STATES
# =========================

init_state("tool_menu_open", False)
init_state("active_view", "home")
init_state("shopping_items", [])
init_state("recipe_notes", "")
init_state("family_note", "")
init_state("last_action", "")

# =========================
# HEADER
# =========================

st.markdown('<div class="main-title">🍳 Cora Family Kitchen</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Ruhig kochen. Klar einkaufen. Weniger Stress im Kopf.</div>',
    unsafe_allow_html=True
)

# =========================
# TOP NAVIGATION
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Start", key="btn_nav_home"):
        set_state("active_view", "home")
        set_state("tool_menu_open", False)

with col2:
    if st.button("🧰 Menü", key="btn_nav_toolbox"):
        toggle_state("tool_menu_open")

with col3:
    if st.button("🛒 Einkauf", key="btn_nav_shopping"):
        set_state("active_view", "shopping")
        set_state("tool_menu_open", False)

with col4:
    if st.button("🍽️ Kochen", key="btn_nav_cooking"):
        set_state("active_view", "cooking")
        set_state("tool_menu_open", False)

# =========================
# TOOLBOX MENU
# =========================

if st.session_state.tool_menu_open:
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🧰 Cora Werkzeugkiste")
    st.caption("Nur das anzeigen, was du gerade brauchst. Kein Chaos.")

    t1, t2, t3 = st.columns(3)

    with t1:
        if st.button("🍳 Rezept finden", key="tool_recipe"):
            set_state("active_view", "recipe")
            set_state("tool_menu_open", False)

    with t2:
        if st.button("🛒 Einkaufsliste", key="tool_shopping"):
            set_state("active_view", "shopping")
            set_state("tool_menu_open", False)

    with t3:
        if st.button("🥘 Was kochen?", key="tool_cooking"):
            set_state("active_view", "cooking")
            set_state("tool_menu_open", False)

    t4, t5, t6 = st.columns(3)

    with t4:
        if st.button("👨‍👧 Familie", key="tool_family"):
            set_state("active_view", "family")
            set_state("tool_menu_open", False)

    with t5:
        if st.button("🧠 Stressfrei planen", key="tool_plan"):
            set_state("active_view", "plan")
            set_state("tool_menu_open", False)

    with t6:
        if st.button("❌ Schließen", key="tool_close"):
            set_state("tool_menu_open", False)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# HOME VIEW
# =========================

if st.session_state.active_view == "home":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### Willkommen ❤️")
    st.write(
        "Cora hilft dir beim Kochen und Einkaufen, ohne dass alles auf einmal sichtbar sein muss."
    )

    st.markdown(
        """
        <div class="cora-box">
        <b>Cora sagt:</b><br>
        Heute nicht kompliziert. Erst schauen, was da ist. Dann entscheiden.
        </div>
        """,
        unsafe_allow_html=True
    )

    h1, h2, h3 = st.columns(3)

    with h1:
        if st.button("Schnell Rezept starten", key="home_start_recipe"):
            set_state("active_view", "recipe")

    with h2:
        if st.button("Einkauf vorbereiten", key="home_start_shopping"):
            set_state("active_view", "shopping")

    with h3:
        if st.button("Was ist zuhause?", key="home_start_cooking"):
            set_state("active_view", "cooking")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# RECIPE VIEW
# =========================

elif st.session_state.active_view == "recipe":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🍳 Rezept finden")

    ingredients = st.text_area(
        "Was hast du zuhause?",
        placeholder="z.B. Reis, Eier, Paprika, Huhn, Nudeln, Käse ...",
        key="recipe_ingredients_input"
    )

    mood = st.selectbox(
        "Worauf hast du Lust?",
        ["Einfach & schnell", "Familienessen", "Resteverwertung", "Billig kochen", "Warm & gemütlich"],
        key="recipe_mood_select"
    )

    r1, r2 = st.columns(2)

    with r1:
        if st.button("✨ Cora Vorschlag", key="btn_recipe_suggestion"):
            if ingredients.strip():
                st.session_state.recipe_notes = (
                    f"Vorschlag für: {ingredients}\n"
                    f"Modus: {mood}\n\n"
                    "Idee: Mach daraus eine einfache Pfanne.\n"
                    "1. Basis kochen: Reis, Nudeln oder Kartoffeln.\n"
                    "2. Gemüse anbraten.\n"
                    "3. Ei/Fleisch/Käse dazu.\n"
                    "4. Würzen: Salz, Paprika, Knoblauch, etwas Sojasauce oder Kräuter.\n"
                    "5. Abschmecken und fertig."
                )
                st.session_state.last_action = "Rezeptvorschlag erstellt."
            else:
                st.session_state.recipe_notes = "Bitte zuerst eintragen, was zuhause ist."
                st.session_state.last_action = "Keine Zutaten eingetragen."

    with r2:
        if st.button("🧹 Rezeptfeld leeren", key="btn_recipe_clear"):
            st.session_state.recipe_notes = ""
            st.session_state.last_action = "Rezeptfeld geleert."

    if st.session_state.recipe_notes:
        st.markdown("#### Ergebnis")
        st.info(st.session_state.recipe_notes)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SHOPPING VIEW
# =========================

elif st.session_state.active_view == "shopping":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🛒 Einkaufsliste")

    new_item = st.text_input(
        "Artikel hinzufügen",
        placeholder="z.B. Milch, Haferflocken, Ketchup ...",
        key="shopping_new_item_input"
    )

    s1, s2 = st.columns(2)

    with s1:
        if st.button("➕ Hinzufügen", key="btn_add_shopping_item"):
            item = new_item.strip()
            if item:
                st.session_state.shopping_items.append(
                    {
                        "name": item,
                        "done": False,
                        "created": datetime.now().strftime("%H:%M")
                    }
                )
                st.session_state.last_action = f"{item} hinzugefügt."
            else:
                st.session_state.last_action = "Kein Artikel eingegeben."

    with s2:
        if st.button("🧹 Liste leeren", key="btn_clear_shopping_list"):
            st.session_state.shopping_items = []
            st.session_state.last_action = "Einkaufsliste geleert."

    st.markdown("#### Deine Liste")

    if not st.session_state.shopping_items:
        st.caption("Noch keine Artikel in der Liste.")
    else:
        for i, item in enumerate(st.session_state.shopping_items):
            c1, c2 = st.columns([4, 1])

            with c1:
                checked = st.checkbox(
                    item["name"],
                    value=item["done"],
                    key=f"shopping_check_{i}_{item['name']}"
                )
                st.session_state.shopping_items[i]["done"] = checked

            with c2:
                if st.button("❌", key=f"delete_item_{i}_{item['name']}"):
                    removed = st.session_state.shopping_items.pop(i)
                    st.session_state.last_action = f"{removed['name']} entfernt."
                    st.rerun()

    if st.session_state.shopping_items:
        done_count = sum(1 for item in st.session_state.shopping_items if item["done"])
        total_count = len(st.session_state.shopping_items)
        st.success(f"Erledigt: {done_count} / {total_count}")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# COOKING VIEW
# =========================

elif st.session_state.active_view == "cooking":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🍽️ Kochmodus")

    st.write("Hier geht es nicht um perfekt. Hier geht es um: Was geht heute einfach?")

    time_mode = st.radio(
        "Wie viel Energie ist heute da?",
        ["Sehr wenig", "Normal", "Heute geht mehr"],
        key="cooking_energy_radio"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("⚡ 10 Minuten Essen", key="cook_10min"):
            st.session_state.last_action = "10-Minuten-Idee gewählt."
            st.info(
                "Idee: Eierbrot, Nudeln mit Butter/Käse, Reis mit Ei, Suppe, Toast oder schnelle Pfanne."
            )

    with c2:
        if st.button("🍚 Reis/Nudel Basis", key="cook_base"):
            st.session_state.last_action = "Basis-Idee gewählt."
            st.info(
                "Basis: Reis oder Nudeln kochen. Dann Gemüse, Ei, Fleisch oder Käse dazu. Fertig."
            )

    with c3:
        if st.button("🥶 Resteverwertung", key="cook_leftovers"):
            st.session_state.last_action = "Resteverwertung gewählt."
            st.info(
                "Restelogik: Alles, was weg muss, klein schneiden. Anbraten. Würzen. Mit Reis/Nudeln/Kartoffeln verbinden."
            )

    st.markdown(
        f"""
        <div class="cora-box">
        <b>Heute Modus:</b> {time_mode}<br>
        <b>Cora:</b> Mach es kleiner, nicht schwerer.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FAMILY VIEW
# =========================

elif st.session_state.active_view == "family":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 👨‍👧 Familienmodus")

    note = st.text_area(
        "Was ist heute wichtig?",
        placeholder="z.B. Schule, Training, Einkauf, Essen, Termine ...",
        key="family_note_input"
    )

    f1, f2 = st.columns(2)

    with f1:
        if st.button("💾 Merken", key="btn_save_family_note"):
            st.session_state.family_note = note
            st.session_state.last_action = "Familiennotiz gespeichert."

    with f2:
        if st.button("🧹 Löschen", key="btn_clear_family_note"):
            st.session_state.family_note = ""
            st.session_state.last_action = "Familiennotiz gelöscht."

    if st.session_state.family_note:
        st.success(st.session_state.family_note)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PLAN VIEW
# =========================

elif st.session_state.active_view == "plan":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🧠 Stressfrei planen")

    st.write("Cora teilt den Kopf auf: Erst Essen, dann Einkauf, dann Familie.")

    p1, p2, p3 = st.columns(3)

    with p1:
        if st.button("1️⃣ Was essen wir?", key="plan_food"):
            st.session_state.last_action = "Plan Schritt 1 gewählt."
            st.info("Erst ein einfaches Essen wählen. Nicht 10 Optionen.")

    with p2:
        if st.button("2️⃣ Was fehlt?", key="plan_missing"):
            st.session_state.last_action = "Plan Schritt 2 gewählt."
            st.info("Dann nur aufschreiben, was wirklich fehlt.")

    with p3:
        if st.button("3️⃣ Einkauf ruhig", key="plan_shop"):
            st.session_state.last_action = "Plan Schritt 3 gewählt."
            st.info("Im Geschäft nur abhaken. Keine neue Baustelle im Kopf.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER / DEBUG
# =========================

st.markdown("---")

if st.session_state.last_action:
    st.caption(f"Letzte Aktion: {st.session_state.last_action}")

with st.expander("🔧 Debug Button-State ansehen"):
    st.write("Aktive Ansicht:", st.session_state.active_view)
    st.write("Menü offen:", st.session_state.tool_menu_open)
    st.write("Einkaufsliste:", st.session_state.shopping_items)v
