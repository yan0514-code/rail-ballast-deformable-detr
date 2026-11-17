# 道床异物检测 · Deformable DETR

本仓库 Fork 自 [fundamentalvision/Deformable-DETR](https://github.com/fundamentalvision/Deformable-DETR)，在其上完成了铁路道床异物检测的训练与结果分析。框架代码版权归原作者，沿用原仓库 Apache-2.0 许可；本仓库新增内容为训练入口脚本与实验报告。

## 新增内容

| 文件 | 说明 |
|---|---|
| `train_deformable_detr.py` | 道床数据集训练入口，含数据加载、训练循环与验证 |
| `train_with_live_loss.bat` | 带实时 loss 曲线的训练启动脚本（Windows） |
| `report/README.md` | 实验报告说明 |
| `report/figures/` | 报告图件：类别分布、混淆矩阵、检测结果、loss 曲线等 |
| `report/tables/` | 报告表格：类别统计、混淆矩阵、预测结果 CSV |
| `report_figures/` | 报告图件编号版（01–11） |

## 复现

```bash
pip install -r requirements.txt
python train_deformable_detr.py
```

需准备 COCO 格式数据并放置于 `data/` 目录。

## 结果

训练 loss、学习率、混淆矩阵与检测可视化见 `report/figures/`，逐类统计与预测明细见 `report/tables/`。

## 数据集与权重

- 数据集为自建道床异物数据，因来源原因不在本仓库公开。
- 训练 checkpoint（单个约 458 MB）未上传至仓库，训练输出目录 `output/` 已在 `.gitignore` 中排除。

## 致谢与许可

基于 Fundamental Vision 的 Deformable DETR 实现，原仓库许可为 Apache-2.0，详见仓库内 `LICENSE`。