import streamlit as st

st.set_page_config(page_title="Cora Family Kitchen", page_icon="🍳", layout="wide")

REZEPTE = [
    {
        "name": "Asia-Pfanne mit Reis",
        "portionen": 4,
        "kochzeit": "25 Minuten",
        "zutaten": [
            "300 g Reis",
            "400 g Hühnerfleisch oder Faschiertes",
            "1 Paprika",
            "2 Karotten",
            "1 Zwiebel",
            "2 EL Sojasauce",
            "1 TL Honig oder Zucker",
            "Knoblauch",
            "Curry oder Paprika",
            "Öl oder Butter"
        ],
        "zubereitung": [
            "Reis nach Packungsanleitung kochen.",
            "Zwiebel, Karotten und Paprika klein schneiden.",
            "Fleisch in einer Pfanne mit Öl oder Butter anbraten.",
            "Gemüse dazugeben und einige Minuten mitbraten.",
            "Sojasauce, Honig, Knoblauch und Gewürze dazugeben.",
            "Alles gut vermischen und kurz einkochen lassen.",
            "Mit Reis servieren."
        ]
    },
    {
        "name": "Spaghetti Bolognese",
        "portionen": 4,
        "kochzeit": "30 Minuten",
        "zutaten": [
            "500 g Spaghetti",
            "500 g Faschiertes",
            "1 Zwiebel",
            "1 Dose Tomaten",
            "Tomatenmark",
            "Knoblauch",
            "Salz",
            "Pfeffer",
            "Oregano",
            "Öl"
        ],
        "zubereitung": [
            "Spaghetti in Salzwasser kochen.",
            "Zwiebel und Knoblauch klein schneiden.",
            "Faschiertes in Öl anbraten.",
            "Zwiebel und Knoblauch dazugeben.",
            "Tomatenmark kurz mitrösten.",
            "Tomaten dazugeben und würzen.",
            "Sauce köcheln lassen und mit Spaghetti servieren."
        ]
    },
    {
        "name": "Eiernockerl",
        "portionen": 4,
        "kochzeit": "20 Minuten",
        "zutaten": [
            "500 g Mehl",
            "3 Eier für Teig",
            "3 Eier zum Anbraten",
            "250 ml Wasser",
            "Salz",
            "Butter"
        ],
        "zubereitung": [
            "Mehl, Eier, Wasser und Salz zu einem Teig verrühren.",
            "Teig durch ein Nockerlsieb oder mit Löffel in kochendes Wasser geben.",
            "Nockerl kochen, bis sie oben schwimmen.",
            "Abseihen.",
            "Butter in einer Pfanne erhitzen.",
            "Nockerl anbraten.",
            "Eier verquirlen, darüber geben und stocken lassen."
        ]
    }
]


def zeige_rezept(rezept):
    st.title(rezept["name"])

    col1, col2 = st.columns(2)
    with col1:
        st.info(f"🍽️ Portionen: {rezept.get('portionen', 'Keine Angabe')}")
    with col2:
        st.info(f"⏱️ Kochzeit: {rezept.get('kochzeit', 'Keine Angabe')}")

    st.subheader("🛒 Zutaten")
    zutaten = rezept.get("zutaten", [])

    if zutaten:
        for zutat in zutaten:
            st.checkbox(zutat, key=f"{rezept['name']}_{zutat}")
    else:
        st.warning("Für dieses Rezept fehlen die Zutaten.")

    st.subheader("👩‍🍳 Zubereitung")
    zubereitung = rezept.get("zubereitung", [])

    if zubereitung:
        for nummer, schritt in enumerate(zubereitung, start=1):
            st.markdown(f"**{nummer}.** {schritt}")
    else:
        st.error("Für dieses Rezept fehlt noch die Zubereitung.")


def main():
    st.sidebar.title("🍳 Cora Family Kitchen")
    seite = st.sidebar.radio(
        "Bereich",
        ["Rezepte", "Einkaufsliste"]
    )

    if seite == "Rezepte":
        st.header("Rezepte")

        rezept_namen = [r["name"] for r in REZEPTE]
        auswahl = st.selectbox("Rezept auswählen", rezept_namen)

        rezept = next(r for r in REZEPTE if r["name"] == auswahl)
        zeige_rezept(rezept)

    if seite == "Einkaufsliste":
        st.header("🛒 Einkaufsliste")

        alle_zutaten = []
        for rezept in REZEPTE:
            alle_zutaten.extend(rezept.get("zutaten", []))

        alle_zutaten = sorted(set(alle_zutaten))

        if alle_zutaten:
            for zutat in alle_zutaten:
                st.checkbox(zutat, key=f"einkauf_{zutat}")
        else:
            st.warning("Keine Zutaten gefunden.")


if __name__ == "__main__":
    main()
