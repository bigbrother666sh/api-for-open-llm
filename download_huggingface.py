import os
import shutil

from huggingface_hub import snapshot_download

from bypy import ByPy


def copy_data(source_directory,target_directory):
  # 遍历源目录中的所有文件和目录
  for entry in os.listdir(source_directory):
      entry_path = os.path.join(source_directory, entry)
      # 检查是否为符号链接
      if os.path.islink(entry_path):
          # 获取符号链接的目标路径
          target_path = os.readlink(entry_path)
          # 构建目标路径的绝对路径
          target_absolute_path = os.path.join(source_directory, target_path)
          # 获取目标路径的文件名或目录名
          target_basename = os.path.basename(target_absolute_path)
          # 构建目标文件或目录的路径
          target_entry_path = os.path.join(target_directory, entry)

          # 复制目标文件或目录到目标目录
          if os.path.isdir(target_absolute_path):
              shutil.copytree(target_absolute_path, target_entry_path)
          else:
              shutil.copy2(target_absolute_path, target_entry_path)
      else:
          # 如果不是符号链接，直接复制到目标目录
          shutil.copy2(entry_path, os.path.join(target_directory, entry))
          
def download(repo_id):
    source_directory = snapshot_download(repo_id=repo_id,cache_dir="/app/data/",force_download =True)
    print("文件路径:",source_directory)
    path_name = repo_id.replace("/","---")
    target_directory = f"{os.getcwd()}/download/{path_name}"
    # 移动文件
    os.system(f"mkdir -p {target_directory}")
    os.system(f"mkdir -p {os.getcwd()}/tar/{path_name}/")
    copy_data(source_directory,target_directory)
    print("复制路径：",target_directory)

    return target_directory

if __name__ == "__main__":
  ## 设置 repo_id
  repo_id = "moka-ai/m3e-base"

  out_path = download(repo_id)
  