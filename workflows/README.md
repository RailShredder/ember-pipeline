# workflows/ — ComfyUI 工作流

存放从 ComfyUI 导出的工作流 JSON。JSON 里写不了注释，所以每个工作流的元信息登记在下方的表格里。

**命名约定**：`<用途>-v<版本>.json`

- `item-batch-v1.json` — 道具图标批量生成
- `character-turnaround-v1.json` — 角色三视图（ControlNet 锁姿态）
- `scene-depth-v1.json` — 场景生成（depth 参考图）
- `inpaint-face-v1.json` — 局部修脸/修手

**约定**：

1. 迭代出新版就升版本号，旧版保留——产物回溯依赖旧版
2. 记不清工作流差异时，看下面这张表，不要靠记忆

## 登记表

| 文件 | 用途 | 底模 | 挂载 LoRA | 状态 |
|---|---|---|---|---|
| （示例行）item-batch-v1.json | 道具图标批量 | SDXL 1.0 | ember-style v1 | 试验中 |
|  |  |  |  |  |
