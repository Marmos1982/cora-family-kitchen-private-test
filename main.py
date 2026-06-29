from pathlib import Path
import py_compile
import shutil

main = Path("main.py")
backup = Path("main_backup_before_mobile_fix.py")

shutil.copy(main, backup)

text = main.read_text(encoding="utf-8")

text = text.replace("use_column_width=True", "use_container_width=True")

old = """    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-bottom: 220px !important;
    }"""

new = """    .block-container {
        padding-top: 120px !important;
        padding-bottom: 430px !important;
        padding-left: 1.15rem !important;
        padding-right: 1.15rem !important;
    }"""

text = text.replace(old, new)

old2 = """.block-container {
    max-width: 780px;
    padding-top: 1.2rem;
    padding-bottom: 200px !important;
}"""

new2 = """.block-container {
    max-width: 780px;
    padding-top: 90px !important;
    padding-bottom: 360px !important;
}"""

text = text.replace(old2, new2)

main.write_text(text, encoding="utf-8")

try:
    py_compile.compile(str(main), doraise=True)
    print("✅ SAFE FIX OK: main.py läuft. Backup:", backup)
except Exception as e:
    shutil.copy(backup, main)
    print("❌ Fehler erkannt. Backup wurde zurückgespielt.")
    print(e)
