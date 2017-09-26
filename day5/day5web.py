import urllib
import urllib2


def section1():
    url = "http://www.wellsfargo.com"
    words = []
    words.extend(urllib2.urlopen(url).read().split())
    print len(words)
    filtered = []
    for word in words:
        if word.isalpha():
            filtered.append(word)
    print filtered


def section2():
    """
    url = 'http://www.indianblooddonors.com/ibd-ws/ws-android-getbloodalerts.php'
    params = urllib.urlencode({'stdcode': '0861', 'bloodgroup': 'AB -ve', 'caller': '9885970033'})
    response = urllib2.urlopen(url, params).read()
    print response
    """
    url = 'http://www.indianblooddonors.com/ibd-ws/ws-stdcode-search.php'
    params = urllib.urlencode({'stdcode': '080', 'bloodgroup': 'B -ve', 'caller': '9885970033', 'testing': 1})
    response = urllib2.urlopen(url, params).read()
    print response


def section3():
    url = 'http://indianblooddonors.com/ibd-ws/ws-python-feedback.php'
    params = urllib.urlencode({
        'name': 'Kailash Sankar',
        'email': 'kailash.sankar@outlook.com',
        'feedback': 'This is an awesome course!'
    })

    response = urllib2.urlopen(url, params).read()
    print response


# section1()
# section2()
section3()
