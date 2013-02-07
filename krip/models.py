from . import db
from ipaddr import IPAddress, IPNetwork, _BaseIP, summarize_address_range
import json

class KRIPAddressEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, KRIPAddress):
            return dict({
                'name': obj.assigned_name,
                'name_en': obj.assigned_name_en,
                'assigned_at': obj.assigned_at.strftime('%Y-%m-%d'),
                'begin': obj.addr_begin.exploded,
                'end': obj.addr_end.exploded
            })
        return json.JSONEncoder.default(self, obj)

class KRIPAddress(db.Model):
    ipaddr_begin = db.Column(db.Integer, primary_key=True)
    ipaddr_end = db.Column(db.Integer, primary_key=True)
    assigned_name = db.Column(db.String, nullable=False)
    assigned_name_en = db.Column(db.String, nullable=False)
    assigned_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, addr_begin, addr_end, name, name_en, assigned_at):
        self.ipaddr_begin = addr_begin
        self.ipaddr_end = addr_end
        self.assigned_name = name
        self.assigned_name_en = name_en
        self.assigned_at = assigned_at

    def __repr__(self):
        return '<KRIPAddress %r(%r) %r>' % (self.addr_range, self.assigned_name_en, self.assigned_at)

    @property
    def addr_begin(self):
        return IPAddress(self.ipaddr_begin)

    @property
    def addr_end(self):
        return IPAddress(self.ipaddr_end)

    @property
    def addr_range(self):
        return summarize_address_range(self.addr_begin, self.addr_end)

    @classmethod
    def find_by_ipaddr(cls, addr):
        if isinstance(addr, basestring)\
           or isinstance(addr, int)\
           or isinstance(addr, _BaseIP):
            addr = IPNetwork(addr)
        else:
            raise TypeError('Invalid argument %s' % addr)

        return cls.query.filter(cls.ipaddr_begin <= int(addr.network),
                                   cls.ipaddr_end >= int(addr.network)).first()
