<h1 align="center">🧮 Huawei Cup Math Modeling Toolkit ✨</h1>

<p align="center">📄 LaTeX 排版 · 📊 科学图件 · 🧭 技术路线图 · ✍️ 写作与审阅</p>

从一次华为杯数学建模论文的制作过程沉淀的通用工具：可复用的模板、Codex skills 和成品图件示例。不包含完整赛题论文；本项目与赛事主办方无官方关联。

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

## 🚀 快速开始

需要论文空白模板时：

```sh
cd latex-paper-template
bash build.sh main.tex
```

需要查看排版效果时，在同一目录运行 `bash build.sh`，查看 [`sample.pdf`](latex-paper-template/preview/sample.pdf)。模板自带最终版所用字体与页面素材；编译器需支持 XeLaTeX。

Codex skill 可分别复制或链接到 `~/.codex/skills/`；每个 skill 的 `SKILL.md` 是入口，`references/` 保存规则依据，`assets/` 提供可复用空白材料，`examples/` 展示实例。按任务选用一个或多个 skill，并以当前论文的题目、数据与最终结果为准。

## 📌 许可

原创代码和文档使用 [MIT License](LICENSE)。成品论文示例图件、字体、赛事页面素材和继承类文件不在该授权范围内；详见 [NOTICE.md](NOTICE.md)。
