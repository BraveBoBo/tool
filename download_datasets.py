#!/usr/bin/env python3
"""
Download the agibot-world/GenieSimAssets dataset with resume & proxy support.

Usage examples
--------------
# 最简单：先在 shell 里 export HF_TOKEN，再直接跑
python download_geniesim_assets.py

# 指定保存目录、并在脚本里直接给 token
python download_geniesim_assets.py \
    --local_dir /data/GenieSimAssets \
    --token hf_xxxxxxxxxxxxxxxxxxxxx

# 在公司/校园网络里走本地代理
python download_geniesim_assets.py --proxy http://127.0.0.1:7890
"""
import argparse
import os
from huggingface_hub import login, snapshot_download


def main() -> None:
    parser = argparse.ArgumentParser(description="Download GenieSimAssets from Hugging Face")
    parser.add_argument(
        "--repo_id",
        default="agibot-world/GenieSimAssets",
        help="HF repo to download (default: agibot-world/GenieSimAssets)",
    )
    parser.add_argument(
        "--local_dir",
        default="/data/robot_dataset/GenieSimAssets",
        help="Where to store the assets",
    )
    parser.add_argument(
        "--token",
        default="hf_xxxxxxxxxxxxxxxxxxxxx",
        help="Hugging Face access token (or set HF_TOKEN env var)",
    )
    parser.add_argument(
        "--max_workers",
        type=int,
        default=8,
        help="Parallel download threads (default 8)",
    )
    # parser.add_argument(
    #     "--proxy",
    #     help="HTTP/HTTPS proxy, e.g. http://127.0.0.1:7890",
    # )
    args = parser.parse_args()

    # ---------- optional proxy ----------
    # if args.proxy:
    #     os.environ["HTTP_PROXY"] = args.proxy
    #     os.environ["HTTPS_PROXY"] = args.proxy

    # ---------- HF authentication ----------
    if args.token:
        login(token=args.token)  # will cache credential in ~/.cache/huggingface/
    else:
        print("❌ 需要 Hugging Face 访问令牌 (--token 或 HF_TOKEN 环境变量)")
        return

    # ---------- start download ----------
    print(f"📦 Start downloading {args.repo_id} → {args.local_dir}")
    snapshot_download(
        repo_id=args.repo_id,
        repo_type="dataset",  # 确保是下载数据集
        local_dir=args.local_dir,
        resume_download=True,      # 断点续传
        max_workers=args.max_workers,
        token=True,                # 强制带 token
    )
    print("✅ Download finished")


if __name__ == "__main__":
    main()
