
class NameRel:

    def __init__(self,
                 name_id,
                 related_name_id='',
                 name_rel_type='',
                 published_in_id='',
                 remarks='',
                 needs_review=''):
        self.name_id = name_id
        self.related_name_id = related_name_id,
        self.name_rel_type = name_rel_type,
        self.published_in_id = published_in_id
        self.remarks = remarks
        self.needs_review = needs_review

    def __str__(self):
        return str(self.name_id) + '\t' + \
               str(self.related_name_id) + '\t' + \
               str(self.name_rel_type) + '\t' + \
               str(self.published_in_id) + '\t' + \
               str(self.remarks) + '\n'

    def __repr__(self):
        return {
            'name_id': self.name_id,
            'related_name_id': self.related_name_id,
            'type': self.name_rel_type,
            'published_in_id': self.published_in_id,
            'remarks': self.remarks,
        }
