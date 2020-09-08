
class TypeMaterial:

    def __init__(self,
                 id,
                 name_id,
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
               str(self.reference_id) + '\t' + \
               str(self.page_reference_id) + '\t' + \
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

    def __repr__(self):
        return {
            'taxon_id': self.id,
            'name_id': self.name_id,
            'citation': self.citation,
            'status': self.status,
            'reference_id': self.reference_id,
            'page_reference_id': self.page_reference_id,
            'locality': self.locality,
            'country': self.country,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'altitude': self.altitude,
            'host': self.host,
            'date': self.date,
            'collector': self.collector,
            'link': self.link,
            'remarks': self.remarks
        }
