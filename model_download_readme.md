
## 3、下载

```bash
conda activate aliendao
# 下载模型，带上mirror优先从镜像下载
python model_download.py --repo_id 模型ID --mirror
# 举例
python model_download.py --repo_id baichuan-inc/Baichuan-7B --mirror
# 下载数据集
python model_download.py --repo_id 数据集ID --repo_type dataset --mirror
# 举例
python model_download.py --repo_id tatsu-lab/alpaca --repo_type dataset --mirror

```
