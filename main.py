import streamlit as st
from pathlib import Path
from textwrap import dedent

st.set_page_config(
    page_title="Cora Family Kitchen",
    page_icon="🔥",
    layout="centered"
)

APP_DIR = Path(__file__).parent

def find_cora_image():
    names = ["cora.png", "cora.png.png", "Cora.png", "Cora.PNG", "cora.PNG", "cora.jpg", "cora.jpeg", "Cora.jpg", "Cora.jpeg", "cora.webp", "Cora.webp"]
    for name in names:
        path = APP_DIR / name
        if path.exists():
            return path
    for path in APP_DIR.iterdir():
        if path.is_file() and "cora" in path.name.lower() and path.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
            return path
    return None

def clean_text(text):
    return dedent(text).strip()

recipes = {'1. Kraut-Karotten-Nudelpfanne': {'info': {'time': '20–25 Min',
                                            'budget': 'Sehr günstig',
                                            'level': 'Einfach',
                                            'family': 'Mild / familientauglich'},
                                   'description': 'Schnell, günstig und perfekt für normale Familientage.\n'
                                                  'Kraut, Karotten, Nudeln und eine einfache Asia-Sauce.\n'
                                                  'Kein Stress. Keine 100 Zutaten. Pfanne heiß, Kopf ruhig.',
                                   'ingredients': ['Nudeln oder Reisnudeln',
                                                   'Weißkraut oder Chinakohl',
                                                   'Karotten',
                                                   'Zwiebel',
                                                   'Knoblauch',
                                                   'Sojasauce',
                                                   'Honig oder Zucker',
                                                   'Öl',
                                                   'Optional: Huhn, Faschiertes oder Ei',
                                                   'Optional: Sweet-Chili-Sauce'],
                                   'shopping': {'🛒 Obst & Gemüse': ['Weißkraut oder Chinakohl',
                                                                    'Karotten',
                                                                    'Zwiebel',
                                                                    'Knoblauch'],
                                                '🥩 Kühlung / Fleisch / Ei': ['Optional: Huhn, Faschiertes oder Eier'],
                                                '🍚 Trockenware': ['Nudeln oder Reisnudeln'],
                                                '🥢 Saucen & Gewürze': ['Sojasauce',
                                                                       'Honig oder Zucker',
                                                                       'Öl',
                                                                       'Optional: Sweet-Chili-Sauce']},
                                   'steps': ['Nudeln oder Reisnudeln kochen.',
                                             'Kraut fein schneiden, Karotten raspeln oder dünn schneiden.',
                                             'Zwiebel und Knoblauch in Öl anbraten.',
                                             'Kraut und Karotten dazugeben und weich braten.',
                                             'Optional Huhn, Faschiertes oder Ei dazugeben.',
                                             'Mit Sojasauce, Honig oder Zucker und etwas Wasser abschmecken.',
                                             'Nudeln dazugeben und alles gut vermischen.',
                                             'Optional mit Sweet-Chili-Sauce servieren.']},
 '2. Asia-Huhn mit Brokkoli': {'info': {'time': '25 Min',
                                        'budget': 'Mittel / Angebot nutzen',
                                        'level': 'Einfach',
                                        'family': 'Sehr familientauglich'},
                               'description': 'Mildes Asia-Huhn mit Brokkoli und Reis.\n'
                                              'Einfach, warm, sättigend und besser als hektisch irgendwas bestellen.',
                               'ingredients': ['Huhn',
                                               'Brokkoli frisch oder TK',
                                               'Karotten',
                                               'Reis',
                                               'Knoblauch',
                                               'Sojasauce',
                                               'Honig oder Zucker',
                                               'Speisestärke',
                                               'Öl'],
                               'shopping': {'🛒 Obst & Gemüse': ['Brokkoli frisch oder TK', 'Karotten', 'Knoblauch'],
                                            '🥩 Kühlung / Fleisch / Ei': ['Huhn'],
                                            '🍚 Trockenware': ['Reis'],
                                            '🥢 Saucen & Gewürze': ['Sojasauce',
                                                                   'Honig oder Zucker',
                                                                   'Speisestärke',
                                                                   'Öl']},
                               'steps': ['Reis kochen.',
                                         'Huhn klein schneiden und in Öl scharf anbraten.',
                                         'Brokkoli und Karotten dazugeben.',
                                         'Sauce aus Sojasauce, Honig oder Zucker, Wasser und Speisestärke rühren.',
                                         'Sauce in die Pfanne geben und kurz eindicken lassen.',
                                         'Mit Reis servieren.']},
 '3. Nasi Goreng Familienversion': {'info': {'time': '20 Min',
                                             'budget': 'Günstig',
                                             'level': 'Einfach',
                                             'family': 'Mild / perfekt für Reste'},
                                    'description': 'Perfekt für Reisreste.\n'
                                                   'Ei, Reis, Gemüse, Sojasauce — fertig.\n'
                                                   'Wenig Aufwand, viel Nutzen.',
                                    'ingredients': ['Reis oder Reisreste',
                                                    'Eier',
                                                    'Karotten',
                                                    'TK-Gemüse oder Erbsen',
                                                    'Zwiebel',
                                                    'Knoblauch',
                                                    'Sojasauce',
                                                    'Öl',
                                                    'Optional: Curry',
                                                    'Optional: Sweet-Chili-Sauce'],
                                    'shopping': {'🛒 Obst & Gemüse': ['Karotten',
                                                                     'TK-Gemüse oder Erbsen',
                                                                     'Zwiebel',
                                                                     'Knoblauch'],
                                                 '🥩 Kühlung / Fleisch / Ei': ['Eier', 'Optional: Huhn'],
                                                 '🍚 Trockenware': ['Reis'],
                                                 '🥢 Saucen & Gewürze': ['Sojasauce',
                                                                        'Öl',
                                                                        'Optional: Curry',
                                                                        'Optional: Sweet-Chili-Sauce']},
                                    'steps': ['Reis vorkochen oder Reisreste verwenden.',
                                              'Zwiebel und Knoblauch anbraten.',
                                              'Gemüse dazugeben.',
                                              'Reis dazugeben und gut anrösten.',
                                              'Ei in die Pfanne geben und unterrühren.',
                                              'Mit Sojasauce und optional Curry abschmecken.',
                                              'Optional mit Sweet-Chili-Sauce servieren.']},
 '4. Kokos-Curry mit Reis': {'info': {'time': '25–30 Min',
                                      'budget': 'Günstig bis mittel',
                                      'level': 'Einfach',
                                      'family': 'Mild möglich'},
                             'description': 'Warmes Kokos-Curry für stressige Tage.\n'
                                            'Reis, Gemüse, Kokosmilch und optional Huhn oder Tofu.',
                             'ingredients': ['Reis',
                                             'Kokosmilch',
                                             'Currypaste oder Currypulver',
                                             'Karotten',
                                             'Brokkoli oder TK-Gemüse',
                                             'Zwiebel',
                                             'Knoblauch',
                                             'Optional: Huhn oder Tofu',
                                             'Öl',
                                             'Sojasauce'],
                             'shopping': {'🛒 Obst & Gemüse': ['Karotten',
                                                              'Brokkoli oder TK-Gemüse',
                                                              'Zwiebel',
                                                              'Knoblauch'],
                                          '🥩 Kühlung / Fleisch / Ei': ['Optional: Huhn oder Tofu'],
                                          '🍚 Trockenware': ['Reis'],
                                          '🥢 Saucen & Gewürze': ['Kokosmilch',
                                                                 'Currypaste oder Currypulver',
                                                                 'Sojasauce',
                                                                 'Öl']},
                             'steps': ['Reis kochen.',
                                       'Zwiebel und Knoblauch in Öl anbraten.',
                                       'Optional Huhn oder Tofu anbraten.',
                                       'Gemüse dazugeben.',
                                       'Kokosmilch und Curry dazugeben.',
                                       '10–15 Minuten köcheln lassen.',
                                       'Mit Sojasauce abschmecken und mit Reis servieren.']},
 '5. Teriyaki-Nudelpfanne': {'info': {'time': '20–25 Min',
                                      'budget': 'Günstig',
                                      'level': 'Einfach',
                                      'family': 'Süßlich / kinderfreundlich'},
                             'description': 'Schnelle Nudelpfanne mit süß-salziger Teriyaki-Richtung.\n'
                                            'Gut für Tage, wo der Kopf keine Diskussion mehr will.',
                             'ingredients': ['Mie-Nudeln oder Spaghetti',
                                             'Karotten',
                                             'Paprika oder TK-Gemüse',
                                             'Zwiebel',
                                             'Knoblauch',
                                             'Sojasauce',
                                             'Honig oder Zucker',
                                             'Optional: Huhn',
                                             'Öl'],
                             'shopping': {'🛒 Obst & Gemüse': ['Karotten',
                                                              'Paprika oder TK-Gemüse',
                                                              'Zwiebel',
                                                              'Knoblauch'],
                                          '🥩 Kühlung / Fleisch / Ei': ['Optional: Huhn'],
                                          '🍚 Trockenware': ['Mie-Nudeln oder Spaghetti'],
                                          '🥢 Saucen & Gewürze': ['Sojasauce', 'Honig oder Zucker', 'Öl']},
                             'steps': ['Nudeln kochen.',
                                       'Gemüse schneiden.',
                                       'Optional Huhn anbraten.',
                                       'Gemüse dazugeben und kurz braten.',
                                       'Sojasauce, Honig oder Zucker und etwas Wasser dazugeben.',
                                       'Nudeln untermischen und kurz ziehen lassen.']},
 '6. Eierreis mit Gemüse': {'info': {'time': '15–20 Min',
                                     'budget': 'Sehr günstig',
                                     'level': 'Sehr einfach',
                                     'family': 'Mild / schnell'},
                            'description': 'Einer der besten Familienretter.\n'
                                           'Reis, Ei, Gemüse, Sojasauce.\n'
                                           'Schnell, günstig, warm.',
                            'ingredients': ['Reis',
                                            'Eier',
                                            'Karotten',
                                            'Erbsen oder TK-Gemüse',
                                            'Zwiebel',
                                            'Knoblauch',
                                            'Sojasauce',
                                            'Öl'],
                            'shopping': {'🛒 Obst & Gemüse': ['Karotten',
                                                             'Erbsen oder TK-Gemüse',
                                                             'Zwiebel',
                                                             'Knoblauch'],
                                         '🥩 Kühlung / Fleisch / Ei': ['Eier'],
                                         '🍚 Trockenware': ['Reis'],
                                         '🥢 Saucen & Gewürze': ['Sojasauce', 'Öl']},
                            'steps': ['Reis kochen oder Reisreste verwenden.',
                                      'Zwiebel und Knoblauch anbraten.',
                                      'Gemüse dazugeben.',
                                      'Reis dazugeben und anrösten.',
                                      'Eier dazugeben und unterrühren.',
                                      'Mit Sojasauce abschmecken.']},
 '7. Erdnuss-Nudeln': {'info': {'time': '15–20 Min',
                                'budget': 'Günstig',
                                'level': 'Einfach',
                                'family': 'Cremig / mild'},
                       'description': 'Cremige Erdnuss-Nudeln.\n'
                                      'Wenig Zutaten, viel Geschmack.\n'
                                      'Perfekt, wenn wenig Energie da ist.',
                       'ingredients': ['Nudeln',
                                       'Erdnussbutter',
                                       'Sojasauce',
                                       'Knoblauch',
                                       'Karotten',
                                       'Optional: Gurke',
                                       'Optional: Sweet-Chili-Sauce',
                                       'Wasser zum Verdünnen'],
                       'shopping': {'🛒 Obst & Gemüse': ['Karotten', 'Knoblauch', 'Optional: Gurke'],
                                    '🥩 Kühlung / Fleisch / Ei': ['Optional: Huhn oder Tofu'],
                                    '🍚 Trockenware': ['Nudeln'],
                                    '🥢 Saucen & Gewürze': ['Erdnussbutter',
                                                           'Sojasauce',
                                                           'Optional: Sweet-Chili-Sauce']},
                       'steps': ['Nudeln kochen.',
                                 'Erdnussbutter mit Sojasauce und warmem Wasser cremig rühren.',
                                 'Knoblauch kurz anbraten.',
                                 'Karotten dazugeben.',
                                 'Nudeln und Sauce untermischen.',
                                 'Optional mit Gurke oder Sweet-Chili servieren.']},
 '8. Sweet-Chili-Huhn mit Reis': {'info': {'time': '25 Min',
                                           'budget': 'Mittel',
                                           'level': 'Einfach',
                                           'family': 'Süß / mild scharf möglich'},
                                  'description': 'Sweet-Chili-Huhn ist schnell, einfach und sehr familientauglich.\n'
                                                 'Reis dazu und fertig ist ein starkes Abendessen.',
                                  'ingredients': ['Huhn',
                                                  'Reis',
                                                  'Karotten',
                                                  'Paprika oder TK-Gemüse',
                                                  'Knoblauch',
                                                  'Sweet-Chili-Sauce',
                                                  'Sojasauce',
                                                  'Öl'],
                                  'shopping': {'🛒 Obst & Gemüse': ['Karotten', 'Paprika oder TK-Gemüse', 'Knoblauch'],
                                               '🥩 Kühlung / Fleisch / Ei': ['Huhn'],
                                               '🍚 Trockenware': ['Reis'],
                                               '🥢 Saucen & Gewürze': ['Sweet-Chili-Sauce', 'Sojasauce', 'Öl']},
                                  'steps': ['Reis kochen.',
                                            'Huhn klein schneiden und anbraten.',
                                            'Gemüse dazugeben.',
                                            'Sweet-Chili-Sauce und etwas Sojasauce dazugeben.',
                                            'Kurz einkochen lassen.',
                                            'Mit Reis servieren.']},
 '9. Ramen mit Ei & Gemüse': {'info': {'time': '15–20 Min',
                                       'budget': 'Günstig',
                                       'level': 'Sehr einfach',
                                       'family': 'Warm / schnell'},
                              'description': 'Schnelle Ramen-Bowl für kalte oder müde Tage.\n'
                                             'Ei, Gemüse, Nudeln, Brühe.\n'
                                             'Kein Luxus, aber echte Entlastung.',
                              'ingredients': ['Ramen- oder Mie-Nudeln',
                                              'Eier',
                                              'Karotten',
                                              'Frühlingszwiebel oder normale Zwiebel',
                                              'Knoblauch',
                                              'Brühe',
                                              'Sojasauce',
                                              'Optional: TK-Gemüse'],
                              'shopping': {'🛒 Obst & Gemüse': ['Karotten',
                                                               'Frühlingszwiebel oder normale Zwiebel',
                                                               'Knoblauch',
                                                               'Optional: TK-Gemüse'],
                                           '🥩 Kühlung / Fleisch / Ei': ['Eier'],
                                           '🍚 Trockenware': ['Ramen- oder Mie-Nudeln'],
                                           '🥢 Saucen & Gewürze': ['Brühe', 'Sojasauce']},
                              'steps': ['Brühe erhitzen.',
                                        'Karotten und Gemüse kurz mitkochen.',
                                        'Nudeln dazugeben.',
                                        'Ei kochen oder direkt in die Suppe geben.',
                                        'Mit Sojasauce abschmecken.',
                                        'Warm servieren.']},
 '10. Asia-Kraut-Wok mit Ei': {'info': {'time': '20 Min',
                                        'budget': 'Sehr günstig',
                                        'level': 'Einfach',
                                        'family': 'Mild / gut für Resteküche'},
                               'description': 'Kraut, Ei und Asia-Sauce.\n'
                                              'Einfach, günstig und überraschend gut.\n'
                                              'Cora sagt: kein Sidequest, nur Pfanne.',
                               'ingredients': ['Weißkraut oder Spitzkohl',
                                               'Eier',
                                               'Karotten',
                                               'Zwiebel',
                                               'Knoblauch',
                                               'Sojasauce',
                                               'Öl',
                                               'Optional: Reis oder Nudeln'],
                               'shopping': {'🛒 Obst & Gemüse': ['Weißkraut oder Spitzkohl',
                                                                'Karotten',
                                                                'Zwiebel',
                                                                'Knoblauch'],
                                            '🥩 Kühlung / Fleisch / Ei': ['Eier'],
                                            '🍚 Trockenware': ['Optional: Reis oder Nudeln'],
                                            '🥢 Saucen & Gewürze': ['Sojasauce', 'Öl']},
                               'steps': ['Kraut fein schneiden.',
                                         'Karotten, Zwiebel und Knoblauch vorbereiten.',
                                         'Zwiebel und Knoblauch in Öl anbraten.',
                                         'Kraut und Karotten dazugeben und braten.',
                                         'Eier dazugeben und unterrühren.',
                                         'Mit Sojasauce abschmecken.',
                                         'Optional mit Reis oder Nudeln servieren.']}}

baking_recipes = {'1. Schneller Kakao-Blechkuchen': {'info': {'time': '25–30 Min Backzeit',
                                             'budget': 'Günstig',
                                             'level': 'Einfach',
                                             'family': 'Kinderfreundlich'},
                                    'description': 'Einfacher Familienkuchen aus Standard-Zutaten.\n'
                                                   'Perfekt, wenn Kinder etwas Süßes wollen und kein Extra-Einkauf '
                                                   'passieren soll.',
                                    'ingredients': ['250 g Mehl',
                                                    '180 g Zucker',
                                                    '3 Eier',
                                                    '150 ml Milch',
                                                    '100 ml Öl',
                                                    '3 EL Kakao',
                                                    '1 Pkg Backpulver'],
                                    'missing_check': ['Mehl',
                                                      'Zucker',
                                                      'Eier',
                                                      'Milch',
                                                      'Öl oder Butter',
                                                      'Kakao',
                                                      'Backpulver'],
                                    'steps': ['Backofen auf 180 °C Ober-/Unterhitze vorheizen.',
                                              'Mehl, Zucker, Kakao und Backpulver mischen.',
                                              'Eier, Milch und Öl dazugeben.',
                                              'Alles glatt rühren.',
                                              'Auf ein kleines Blech oder in eine Form geben.',
                                              'Ca. 25–30 Minuten backen.',
                                              'Abkühlen lassen und servieren.']},
 '2. Cora Waffeln': {'info': {'time': '20 Min',
                              'budget': 'Sehr günstig',
                              'level': 'Einfach',
                              'family': 'Perfekt mit Kindern'},
                     'description': 'Waffeln retten viele Nachmittage.\nMehl, Milch, Eier, Zucker — fertig.',
                     'ingredients': ['250 g Mehl',
                                     '2 Eier',
                                     '300 ml Milch',
                                     '2 EL Zucker',
                                     '1 Prise Salz',
                                     '1 TL Backpulver',
                                     'Öl oder Butter fürs Waffeleisen'],
                     'missing_check': ['Mehl', 'Eier', 'Milch', 'Zucker', 'Backpulver', 'Öl oder Butter'],
                     'steps': ['Alle Zutaten zu einem glatten Teig rühren.',
                               'Waffeleisen vorheizen.',
                               'Leicht einfetten.',
                               'Waffeln portionsweise backen.',
                               'Mit Zucker, Obst oder Marmelade servieren.']},
 '3. Bananen-Pancakes': {'info': {'time': '15–20 Min',
                                  'budget': 'Günstig',
                                  'level': 'Sehr einfach',
                                  'family': 'Gut für reife Bananen'},
                         'description': 'Gut, wenn Bananen weg müssen.\nSchnell, weich, familientauglich.',
                         'ingredients': ['2 reife Bananen',
                                         '2 Eier',
                                         '120 g Mehl',
                                         '120 ml Milch',
                                         '1 TL Backpulver',
                                         'Öl oder Butter'],
                         'missing_check': ['Bananen', 'Eier', 'Mehl', 'Milch', 'Backpulver', 'Öl oder Butter'],
                         'steps': ['Bananen zerdrücken.',
                                   'Eier, Mehl, Milch und Backpulver einrühren.',
                                   'Pfanne erhitzen und etwas Öl oder Butter verwenden.',
                                   'Kleine Pancakes ausbacken.',
                                   'Warm servieren.']},
 '4. Apfelkuchen einfach': {'info': {'time': '35–45 Min',
                                     'budget': 'Günstig',
                                     'level': 'Einfach',
                                     'family': 'Klassiker'},
                            'description': 'Einfacher Apfelkuchen für Familie und Wochenende. Gut, wenn Äpfel da sind.',
                            'ingredients': ['250 g Mehl',
                                            '120 g Zucker',
                                            '2 Eier',
                                            '120 g Butter oder Öl',
                                            '3 Äpfel',
                                            '1 Pkg Backpulver',
                                            'Milch nach Bedarf'],
                            'missing_check': ['Mehl',
                                              'Zucker',
                                              'Eier',
                                              'Butter oder Öl',
                                              'Äpfel',
                                              'Backpulver',
                                              'Milch'],
                            'steps': ['Backofen auf 180 °C vorheizen.',
                                      'Äpfel schneiden.',
                                      'Teig rühren.',
                                      'Äpfel unterheben oder oben auflegen.',
                                      'Ca. 35–45 Minuten backen.']},
 '5. Marmorkuchen': {'info': {'time': '45–55 Min', 'budget': 'Günstig', 'level': 'Einfach', 'family': 'Hält gut'},
                     'description': 'Einfacher Vorratskuchen. Gut für mehrere Tage und Jause.',
                     'ingredients': ['300 g Mehl',
                                     '180 g Zucker',
                                     '3 Eier',
                                     '150 ml Milch',
                                     '120 ml Öl',
                                     '2 EL Kakao',
                                     '1 Pkg Backpulver'],
                     'missing_check': ['Mehl', 'Zucker', 'Eier', 'Milch', 'Öl', 'Kakao', 'Backpulver'],
                     'steps': ['Teig rühren.',
                               'Hälfte hell lassen, Hälfte mit Kakao mischen.',
                               'In Form geben.',
                               'Ca. 45–55 Minuten backen.']},
 '6. Muffins Grundrezept': {'info': {'time': '20–25 Min Backzeit',
                                     'budget': 'Günstig',
                                     'level': 'Einfach',
                                     'family': 'Kinderfreundlich'},
                            'description': 'Kleine Kuchen, einfach portioniert. Gut für Schule, Nachmittag oder '
                                           'Besuch.',
                            'ingredients': ['250 g Mehl',
                                            '120 g Zucker',
                                            '2 Eier',
                                            '200 ml Milch',
                                            '80 ml Öl',
                                            '1 Pkg Backpulver'],
                            'missing_check': ['Mehl', 'Zucker', 'Eier', 'Milch', 'Öl', 'Backpulver'],
                            'steps': ['Alles zu einem Teig rühren.',
                                      'In Muffinformen füllen.',
                                      'Ca. 20–25 Minuten backen.']},
 '7. Schoko-Muffins': {'info': {'time': '20–25 Min Backzeit', 'budget': 'Günstig', 'level': 'Einfach', 'family': 'Süß'},
                       'description': 'Muffins mit Kakao. Schnell, einfach und meistens beliebt.',
                       'ingredients': ['250 g Mehl',
                                       '140 g Zucker',
                                       '2 Eier',
                                       '200 ml Milch',
                                       '80 ml Öl',
                                       '3 EL Kakao',
                                       '1 Pkg Backpulver'],
                       'missing_check': ['Mehl', 'Zucker', 'Eier', 'Milch', 'Öl', 'Kakao', 'Backpulver'],
                       'steps': ['Teig rühren.', 'In Muffinformen füllen.', 'Ca. 20–25 Minuten backen.']},
 '8. Palatschinken': {'info': {'time': '20 Min', 'budget': 'Sehr günstig', 'level': 'Einfach', 'family': 'Alltag'},
                      'description': 'Schnell aus Basis-Zutaten. Gut, wenn wenig da ist.',
                      'ingredients': ['250 g Mehl', '2 Eier', '500 ml Milch', '1 Prise Salz', 'Öl oder Butter'],
                      'missing_check': ['Mehl', 'Eier', 'Milch', 'Öl oder Butter'],
                      'steps': ['Teig rühren.',
                                'Kurz rasten lassen.',
                                'Dünn in Pfanne ausbacken.',
                                'Mit Marmelade oder Zucker servieren.']},
 '9. Kaiserschmarrn': {'info': {'time': '20–25 Min', 'budget': 'Günstig', 'level': 'Einfach', 'family': 'Sattmacher'},
                       'description': 'Süßer Sattmacher. Gut, wenn Kochen einfach bleiben soll.',
                       'ingredients': ['200 g Mehl', '3 Eier', '300 ml Milch', '2 EL Zucker', 'Butter oder Öl'],
                       'missing_check': ['Mehl', 'Eier', 'Milch', 'Zucker', 'Butter oder Öl'],
                       'steps': ['Teig rühren.',
                                 'In Pfanne stocken lassen.',
                                 'Zerteilen und goldbraun braten.',
                                 'Mit Zucker servieren.']},
 '10. Arme Ritter': {'info': {'time': '15 Min',
                              'budget': 'Sehr günstig',
                              'level': 'Sehr einfach',
                              'family': 'Resteverwertung'},
                     'description': 'Perfekt für altes Brot oder Toast. Wenig Zutaten, schneller Nutzen.',
                     'ingredients': ['Brot oder Toast', '2 Eier', 'Milch', 'Zucker', 'Butter oder Öl'],
                     'missing_check': ['Brot oder Toast', 'Eier', 'Milch', 'Zucker', 'Butter oder Öl'],
                     'steps': ['Eier mit Milch verrühren.',
                               'Brot einlegen.',
                               'In Pfanne ausbacken.',
                               'Mit Zucker servieren.']}}

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background:
        radial-gradient(circle at top center, rgba(255, 110, 20, 0.18), transparent 32%),
        linear-gradient(180deg, #160600 0%, #070301 58%, #000000 100%);
    color: #f7efe7;
}

.block-container {
    max-width: 820px;
    padding-top: 1rem;
    padding-bottom: 160px;
}

p, div, span, label {
    color: #f1e7dc !important;
}

[data-testid="stImage"] img {
    border-radius: 22px;
    border: 1px solid rgba(255, 160, 55, 0.38);
    box-shadow: 0 0 30px rgba(255, 110, 20, 0.18);
}

.cora-header, .cora-card {
    background: rgba(0, 0, 0, 0.72);
    border: 1px solid rgba(255, 160, 55, 0.35);
    border-radius: 22px;
    padding: 18px;
    margin-bottom: 18px;
    box-shadow: 0 0 24px rgba(255, 110, 20, 0.10);
}

.cora-title {
    color: #ff9f2f !important;
    font-size: 2rem;
    font-weight: 950;
    margin-bottom: 8px;
}

.cora-subtitle, .card-text {
    color: #f8eadf !important;
    font-size: 1.02rem;
    line-height: 1.55;
}

.card-title, .section-title, .shopping-category-title {
    color: #ff9f2f !important;
    font-weight: 950;
}

.card-title {
    font-size: 1.35rem;
    margin-bottom: 10px;
}

.section-title {
    font-size: 1.32rem;
    margin-top: 24px;
    margin-bottom: 12px;
}

.shopping-category-title {
    font-size: 1.16rem;
    margin-top: 20px;
    margin-bottom: 8px;
}

.list-item {
    background: rgba(255, 255, 255, 0.060);
    border: 1px solid rgba(255, 160, 55, 0.18);
    border-radius: 13px;
    padding: 9px 12px;
    margin-bottom: 8px;
    font-size: 1rem;
    font-weight: 600;
    line-height: 1.45;
}

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
}

.stButton > button {
    background: linear-gradient(135deg, #ff9f2f, #ff4d1a);
    color: #160600 !important;
    border: none;
    border-radius: 15px;
    font-weight: 950;
    padding: 0.75rem 1rem;
    width: 100%;
}

.stSelectbox label, .stMultiSelect label, .stRadio label, [data-testid="stFileUploader"] label {
    color: #ffb14a !important;
    font-weight: 900 !important;
}

.stSelectbox div[data-baseweb="select"] > div,
.stMultiSelect div[data-baseweb="select"] > div {
    background: rgba(0, 0, 0, 0.86) !important;
    border: 1px solid rgba(255, 160, 55, 0.50) !important;
    border-radius: 15px !important;
    min-height: 50px !important;
}

.stSelectbox div[data-baseweb="select"] span,
.stSelectbox div[data-baseweb="select"] div,
.stMultiSelect div[data-baseweb="select"] span,
.stMultiSelect div[data-baseweb="select"] div {
    color: #fff3e4 !important;
}

[data-testid="stFileUploader"] {
    background: rgba(0, 0, 0, 0.72);
    border: 1px dashed rgba(255, 160, 55, 0.60);
    border-radius: 18px;
    padding: 14px;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 0.95rem;
        padding-right: 0.95rem;
    }
    .cora-title {
        font-size: 1.55rem;
    }
    .info-grid {
        grid-template-columns: 1fr;
    }
}

/* V7 visible stable nav */
.nav-title {
    margin-top: 18px !important;
    margin-bottom: 8px !important;
}

.stButton > button {
    min-height: 54px !important;
    font-size: 1.02rem !important;
    font-weight: 950 !important;
    border-radius: 16px !important;
    background: linear-gradient(135deg, #ff9f2f, #ff4d1a) !important;
    color: #100400 !important;
    border: 1px solid rgba(255, 190, 90, 0.85) !important;
    box-shadow: 0 0 18px rgba(255, 110, 20, 0.22) !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #ffbd5b, #ff6b2a) !important;
    color: #000000 !important;
    border: 1px solid rgba(255, 220, 150, 1) !important;
}

.stButton > button:focus {
    outline: 3px solid rgba(255, 190, 80, 0.65) !important;
    color: #000000 !important;
}

[data-testid="column"] {
    padding: 0.15rem 0.15rem !important;
}

@media (max-width: 600px) {
    .stButton > button {
        min-height: 58px !important;
        font-size: 0.95rem !important;
        padding: 0.7rem 0.35rem !important;
        white-space: normal !important;
    }

    .cora-title {
        font-size: 1.45rem !important;
    }

    .card-text {
        font-size: 0.94rem !important;
    }
}


/* V8 recipe selector fix: no white dropdowns */
.stRadio {
    background: rgba(0, 0, 0, 0.68) !important;
    border: 1px solid rgba(255, 160, 55, 0.35) !important;
    border-radius: 18px !important;
    padding: 12px 14px !important;
    margin-bottom: 16px !important;
}

.stRadio > label {
    color: #ffb14a !important;
    font-size: 1.02rem !important;
    font-weight: 950 !important;
}

.stRadio div[role="radiogroup"] {
    gap: 0.35rem !important;
}

.stRadio div[role="radiogroup"] label {
    background: rgba(255, 255, 255, 0.055) !important;
    border: 1px solid rgba(255, 160, 55, 0.18) !important;
    border-radius: 13px !important;
    padding: 8px 10px !important;
    margin-bottom: 6px !important;
}

.stRadio div[role="radiogroup"] label:hover {
    background: rgba(255, 120, 20, 0.14) !important;
    border: 1px solid rgba(255, 160, 55, 0.36) !important;
}

.stRadio div[role="radiogroup"] label span,
.stRadio div[role="radiogroup"] label div,
.stRadio div[role="radiogroup"] label p {
    color: #fff3e4 !important;
    font-size: 0.98rem !important;
    font-weight: 750 !important;
}

/* Keep multiselect readable in Plan-Einkauf */
.stMultiSelect div[data-baseweb="select"] > div {
    background: rgba(0, 0, 0, 0.88) !important;
    border: 1px solid rgba(255, 160, 55, 0.52) !important;
    border-radius: 15px !important;
}

div[role="listbox"] {
    background: #090302 !important;
    border: 1px solid rgba(255, 160, 55, 0.55) !important;
}

div[role="option"] {
    color: #fff3e4 !important;
    background: #090302 !important;
    font-weight: 800 !important;
}

div[role="option"]:hover {
    background: rgba(255, 120, 20, 0.22) !important;
}

@media (max-width: 600px) {
    .stRadio {
        padding: 10px 10px !important;
    }

    .stRadio div[role="radiogroup"] label {
        padding: 9px 9px !important;
    }

    .stRadio div[role="radiogroup"] label span,
    .stRadio div[role="radiogroup"] label div,
    .stRadio div[role="radiogroup"] label p {
        font-size: 0.92rem !important;
    }
}


/* V9 button chooser: recipes must show, no dropdown/radio bug */
.section-title {
    clear: both !important;
}

.stButton > button {
    white-space: normal !important;
    text-align: center !important;
}

@media (max-width: 600px) {
    .stButton > button {
        min-height: 54px !important;
        font-size: 0.90rem !important;
        line-height: 1.2 !important;
    }
}


/* V10 Plan-Einkauf Lesbarkeit Fix */
.stMultiSelect label {
    color: #ffb14a !important;
    font-size: 1.05rem !important;
    font-weight: 950 !important;
}

/* Hauptfeld vom Multiselect */
.stMultiSelect div[data-baseweb="select"] > div {
    background: rgba(0, 0, 0, 0.92) !important;
    border: 1px solid rgba(255, 160, 55, 0.65) !important;
    border-radius: 15px !important;
    min-height: 54px !important;
    color: #fff3e4 !important;
}

/* Text im Feld */
.stMultiSelect div[data-baseweb="select"] span,
.stMultiSelect div[data-baseweb="select"] div,
.stMultiSelect div[data-baseweb="select"] input {
    color: #fff3e4 !important;
    font-weight: 800 !important;
}

/* Placeholder */
.stMultiSelect input::placeholder {
    color: #ffe0b8 !important;
    opacity: 1 !important;
}

/* Ausgewählte Chips */
.stMultiSelect span[data-baseweb="tag"] {
    background: linear-gradient(135deg, #ff9f2f, #ff4d1a) !important;
    border: 1px solid rgba(255, 210, 140, 0.85) !important;
    border-radius: 12px !important;
}

.stMultiSelect span[data-baseweb="tag"] span,
.stMultiSelect span[data-baseweb="tag"] div,
.stMultiSelect span[data-baseweb="tag"] svg {
    color: #130500 !important;
    fill: #130500 !important;
    font-weight: 950 !important;
}

/* Offene Dropdown-Liste */
div[data-baseweb="popover"] {
    z-index: 999999 !important;
}

div[role="listbox"] {
    background: #080302 !important;
    border: 1px solid rgba(255, 160, 55, 0.70) !important;
    border-radius: 14px !important;
    box-shadow: 0 0 24px rgba(255, 110, 20, 0.20) !important;
}

/* Optionen in der Dropdown-Liste */
div[role="option"] {
    background: #080302 !important;
    color: #fff3e4 !important;
    font-weight: 850 !important;
    min-height: 42px !important;
}

div[role="option"] span,
div[role="option"] div {
    color: #fff3e4 !important;
    font-weight: 850 !important;
}

div[role="option"]:hover,
div[role="option"][aria-selected="true"] {
    background: rgba(255, 120, 20, 0.28) !important;
    color: #ffffff !important;
}

/* Kleine Helligkeits-Fallen in Plan-Einkauf */
.stMultiSelect [data-testid="stMarkdownContainer"] p {
    color: #fff3e4 !important;
}

@media (max-width: 600px) {
    .stMultiSelect div[data-baseweb="select"] > div {
        min-height: 58px !important;
    }

    div[role="option"] {
        min-height: 46px !important;
        font-size: 0.95rem !important;
    }
}

</style>
""", unsafe_allow_html=True)

def show_card(title, text):
    text = str(text).replace("\n", "<br>")
    st.markdown(f"""
    <div class="cora-card">
        <div class="card-title">{title}</div>
        <div class="card-text">{text}</div>
    </div>
    """, unsafe_allow_html=True)

def show_info(recipe):
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

def show_list(title, items, icon="🧾"):
    st.markdown(f'<div class="section-title">{icon} {title}</div>', unsafe_allow_html=True)
    for item in items:
        st.markdown(f'<div class="list-item">{item}</div>', unsafe_allow_html=True)

def normalize_item(item):
    return " ".join(str(item).replace("Optional:", "").strip().split())

def bake_category(item):
    l = item.lower()
    if any(x in l for x in ["milch", "eier", "butter", "topfen", "joghurt"]):
        return "🥛 Kühlung / Backen"
    if any(x in l for x in ["apfel", "äpfel", "bananen", "obst"]):
        return "🛒 Obst & Gemüse"
    return "🍚 Vorrat / Backen"

def collect_plan(selected_cooking, selected_baking):
    result = {}
    def add(cat, item, source):
        item = normalize_item(item)
        if not item:
            return
        result.setdefault(cat, {})
        result[cat].setdefault(item, set())
        result[cat][item].add(source)
    for name in selected_cooking:
        r = recipes.get(name)
        if not r:
            continue
        for cat, items in r["shopping"].items():
            for item in items:
                add(cat, item, name)
    for name in selected_baking:
        b = baking_recipes.get(name)
        if not b:
            continue
        for item in b.get("missing_check", b.get("ingredients", [])):
            add(bake_category(item), item, name)
    return result

def estimate_budget(period, cooking_count, baking_count):
    base = {"1 Woche": (45, 95), "2 Wochen": (85, 160), "1 Monat": (160, 300)}.get(period, (45, 95))
    low, high = base
    if cooking_count > 5:
        low += (cooking_count - 5) * 7
        high += (cooking_count - 5) * 10
    low += baking_count * 3
    high += baking_count * 7
    return low, high


def choose_from_buttons(title, names, state_key, prefix):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)

    if state_key not in st.session_state or st.session_state[state_key] not in names:
        st.session_state[state_key] = names[0]

    for start in range(0, len(names), 2):
        cols = st.columns(2)
        for idx, name in enumerate(names[start:start + 2]):
            with cols[idx]:
                number = names.index(name) + 1
                active = " ✅" if st.session_state[state_key] == name else ""
                if st.button(f"{number}. {name.split('. ', 1)[-1]}{active}", key=f"{prefix}_{number}", use_container_width=True):
                    st.session_state[state_key] = name
                    st.rerun()

    return st.session_state[state_key]


def quick_selected_line(label, selected):
    st.markdown(
        f'<div class="list-item"><b>{label}:</b> {selected}</div>',
        unsafe_allow_html=True
    )

CORA_IMAGE = find_cora_image()
if CORA_IMAGE:
    st.image(str(CORA_IMAGE), width="stretch")

st.markdown("""
<div class="cora-header">
    <div class="cora-title">🔥 Cora Family Kitchen</div>
    <div class="cora-subtitle">
        Planen. Einkaufen. Kochen. Backen.<br>
        Weniger Chaos im Kopf. Mehr Sicherheit im Alltag.
    </div>
</div>
""", unsafe_allow_html=True)

pages = ["🏠 Start", "🍳 Rezept", "📅 Plan-Einkauf", "🛒 Einkauf", "👨‍🍳 Kochen", "📸 Upload"]

if "page" not in st.session_state:
    st.session_state.page = "🏠 Start"

def set_page(new_page):
    st.session_state.page = new_page

st.markdown('<div class="section-title nav-title">Menü</div>', unsafe_allow_html=True)

nav_rows = [
    ["🏠 Start", "🍳 Rezept"],
    ["📅 Plan-Einkauf", "🛒 Einkauf"],
    ["👨‍🍳 Kochen", "📸 Upload"],
]

for row in nav_rows:
    cols = st.columns(2)
    for col, nav_page in zip(cols, row):
        with col:
            active = " ✅" if st.session_state.page == nav_page else ""
            st.button(
                f"{nav_page}{active}",
                key=f"nav_btn_{nav_page}",
                use_container_width=True,
                on_click=set_page,
                args=(nav_page,)
            )

page = st.session_state.page

if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = list(recipes.keys())[0]
if "selected_baking" not in st.session_state:
    st.session_state.selected_baking = list(baking_recipes.keys())[0]
if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

st.markdown(f'<div class="list-item">Aktuell offen: <b>{page}</b></div>', unsafe_allow_html=True)

recipe_names = list(recipes.keys())
baking_names = list(baking_recipes.keys())

if page == "🏠 Start":
    show_card("Willkommen", "Cora hat eine Aufgabe: Einkaufen und Kochen leichter machen. Wähle ein Rezept, plane mehrere Gerichte oder lade Bilder hoch.")
    c1, c2 = st.columns(2)
    with c1:
        st.info("Nutze oben das Menü.")
    with c2:
        st.info("Plan-Einkauf ist für Woche oder Monat.")

elif page == "🍳 Rezept":
    mode = st.radio("Bereich wählen", ["🍲 Kochen", "🍰 Backen"], horizontal=True)
    if mode == "🍲 Kochen":
        selected = choose_from_buttons("Gericht auswählen", recipe_names, "selected_recipe", "recipe_main")
        quick_selected_line("Ausgewählt", selected)
        recipe = recipes[selected]
        show_card(selected, recipe["description"])
        show_info(recipe)
        show_list("Zutaten", recipe["ingredients"])
    else:
        selected = choose_from_buttons("Backidee auswählen", baking_names, "selected_baking", "baking_main")
        quick_selected_line("Ausgewählt", selected)
        bake = baking_recipes[selected]
        show_card(selected, bake["description"])
        show_info(bake)
        show_list("Back-Zutaten", bake["ingredients"])

elif page == "📅 Plan-Einkauf":
    show_card("📅 Plan-Einkauf", "Plane 1 Woche, 2 Wochen oder 1 Monat. Wähle Kochen und Backen aus. Cora macht daraus eine gemeinsame Einkaufsliste.")
    period = st.radio("Zeitraum wählen", ["1 Woche", "2 Wochen", "1 Monat"], horizontal=True)
    selected_cooking = st.multiselect("🍲 Kochideen auswählen", recipe_names)
    selected_baking = st.multiselect("🍰 Backideen auswählen", baking_names)

    if selected_cooking or selected_baking:
        low, high = estimate_budget(period, len(selected_cooking), len(selected_baking))
        show_card("💰 Cora Preisgefühl", f"Zeitraum: <b>{period}</b><br>Auswahl: <b>{len(selected_cooking)}</b> Kochidee(n) + <b>{len(selected_baking)}</b> Backidee(n)<br><br>Grobe Schätzung: <b>ca. {low}–{high} €</b><br>Preise können je nach Aktion, Filiale und Vorrat abweichen.")

    if st.button("🛒 Einkaufsliste erstellen", use_container_width=True):
        st.session_state.plan_ready = True

    if st.session_state.get("plan_ready"):
        if not selected_cooking and not selected_baking:
            show_card("Noch nichts ausgewählt", "Wähle mindestens eine Kochidee oder Backidee aus.")
        else:
            plan = collect_plan(selected_cooking, selected_baking)
            st.markdown('<div class="section-title">🛒 Gemeinsame Einkaufsliste</div>', unsafe_allow_html=True)
            show_card("Cora hat zusammengelegt", "Gleiche Zutaten stehen nur einmal auf der Liste. Die Liste ist nach Marktbereichen sortiert.")
            for cat, items in plan.items():
                st.markdown(f'<div class="shopping-category-title">{cat}</div>', unsafe_allow_html=True)
                for item, sources in sorted(items.items(), key=lambda x: x[0].lower()):
                    note = f" — für {len(sources)} Auswahl(en)" if len(sources) > 1 else ""
                    st.checkbox(f"{item}{note}", key=f"plan_{st.session_state.reset_counter}_{cat}_{item}")
            show_card("📦 Hinweis", "Vorrat hält länger. Frische Ware bewusst prüfen, damit nichts schlecht wird.")

elif page == "🛒 Einkauf":
    selected = choose_from_buttons("Gericht für Einkaufsliste auswählen", recipe_names, "selected_recipe", "recipe_shop")
    quick_selected_line("Ausgewählt", selected)
    recipe = recipes[selected]
    st.markdown('<div class="section-title">🛒 Einkaufsliste</div>', unsafe_allow_html=True)
    for cat, items in recipe["shopping"].items():
        st.markdown(f'<div class="shopping-category-title">{cat}</div>', unsafe_allow_html=True)
        for item in items:
            st.checkbox(item, key=f"shop_{st.session_state.reset_counter}_{selected}_{cat}_{item}")
    if st.button("✅ Einkaufsliste zurücksetzen", use_container_width=True):
        st.session_state.reset_counter += 1
        st.rerun()

elif page == "👨‍🍳 Kochen":
    selected = choose_from_buttons("Gericht auswählen", recipe_names, "selected_recipe", "recipe_cooking")
    quick_selected_line("Ausgewählt", selected)
    recipe = recipes[selected]
    show_card(selected, recipe["description"])
    st.markdown('<div class="section-title">👨‍🍳 Kochschritte</div>', unsafe_allow_html=True)
    for i, step in enumerate(recipe["steps"], start=1):
        st.markdown(f'<div class="list-item"><b>{i}.</b> {step}</div>', unsafe_allow_html=True)

elif page == "📸 Upload":
    show_card("📸 Was ist da?", "Lade Bilder von Kühlschrank, Vorrat oder Tiefkühl hoch. Cora nutzt das später für Ideen und fehlende Zutaten.")
    uploaded_photos = st.file_uploader(
        "📸 Bilder hochladen",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
        key="photo_upload"
    )
    if uploaded_photos:
        st.success(f"✅ {len(uploaded_photos)} Bild(er) geladen.")
        cols = st.columns(3)
        for idx, photo in enumerate(uploaded_photos[:3]):
            with cols[idx % 3]:
                st.image(photo, width="stretch")
        if st.button("✨ Cora prüfen und sortieren", use_container_width=True):
            st.session_state.photos_checked = True

    if st.session_state.get("photos_checked"):
        show_card("📦 Cora Demo-Sortierung", "Basis: Reis, Nudeln, Kartoffeln<br>Gemüse/TK: TK Gemüse, Karotten, Zwiebel<br>Eiweiß: Eier, Putenfleisch<br>Backen: Mehl, Zucker, Milch, Kakao")
        show_card("💡 Cora Ideen", "Asia-Reis mit Gemüse und Ei<br>Nudelpfanne mit Karotten und Zwiebel<br>Kartoffelpfanne<br>Schneller Kakao-Blechkuchen")
