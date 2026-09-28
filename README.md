<img src="showcase/banner.png" alt="华为杯数学建模：像素小猫与赛题、建模、绘图、写作、审阅五个步骤" width="100%">

# 华为杯数学建模

> 从一次华为杯数学建模论文的制作过程，整理出可复用的 LaTeX 模板、科学图件示例与 Codex skills。

[论文模板](latex-paper-template/README.md) · [图件制作](math-modeling-figure/README.md) · [技术路线图](math-modeling-roadmap/README.md) · [写作与审阅](math-modeling-paper-writing/README.md)

## 🎨 正文图件一览

[![九张正文图件拼贴：三维地形、通信航迹、地形重建、运输网络及资源调度](showcase/figure-gallery.png)](showcase/figure-gallery.png)

## 👀 模板与路线图

| 📄 论文封面与排版 | 🧭 总体技术路线图 |
|:---:|:---:|
| <a href="latex-paper-template/preview/sample.pdf"><img src="showcase/cover-preview.png" alt="LaTeX 模板封面预览" width="305"></a> | <a href="math-modeling-roadmap/examples/roadmap-final.png"><img src="math-modeling-roadmap/examples/roadmap-final.png" alt="总体技术路线图" width="520"></a> |
| [完整排版 PDF](latex-paper-template/preview/sample.pdf) · [正文写作模板 PDF](showcase/writing-template-example.pdf) | [Excalidraw 画布](math-modeling-roadmap/examples/roadmap-final.excalidraw) · [路线图 skill](math-modeling-roadmap/SKILL.md) |

## 🧰 工具与模板

| 目录 | 内容 | 开始使用 |
|---|---|---|
| [📄 LaTeX 论文模板](latex-paper-template/README.md) | 最终工程的完整排版、字体、页面素材和 PDF 样张 | 在该目录运行 `bash build.sh` |
| [📊 科学图件](math-modeling-figure/README.md) | 图件制作 skill、示例和审阅方法 | 阅读 `SKILL.md` |
| [🧭 技术路线图](math-modeling-roadmap/README.md) | 路线图 skill、规划表和成品实例 | 阅读 `SKILL.md` |
| [✍️ 正文写作](math-modeling-paper-writing/README.md) | 写作、证据核验与审阅 skill | 阅读 `SKILL.md` |

## ✍️ 如何使用写作 skill

1. 将 [`math-modeling-paper-writing`](math-modeling-paper-writing/) 整个目录复制或链接到 `~/.codex/skills/`，保留其中的 `SKILL.md`、`references/` 和 `assets/`。在 Codex 中用 `$math-modeling-paper-writing` 明确指定它。
2. 提供赛题与附件、已确认的模型和求解结果、当前正文，以及相关图表。说明这次要**讨论结构、起草、审阅**还是**按审阅意见修订**。暂缺的材料也可以直接说明。
3. 分轮推进：先确定章节要回答的问题与证据，再写初稿；审阅时核对题意、模型、实现和结果的一致性，最后修订表达与摘要。只需要审阅意见时，明确要求停在审阅层。

起草正文时，可以直接发送：

```text
使用 $math-modeling-paper-writing。依据我提供的赛题、已确认的模型、计算结果和图表，
先梳理第 3 章各节的职责与前后衔接，再写可审阅的正文初稿。
对缺少证据的数值和结论标明待核实，不要补造结果。
```

审阅现有章节时，可以直接发送：

```text
使用 $math-modeling-paper-writing，只审阅我提供的第 3 章，不改写正文。
按影响、位置、依据、改法列出实质问题，重点核对模型假设、代码实现、图表和结论范围。
```

这个 skill 负责正文论证与审阅；图件绘制使用 [科学图件 skill](math-modeling-figure/SKILL.md)，页面字体、公式和表格排版使用 [LaTeX 模板](latex-paper-template/README.md)。完整的阶段规则与工作记录见 [写作 skill 目录](math-modeling-paper-writing/README.md)。

## 🚀 快速开始

需要论文空白模板时：

```sh
cd latex-paper-template
bash build.sh main.tex
```

需要查看排版效果时，在同一目录运行 `bash build.sh`，查看 [`sample.pdf`](latex-paper-template/preview/sample.pdf)。模板自带最终版所用字体与页面素材；编译器需支持 XeLaTeX。

其他 Codex skill 也可分别复制或链接到 `~/.codex/skills/`；每个 skill 的 `SKILL.md` 是入口，`references/` 保存规则依据，`assets/` 提供可复用空白材料，`examples/` 展示实例。按任务选用，并以当前论文的题目、数据与最终结果为准。

## 📌 许可

原创代码和文档使用 [MIT License](LICENSE)。成品论文示例图件、字体、赛事页面素材和继承类文件不在该授权范围内；详见 [NOTICE.md](NOTICE.md)。

本项目不包含完整赛题论文，与赛事主办方无官方关联。
