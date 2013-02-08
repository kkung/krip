import urllib2
from bs4 import BeautifulSoup
from ipaddr import IPAddress, summarize_address_range
from krip import db
from krip.models import KRIPAddress
from datetime import datetime

KISA_ADDR = 'http://krnic.kisa.or.kr/jsp/ipas/ipv4Reg/ipv4IspAddrListExcel.jsp'

def update():
    content = urllib2.urlopen(KISA_ADDR)
    soup = BeautifulSoup(content)
    for row in soup.select("tbody > tr"):
        cells = row.find_all('td')
        name = cells[0].string.strip()
        name_en = cells[1].string.strip()
        ipaddr_st = IPAddress(cells[2].string)
        ipaddr_ed = IPAddress(cells[3].string)
        assigned_at = cells[5].string.strip()

        networks = summarize_address_range(ipaddr_st, ipaddr_ed)

        for net in networks:
            krip = KRIPAddress(int(net.network),
                               int(net.broadcast),
                               name,
                               name_en,
                               datetime.strptime(assigned_at, '%Y%m%d'))
        db.session.add(krip)
        # int(r.network) < int(s.network) < int(r.broadcast)
        print '%s - %s(%s) : %s' % (ipaddr_st, ipaddr_ed, net, assigned_at)

    db.session.commit()
if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    update()
