# lora/ — LoRA 训练配置

存放 kohya_sd-scripts 的训练配置（`.toml`）与数据集清单。

**LoRA 权重文件本身不进仓库**——保存在 5080 本地（按版本号命名目录）+ 云盘备份。本仓只登记"哪个版本、什么配方、什么结论"。

## 文件约定

- 训练配置：`ember-style-v<N>.toml`（风格 LoRA 版本号只增不改）
- 数据集清单：`ember-style-v<N>.dataset.md`，内容包括：图片数量、来源、打标方式、清洗规则
- 数据集图片本体留在 5080 本地 `datasets/ember-style-v<N>/`

## 流程

训练 → 本地验证（固定 10 个测试 prompt + 固定 seed）→ 结论写入 `VERSIONS.md` → 通过则在 workflows 和 prompts 中更新引用的 LoRA 版本号
