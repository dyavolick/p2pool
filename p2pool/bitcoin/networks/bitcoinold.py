import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d9'.decode('hex')
P2P_PORT = 35333
ADDRESS_VERSION = 0
RPC_PORT = 8311
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '000000009721ce4bb0480e087862bad683c7273ee78dfab4dba1496a152780b9')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'BOL'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoinold') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoinold/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcoinold'), 'bitcoinold.conf')
BLOCK_EXPLORER_URL_PREFIX = '#'
ADDRESS_EXPLORER_URL_PREFIX = '#'
TX_EXPLORER_URL_PREFIX = '#'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8