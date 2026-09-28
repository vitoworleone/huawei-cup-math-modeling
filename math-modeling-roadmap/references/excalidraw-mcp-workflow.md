# Excalidraw MCP 操作与迭代

此流程来自本次总体技术路线图的多版制作记录。第三版的图件、字形与布局先由本地代码生成，随后导入 Excalidraw MCP 检查并导出画布；它不是只靠 `batch_create_elements` 自动生成的图。新任务可以直接用 MCP 搭框架，也可以把本地制作的复杂图件导入 MCP 核验。

## 1. 开始前确认画布和内容

先调用 `read_diagram_guide` 了解当前工具的参数、箭头绑定和配色提示；其通用色板不能覆盖用户已经确认的参考风格。用 `describe_scene` 查看现有画布。已有内容时，先 `snapshot_scene`，需要长期留存时再 `export_scene` 到工作目录；不要直接 `clear_canvas`。只有确认画布为空或专用于本图时，才用 `import_scene(mode="replace")`。

依据当前正文填好 [路线图计划表](../assets/roadmap-plan-template.md)。至少明确各问的任务、方法、结果证据和传给下一问的具体对象。模型名称、数值与箭头语义必须能在正文找到依据。

## 2. 建立画布

分区和方法框优先批量创建，给关键形状指定稳定 ID，箭头以 `startElementId` 和 `endElementId` 绑定。更新单个元素时用 `update_element`；多项同类元素可用 `align_elements`、`distribute_elements`，随后检查是否破坏了错位区块或跨问关系。不要为追求平均分布而抹平已确认的设计。

结果缩略图只能从对应成品图取得。MCP 的 `batch_create_elements` 不负责可靠地把本地图像数据放入 `files`；含真实图件的复杂画布可由 Excalidraw 文件生成器或编辑器建立，然后 `import_scene`。导入后核对每个 `image.fileId` 都存在于 `files`，图像数量和内容哈希与源画布相符。路径化中文可以避免字体替换，但改字需要回到文本源或生成代码。

## 3. 回读和目视检查

用 `describe_scene` 查看总元素数、类型和主要区块，再 `export_scene` 回读文件，对比元素 ID、坐标、尺寸、连接点、图像资产 ID 与数据。MCP 可能加入 `index`、`roundness` 等规范化字段；只把有视觉或语义影响的变化视为失败。箭头的 `x/y/width/height` 可能与局部 `points` 方向不同，检查出界时应计算实际点位，不能只用工具给出的总 bounding box。

若 Excalidraw 浏览器前端已连接，执行 `set_viewport(scrollToContent=true)`，再 `get_canvas_screenshot` 和 `export_to_image`，检查原生渲染。工具返回“没有前端连接”时，记录此限制，用源图 PNG 或本地渲染的导出图做目视检查；此时不能声称已经检查了 MCP 原生截图。不要调用 `export_to_excalidraw_url` 来替代本地预览，因为该工具会上传并产生公开可访问链接。

## 4. 纸面验收与修改循环

按论文真实插入宽度缩放，先看四问、方法、结果标题和跨问箭头是否一眼可辨，再看作为推论依据的图例、轴字与数字。仅供指认的缩略图可以通过明确图注和正文图号引导读者；如果需要从缩略图直接读数，就必须放大、裁切或从数据制作简图。检查白底、灰度、中文字体、图像比例、箭头落点、底部留白和裁切边界。

若有一项不达标，说明它影响哪个阅读动作，修改最小的相关元素或减少图件数量，再导出并按同一纸宽复查。只有结构回读、视觉检查和正文证据三类检查都通过，才交付可编辑画布、预览 PNG，以及必要的论文插入格式。把每轮问题和修改记入验收记录；[第三版回读记录](../examples/verification.md)示范如何区分通过项与未执行项。
