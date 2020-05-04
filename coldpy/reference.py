
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
                 remarks=''):
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
