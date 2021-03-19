"""In diesem Fragebogen-Programm werdet ihr folgendes lernen:

* Funktionen benutzen um Aufgaben zu trennen: eine Funktion pro Frage
* Variablen optimal nutzen um Wiederholungen zu sparen
* Warten auf Eingabe des Benutzers
* Rückmeldung mit Emojis und Farben
* Definition von Farben
* Benutzer alle Fragen stellen und die Anzahl der richtigen Antworten sammeln
"""

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


def frage1():
    console.print("Laut den monotheistischen Religionen (Judentum, Christentum, Islam) hießen die ersten Menschen:")
    antwort = console.input(auswahl_vorlage.format("Jesua & Elisa", "Adam & Eva", "Lorem & Ipsum"))

    if antwort.lower() == "b":
        console.print(richtig, style="richtig")
        RICHTIGE_ANTWORTEN.append(1)
    else:
        console.print(falsch, style="falsch")
    return None


def frage2():
    console.print("Folgender Prophet wird im Koran am meisten erwähnt:")
    antwort = console.input(auswahl_vorlage.format("Mohammad a.s.", "Jesus", "Abraham"))

    if antwort.lower() == "b":
        console.print(richtig, style="richtig")
        RICHTIGE_ANTWORTEN.append(1)
    else:
        console.print(falsch, style="falsch")


if __name__ == '__main__':
    alle_fragen = [frage1, frage2]
    for frage in alle_fragen:
        frage()
    console.print(
        f"Du hast alle Fragen beantwortet und {sum(RICHTIGE_ANTWORTEN)} von {len(alle_fragen)} richtig beantwortet!")
