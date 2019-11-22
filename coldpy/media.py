
class Media:

    def __init__(self,
                 taxon_id,
                 url,
                 media_type='',
                 media_format='',
                 title='',
                 created='',
                 creator='',
                 license='',
                 link=''):
        self.taxon_id = taxon_id
        self.url = url
        self.media_type = media_type
        self.media_format = media_format
        self.title = title
        self.created = created
        self.creator = creator
        self.license = license
        self.link = link

    def __str__(self):
        return str(self.taxon_id) + '\t' + \
               str(self.url) + '\t' + \
               str(self.media_type) + '\t' + \
               str(self.media_format) + '\t' + \
               str(self.title) + '\t' + \
               str(self.created) + '\t' + \
               str(self.creator) + '\t' + \
               str(self.license) + '\t' + \
               str(self.link) + '\n'

    def __repr__(self):
        return {
            'taxon_id': self.taxon_id,
            'url': self.url,
            'media_type': self.media_type,
            'media_format': self.media_format,
            'title': self.title,
            'created': self.created,
            'creator': self.creator,
            'license': self.license,
            'link': self.link
        }
