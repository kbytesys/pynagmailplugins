import unittest
from nagmail.common import MailQueueParsingError

from snowpenguin.nagmail.postfix import PostfixMailQueue

mailq_example = \
"""
-Queue ID-     -Size- ----Arrival Time--- -Sender/Recipient-------
3E968141EA6E*   26451 Tue Jan 16 16:33:58  stephen@quasarman.biz
                                         wintor@geology.ucdavis.edu

8B715141EA57*   25933 Tue Jan 16 16:33:53  dbflup@moditory.com
                                         oslagar@geology.ucdavis.edu

97603141EA58!    1829 Tue Jan 16 16:33:54  bggbjlooody@biren.com
                                         koepel@geology.ucdavis.edu

DA860141DE54     4314 Tue Jan 16 16:13:35  info@limburger.de
(host g.mx.mail.yahoo.com[209.191.88.239] said: 451 Message temporarily deferred - [170] (in reply to end of DATA command))
                                         georocker@yahoo.com

B7972141AED1     4291 Tue Jan 16 14:55:35  info@chuckies.co.uk
(host cal.net.mail5.psmtp.com[64.18.5.10] said: 450 : Sender address rejected: Domain not found (in reply to RCPT TO command))
                                         rambo@cal.net

CA3BA141AED2     4292 Tue Jan 16 14:55:35  info@chuckies.co.uk
(host mx4.gatech.edu[130.207.165.59] said: 450 : Sender address rejected: Domain not found (in reply to RCPT TO command))
                                         mschmits@eas.gatech.edu

"""

class PostfixQueueTest(unittest.TestCase):
    def test_parse_string(self):
        pq = PostfixMailQueue()
        try:
            pq.parse_mailq_output(mailq_example)
            self.assertTrue(True)
        except MailQueueParsingError:
            self.assertTrue(False)

    def test_counters(self):
        pq = PostfixMailQueue()
        pq.parse_mailq_output(mailq_example)
        self.assertTrue(
            pq.get_active_counter() == 2 and pq.get_deferred_counter() == 3 and pq.get_total_counter() == 6
        )
