
# !pip install Twython
from twython import TwythonStreamer
import sys
import json
import time

tweets = []


class MyStreamer(TwythonStreamer):

    try:
        def on_success(self, data):
            if ('lang' in data and data['lang'] == 'en'):
                # put the name of the states under observation
                if ((data['user'])['location']) != None and ('AL' in ((data['user'])['location'])or 'Alabama' in ((data['user'])['location']) or
                        'AK' in ((data['user'])['location'])or 'Alaska' in ((data['user'])['location']) or
                        'AZ' in ((data['user'])['location'])or 'Arizona' in ((data['user'])['location']) or
                        'Arkansas' in ((data['user'])['location'])or 'AR' in ((data['user'])['location']) or
                        'California' in ((data['user'])['location']) or 'CA' in ((data['user'])['location']) or
                        'Colorado' in ((data['user'])['location']) or 'CO' in ((data['user'])['location']) or
                        'Connecticut' in ((data['user'])['location']) or 'CT' in ((data['user'])['location']) or
                        'Delaware' in ((data['user'])['location']) or 'DE' in ((data['user'])['location']) or
                        'Florida' in ((data['user'])['location']) or 'FL' in ((data['user'])['location']) or
                        'Georgia' in ((data['user'])['location']) or 'GA' in ((data['user'])['location']) or
                        'Hawaii' in ((data['user'])['location']) or 'HI' in ((data['user'])['location']) or
                        'Idaho' in ((data['user'])['location']) or 'ID' in ((data['user'])['location']) or
                        'Illinois' in ((data['user'])['location']) or 'IL' in ((data['user'])['location']) or
                        'Indiana' in ((data['user'])['location']) or 'IN' in ((data['user'])['location']) or
                        'Iowa' in ((data['user'])['location']) or 'IA' in ((data['user'])['location']) or
                        'Kansas' in ((data['user'])['location']) or 'KS' in ((data['user'])['location']) or
                        'Kentucky' in ((data['user'])['location']) or 'KY' in ((data['user'])['location']) or
                        'Louisiana' in ((data['user'])['location']) or 'LA' in ((data['user'])['location']) or
                        'Maine' in ((data['user'])['location']) or 'ME' in ((data['user'])['location']) or
                        'Maryland' in ((data['user'])['location']) or 'MD' in ((data['user'])['location']) or
                        'Massachusetts' in ((data['user'])['location']) or 'MA' in ((data['user'])['location']) or
                        'Michigan' in ((data['user'])['location']) or 'MI' in ((data['user'])['location']) or
                        'Minnesota' in ((data['user'])['location']) or 'MN' in ((data['user'])['location']) or
                        'Mississippi' in ((data['user'])['location']) or 'MS' in ((data['user'])['location']) or
                        'Missouri' in ((data['user'])['location']) or 'MO' in ((data['user'])['location']) or
                        'Montana' in ((data['user'])['location']) or 'MT' in ((data['user'])['location']) or
                        'Nebraska' in ((data['user'])['location']) or 'NE' in ((data['user'])['location']) or
                        'Nevada' in ((data['user'])['location']) or 'NV' in ((data['user'])['location']) or
                        'New Hampshire' in ((data['user'])['location']) or 'NH' in ((data['user'])['location']) or
                        'New Jersey' in ((data['user'])['location']) or 'NJ' in ((data['user'])['location']) or
                        'New Mexico' in ((data['user'])['location']) or 'NM' in ((data['user'])['location']) or
                        'Newyork' in ((data['user'])['location']) or 'NY' in ((data['user'])['location']) or
                        'North Carolina' in ((data['user'])['location']) or 'NC' in ((data['user'])['location']) or
                        'North Dakota' in ((data['user'])['location']) or 'ND' in ((data['user'])['location']) or
                        'Ohio' in ((data['user'])['location']) or 'OH' in ((data['user'])['location']) or
                        'Oklahoma' in ((data['user'])['location']) or 'OK' in ((data['user'])['location']) or
                        'Oregon' in ((data['user'])['location']) or 'OR' in ((data['user'])['location']) or
                        'Pennsylvania' in ((data['user'])['location']) or 'PA' in ((data['user'])['location']) or
                        'Rhode Island' in ((data['user'])['location']) or 'RI' in ((data['user'])['location']) or
                        'South Carolina' in ((data['user'])['location']) or 'SC' in ((data['user'])['location']) or
                        'South Dakota' in ((data['user'])['location']) or 'SD' in ((data['user'])['location']) or
                        'Tennessee' in ((data['user'])['location']) or 'TN' in ((data['user'])['location']) or
                        'Texas' in ((data['user'])['location']) or 'TX' in ((data['user'])['location']) or
                        'Utah' in ((data['user'])['location']) or 'UT' in ((data['user'])['location']) or
                        'Vermont' in ((data['user'])['location']) or 'VT' in ((data['user'])['location']) or
                        'Virginia' in ((data['user'])['location']) or 'VA' in ((data['user'])['location']) or
                        'Washington' in ((data['user'])['location']) or 'WA' in ((data['user'])['location']) or
                        'West Virginia' in ((data['user'])['location']) or 'WV' in ((data['user'])['location']) or
                        'Wisconsin' in ((data['user'])['location']) or 'WI' in ((data['user'])['location']) or
                        'Wyoming' in ((data['user'])['location']) or 'WY' in ((data['user'])['location'])
                        ):

                    tweets.append(data)  # .encode("utf-8")
                    print('received tweet #', len(tweets), data['text'].encode("utf-8"))
                    print(data)

                    with open('tweets1_opoid_drugs.txt', 'a') as f:
                          f.write(data['text'].strip( )+'==='+data['user']['location'])
                          f.write("\n")
                          f.close()

                # elif ((data['user'])['location']) != None and (
                #                     'CA' in ((data['user'])['location']) or 'california' in (
                #             (data['user'])['location']) or 'California' in (
                #         (data['user'])['location'])):
                #     tweets.append(data)  # .encode("utf-8")
                #     print('received tweet #', len(tweets), data['text'].encode("utf-8"))
                #     print(data)
                #     with open('data\\CA_opoid.txt', 'a') as f:
                #         f.write(json.dumps(data['text'].encode("utf-8")) + '\n')
                #
                # #         # json.dump(data['text'].encode("utf-8"),f,indent=2)
                # #         # f.write(data['text'])
                # #         # f.close()


                else:
                    print('irrelevant')

                    #
                    # if len(tweets) >= 1000:
                    #      self.store_json()
                    #      self.disconnect()
                    # # #if len(tweets)%5 == 0:
                    # # #    time.sleep(10)
    except:
        pass

    # overriding
    try:
        def on_error(self, status_code, data):
            print(status_code, data)
            self.disconnect()
    except:
        pass
        #
        # def store_json(self):
        # #     #change the 'UT_AZ' value to the states under observation
        #     with open('healthyq.json', 'a') as f:
        #        json.dump(tweets['text'], f, indent=4)


if __name__ == '__main__':

    #   with open('sidrah.json', 'r') as f:
    # with open('../../../JG_Ch09_Getting_Data/04_api/gene_twitter_credentials.json', 'r') as f:
    # credentials = json.load(f)

    # create your own app to get consumer key and secret
    CONSUMER_KEY = 'CrVNLDfE5Lif3rEdQ5RVL0SkK'
    CONSUMER_SECRET = 'bXytUe2etgEwXquwMTjvkOGYiS8bKYHzbMnCpekgEtiQhoJIiA'
    ACCESS_TOKEN = '4826465952-FXk4cdtvtmgyanuCBDoJFy4YU2xvXGEwF8Zk0a5'
    ACCESS_TOKEN_SECRET = 'pfWbZd74S6k4wHf6RqZRTe50MIsV7fmz7ZdONFyoSiCI2'

    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # if len(sys.argv) > 1:
    #    keyword = sys.argv[1]
    # else:
    #    keyword = 'trump'

    # To overcome ChunckedEncodingError-IncompleteRead
    counter = 0
    while (len(tweets) < 1000):
        counter += 1
        try:
            if (counter % 3 != 0):
                # Taken from- https://dev.twitter.com/streaming/overview/request-parameters#track
                # Locations taken from http://boundingbox.klokantech.com/
                # change the location values & run again to get another state or combination of states.
                stream.statuses.filter(
                                       track=['Opium overdose','Heroin overdose','OpioidEpidemic','opioidoverdose','#opioidcrisis','StopOpioidOD','opioidepidemic','drug overdose','morphine overdose','methadone overdose','opioid misuse'], language=['en'])
            else:
                # Taken from - http://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
                # to overcome error: 420 Easy there Turbo, too many requests recently
                time.sleep(10)
        except:
            continue
