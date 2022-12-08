TEST_MODE = False  # The mode when the bot uses test database
TRANSFERS_TO_CONFIRM = 50  # Amount of transfers to check the address
NEWLY_CREATED_MAX_TRANSACTIONS_AMOUNT = 5  # Address is newly created if its number of txs is below this value
TRANSFER_THRESHOLD_IN_USD = 10  # Bot doesn't emit alerts if value in usd is below this
FUNDING_CRITICAL = 10000000  # Critical th for funding
FUNDING_HIGH = 1000000  # High th for funding
FUNDING_MEDIUM = 100000  # Medium th for funding
FUNDING_LOW = 10000  # Low th for funding
LAUNDERING_CRITICAL = 10000000  # Critical th for laundering
LAUNDERING_HIGH = 1000000  # High th for laundering
LAUNDERING_MEDIUM = 100000  # Medium th for laundering
LAUNDERING_LOW = 10000  # Low` th for laundering
DEX_DISABLE = False  # Disables DEX-related alerts
INFO_ALERTS = False  # Disables INFO alerts
