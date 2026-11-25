from pathlib import Path
import sys

DIRETORIO_ATUAL = str(Path(__file__).resolve().parent)
if DIRETORIO_ATUAL not in sys.path:
    sys.path.insert(0, DIRETORIO_ATUAL)

try:
    from .menu import MenuFinanceiro
except ImportError:
    from menu import MenuFinanceiro


def main():
    app = MenuFinanceiro()
    app.mainloop()


if __name__ == "__main__":
    main()
