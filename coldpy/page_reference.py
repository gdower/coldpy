
class PageReference:

    def __init__(self,
                 id,
                 reference_id='',
                 page='',
                 link='',
                 remarks='',
                 needs_review=''):
        self.id = id
        self.reference_id = reference_id
        self.page = page
        self.link = link
        self.remarks = remarks
        self.needs_review = needs_review

    def __str__(self):
        return str(self.id) + '\t' + \
               str(self.reference_id) + '\t' + \
               str(self.page) + '\t' + \
               self.link + '\t' + \
               self.remarks + '\n'

    def __repr__(self):
        return {
            'id': self.id,
            'citation': self.reference_id,
            'author': self.page,
            'title': self.link,
            'year': self.remarks
        }
