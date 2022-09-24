from dotenv import load_dotenv
load_dotenv()  

import os


import mintapi

mint = mintapi.Mint(
    os.environ.get('MINT_USERNAME'),
    os.environ.get('MINT_PASSWORD'),
    # headless=True,
		# use_chromedriver_on_path=True,
    # wait_for_sync=False,  # do not wait for accounts to sync
		# wait_for_sync_timeout=100,  # number of seconds to wait for sync
		# mfa_method='sms', # Can be 'sms' (default), 'email', or 'soft-token'.
		# 									# if mintapi detects an MFA request, it will trigger the requested method
		# 									# and prompt on the command line.
)

# Optional parameters
# 
# mfa_input_callback=None,  # A callback accepting a single argument (the prompt)
#                           # which returns the user-inputted 2FA code. By default
#                           # the default Python `input` function is used.
# session_path=None, # Directory that the Chrome persistent session will be written/read from.
#                    # To avoid the 2FA code being asked for multiple times, you can either set
#                    # this parameter or log in by hand in Chrome under the same user this runs
#                    # as.
# imap_account=None, # account name used to log in to your IMAP server
# imap_password=None, # account password used to log in to your IMAP server
# imap_server=None,  # IMAP server host name
# imap_folder='INBOX',  # IMAP folder that receives MFA email

tx_data = mint.get_transaction_data(
	limit=5000,
	include_investment=True,
	start_date='01-01-22',
	end_date=None,
	remove_pending=False)

