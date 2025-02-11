

# Fonction pour trouver le journal qui mentionne le plus de médicaments
def journal_with_most_drug_mentions(mentions_graph):
    journal_dict = {}
    for drug, mentions in mentions_graph.items():
        for mention in mentions:
            journal = mention['journal']
            if journal not in journal_dict:
                journal_dict[journal] = set()
            journal_dict[journal].add(drug)
    
    max_drugs_journal = max(journal_dict, key=lambda j: len(journal_dict[j]))

    #On peut utiliser ces lignes pour remplacer lambda
    #max_count = 0
    #for journal, drugs in journal_dict.items():
    #drug_count = len(drugs)
    #if drug_count > max_count:
    #    max_count = drug_count
    #    max_drugs_journal = journal
    
    return max_drugs_journal, len(journal_dict[max_drugs_journal])

# Fonction pour trouver les autres médicaments mentionnés dans les mêmes journaux PubMed 
# mais pas dans Clinical Trials
def drugs_in_same_pubmed_journals(drug, mentions_graph):
    pubmed_journals = set()
    if drug in mentions_graph:
        for mention in mentions_graph[drug]:
            if mention['type'] == 'PubMed':
                pubmed_journals.add(mention['journal'])
    
    other_mentioned_drugs = set()
    for other_drug, mentions in mentions_graph.items():
        if other_drug != drug:
            for mention in mentions:
                if mention['journal'] in pubmed_journals and mention['type'] == 'PubMed':
                    other_mentioned_drugs.add(other_drug)
    
    return other_mentioned_drugs
