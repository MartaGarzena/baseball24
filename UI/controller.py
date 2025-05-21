import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI

        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        pass

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass

    def fillDDYear(self):
        years = self._model.getYears()  #lista di oggetti
        yearsDD = map(lambda x: ft.dropdown.Option(x), years)
        #map prende funzione e iterable e applica la funzione a ogni oggetto.

        self._view._ddAnno.options = yearsDD
        self._view.update_page()

    def handleDDYearSelection(self, e):
        teams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(
            ft.Text(f"Ho trovato {len(teams)} "
                    f"squade che hanno giocato nel {self._view._ddAnno.value}."))
        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{t.teamCode}"))
            self._view._ddSquadra.options.append(
                ft.dropdown.Option(data=t, text=t.teamCode, on_click=self.readDDTeams))
        self._view.update_page()

    def readDDTeams(self, e):
        if e.control.data is None:
            self._selectedTeam = None
        else:
            self.selectedTeam = e.control.data
        print(F"readDDTeams chiamata: {e.control.data}")
