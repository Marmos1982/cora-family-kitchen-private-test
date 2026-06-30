import streamlit as st
from datetime import datetime

# =========================================================
# CORA FAMILY KITCHEN — DESIGN SAFE + MOBILE FALLBACK
# =========================================================
# Für Tester:
# - Design bleibt warm / Cora Kitchen
# - Desktop Buttons bleiben
# - Mobile/App bekommt zusätzlich stabile Auswahl
# - Upload ist direkt erreichbar
# - Keine hässliche Link-Navigation
# - Kein st.rerun()
# =========================================================

st.set_page_config(
    page_title="Cora Family Kitchen",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# STYLE — DESIGN BLEIBT
# =========================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #fff8ef 0%, #f3e6d4 100%);
        color: #2b1a10;
    }

    .main .block-container {
        padding-top: 2rem;
        max-width: 1180px;
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

    .cora-mobile-box {
        background: rgba(255,250,243,0.92);
        padding: 14px;
        border-radius: 18px;
        border: 1px solid #ead8c4;
        margin: 10px 0 18px 0;
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

    div[data-baseweb="select"] > div {
        background-color: #fffaf3;
        border-radius: 14px;
        border-color: #d8b993;
        min-height: 48px;
    }

    .small {
        font-size: 13px;
        color: #7a563c;
    }

    @media (max-width: 700px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }

        .cora-title {
            font-size: 30px;
        }

        .cora-subtitle {
            font-size: 15px;
        }
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
init_state("mobile_select", "🏠 Start")

# =========================================================
# HELPERS
# =========================================================

def set_msg(text):
    st.session_state.message = text


def go_to(view_name):
    st.session_state.active_view = view_name
    st.session_state.menu_open = False
    st.session_state.message = f"Geöffnet: {view_name}"


def toggle_menu():
    st.session_state.menu_open = not st.session_state.menu_open
    set_msg("Menü geöffnet." if st.session_state.menu_open else "Menü geschlossen.")


def mobile_label_to_view(label):
    mapping = {
        "🏠 Start": "home",
        "🍳 Rezept": "recipe",
        "🛒 Einkauf": "shopping",
        "🍽️ Kochen": "cooking",
        "👨‍👧 Familie": "family",
        "🧠 Planen": "plan",
        "📸 Upload": "upload",
    }
    return mapping.get(label, "home")


def sync_mobile_select_to_view():
    current = st.session_state.mobile_select
    selected_view = mobile_label_to_view(current)
    st.session_state.active_view = selected_view
    st.session_state.menu_open = False
    st.session_state.message = f"Mobile Auswahl: {selected_view}"


def add_shopping_item():
    item = st.session_state.get("new_shopping_item", "").strip()

    if not item:
        set_msg("Kein Artikel eingegeben.")
        return

    st.session_state.shopping_items.append(
        {
            "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
            "name": item,
            "done": False,
            "time": datetime.now().strftime("%H:%M"),
        }
    )

    st.session_state.new_shopping_item = ""
    set_msg(f"{item} hinzugefügt.")


def clear_shopping_list():
    st.session_state.shopping_items = []
    set_msg("Einkaufsliste geleert.")


def delete_shopping_item(item_id):
    removed_name = ""
    new_items = []

    for item in st.session_state.shopping_items:
        if item["id"] == item_id:
            removed_name = item["name"]
        else:
            new_items.append(item)

    st.session_state.shopping_items = new_items

    if removed_name:
        set_msg(f"{removed_name} entfernt.")
    else:
        set_msg("Artikel entfernt.")


def save_family_note():
    st.session_state.family_note_saved = st.session_state.get("family_note_input", "")
    set_msg("Familiennotiz gespeichert.")


def delete_family_note():
    st.session_state.family_note_saved = ""
    st.session_state.family_note_input = ""
    set_msg("Familiennotiz gelöscht.")


def generate_recipe():
    ingredients = st.session_state.get("recipe_ingredients", "").strip()
    mode = st.session_state.get("recipe_mode", "Schnell & einfach")

    if not ingredients:
        st.session_state.recipe_result = "Bitte zuerst eintragen, was zuhause ist."
        set_msg("Keine Zutaten eingetragen.")
        return

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

# =========================================================
# HEADER
# =========================================================

st.markdown('<div class="cora-title">🍳 Cora Family Kitchen</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="cora-subtitle">Ruhig kochen. Klar einkaufen. Weniger Stress im Kopf.</div>',
    unsafe_allow_html=True,
)

# =========================================================
# DESKTOP BUTTON NAVIGATION — DESIGN BLEIBT
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
# MOBILE FALLBACK — GLEICHES DESIGN, NICHT ERSETZEN
# =========================================================

st.markdown('<div class="cora-mobile-box">', unsafe_allow_html=True)
st.caption("📱 Falls Buttons in der App nicht reagieren: Bereich hier wählen.")
st.selectbox(
    "Mobile Schnellwahl",
    ["🏠 Start", "🍳 Rezept", "🛒 Einkauf", "🍽️ Kochen", "👨‍👧 Familie", "🧠 Planen", "📸 Upload"],
    key="mobile_select",
    on_change=sync_mobile_select_to_view,
)
st.markdown("</div>", unsafe_allow_html=True)

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

    if st.button("❌ Schließen", key="menu_close"):
        st.session_state.menu_open = False
        set_msg("Menü geschlossen.")

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
            go_to("recipe")

    with h2:
        if st.button("🛒 Einkauf starten", key="home_shopping"):
            go_to("shopping")

    with h3:
        if st.button("📸 Bild hochladen", key="home_upload"):
            go_to("upload")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RECIPE
# =========================================================

elif st.session_state.active_view == "recipe":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 🍳 Rezept finden")

    st.text_area(
        "Was hast du zuhause?",
        placeholder="z.B. Reis, Eier, Paprika, Nudeln, Käse, Huhn ...",
        key="recipe_ingredients",
    )

    st.selectbox(
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
            generate_recipe()

    with r2:
        if st.button("🧹 Ergebnis leeren", key="recipe_clear"):
            st.session_state.recipe_result = ""
            set_msg("Rezeptfeld geleert.")

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

    st.text_input(
        "Artikel hinzufügen",
        placeholder="z.B. Milch, Haferflocken, Ketchup ...",
        key="new_shopping_item",
    )

    s1, s2 = st.columns(2)

    with s1:
        if st.button("➕ Hinzufügen", key="shopping_add"):
            add_shopping_item()

    with s2:
        if st.button("🧹 Liste leeren", key="shopping_clear"):
            clear_shopping_list()

    st.markdown("#### Liste")

    if not st.session_state.shopping_items:
        st.caption("Noch keine Artikel in der Liste.")
    else:
        for item in list(st.session_state.shopping_items):
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
                    delete_shopping_item(item["id"])

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
            set_msg("Schnelle Kochidee gewählt.")

    with c2:
        if st.button("🍚 Basis + Reste", key="cook_base"):
            st.info("Reis/Nudeln/Kartoffeln als Basis. Reste anbraten. Würzen. Fertig.")
            set_msg("Basis-Idee gewählt.")

    with c3:
        if st.button("🥶 Kühlschrank leer?", key="cook_empty"):
            st.info("Dann einfach halten: Nudeln, Ei, Brot, Suppe, Reis, Tiefkühlgemüse.")
            set_msg("Notfall-Idee gewählt.")

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

    st.text_area(
        "Was ist heute wichtig?",
        placeholder="z.B. Schule, Training, Essen, Termine, Einkauf ...",
        key="family_note_input",
    )

    f1, f2 = st.columns(2)

    with f1:
        if st.button("💾 Merken", key="family_save"):
            save_family_note()

    with f2:
        if st.button("🧹 Löschen", key="family_delete"):
            delete_family_note()

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
            set_msg("Plan Schritt 1.")

    with p2:
        if st.button("2️⃣ Was fehlt?", key="plan_missing"):
            st.info("Nur aufschreiben, was wirklich fehlt.")
            set_msg("Plan Schritt 2.")

    with p3:
        if st.button("3️⃣ Ruhig einkaufen", key="plan_shop"):
            st.info("Im Geschäft nur abhaken. Keine neue Baustelle im Kopf.")
            set_msg("Plan Schritt 3.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# UPLOAD
# =========================================================

elif st.session_state.active_view == "upload":
    st.markdown('<div class="cora-card">', unsafe_allow_html=True)
    st.markdown("### 📸 Bild hochladen")
    st.write("Hier kannst du ein Küchenbild, Kühlschrankbild oder Einkaufsbild laden.")

    uploaded_image = st.file_uploader(
        "Bild auswählen",
        type=["png", "jpg", "jpeg", "webp"],
        key="kitchen_image_upload",
        accept_multiple_files=False,
    )

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Hochgeladenes Bild", use_container_width=True)
        st.success("Bild wurde geladen.")
        st.caption(f"Datei: {uploaded_image.name}")

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
