import roll_marker_backend
import roll_marker_frontend

class RollMarkerApplication:
    def __init__(self):
        self.__roll_marker_backend = roll_marker_backend.BackEnd("dataset.csv")
        self.__roll_marker_frontend = roll_marker_frontend.FrontEnd(self.__roll_marker_backend)

app = RollMarkerApplication()
