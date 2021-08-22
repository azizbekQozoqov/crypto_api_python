# crypto-api-python
This module is a module that makes it easy to work with the CoinMarketCap API. 
[Visit **CoinMarketCap** site](https://coinmarketcap.com/api/documentation/v1)


## How to use this module ?
___
### 1. **First - go to the [CoinMarketCap.com API](https://coinmarketcap.com/api) and activate your API KEY**

### 2. **Second - clone that git repositorie**

Go to the your project folder >
```bash
git clone https://github.com/azizbekQozoqov/crypto_api_python.git
```

### 3. **Third - import this module to your python project**

```python
from crypto_api_python.API import Cryptos
```

### 4. **Create your own cryptocurrency program.**

```python
CR = Cryptos("<YOUR_API_KEY_HERE>", "<YOUR LIMIT>", "<CONVERT CODE>")
```

The main class in the module is the Cryptos class. The crypto class accepts 3 arguments.
* *API_KEY* - API key activated from [CoinMarketCap.com API](https://coinmarketcap.com/api)

* *LIMIT* - The limit of the currencies you want to get

* *CONVERT* - In what currency to get the value of cryptocurrency


**EXAMPLE**

```python
from crypto_api_python.API import Cryptos
CR = Cryptos("xxxxxxxxxxxxxxxxxxxxxxxxx", 5, "UZS")
print(CR.ALL)
```
**OUTPUT**
```bash
{
   "status":{
      "timestamp":"2021-08-22T06:29:50.716Z",
      "error_code":0,
      "error_message":"None",
      "elapsed":15,
      "credit_count":1,
      "notice":"None",
      "total_count":6115
   },
   "data":[
      {
         "id":1,
         "name":"Bitcoin",
         "symbol":"BTC",
         "slug":"bitcoin",
         "num_market_pairs":8910,
         "date_added":"2013-04-28T00:00:00.000Z",
         "tags":[
            "mineable",
            "pow",
            "sha-256",
            "store-of-value",
            "state-channels",
            "coinbase-ventures-portfolio",
            "three-arrows-capital-portfolio",
            "polychain-capital-portfolio",
            "binance-labs-portfolio",
            "arrington-xrp-capital",
            "blockchain-capital-portfolio",
            "boostvc-portfolio",
            "cms-holdings-portfolio",
            "dcg-portfolio",
            "dragonfly-capital-portfolio",
            "electric-capital-portfolio",
            "fabric-ventures-portfolio",
            "framework-ventures",
            "galaxy-digital-portfolio",
            "huobi-capital",
            "alameda-research-portfolio",
            "a16z-portfolio",
            "1confirmation-portfolio",
            "winklevoss-capital",
            "usv-portfolio",
            "placeholder-ventures-portfolio",
            "pantera-capital-portfolio",
            "multicoin-capital-portfolio",
            "paradigm-xzy-screener"
         ],
         "max_supply":21000000,
         "circulating_supply":18793556,
         "total_supply":18793556,
         "platform":"None",
         "cmc_rank":1,
         "last_updated":"2021-08-22T06:29:02.000Z",
         "quote":{
            "UZS":{
               "price":522442635.9856144,
               "volume_24h":372654879349574.44,
               "percent_change_1h":0.42347489,
               "percent_change_24h":0.57344502,
               "percent_change_7d":5.68472987,
               "percent_change_30d":51.09516228,
               "percent_change_60d":43.94435206,
               "percent_change_90d":38.82809194,
               "market_cap":9818554936183260,
               "market_cap_dominance":44.0127,
               "fully_diluted_market_cap":10971295355697894,
               "last_updated":"2021-08-22T06:29:28.000Z"
            }
         }
      },
      {
         "id":1027,
         "name":"Ethereum",
         "symbol":"ETH",
         "slug":"ethereum",
         "num_market_pairs":5575,
         "date_added":"2015-08-07T00:00:00.000Z",
         "tags":[
            "mineable",
            "pow",
            "smart-contracts",
            "ethereum",
            "binance-smart-chain",
            "coinbase-ventures-portfolio",
            "three-arrows-capital-portfolio",
            "polychain-capital-portfolio",
            "binance-labs-portfolio",
            "arrington-xrp-capital",
            "blockchain-capital-portfolio",
            "boostvc-portfolio",
            "cms-holdings-portfolio",
            "dcg-portfolio",
            "dragonfly-capital-portfolio",
            "electric-capital-portfolio",
            "fabric-ventures-portfolio",
            "framework-ventures",
            "hashkey-capital-portfolio",
            "kinetic-capital",
            "huobi-capital",
            "alameda-research-portfolio",
            "a16z-portfolio",
            "1confirmation-portfolio",
            "winklevoss-capital",
            "usv-portfolio",
            "placeholder-ventures-portfolio",
            "pantera-capital-portfolio",
            "multicoin-capital-portfolio",
            "paradigm-xzy-screener"
         ],
         "max_supply":"None",
         "circulating_supply":117206187.124,
         "total_supply":117206187.124,
         "platform":"None",
         "cmc_rank":2,
         "last_updated":"2021-08-22T06:29:02.000Z",
         "quote":{
            "UZS":{
               "price":34471346.25160137,
               "volume_24h":176842200318386.28,
               "percent_change_1h":0.44165281,
               "percent_change_24h":-1.44295331,
               "percent_change_7d":0.45456831,
               "percent_change_30d":56.66017416,
               "percent_change_60d":60.46953305,
               "percent_change_90d":51.1075844,
               "market_cap":4040255059181386,
               "market_cap_dominance":18.1004,
               "fully_diluted_market_cap":4040255059181406.5,
               "last_updated":"2021-08-22T06:29:28.000Z"
            }
         }
      },
      {
         "id":2010,
         "name":"Cardano",
         "symbol":"ADA",
         "slug":"cardano",
         "num_market_pairs":295,
         "date_added":"2017-10-01T00:00:00.000Z",
         "tags":[
            "mineable",
            "dpos",
            "pos",
            "platform",
            "research",
            "smart-contracts",
            "staking",
            "binance-smart-chain"
         ],
         "max_supply":45000000000,
         "circulating_supply":32143119602.564,
         "total_supply":33027817833.801,
         "platform":"None",
         "cmc_rank":3,
         "last_updated":"2021-08-22T06:28:09.000Z",
         "quote":{
            "UZS":{
               "price":27141.410482971067,
               "volume_24h":50484822135965.484,
               "percent_change_1h":2.08197276,
               "percent_change_24h":2.36624481,
               "percent_change_7d":19.06089067,
               "percent_change_30d":113.94173139,
               "percent_change_60d":98.50125752,
               "percent_change_90d":85.98852412,
               "market_cap":872409603336423.2,
               "market_cap_dominance":3.9084,
               "fully_diluted_market_cap":1221363471733668.8,
               "last_updated":"2021-08-22T06:29:28.000Z"
            }
         }
      },
      {
         "id":1839,
         "name":"Binance Coin",
         "symbol":"BNB",
         "slug":"binance-coin",
         "num_market_pairs":546,
         "date_added":"2017-07-25T00:00:00.000Z",
         "tags":[
            "marketplace",
            "centralized-exchange",
            "payments",
            "binance-smart-chain",
            "alameda-research-portfolio",
            "multicoin-capital-portfolio"
         ],
         "max_supply":168137036,
         "circulating_supply":168137036,
         "total_supply":168137036,
         "platform":"None",
         "cmc_rank":4,
         "last_updated":"2021-08-22T06:29:08.000Z",
         "quote":{
            "UZS":{
               "price":4828349.809091462,
               "volume_24h":20913066561587.93,
               "percent_change_1h":1.09293208,
               "percent_change_24h":-1.10719024,
               "percent_change_7d":12.69697914,
               "percent_change_30d":52.60158759,
               "percent_change_60d":55.08957344,
               "percent_change_90d":65.37818149,
               "market_cap":811824425671804.2,
               "market_cap_dominance":3.637,
               "fully_diluted_market_cap":811824425671822.6,
               "last_updated":"2021-08-22T06:29:28.000Z"
            }
         }
      },
      {
         "id":825,
         "name":"Tether",
         "symbol":"USDT",
         "slug":"tether",
         "num_market_pairs":17176,
         "date_added":"2015-02-25T00:00:00.000Z",
         "tags":[
            "payments",
            "stablecoin",
            "stablecoin-asset-backed",
            "binance-smart-chain",
            "avalanche-ecosystem",
            "solana-ecosystem"
         ],
         "max_supply":"None",
         "circulating_supply":64626834130.548836,
         "total_supply":66468847059.56271,
         "platform":{
            "id":1027,
            "name":"Ethereum",
            "symbol":"ETH",
            "slug":"ethereum",
            "token_address":"0xdac17f958d2ee523a2206206994597c13d831ec7"
         },
         "cmc_rank":5,
         "last_updated":"2021-08-22T06:28:09.000Z",
         "quote":{
            "UZS":{
               "price":10629.489073063185,
               "volume_24h":770680009306678.2,
               "percent_change_1h":0.0883035,
               "percent_change_24h":-0.17944855,
               "percent_change_7d":-0.13253732,
               "percent_change_30d":0.09668492,
               "percent_change_60d":0.03989093,
               "percent_change_90d":-0.06301121,
               "market_cap":686950227217335.8,
               "market_cap_dominance":3.0793,
               "fully_diluted_market_cap":706529883518731.2,
               "last_updated":"2021-08-22T06:29:28.000Z"
            }
         }
      }
   ]
}
```
### 5. **There are several methods in the _crypto_a|pi_python_ module**


* get_all() - Returns all cryptocurrencies.
* get_by_ID(ID) - Returns via the given special ID.
* get_price_by_ID(ID) - The price of the cryptocurrency is refunded based on the ID provided

## Special IDs of cryptocurrencies
```
Bitcoin - 1
Ethereum - 1027
Cardano - 2010
Binance Coin - 1839
Tether - 825
XRP - 52
Dogecoin - 74
Polkadot - 6636
USD Coin - 3408
Solana - 5426
Uniswap - 7083
Bitcoin Cash - 1831
Chainlink - 1975
Binance USD - 4687
Litecoin - 2
Terra - 4172
Polygon - 3890
Internet Computer - 8916
Wrapped Bitcoin - 3717
Ethereum Classic - 1321
Stellar - 512
VeChain - 3077
Avalanche - 5805
THETA - 2416
Filecoin - 2280
TRON - 1958
Dai - 4943
Aave - 7278
EOS - 1765
Monero - 328
PancakeSwap - 7186
Cosmos - 3794
The Graph - 6719
Axie Infinity - 6783
FTX Token - 4195
Klaytn - 4256
Neo - 1376
Algorand - 4030
Maker - 1518
Crypto.com Coin - 3635
Bitcoin BEP2 - 4023
SHIBA INU - 5994
Tezos - 2011
Bitcoin SV - 3602
IOTA - 1720
Elrond - 6892
BitTorrent - 3718
UNUS SED LEO - 3957
Kusama - 5034
Waves - 1274
Compound - 5692
Amp - 6945
Dash - 131
Huobi Token - 2502
THORChain - 4157
Chiliz - 4066
Decred - 1168
Hedera Hashgraph - 4642
TerraUSD - 7129
Quant - 3155
NEAR Protocol - 6535
Helium - 5665
XinFin Network - 2634
Zcash - 1437
Holo - 2682
NEM - 873
Theta Fuel - 3822
SushiSwap - 6758
Stacks - 4847
Decentraland - 1966
Synthetix - 2586
Enjin Coin - 2130
yearn.finance - 5864
Qtum - 1684
Flow - 4558
TrueUSD - 2563
Ravencoin - 2577
Celsius - 2700
OKB - 3897
Fantom - 3513
Bitcoin Gold - 2083
Zilliqa - 2469
Audius - 7455
Basic Attention Token - 1697
Telcoin - 2394
Harmony - 3945
Nexo - 2694
Voyager Token - 1817
DigiByte - 109
Bancor - 1727
KuCoin Token - 2087
Arweave - 5632
Ontology - 2566
Revain - 2135
Paxos Standard - 3330
SwissBorg - 2499
Siacoin - 1042
ICON - 2099
OMG Network - 1808
Celo - 5567
Curve DAO Token - 6538
0x - 1896
Horizen - 1698
Mdex - 8335
Nano - 1567
UMA - 5617
Perpetual Protocol - 6950
IoTeX - 2777
Ankr - 3783
Swipe - 4279
renBTC - 5777
Dent - 1886
Lisk - 1214
Reserve Rights - 3964
1inch - 8104
Mina - 8646
Ocean Protocol - 3911
Ren - 2539
Kava.io - 4846
The Sandbox - 6210
IOST - 2405
Verge - 693
Bitcoin Diamond - 2222
VeThor Token - 3012
WINkLink - 4206
HUSD - 4779
WazirX - 5161
Ergo - 1762
Neutrino USD - 5068
Livepeer - 3640
Loopring - 1934
BakeryToken - 7064
Numeraire - 1732
Golem - 1455
Injective Protocol - 7226
Fetch.ai - 3773
Storj - 1772
Fei Protocol - 8642
MediBloc - 2303
SKALE Network - 5691
Nervos Network - 4948
Alpha Finance Lab - 7232
MyNeighborAlice - 8766
Energy Web Token - 5268
Serum - 6187
Origin Protocol - 5117
Venus - 7288
Wootrade - 7501
Constellation - 2868
iExec RLC - 1637
Unibright - 2758
FUNToken - 1757
GateToken - 4269
Status - 1759
Prometeus - 4120
ASD - 3673
PAX Gold - 4705
Band Protocol - 4679
Cartesi - 5444
Gnosis - 1659
WAX - 2300
Augur - 1104
Stratis - 1343
StormX - 2297
Reef - 6951
NKN - 2780
Kin - 1993
Request - 2071
Bitcoin Standard Hashrate Token - 8891
Orchid - 5026
Conflux Network - 7334
Ardor - 1320
TomoChain - 2570
MaidSafeCoin - 291
Celer Network - 3814
Ontology Gas - 3217
SingularityNET - 2424
Badger DAO - 7859
COTI - 3992
DODO - 7224
Smooth Love Potion - 5824
Civic - 1816
Steem - 1230
Orbs - 3835
MVL - 2982
Ultra - 4189
Aragon - 1680
Phala Network - 6841
Hive - 5370
Balancer - 5728
Utrust - 2320
NuCypher - 4761
Polymath - 2496
Gemini Dollar - 3306
BORA - 3801
Metal - 1788
RSK Infrastructure Framework - 3701
Chromia - 3978
BitShares - 463
Uquid Coin - 2273
HEX - 5015
Wrapped BNB - 7192
stETH (Lido) - 8085
Huobi BTC - 6941
Counos X - 5482
Creditcoin - 5198
Bitcoin Cash ABC - 7686
eCash - 10791
The Transfer Token - 5514
Egoras - 5075
SafeMoon - 8757
INO COIN - 3085
yOUcash - 7321
DeFiChain - 5804
Symbol - 8677
NXM - 5830
Pirate Chain - 3951
Venus BNB - 7961
WhiteCoin - 268
Liquity USD - 9566
Orbit Chain - 5326
Yield Guild Games - 10688
Coin98 - 10903
Zelwin - 5614
Pundi X[new] - 9040
ECOMI - 6432
Bifrost (BFC) - 7817
Raydium - 8526
Bitpanda Ecosystem Token - 4361
TitanSwap - 7206
BitDAO - 11221
HedgeTrade - 3662
Kyber Network Crystal v2 - 9444
Anchor Protocol - 8857
Mirror Protocol - 7857
Persistence - 7281
Illuvium - 8719
Electroneum - 2137
Frax - 6952
sUSD - 2927
Dawn Protocol - 5618
Orion Protocol - 5631
Bytecoin - 372
Alien Worlds - 9119
Akash Network - 7431
Alchemy Pay - 6958
Ethernity Chain - 8615
KOK - 5185
Linear - 7102
Toko Token - 9020
QuickSwap - 8206
Ellipsis - 8938
Keep Network - 5566
Soda Coin - 5126
Trust Wallet Token - 5964
Alpaca Finance - 8707
Venus BTC - 7962
Clover Finance - 8384
Render Token - 5690
Sapphire - 4121
Doctors Coin - 5796
ApeSwap Finance - 8497
Sologenic - 5279
PlayDapp - 7461
KLAYswap Protocol - 8296
LUKSO - 5625
Rocket Pool - 2943
dKargo - 5908
CRYPTO20 - 2444
AllianceBlock - 6957
Bonfida - 7978
Sun (New) - 10529
Strike - 8911
Wanchain - 2606
Folgory Coin - 4842
Enzyme - 1552
Ark - 1586
ZKSwap - 8202
Radicle - 6843
Dero - 2665
Tribe - 9025
aelf - 2299
Venus XVS - 7960
DFI.Money - 5957
Travala.com - 2776
Terra Virtua Kolect - 8037
SafePal - 8119
Hathor - 5552
Harvest Finance - 6859
Syscoin - 541
JUST - 5488
Metadium - 3418
KardiaChain - 5453
MCO - 1776
DigitalBits - 4566
Casper - 5899
Oasis Network - 7653
Klever - 6724
Lido DAO Token - 8000
MATH - 5616
MOBOX - 9175
Komodo - 1521
ZB Token - 3351
Rakon - 5072
Everipedia - 2930
Populous - 1789
Syntropy - 4191
Gala - 7080
Powerledger - 2132
Convex Finance - 9903
ABBC Coin - 3437
Ampleforth Governance Token - 9421
TrustSwap - 5829
Shyft Network - 8917
Litentry - 6833
TokenPocket - 5947
Rally - 8075
Alitas - 10897
Venus ETH - 7963
Aavegotchi - 7046
Polkastarter - 7208
Bytom - 1866
Sport and Leisure - 3977
Wrapped NXM - 5939
EFFORCE - 7882
IRISnet - 3874
QuarkChain - 2840
Verasity - 3816
Streamr - 2143
Hifi Finance - 2896
CertiK - 4807
XeniosCoin - 5060
OriginTrail - 2467
Darma Cash - 5622
SuperRare - 11294
Ampleforth - 4056
MXC - 3628
KeeperDAO - 7678
Secret - 5604
Gitcoin - 10052
unFederalReserve - 7553
USDX [Kava] - 6651
Hxro - 3748
RAMP - 7463
Cream Finance - 6193
Tellor - 4944
Divi - 3441
BarnBridge - 7440
Rarible - 5877
XYO - 2765
bZx Protocol - 5810
Handshake - 5221
district0x - 1856
Molecular Future - 2441
Velas - 4747
Kadena - 5647
Automata Network - 10188
Mask Network - 8536
Elitium - 3968
ReddCoin - 118
Rari Governance Token - 7486
MonaCoin - 213
Centrifuge - 6748
Newscrypto - 4890
Akropolis - 4134
Sentinel - 2643
Oxygen - 8029
Flamingo - 7150
STASIS EURO - 2989
PARSIQ - 5410
SuperFarm - 8290
Alchemix - 8613
Dego Finance - 7087
DerivaDAO - 7228
Radix - 7692
Gas - 1785
Tokenlon Network Token - 8083
PEAKDEFI - 5354
Paris Saint-Germain Fan Token - 5226
Venus USDC - 7958
RedFOX Labs - 7654
Aion - 2062
Chimpion - 3742
Kleros - 3581
ShareToken - 4197
Loom Network - 2588
NewYork Exchange - 4268
Carry - 3946
Crust Network - 6747
TrueFi - 7725
Belt Finance - 8730
DAD - 4862
RSK Smart Bitcoin - 3626
PAC Protocol - 1107
Nerve Finance - 8755
Centrality - 2585
LTO Network - 3714
Hegic - 6929
ankrETH - 8100
MiL.k - 5266
LGCY Network - 6665
Maro - 3175
PAID Network - 8329
Firo - 1414
Energi - 3218
HARD Protocol - 7576
Beefy.Finance - 7311
DIA - 6138
inSure DeFi - 5113
ARPA Chain - 4039
Bloomzed Loyalty Club Ticket - 5280
ZEON - 3795
Vai - 7824
TROY - 5007
BEPRO Network - 5062
Thunder Token - 3930
Sentinel Protocol - 2866
saffron.finance - 7617
MX Token - 4041
FIO Protocol - 5865
WHALE - 6679
Decentral Games - 7798
GNY - 3936
Bluzelle - 2505
DAO Maker - 8420
cVault.finance - 7242
Burger Swap - 7158
Efinity - 8985
Function X - 3884
Pangolin - 8422
Covalent - 7411
Contentos - 4036
NFTX - 8191
Standard Tokenization Protocol - 4006
Bounce Token - 8602
WELL - 7883
CUMROCKET - 9212
DEXTools - 5866
RChain - 2021
Dvision Network - 7590
Bella Protocol - 6928
Sora - 5802
MANTRA DAO - 6536
Morpheus.Network - 2763
FC Barcelona Fan Token - 5225
Alpha Quark Token - 7460
Vulcan Forged PYR - 9308
AdEx Network - 1768
Karura - 10042
Dock - 2675
Qcash - 2319
Waltonchain - 1925
Massnet - 5548
Groestlcoin - 258
Auto - 8387
Beam - 3702
Hydra - 8245
Super Zero Protocol - 4078
Basid Coin - 7157
Elastos - 2492
Frontier - 5893
Steem Dollars - 1312
Wilder World - 9674
Haven Protocol - 2662
Refereum - 2553
Frax Share - 6953
Unifi Protocol DAO - 7672
Humanscape - 3600
Marlin - 7497
StableXSwap - 7502
API3 - 7737
Edgeware - 5274
Zenon - 4003
OpenOcean - 9938
Manchester City Fan Token - 10049
GlitzKoin - 3914
NULS - 2092
Rai Reflex Index - 8525
PIVX - 1169
REVV - 6993
Anyswap - 5892
AMO Coin - 3260
Neutrino Token - 7320
Dusk Network - 4092
Mithril - 2608
AXEL - 6216
Telos - 4660
MimbleWimbleCoin - 5031
Eden - 7750
Kylin - 8644
VerusCoin - 5049
CUDOS - 8258
Boson Protocol - 8827
ForTube - 4118
ChainX - 4200
CargoX - 2490
YIELD App - 8066
Liquity - 7429
Aergo - 3637
CoinEx Token - 2941
```

# EXAMPLES

### Code
```python
from crypto_api_python.API import Cryptos

CR = Cryptos("xxxxxxxxxxxxxxxxxx", 5, "USD")

result = CR.get_by_ID(1)
print(result)
```

### Output
```bash

{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'num_market_pairs': 8910, 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channels', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'arrington-xrp-capital', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures', 'galaxy-digital-portfolio', 'huobi-capital', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-xzy-screener'], 'max_supply': 21000000, 'circulating_supply': 18793556, 'total_supply': 18793556, 'platform': None, 'cmc_rank': 1, 'last_updated': '2021-08-22T07:11:02.000Z', 'quote': {'USD': {'price': 49242.439355065835, 'volume_24h': 34484594453.51295, 'percent_change_1h': 0.20415936, 'percent_change_24h': 1.11625557, 'percent_change_7d': 6.36875859, 'percent_change_30d': 51.68847837, 'percent_change_60d': 44.8658615, 'percent_change_90d': 34.51513836, 'market_cap': 925440541596.0337, 'market_cap_dominance': 43.9516, 'fully_diluted_market_cap': 1034091226456.38, 'last_updated': '2021-08-22T07:11:02.000Z'}}}
```


### Code
```python
from crypto_api_python.API import Cryptos

CR = Cryptos("xxxxxxxxxxxxxxxxxx", 5, "USD")

result = CR.get_price_by_ID(1)
print(result)
```

### Output
```bash
49217.80537227381
```

### Code
```python
from crypto_api_python.API import Cryptos

CR = Cryptos("xxxxxxxxxxxxxxxxxx", 5, "USD")

result = CR.get_price_by_ID(1, formated=True)
print(result)
```

### Output
```bash
49,204.55 USD
```
**_CRYPTO_API_PYTHON_ version beta 1.0.0**

Developed by **[Azizbek Developer](https://azizbekportfolio.vercel.app "Visit portfolio site")**

&copy; 2020 - 2021 **AzizbekDeveloper**