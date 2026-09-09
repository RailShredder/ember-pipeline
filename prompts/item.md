# 道具图标模板

- 底模：SDXL 1.0
- LoRA：ember-style（版本以 lora/VERSIONS.md 最新稳定版为准）
- 参数：1024×1024 · 30 steps · CFG 6 · seed 段固定 100000~100999（同批资产用连续 seed，便于回溯）

## 正向模板

```
{item_en_name}, single {item_type} icon, centered, plain white background,
{style_keywords}, no text, no watermark
```

## 负向

```
lowres, blurry, multiple items, cropped, text, signature, hands
```

## 占位符说明

- `{item_en_name}`：道具英文名（英文 prompt 响应比中文稳定）
- `{item_type}`：weapon / potion / scroll / gem / key ...
- `{style_keywords}`：从 style/ 里的固定风格词组取，不临场发挥
