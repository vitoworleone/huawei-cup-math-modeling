# Huawei Cup Math Modeling Toolkit

从一次华为杯数学建模论文的制作过程沉淀的通用工具：论文 LaTeX 排版、科学图件、总体技术路线图，以及正文写作与审阅方法。这里提供可复用的模板和工作流程，不包含完整赛题论文。

> 非赛事官方项目。示例图件的使用范围见 [许可范围](NOTICE.md)。

## 内容

| 目录 | 内容 | 开始使用 |
|---|---|---|
| [`latex-paper-template/`](latex-paper-template/README.md) | 最终工程的完整 LaTeX 模板、字体、页面素材、排版规范和 PDF 样张 | 在该目录运行 `bash build.sh` |
| [`math-modeling-figure/`](math-modeling-figure/README.md) | 科学图件制作 skill、示例和图形审阅方法 | 阅读 `SKILL.md` |
| [`math-modeling-roadmap/`](math-modeling-roadmap/README.md) | 总体技术路线图 skill、规划表、成品实例 | 阅读 `SKILL.md` |
| [`math-modeling-paper-writing/`](math-modeling-paper-writing/README.md) | 正文写作、证据核验与审阅 skill | 阅读 `SKILL.md` |

## 快速开始

需要论文空白模板时：

```sh
cd latex-paper-template
bash build.sh main.tex
```

需要查看排版效果时，在同一目录运行 `bash build.sh`，查看 [`sample.pdf`](latex-paper-template/preview/sample.pdf)。模板自带最终版所用字体与页面素材；编译器需支持 XeLaTeX。

Codex skill 可分别复制或链接到 `~/.codex/skills/`；每个 skill 的 `SKILL.md` 是入口，`references/` 保存规则依据，`assets/` 提供可复用空白材料，`examples/` 展示实例。按任务选用一个或多个 skill，并以当前论文的题目、数据与最终结果为准。

## 许可

原创代码和文档使用 [MIT License](LICENSE)。成品论文示例图件、字体、赛事页面素材和继承类文件不在该授权范围内；详见 [NOTICE.md](NOTICE.md)。
