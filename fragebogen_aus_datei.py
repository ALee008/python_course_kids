from rich.console import Console
from rich.theme import Theme

farben = Theme({
    "richtig": "green",
    "falsch": "red",
    "wichtig": "bold white",
    "auswahl": "white"
})

console = Console(theme=farben, record=True)
auswahl_vorlage = "[auswahl]a)[/auswahl] {} [auswahl]b)[/auswahl] {} [auswahl]c)[/auswahl] {}\n>>> "
richtig = "Richtig :thumbsup:, weiter zur nächsten Frage."
falsch = "Schade :pensive:, leider war das die falsche Antwort. Aber weiter geht's!"

RICHTIGE_ANTWORTEN = []


def hole_alle_fragen_und_antworten(datei: str) -> list:
    with open(datei, "r") as fragen_datei:
        fragen_und_antworten = fragen_datei.readlines()

    return fragen_und_antworten[1:]


def stelle_fragen(fragen_und_antworten: list) -> None:
    frage_auswahl: str
    for frage_auswahl in fragen_und_antworten:
        frage, ant_a, ant_b, ant_c, richtige_antwort = frage_auswahl.split(";")
        console.print(frage + ':')
        antwort = console.input(auswahl_vorlage.format(ant_a, ant_b, ant_c))

        if antwort.lower() == richtige_antwort.strip():
            console.print(richtig, style="richtig")
            RICHTIGE_ANTWORTEN.append(1)
        else:
            console.print(falsch, style="falsch")

    return None


if __name__ == '__main__':
    alle_fragen_und_antworten = hole_alle_fragen_und_antworten("fragen.csv")
    stelle_fragen(alle_fragen_und_antworten)
    console.print(f"\n:tada::confetti_ball: Du hast alle Fragen beantwortet und {sum(RICHTIGE_ANTWORTEN)} "
                  f"von {len(alle_fragen_und_antworten)} richtig beantwortet! :balloon::tada:")
