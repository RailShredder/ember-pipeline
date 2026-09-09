# ember-pipeline

余烬（ember）的美术生产管线仓库——**配方仓**：存放"怎么生产资产"的全部配方，不存放生产出来的产物。

## 与 ember 主仓的分工

```
ember-pipeline（本仓·配方仓）                    ember（游戏主仓）
工作流 / 训练配置 / 脚本 / 模板 / 调色板  ──生产──▶  成品资产 + meta.json + 游戏代码
```

一条产线：本仓的配方出图 → 后处理脚本加工 → 通过验收的成品连同 meta 进主仓，被 Godot 工程引用。

## 装 / 不装

| 装（本仓，小文本为主） | 不装（留 5080 本地 + 云盘备份） |
|---|---|
| ComfyUI 工作流 JSON（`workflows/`） | LoRA 权重文件（几百 MB） |
| 训练配置与数据集清单（`lora/`） | 训练数据集图片 |
| 后处理与编排脚本（`scripts/`） | 批量生成的原始图 |
| 提示词模板（`prompts/`） | Godot 工程与游戏代码（在主仓） |
| 调色板与风格定义（`style/`） | |

## 目录结构

```
workflows/   ComfyUI 工作流 JSON（按 用途-v版本 命名）
lora/        LoRA 训练配置 + 数据集清单 + VERSIONS.md 版本记录
scripts/     后处理脚本与远程编排 CLI
prompts/     提示词模板（一类型资产一个模板）
style/       调色板与风格定义（Style Guide 的机器可读版）
```

## 核心制度：版本记录

每次训练 LoRA 或迭代工作流，必须在 `lora/VERSIONS.md`（工作流则在 `workflows/README.md` 的登记表）追加一条记录。这是整条美术体系**可复现、可回滚**的依据——三个月后要复现某批资产，靠这份记录，不靠记忆。

## 分支与提交

- main 分支保护，改动走 PR
- 提交信息遵循 Conventional Commits（详见主仓 `COMMIT_CONVENTION.md`），scope 统一用 `pipeline`
- 本仓保持私有；通用工具脚本（后处理、编排 CLI）日后可拆分公开，LICENSE 已备
