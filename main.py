import streamlit as st
from datetime import datetime

# =========================================================
# CORA FAMILY KITCHEN — BUTTON FIX VERSION
# =========================================================
# Fix:
# - Kein st.rerun()
# - Kein on_click
# - Kein HTML-Wrapper um Buttons
# - Buttons setzen nur session_state
# - Upload direkt erreichbar
# =========================================================

st.set_page_config(
    page_title="Cora Family Kitchen",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# STYLE — SAFE CSS
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
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# SESSION STATE
# =========================================================

def init_state(key, value):
    if key not in st.session_state:
        st.session_state[key] = value


init_state("active_view", "home")
init_state("menu_open", False)
init_state("message", "")
init_state("shopping_items", [])
init_state("recipe_result", "")
init_state("family_note_saved", "")

# =========================================================
# NAVIGATION — OHNE RERUN
# =========================================================

def go_to(view_name):
    st.session_state.active_view = view_name
    st.session_state.menu_open = False
    st.session_state.message = f"Geöffnet: {view_name}"


def toggle_menu():
    st.session_state.menu_open = not st.session_state.menu_open
    if st.session_state.menu_open:
        st.session_state.message = "Menü geöffnet."
    else:
        st.session_state.message = "Menü geschlossen."


def set_msg(text):
    st.session_state.message = text


# =========================================================
# HEADER
# =========================================================

st.markdown('<div class="cora-title">🍳 Cora Family Kitchen</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="cora-subtitle">Ruhig kochen. Klar einkaufen. Weniger Stress im Kopf.</div>',
    unsafe_allow_html=True,
)

# =========================================================
# TOP NAVIGATION
# =========================================================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 Start", key="top_home"):
        go_to("home")

with col2:
    if st.button("🧰 Menü", key="top_menu"):
        toggle_menu()

with col3:
    if st.button("🛒 Einkauf", key="top_shopping"):
        go_to("shopping")

with col4:
    if st.button("🍽️ Kochen", key="top_cooking"):
        go_to("cooking")

with col5:
    if st.button("📸 Upload", key="top_upload"):
        go_to("upload")

# =========================================================
# MENU
# =========================================================

if st.session_state.menu_open:
    st.divider()
    st.markdown("### 🧰 Cora Werkzeugkiste")
    st.caption("Nicht alles auf einmal. Nur das, was du gerade brauchst.")

    m1, m2, m3 = st.columns(3)

    with m1:
        if st.button("🍳 Rezept", key="menu_recipe"):
            go_to("recipe")

    with m2:
        if st.button("🛒 Einkaufsliste", key="menu_shopping"):
            go_to("shopping")

    with m3:
        if st.button("🥘 Kochhilfe", key="menu_cooking"):
            go_to("cooking")

    m4, m5, m6 = st.columns(3)

    with m4:
        if st.button("👨‍👧 Familie", key="menu_family"):
            go_to("family")

    with m5:
        if st.button("🧠 Planen", key="menu_plan"):
            go_to("plan")

    with m6:
        if st.button("📸 Bild Upload", key="menu_upload"):
            go_to("upload")

    if st.button("❌ Menü schließen", key="menu_close"):
        st.session_state.menu_open = False
        set_msg("Menü geschlossen.")

# =========================================================
# HOME
# =========================================================

if st.session_state.active_view == "home":
    st.divider()
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
            go_to("recipe")

    with h2:
        if st.button("🛒 Einkauf starten", key="home_shopping"):
            go_to("shopping")

    with h3:
        if st.button("📸 Bild hochladen", key="home_upload"):
            go_to("upload")

# =========================================================
# RECIPE
# =========================================================

elif st.session_state.active_view == "recipe":
    st.divider()
    st.markdown("### 🍳 Rezept finden")

    ingredients = st.text_area(
        "Was hast du zuhause?",
        placeholder="z.B. Reis, Eier, Paprika, Nudeln, Käse, Huhn ...",
        key="recipe_ingredients_input",
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
        key="recipe_mode_input",
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
                set_msg("Rezeptvorschlag erstellt.")
            else:
                st.session_state.recipe_result = "Bitte zuerst eintragen, was zuhause ist."
                set_msg("Keine Zutaten eingetragen.")

    with r2:
        if st.button("🧹 Ergebnis leeren", key="recipe_clear"):
            st.session_state.recipe_result = ""
            set_msg("Rezeptfeld geleert.")

    if st.session_state.recipe_result:
        st.markdown("#### Ergebnis")
        st.info(st.session_state.recipe_result)

# =========================================================
# SHOPPING
# =========================================================

elif st.session_state.active_view == "shopping":
    st.divider()
    st.markdown("### 🛒 Einkaufsliste")

    new_item = st.text_input(
        "Artikel hinzufügen",
        placeholder="z.B. Milch, Haferflocken, Ketchup ...",
        key="shopping_new_item_input",
    )

    s1, s2 = st.columns(2)

    with s1:
        if st.button("➕ Hinzufügen", key="shopping_add"):
            item_name = new_item.strip()

            if item_name:
                st.session_state.shopping_items.append(
                    {
                        "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
                        "name": item_name,
                        "done": False,
                        "time": datetime.now().strftime("%H:%M"),
                    }
                )
                set_msg(f"{item_name} hinzugefügt.")
            else:
                set_msg("Kein Artikel eingegeben.")

    with s2:
        if st.button("🧹 Liste leeren", key="shopping_clear"):
            st.session_state.shopping_items = []
            set_msg("Einkaufsliste geleert.")

    st.markdown("#### Liste")

    if not st.session_state.shopping_items:
        st.caption("Noch keine Artikel in der Liste.")
    else:
        delete_id = None

        for item in st.session_state.shopping_items:
            row1, row2 = st.columns([5, 1])

            with row1:
                checked = st.checkbox(
                    item["name"],
                    value=item["done"],
                    key=f"shopping_check_{item['id']}",
                )
                item["done"] = checked

            with row2:
                if st.button("❌", key=f"shopping_delete_{item['id']}"):
                    delete_id = item["id"]

        if delete_id:
            st.session_state.shopping_items = [
                item for item in st.session_state.shopping_items if item["id"] != delete_id
            ]
            set_msg("Artikel entfernt.")

        done_count = sum(1 for item in st.session_state.shopping_items if item["done"])
        total_count = len(st.session_state.shopping_items)
        st.success(f"Erledigt: {done_count} / {total_count}")

# =========================================================
# COOKING
# =========================================================

elif st.session_state.active_view == "cooking":
    st.divider()
    st.markdown("### 🍽️ Kochmodus")

    energy = st.radio(
        "Wie viel Energie ist heute da?",
        ["Sehr wenig", "Normal", "Heute geht mehr"],
        key="cooking_energy_radio",
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("⚡ 10 Minuten", key="cook_fast"):
            set_msg("Schnelle Kochidee gewählt.")
            st.info("Eierbrot, Nudeln mit Butter/Käse, Reis mit Ei, Suppe oder Toast.")

    with c2:
        if st.button("🍚 Basis + Reste", key="cook_base"):
            set_msg("Basis-Idee gewählt.")
            st.info("Reis/Nudeln/Kartoffeln als Basis. Reste anbraten. Würzen. Fertig.")

    with c3:
        if st.button("🥶 Kühlschrank leer?", key="cook_empty"):
            set_msg("Notfall-Idee gewählt.")
            st.info("Dann einfach halten: Nudeln, Ei, Brot, Suppe, Reis, Tiefkühlgemüse.")

    st.markdown(
        f"""
        <div class="cora-box">
        <b>Heute Modus:</b> {energy}<br>
        <b>Cora:</b> Mach es kleiner, nicht schwerer.
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# FAMILY
# =========================================================

elif st.session_state.active_view == "family":
    st.divider()
    st.markdown("### 👨‍👧 Familienmodus")

    family_note = st.text_area(
        "Was ist heute wichtig?",
        placeholder="z.B. Schule, Training, Essen, Termine, Einkauf ...",
        key="family_note_input_area",
    )

    f1, f2 = st.columns(2)

    with f1:
        if st.button("💾 Merken", key="family_save"):
            st.session_state.family_note_saved = family_note
            set_msg("Familiennotiz gespeichert.")

    with f2:
        if st.button("🧹 Löschen", key="family_delete"):
            st.session_state.family_note_saved = ""
            set_msg("Familiennotiz gelöscht.")

    if st.session_state.family_note_saved:
        st.success(st.session_state.family_note_saved)

# =========================================================
# PLAN
# =========================================================

elif st.session_state.active_view == "plan":
    st.divider()
    st.markdown("### 🧠 Stressfrei planen")

    st.write("Nicht alles gleichzeitig. Cora macht daraus drei kleine Schritte.")

    p1, p2, p3 = st.columns(3)

    with p1:
        if st.button("1️⃣ Essen wählen", key="plan_food"):
            st.info("Ein einfaches Essen wählen. Nicht zehn Ideen gleichzeitig.")
            set_msg("Plan Schritt 1.")

    with p2:
        if st.button("2️⃣ Was fehlt?", key="plan_missing"):
            st.info("Nur aufschreiben, was wirklich fehlt.")
            set_msg("Plan Schritt 2.")

    with p3:
        if st.button("3️⃣ Ruhig einkaufen", key="plan_shop"):
            st.info("Im Geschäft nur abhaken. Keine neue Baustelle im Kopf.")
            set_msg("Plan Schritt 3.")

# =========================================================
# UPLOAD
# =========================================================

elif st.session_state.active_view == "upload":
    st.divider()
    st.markdown("### 📸 Bild hochladen")

    st.write("Hier kannst du ein Küchenbild, Kühlschrankbild oder Einkaufsbild laden.")

    uploaded_image = st.file_uploader(
        "Bild auswählen",
        type=["png", "jpg", "jpeg", "webp"],
        key="safe_image_uploader",
        accept_multiple_files=False,
    )

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Hochgeladenes Bild", use_container_width=True)
        st.success("Bild wurde geladen.")
        st.caption(f"Datei: {uploaded_image.name}")

# =========================================================
# FOOTER
# =========================================================

st.divider()

if st.session_state.message:
    st.caption(f"Letzte Aktion: {st.session_state.message}")

with st.expander("🔧 Debug"):
    st.write("Aktive Ansicht:", st.session_state.active_view)
    st.write("Menü offen:", st.session_state.menu_open)
    st.write("Einkaufsliste:", st.session_state.shopping_items)
