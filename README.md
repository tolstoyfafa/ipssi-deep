## Lancez Tenserflow Serving
`docker run -p 8502:8501 --name=fafa -v YOUR_PATH/ipssi-deep/saved_model/:/models/horse-vs-human/1 -e MODEL_NAME=horse-vs-human tensorflow/serving`


## Comment tester le playboo
- créez un environement virtuel python 3.8
- lancez la commande `pip install -r requirements.txt`
- lancez jupyter notebook
- executez les cellules 1 par 1
- ATTENTION: l'entrainement peut prendre beaucoup de temps veuiellez donc à mettre un epoche = 2 pour tester
- enregistrer le model
- lancez l'application Flask on faisant `python app.py` à la racince du repértoire
- faites vous plaisir en allant sur l'url: `localhost:5000`

