# Camp_ID	
# gi	
# UniProt_id	
# PDBID	
# Title	
# Source_Organism	
# Taxonomy	
# Seqence	
# Length	
# Pubmed_id	Activity	
# Gram_Nature	
# Validation


def fromText(line):
    Camp_ID = line.split('\t')[0]
    gi = line.split('\t')[1]
    UniProt_id = line.split('\t')[2]
    PDBID = line.split('\t')[3]
    Title = line.split('\t')[4]
    Source_Organism = line.split('\t')[5]
    Taxonomy = line.split('\t')[6]
    Seqence = line.split('\t')[7]
    Length = line.split('\t')[8]
    Pubmed_id = line.split('\t')[9]
    Activity = line.split('\t')[10]
    Gram_Nature = line.split('\t')[11]
    Validation = line.split('\t')[12]
    return Camp(Camp_ID, gi, UniProt_id, PDBID, Title, Source_Organism, Taxonomy, 
                Seqence, Length, Pubmed_id, Activity, Gram_Nature, Validation)

class Camp:
    def __init__(
            self, 
                Camp_ID, gi, UniProt_id, PDBID, Title, Source_Organism, Taxonomy, 
                Seqence, Length, Pubmed_id, Activity, Gram_Nature, Validation
            ):
        self.camp_id = Camp_ID
        self.gi = gi
        self.uniprot_id = UniProt_id
        self.pdbid = PDBID
        self.title = Title
        self.source_organism = Source_Organism
        self.taxonomy = Taxonomy
        self.seqence = Seqence
        self.length = Length
        self.pubmed_id = Pubmed_id
        self.activity = Activity
        self.gram_nature = Gram_Nature
        self.validation = Validation
    
    # to json
    def to_json(self):
        return {
            "camp_id": self.camp_id,
            "gi": self.gi,
            "uniprot_id": self.uniprot_id,
            "pdbid": self.pdbid,
            "title": self.title,
            "source_organism": self.source_organism,
            "taxonomy": self.taxonomy,
            "seqence": self.seqence,
            "length": self.length,
            "pubmed_id": self.pubmed_id,
            "activity": self.activity,
            "gram_nature": self.gram_nature,
            "validation": self.validation
        }
    