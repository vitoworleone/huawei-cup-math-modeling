# 数学建模论文 LaTeX 完整模板

本目录保留按最终 D 题工程整理的完整版排版：类文件、全部字体、赛事封面与摘要素材、空白入口、排版样张和 PDF 预览都在这里。封面、摘要、目录、正文、公式、图表、参考文献和附录的具体用法见 [排版规范](formatting-guide.md)。

| 路径 | 用途 |
|---|---|
| [`main.tex`](main.tex) | 不含赛题正文和计算结果的空白论文入口 |
| [`sample.tex`](sample.tex)、[`preview/sample.pdf`](preview/sample.pdf) | 公式、插图、三线表及章节层级的可编译样张与预览 |
| [`gmcmthesis.cls`](gmcmthesis.cls)、`preamble.tex`、`table-style.tex` | 最终工程的版式与命令 |
| `front-matter.tex`、`assets/` | 封面与摘要页面素材 |
| `fonts/` | 精确复现样张所需字体 |
| [`build.sh`](build.sh)、`latexmkrc` | XeLaTeX 编译入口 |

## 使用

在本目录运行 `bash build.sh` 编译短样张，输出为 `preview/sample.pdf`；运行 `bash build.sh main.tex` 编译空白入口。复制模板编写新论文时，根据所参加赛事当届规定替换封面和摘要页素材，填写题目及正文，并逐页核对输出。

这里的字体、赛事素材和继承类文件不适用仓库原创部分的 MIT 授权；详见仓库根目录的 [NOTICE.md](../NOTICE.md)。
