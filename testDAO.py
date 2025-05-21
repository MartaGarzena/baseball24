from database.DAO import DAO
from model.model import Model

listObjects = DAO.getTeamsFromYear(2015)

print(listObjects)
