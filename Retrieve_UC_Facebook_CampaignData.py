# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

"""
Example from Facebook Meta for Develpers:   https://developers.facebook.com/apps/597369678448697/marketing-api/quickstart/
Modified by L Clarage for Tufts University, 9/21/22.
"""

"""
WHAT I RUN IN JUPYTER LABS ON MY WINDOWS MACHINE: 
       %run Retrieve_UC_Facebook_CampaignData.py
"""  
#-----------------------------------------------------------------------------


from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.api import FacebookAdsApi

access_token = 'EAAIfTfd7yDkBAPVZAVejo7SzqlrMaoOR99QrO7PlyWnXZCmYdsfbu1aq2RNoDqwogRH6ZBph5SKaeVcqBveMAZAovec6x1ur4nYciHMjNMgRswZAXkz7Y2IELohldj27CU0gq1CgV7IU7flMjsAZBePVHC11UTVg4HLCovUY3VwzhPBwNvq1S7wlsy3N2sGbsZD'
ad_account_id = 'act_1755149518150648'
app_secret = '41705096fcc4faeacdb32b8c22b9b2af'
app_id = '597369678448697'
FacebookAdsApi.init(access_token=access_token)


fields = [
    'account_name',
    'account_id',
    'campaign_name',
    'campaign_id',
    'date_start',
    'date_stop',
    'impressions',
    'clicks',
    'spend',
]
params = {
    'time_range': {'since':'2022-09-09','until':'2022-09-16'},
    'filtering': [],
    'level': 'campaign',
    'time_increment': '1',
}
print (AdAccount(ad_account_id).get_insights(
    fields=fields,
    params=params,
)
      )

