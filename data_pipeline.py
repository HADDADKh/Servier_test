
import json

# Fonction pour créer lr graphe dans un fichier JSON
def get_mentions_graph(df_list, titles, drugs_list, sources, output_file):
    mentions_graph = {}
    for df, title, source in zip(df_list, titles, sources):
        for drug in drugs_list:
            matches = df[df[title].str.contains(drug, case=False, na=False)]
            for _, row in matches.iterrows():
                if drug not in mentions_graph:
                    mentions_graph[drug] = []
                mentions_graph[drug].append({
                    'journal': row['journal'],
                    'date': row['date'],
                    'title': row[title],
                    'type': source  # soit PubMed ou Clinical Trials
                })

    with open(output_file, 'w') as json_file:
        json.dump(mentions_graph, json_file, indent=4)

    print(f"Fichier JSON généré : {output_file}")

# Fonction pour charger le graphe depuis un fichier JSON
def load_mentions_graph(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)
