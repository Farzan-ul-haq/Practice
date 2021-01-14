import datetime
# def match_sentence(texta, textb):
#     """
#     this function will findout the
#     difference in both 

#     @args:
#         - texta (str): text stable version
#         - textb (str): text new version
    
#     @return:
#         textc (str): 
#     """
#     a=texta.split()
#     b=textb.split()
#     for i in a:
#         if a in b:
#             print()

def str_time(date_time):
    '''
    this function will take datetimeobject as argument
    and returns the natural time.
    @args:
        - datetime (datetime object)
    @return:
        - naturaltime (str) e.g. "10 minutes ago"
    '''

    timings={'years' : 31536000,
            'months' : 2592000,
            'days'   : 86400,
            'hours'  : 3600,
            'minutes': 60,
            }
    date_now=datetime.datetime.now()
    duration=(date_now-date_time).total_seconds()
    for i,j in timings.items():
        if duration >= j:
            return f'{int(duration//j)} {i} ago'
    return f"{int(duration)} seconds ago"

# print(str_time(datetime.datetime(2019, 1, 11, 16, 20, 30)))
# print(str_time(datetime.datetime(2020, 11, 14, 16, 20, 30)))
# print(str_time(datetime.datetime(2020, 1, 16, 16, 20, 30)))
# print(str_time(datetime.datetime(2021, 1, 14, 16, 50, 30)))
# print(str_time(datetime.datetime(2021, 1, 14, 16, 55, 45)))
def test():
    date_now=datetime.datetime.now()
    year=date_now + datetime.timedelta(days=-365)
    assert str_time(year) == '1 years ago'
    month=date_now + datetime.timedelta(days=-30)
    assert str_time(month) == '1 months ago'
    day=date_now + datetime.timedelta(days=-1)
    assert str_time(day) == '1 days ago'
    day=date_now + datetime.timedelta(days=-10)
    assert str_time(day) == '10 days ago'
    minute=date_now + datetime.timedelta(seconds=-7200)
    assert str_time(minute) == '2 hours ago'
    minute=date_now + datetime.timedelta(seconds=-60)
    assert str_time(minute) == '1 minutes ago'
    minute=date_now + datetime.timedelta(seconds=-300)
    assert str_time(minute) == '5 minutes ago'
    second=date_now + datetime.timedelta(seconds=-50)
    assert str_time(second) == '50 seconds ago'

test()
