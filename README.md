# KRIP

Check whether given ip-address is assigned by [KRNIC](http://krnic.or.kr/)

## Usage


    $ curl http://krip.kkung.net/
    {"return_value": {"begin": "1.208.0.0", "name": "\uc8fc\uc2dd\ud68c\uc0ac \uc5d8\uc9c0\uc720\ud50c\ub7ec\uc2a4", "end": "1.223.255.255", "name_en": "BORANET", "assigned_at": "2010-06-14"}, "result": true}
    
    $ curl http://krip.kkung.net/8.8.8.8
    {"return_value": "8.8.8.8 was not assigned by KRNIC", "result": false}
    
    $ curl http://krip.kkung.net/?address=1.111.111.0/24
    {"return_value": {"begin": "1.96.0.0", "name": "\uc8fc\uc2dd\ud68c\uc0ac \ucf00\uc774\ud2f0", "end": "1.111.255.255", "name_en": "KTFWING", "assigned_at": "2010-06-07"}, "result": true}%

    $ curl http://krip.kkung.net/?callback=chk_kr
    chk_kr({"return_value": {"begin": "1.208.0.0", "name": "\uc8fc\uc2dd\ud68c\uc0ac \uc5d8\uc9c0\uc720\ud50c\ub7ec\uc2a4", "end": "1.223.255.255", "name_en": "BORANET", "assigned_at": "2010-06-14"}, "result": true})
    

## License
The MIT License (MIT)
Copyright (c) 2012 Minyoung Jeong (http://kkung.net)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
