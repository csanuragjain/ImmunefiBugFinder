## contracts_merged_index.db:

Contains Immunefi program contract (till 3rd Dec 2024) from "Supported Chains" section in a Sqllite DB with below schema:

```
CREATE TABLE IF NOT EXISTS file_index (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            path TEXT,
            size INTEGER,
            content TEXT,
            last_modified REAL
        )
```

## Fields:
- name: Name of the contract
- path: Contract address on scan explorer 
- size: Size of file
- content: Content of the contract

## Run:
`searchKeyword.py` contains sample python which could be used to find keywords from the database.
You can modify or create new python script to customize logic (or simply replace keywords)

```
python searchKeyword.py
```

## Map contract with Immunefi program:
The resulting contract from keyword search can be mapped to there respective program using HTML within Program List folder

## Supported Chains:

1. Ethereum
2. BSC
3. Arbitrum
4. Optimism
5. Polygon
6. SnowTrace
7. FTM
8. Gnosis
9. Linea
10. Mantle
11. Moon
12. Base
13. Blast
14. Celo
15. Scroll
16. Zkevm

## Note
Database contains 15887 contracts data and misses 1320 contract data due to some weird JSON decode error

## Sample output

```
$ python searchKeyword.py
Entries containing keywords lastTimeRewardApplicable, rewardPerTokenStored:
Name: CellarStaking, Path: https://etherscan.io/address/0x7bAD5DF5E11151Dc5Ee1a648800057C5c934c0d5
Name: ICellarStaking, Path: https://etherscan.io/address/0x7bAD5DF5E11151Dc5Ee1a648800057C5c934c0d5
Name: IAuraBalRewardPool, Path: https://etherscan.io/address/0x7275fd8a1b5f4874b10066236309d8901a848228
Name: ArcadeStakingRewards, Path: https://etherscan.io/address/0x80bDdd56b947c547Ab8964D80E98E42Ff77a5793
Name: IArcadeStakingRewards, Path: https://etherscan.io/address/0x80bDdd56b947c547Ab8964D80E98E42Ff77a5793
Name: LockedBalance, Path: https://etherscan.io/address/0x03AB03DA2c5012855c743bc318c19EF3dE5Bc906
Name: AuraBalRewardPool, Path: https://etherscan.io/address/0xC47162863a12227E5c3B0860715F9cF721651C0c
Name: AuraLocker, Path: https://etherscan.io/address/0x3Fa73f1E5d8A792C80F426fc8F84FBF7Ce9bBCAC
Name: ISmartVault, Path: https://etherscan.io/address/0xBb84098e47d217f51cB014f692eada1F2280a179
Name: VirtualBalanceRewardPool, Path: https://etherscan.io/address/0x00A7BA8Ae7bca0B10A32Ea1f8e2a1Da980c6CAd2
Name: BaseRewardPool, Path: https://etherscan.io/address/0x00A7BA8Ae7bca0B10A32Ea1f8e2a1Da980c6CAd2
Name: ICvxRewardPool, Path: https://etherscan.io/address/0xC68421f20bf6f0Eb475F00b9C5484f7D0AC0331e
Name: StakingRewardsV2, Path: https://etherscan.io/address/0xb7cc88a13586d862b97a677990de14a122b74598
Name: StakingRewards, Path: https://etherscan.io/address/0xb7cc88a13586d862b97a677990de14a122b74598
Name: EUSDMiningIncentives, Path: https://etherscan.io/address/0xdD906b65Da28EEBB615C086BBb9508D04D9fec13
Name: FlokiStakingPool, Path: https://etherscan.io/address/0x1e7866b5a5a4f09efd235d28d49568c2fe2f7ecd
Name: Gauge, Path: https://etherscan.io/address/0x7Fd8Af959B54A677a1D8F92265Bd0714274C56a3
Name: BaseGauge, Path: https://etherscan.io/address/0x7Fd8Af959B54A677a1D8F92265Bd0714274C56a3
Name: StakingDelegateRewards, Path: https://etherscan.io/address/0x9AA729FA58e8298AaEC4C4c33189ED137B3B74f0
Name: MultiFeeDistribution, Path: https://etherscan.io/address/0x28E395a54a64284DBA39652921Cd99924f4e3797
Name: ProtocolRewardsPool, Path: https://etherscan.io/address/0xC2966A73Bbc53f3C99268ED84D245dBE972eD89e
Name: SmartVault, Path: https://etherscan.io/address/0xFE700D523094Cc6C673d78F1446AE0743C89586E
Name: SpoolStaking, Path: https://etherscan.io/address/0xc3160C5cc63B6116DD182faA8393d3AD9313e213
Name: stakerewardV2pool, Path: https://etherscan.io/address/0x19d7cB89E1F92f21d71dB34BeF4944b9f3344d6E
Name: YelayStaking, Path: https://etherscan.io/address/0x8e933387AFc6F0F67588e5Dac33EBa97eF988C69
Name: LockedBalance, Path: https://arbiscan.io/address/0x0D914606f3424804FA1BbBE56CCC3416733acEC6
Name: IAuraBalRewardPool, Path: https://arbiscan.io/address/0x1992af61fbf8ee38741bcc57d636caa22a1a7702
Name: IStakingRewards, Path: https://arbiscan.io/address/0x5ad70224d23c6e39801e3ca1ee00a46c0788fbd1
Name: MultiFeeDistribution, Path: https://arbiscan.io/address/0x76ba3eC5f5adBf1C58c91e86502232317EeA72dE
Name: stakerewardPoolOnArbi, Path: https://arbiscan.io/address/0xed1167b6Dc64E8a366DB86F2E952A482D0981ebd
Name: LockedBalance, Path: https://bscscan.com/address/0x34d4f4459c1b529bebe1c426f1e584151be2c1e5
Name: BaseRewardPoolV2, Path: https://bscscan.com/address/0x00DdD67d200d0c8AF4d37A6F9458333Db2F7aA4e
Name: FlokiStakingPool, Path: https://bscscan.com/address/0x1e7866b5a5a4f09efd235d28d49568c2fe2f7ecd
Name: jar, Path: https://bscscan.com/address/0x0a1Fd12F73432928C190CAF0810b3B767A59717e
Name: BaseRewardPool, Path: https://bscscan.com/address/0xa3B615667CBd33cfc69843Bf11Fbb2A1D926BD46
Name: BaseRewardPoolV3, Path: https://bscscan.com/address/0xa3B615667CBd33cfc69843Bf11Fbb2A1D926BD46
Name: MultiFeeDistribution, Path: https://bscscan.com/address/0x4fd9f7c5ca0829a656561486bada018505dfcb5e
Name: Unipool, Path: https://bscscan.com/address/0x2fa41cbbb40c22e9fb9a110b403841d13cdb0590
Name: IUnipool, Path: https://bscscan.com/address/0x2fa41cbbb40c22e9fb9a110b403841d13cdb0590
Name: vlMGPBaseRewarder, Path: https://bscscan.com/address/0x94Eb0E6800F10E22550e104EC04f98F043B6b3ad
Name: Gauge, Path: https://optimistic.etherscan.io/address/0x8391fE399640E7228A059f8Fa104b8a7B4835071
Name: IGauge, Path: https://optimistic.etherscan.io/address/0x8391fE399640E7228A059f8Fa104b8a7B4835071
Name: IStakingRewards, Path: https://optimistic.etherscan.io/address/0xbb505c54d71e9e599cb8435b4f0ceec05fc71cbd
Name: StakingRewards, Path: https://optimistic.etherscan.io/address/0xbb505c54d71e9e599cb8435b4f0ceec05fc71cbd
Name: VaultFeeReward, Path: https://optimistic.etherscan.io/address/0x0e431Ea7E58e15a18f3334E3A6D195917fe1011a
Name: ISmartVault, Path: https://polygonscan.com/address/0x286c02C93f3CF48BB759A93756779A1C78bCF833
Name: ERC20RewardPool, Path: https://polygonscan.com/address/0xD3A9CAa25393765c05ce9f332B5E33b5E33D8B8F
Name: jar, Path: https://polygonscan.com/address/0xE69a1876bdACfa7A7a4F6D531BE2FDE843D2165C
Name: PolygonLandWeightedSANDRewardPool, Path: https://polygonscan.com/address/0x4ab071c42c28c4858c4bac171f06b13586b20f30
Name: SandRewardPool, Path: https://polygonscan.com/address/0xa6e383bda26e4c52a3a3a3463552c42494669abd
Name: SmartVault, Path: https://polygonscan.com/address/0x225084d30cc297f3b177d9f93f5c3ab8fb6a1454

```

## Disclaimer
This project is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, or non-infringement. In no event shall the authors or contributors be held liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the project or the use or other dealings in the project.

By using this project, you acknowledge that:

1. You are responsible for compliance with any applicable laws and regulations regarding the use of this project.
2. The authors and contributors are not liable for any issues arising from its use in production or other environments.
