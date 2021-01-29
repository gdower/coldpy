
class TypeMaterial:

    def __init__(self,
                 name_id,
                 id='',
                 citation='',
                 status='',
                 reference_id='',
                 page_reference_id='',
                 locality='',
                 country='',
                 latitude='',
                 longitude='',
                 altitude='',
                 host='',
                 date='',
                 collector='',
                 link='',
                 remarks='',
                 needs_review=''):
        self.id = id
        self.name_id = name_id
        self.citation = citation
        self.status = status
        self.reference_id = reference_id
        self.page_reference_id = page_reference_id
        self.locality = locality
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.host = host
        self.date = date
        self.collector = collector
        self.link = link
        self.remarks = remarks
        self.needs_review = needs_review

    def __str__(self):
        return str(self.id) + '\t' + \
               self.name_id + '\t' + \
               self.citation + '\t' + \
               self.status + '\t' + \
               self.reference_id + '\t' + \
               self.page_reference_id + '\t' + \
               self.locality + '\t' + \
               self.country + '\t' + \
               self.latitude + '\t' + \
               self.longitude + '\t' + \
               self.altitude + '\t' + \
               self.host + '\t' + \
               self.date + '\t' + \
               self.collector + '\t' + \
               self.link + '\t' + \
               self.remarks + '\n'

    # def __repr__(self):
    #     return {
    #         'id': self.id,
    #         'name_id': self.name_id,
    #         'citation': self.citation,
    #         'status': self.status,
    #         'reference_id': self.reference_id,
    #         'page_reference_id': self.page_reference_id,
    #         'locality': self.locality,
    #         'country': self.country,
    #         'latitude': self.latitude,
    #         'longitude': self.longitude,
    #         'altitude': self.altitude,
    #         'host': self.host,
    #         'date': self.date,
    #         'collector': self.collector,
    #         'link': self.link,
    #         'remarks': self.remarks
    #     }


class TypeMaterials:

    def __init__(self, output_tsv):
        self.type_materials = []
        self.output_tsv = output_tsv

    def append(self, type_material):
        if isinstance(type_material, TypeMaterial):
            self.type_materials.append(type_material)
        else:
            print('Error: type_material must be TypeMaterial type')

    def write_output(self, output_tsv=''):
        if output_tsv == '' and self.output_tsv != '':
            output_tsv = self.output_tsv
        file = open(output_tsv, 'w')
        if len(self.type_materials) > 0:
            header = '\t'.join(self.type_materials[0].__dict__.keys()) + '\n'
            file.write(header)
        for name in self.type_materials:
            row = '\t'.join(str(v) for v in name.__dict__.values()) + '\n'
            file.write(row)
        file.close()
