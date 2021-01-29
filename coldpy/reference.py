
class Reference:

    def __init__(self,
                 id,
                 citation='',
                 author='',
                 title='',
                 year='',
                 source='',
                 details='',
                 doi='',
                 link='',
                 remarks='',
                 needs_review=''):
        self.id = id
        self.citation = citation
        self.author = author
        self.title = title
        self.year = year
        self.source = source
        self.details = details
        self.doi = doi
        self.link = link
        self.remarks = remarks
        self.needs_review = needs_review

    def __str__(self):
        return str(self.id) + '\t' + \
               self.citation + '\t' + \
               self.author + '\t' + \
               self.title + '\t' + \
               str(self.year) + '\t' + \
               self.source + '\t' + \
               self.details + '\t' + \
               self.doi + '\t' + \
               self.link + '\t' + \
               self.remarks + '\n'

    def __repr__(self):
        return {
            'id': self.id,
            'citation': self.citation,
            'author': self.author,
            'title': self.title,
            'year': self.year,
            'source': self.source,
            'details': self.details,
            'doi': self.doi,
            'link': self.link,
            'remarks': self.remarks
        }


class References:

    def __init__(self, output_tsv):
        self.references = []
        self.output_tsv = output_tsv

    def append(self, reference):
        if isinstance(reference, Reference):
            self.references.append(reference)
        else:
            print('Error: reference must be Reference type')

    def write_output(self, output_tsv=''):
        if output_tsv == '' and self.output_tsv != '':
            output_tsv = self.output_tsv
        file = open(output_tsv, 'w')
        if len(self.references) > 0:
            header = '\t'.join(self.references[0].__dict__.keys()) + '\n'
            file.write(header)
        for name in self.references:
            row = '\t'.join(str(v) for v in name.__dict__.values()) + '\n'
            file.write(row)
        file.close()
