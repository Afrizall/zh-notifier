print("""
########################
# Coded By Afrizal F.A #
# Auto Mirror Zone-H   #
########################
""")

import re, random, requests
from argparse import ArgumentParser
from multiprocessing.pool import ThreadPool

class notify:

   def useragent(self):

        arr = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)", "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3", "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16", "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"]
        return arr[random.randint(0, len(arr)-1)]

   def post(self, url):

      try:

         mirror = requests.post(
            url="http://www.zone-h.org/notify/single?hz=1",
            data={
                  "defacer": self.args.nickname,
                  "domain1": url,
                  "hackmode": 1,
                  "reason": 1
               },
            headers={
                  "User-Agent": self.useragent()
               },
            timeout=self.args.timeout
            )
      
         if re.search("ERROR", mirror.text) :

            print("[-] [Error] [{}]".format(url))
         
         else :

            print("[+] [OK] [{}]".format(url))

      except:

         print("[-] [Error] [{}]".format(url))

   def __init__(self):

      parser = ArgumentParser()
      parser.add_argument("-x", "--nickname", required=True)
      parser.add_argument("-l", "--list", required=True)
      parser.add_argument("-t", "--thread", required=True, type=int)
      parser.add_argument("-d", "--timeout", required=True, type=int)
      self.args = parser.parse_args()
      ThreadPool(self.args.thread).map(self.post, open(self.args.list).read().splitlines())

notify() if __name__ == "__main__" else exit()
