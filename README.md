<img src="showcase/banner.png" alt="华为杯数学建模：像素小猫与赛题、建模、绘图、写作、审阅五个步骤" width="100%">

# 华为杯数学建模

> 从一次华为杯数学建模论文的制作过程，整理出可复用的 LaTeX 模板、科学图件示例与 Codex skills。

本项目不包含完整赛题论文，与赛事主办方无官方关联。

📄 [论文模板](#-论文模板从样张到新论文)<br>
📊 [图件制作](#-科学图件从结果到论文插图)<br>
🧭 [技术路线图](#-技术路线图从多问关系到可编辑画布)<br>
✍️ [写作与审阅](#-正文写作从结构讨论到审阅修订)

## 🎨 正文图件一览

[![九张正文图件拼贴：三维地形、通信航迹、地形重建、运输网络及资源调度](showcase/figure-gallery.png)](showcase/figure-gallery.png)

## 👀 模板与路线图

| 📄 论文封面与排版 | 🧭 总体技术路线图 |
|:---:|:---:|
| <a href="latex-paper-template/preview/sample.pdf"><img src="showcase/cover-preview.png" alt="LaTeX 模板封面预览" width="305"></a> | <a href="math-modeling-roadmap/examples/roadmap-final.png"><img src="math-modeling-roadmap/examples/roadmap-final.png" alt="总体技术路线图" width="520"></a> |

📄 [完整排版 PDF](latex-paper-template/preview/sample.pdf)<br>
📝 [正文写作模板 PDF](showcase/writing-template-example.pdf)<br>
🎨 [Excalidraw 画布](math-modeling-roadmap/examples/roadmap-final.excalidraw)<br>
🧭 [路线图 skill](math-modeling-roadmap/SKILL.md)

## 🧰 四部分怎么配合

| 部分 | 什么时候用 | 主要产物 |
|---|---|---|
| [📄 LaTeX 论文模板](latex-paper-template/README.md) | 要写新论文，或检查封面、摘要、公式、图表和目录的排版 | 可编译的 `main.tex` 与 PDF |
| [📊 科学图件](math-modeling-figure/README.md) | 已有数据或模型结果，需要选图、绘图及核验 | PNG、PDF、SVG 和审阅记录 |
| [🧭 技术路线图](math-modeling-roadmap/README.md) | 要解释各问如何衔接，以及方法和结果证据的关系 | 可编辑画布与论文插图 |
| [✍️ 写作与审阅](math-modeling-paper-writing/README.md) | 要规划章节、写正文、核对论证或修订摘要 | 正文草稿、审阅意见与修订稿 |

## 🚀 快速开始

先克隆仓库：

```sh
git clone https://github.com/vitoworleone/huawei-cup-math-modeling-toolkit.git
cd huawei-cup-math-modeling-toolkit
```

只使用 LaTeX 模板时，直接进入 `latex-paper-template/`。需要让 Codex 调用三个 skills 时，将各目录**完整**复制到个人 skills 目录，保留 `SKILL.md` 和目录内的支持文件：

```sh
mkdir -p "$HOME/.codex/skills"
cp -R math-modeling-figure math-modeling-roadmap math-modeling-paper-writing "$HOME/.codex/skills/"
```

还没有确定从哪里开始，可以把仓库交给 Codex，先只做材料盘点：

```text
请阅读这个仓库的 README 和相关 SKILL.md。根据我提供的赛题、已有模型、
计算结果和论文草稿，指出接下来该使用哪部分工具、还缺哪些材料，
并给出工作顺序。这一步先不要编造数据或直接写结论。
```

### 📄 论文模板：从样张到新论文

1. 先打开 [排版样张](latex-paper-template/preview/sample.pdf) 和 [排版规范](latex-paper-template/formatting-guide.md)，确认封面、摘要、目录、公式、插图与三线表的效果。
2. 在 `latex-paper-template/` 运行下列命令。第一条重新生成 `preview/sample.pdf`；第二条编译不含赛题正文的 `main.tex`，输出 `build/main.pdf`。

   ```sh
   cd latex-paper-template
   bash build.sh
   bash build.sh main.tex
   ```

3. 以 [`main.tex`](latex-paper-template/main.tex) 为入口，填写摘要并按需启用路线图、目录、章节、参考文献和附录。公式用 `equation` 与 `\label`，插图用 `\paperfigure`，表格使用三线表；各自的完整示例都在 [排版规范](latex-paper-template/formatting-guide.md)。
4. 换赛或换届时，核对并替换相应的封面与摘要页面素材，最后按真实论文逐页检查字体、图表位置、编号和引用。模板保留完整字体与页面素材，编译需要 XeLaTeX 或兼容的 Tectonic。

### 📊 科学图件：从结果到论文插图

1. 准备**已确认的结果数据**、变量与单位、目标章节和预计插入宽度。先填 [图件计划表](math-modeling-figure/assets/figure-plan-template.md)，明确每张图要证明什么，再参考 [七张成品图](math-modeling-figure/examples/README.md)选择合适的表达方式。
2. 在 Codex 中调用 `$math-modeling-figure`，要求它先核对数据来源和图型，再制作图件。可以这样描述任务：

   ```text
   使用 $math-modeling-figure。依据我提供的结果文件和论文第 4 章，
   先列出每张图的论证作用、数据来源、变量单位和插入宽度，
   再绘图并检查图号、图注、数值和纸面可读性。
   ```

3. 需要可运行的二维起点时，可在字体准备好后使用 [Matplotlib 模板](math-modeling-figure/assets/plot_template.py)：

   ```sh
   cd math-modeling-figure
   python3 assets/plot_template.py assets/demo.csv \
     --y-columns 基准方案 比较方案 --out output/demo
   ```

   命令会生成 `output/demo.png`、`output/demo.pdf`、`output/demo.svg` 和来源记录 `output/demo.json`。所需 Matplotlib 与字体、非默认字体路径参数见 [绘图目录说明](math-modeling-figure/README.md)。`demo.csv` 是虚构数据，写论文时须换成自己的结果；热图、甘特图和三维图需要重写主体绘制逻辑。
4. 按论文实际插入尺寸检查图内文字和图例，再按 [AI 审计与迭代流程](math-modeling-figure/references/ai-audit-and-iteration.md)记录问题、局部修改和复核结果。

### 🧭 技术路线图：从多问关系到可编辑画布

1. 准备各问的最终任务、方法、结果图及当前正文。先填 [路线图计划表](math-modeling-roadmap/assets/roadmap-plan-template.md)，特别写清前一问传给后一问的条件、哪些决策被冻结、哪些需要重新求解。
2. 在 Codex 中调用 `$math-modeling-roadmap`。已配置 Excalidraw MCP 时，先让它检查画布并遵循 [MCP 操作与迭代流程](math-modeling-roadmap/references/excalidraw-mcp-workflow.md)：

   ```text
   使用 $math-modeling-roadmap。依据当前正文和已确认结果，
   先列出各问的输入、方法、结果证据及跨问接口，再制作总体技术路线图。
   请保存可编辑源文件和预览图，并按论文插入宽度审查；
   看不清或与正文不符的部分继续修改。
   ```

3. 用 [第三版成品路线图](math-modeling-roadmap/examples/README.md)参考布局和审阅方法，重新填写自己论文的内容。交付时保存 `.excalidraw` 或其他可编辑源、PNG 预览和必要的纸面检查记录。

### 📝 正文写作：从结构讨论到审阅修订

1. 提供赛题与附件、已确认的模型和求解结果、当前正文，以及相关图表。说明本轮要**讨论结构、起草、审阅**还是**按审阅意见修订**。材料不齐时先标出缺口。
2. 将 [写作 skill](math-modeling-paper-writing/SKILL.md) 作为入口，用 `$math-modeling-paper-writing` 指定任务。起草时先明确章节要回答的问题和证据，再形成可审阅的初稿：

   ```text
   使用 $math-modeling-paper-writing。依据我提供的赛题、已确认的模型、
   计算结果和图表，先梳理第 3 章各节的职责与前后衔接，
   再写可审阅的正文初稿。对缺少证据的数字和结论标明待核实。
   ```

3. 审阅时先核对题意、假设、模型、实现和结果是否一致，再处理段落逻辑与语言。只想得到审查意见时可以明确限定交付：

   ```text
   使用 $math-modeling-paper-writing，只审阅我提供的第 3 章，不改写正文。
   按影响、位置、依据、改法列出实质问题，
   重点核对模型假设、代码实现、图表和结论范围。
   ```

4. 按意见修订后，再从已确认正文提炼摘要、核对参考文献用途和跨章术语。需要保留每轮依据时，复制 [工作记录模板](math-modeling-paper-writing/assets/work-record-template.md)。完整规则见 [写作 skill 目录](math-modeling-paper-writing/README.md)。

这些模块可以按材料成熟度交替使用。数值与结论始终以当前赛题、代码和确认的结果为准；示例图与样张只展示做法。

## ⭐ Star History

<p align="center">
  <a href="https://www.star-history.com/#vitoworleone/huawei-cup-math-modeling-toolkit&Date"><img src="https://api.star-history.com/svg?repos=vitoworleone/huawei-cup-math-modeling-toolkit&amp;type=Date" alt="Star History" width="620"></a>
</p>

## 📜 许可

原创代码和文档采用 [MIT License](LICENSE)；其他素材的使用范围见 [NOTICE.md](NOTICE.md)。
