from db.mysql_repository import MysqlRepository

LANGUAGE_COUNTRIES = {
    'German': [
        ('Germany', 'ß used in standard orthography'),
        ('Austria', 'ß used in standard orthography'),
        ('Switzerland', "ß not used; expect 'Strasse' instead"),
        ('Liechtenstein', "ß not used; expect 'Strasse' instead"),
    ],
    'English': [
        ('United Kingdom', ''),
        ('United States', ''),
        ('Canada', ''),
        ('Australia', ''),
        ('Ireland', ''),
    ],
}

class Services:
    def __init__(self, repository=None):
        self.repository = repository if repository is not None else MysqlRepository()

    def id_countries(self, text):
        characters = {c for c in text.lower() if c.isalpha()}
        orthographies = self.repository.load_orthographies()

        scored = {}
        for lang, inventory in orthographies.items():
            matched = characters & inventory
            unmatched = characters - inventory
            score = len(matched) / len(characters) if characters else 0
            scored[lang] = {'score': score, 'matched': matched, 'unmatched': unmatched}
        ranked = sorted(scored.items(), key=lambda pair: pair[1]['score'], reverse=True)
        return ranked
    def rank_countries(self, text):
        results = []
        rlist = self.id_countries(text)
        for lang, stats in rlist:
            if lang in LANGUAGE_COUNTRIES:
                for country, note in LANGUAGE_COUNTRIES[lang]:
                    results.append((country, lang, stats['score'], note))
        return results
            