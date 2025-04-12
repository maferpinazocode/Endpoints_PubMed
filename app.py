from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)
CORS(app)
# Endpoint para buscar títulos de papers
@app.route('/papers', methods=['GET'])
def get_paper_titles():
    search_term = request.args.get('term')

    if not search_term:
        return jsonify({'error': 'Falta el parámetro "term"'}), 400

    # Paso 1: Buscar IDs usando esearch.fcgi
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": search_term,
        "retmode": "json",
        "retmax": 5  # Puedes ajustar cuántos resultados quieres
    }

    search_response = requests.get(search_url, params=search_params)
    if search_response.status_code != 200:
        return jsonify({'error': 'Error al buscar IDs'}), 500

    id_list = search_response.json().get("esearchresult", {}).get("idlist", [])
    if not id_list:
        return jsonify({'titles': []})

    ids_str = ",".join(id_list)

    # Paso 2: Obtener detalles usando efetch.fcgi
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ids_str,
        "rettype": "abstract",
        "retmode": "xml"
    }

    fetch_response = requests.get(fetch_url, params=fetch_params)
    if fetch_response.status_code != 200:
        return jsonify({'error': 'Error al obtener detalles'}), 500

    # Paso 3: Parsear XML y extraer títulos
    root = ET.fromstring(fetch_response.text)
    titles = []

    for article in root.findall(".//PubmedArticle"):
        title_elem = article.find(".//ArticleTitle")
        if title_elem is not None:
            titles.append(title_elem.text)

    return jsonify({'titles': titles})

# Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True)