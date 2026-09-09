# scripts/ — 后处理与编排脚本

- `postprocess/`：AI 原图 → 成品的加工脚本（去背景 / 量化调色板 / 居中导出）
- （规划）`orchestrate/`：Mac 远程调用 Windows ComfyUI API 的编排 CLI——一条命令完成"生成 → 回传 → 后处理 → 写 meta"

## 运行环境

Python 3.10+，`pip install pillow rembg`

## 新脚本的三条要求

1. 可独立运行（CLI 传参，不写死路径）
2. 幂等（重跑不产生不同结果）
3. 所用参数能被写进主仓资产的 meta.json——产物必须可追溯到脚本与参数
