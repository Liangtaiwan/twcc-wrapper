# TWCC-slurm-wrapper
A wrapper for slurm especially on Taiwania2 (HPC CLI).

For Taiwania2 (HPC CLI) usage, please refer to [here](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Ftwnia2-overview-zh). (中文)

## How to Install?
```sh
git clone git@github.com:Liangtaiwan/twcc-wrapper.git
mv twcc-wrapper $HOME/.wrapper
```

Add the following to your `.bashrc` or `.zshrc`
```
export PATH=$PATH:$HOME/.wrapper
export TWCC_ACCOUNT=<YOUR ACCOUNT ID>
```

## For NTU SPML Lab
基本上使用方法跟戰艦ㄧ樣，`hrun`改為`trun`，但無其他`hxxx`系列功能（戰艦allocate info為我們自己寫的service，國網不支援）

唯有`-s`從spot job改為使用singularity。

跨節點功能暫不支援（我懶的加，有要用跟我說，應該不需要花太久的時間）
