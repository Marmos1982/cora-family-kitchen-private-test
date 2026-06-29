from pathlib import Path
import shutil
import py_compile

main = Path("main.py")
backup = Path("main_backup_before_button_fix.py")

shutil.copy(main, backup)
text = main.read_text(encoding="utf-8")

# Alte Button-Regel gezielt verbessern
text = text.replace(
"""/* Navigation: bigger touch targets, stable on desktop and mobile */
div[data-testid="column"] .stButton > button {
    min-height: 52px;
    padding: 0.70rem 0.55rem;
    font-size: 0.96rem;
    white-space: normal;
}""",
"""/* Navigation: iPhone safe buttons */
div[data-testid="column"] .stButton > button {
    min-height: 76px !important;
    padding: 0.85rem 0.55rem !important;
    font-size: 1.05rem !important;
    border-radius: 20px !important;
    white-space: normal !important;
}"""
)

# Mobile-Regel ergänzen
mobile_marker = """    .stCheckbox label {
        font-size: 0.98rem !important;
    }
}"""

mobile_new = """    .stCheckbox label {
        font-size: 0.98rem !important;
    }

    div[data-testid="column"] .stButton > button {
        min-height: 82px !important;
        font-size: 1.08rem !important;
        padding: 0.9rem 0.5rem !important;
    }
}"""

text = text.replace(mobile_marker, mobile_new)

main.write_text(text, encoding="utf-8")

try:
    py_compile.compile(str(main), doraise=True)
    print("✅ BUTTON FIX OK. Backup:", backup)
except Exception as e:
    shutil.copy(backup, main)
    print("❌ Fehler. Backup zurückgespielt.")
    print(e)
