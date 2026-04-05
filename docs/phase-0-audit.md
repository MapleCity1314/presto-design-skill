# Phase 0 审计报告

> 审计日期：2026-04-04
> 审计范围：41 个 skill，位于 `.claude/skills/` 目录

---

## 来源分组说明

根据 skill 的功能定位和风格特征，将 41 个 skill 划分为以下来源组：

| 来源组 | Skill 列表 |
|--------|-----------|
| **pbakaus/impeccable**（核心设计流程 skill） | adapt, animate, arrange, audit, bolder, clarify, colorize, critique, delight, distill, extract, frontend-design, harden, normalize, onboard, optimize, overdrive, polish, quieter, teach-impeccable, typeset |
| **leonxlnx/taste-skill**（风格主张 skill） | baseline-ui, design-taste-frontend, full-output-enforcement, high-end-visual-design, industrial-brutalist-ui, minimalist-ui, redesign-existing-projects, stitch-design-taste |
| **greensock/gsap-skills**（GSAP 官方 skill） | gsap-core, gsap-frameworks, gsap-performance, gsap-plugins, gsap-react, gsap-scrolltrigger, gsap-timeline, gsap-utils |
| **ibelick/ui-skills**（UI 约束检查 skill） | fixing-accessibility, fixing-metadata, fixing-motion-performance |
| **better-auth/better-icons** | better-icons |

---

## 一、pbakaus/impeccable 核心设计流程 skill

### adapt

**Token 体量**
- 字符数：7328 | 估算 token：~1832 | 体量级别：**M**

**核心功能**
adapt 负责将现有设计适配到不同屏幕尺寸、设备类型、平台或使用场景。强制先运行 `/frontend-design` 和 `/teach-impeccable` 收集上下文，然后系统地分析源场景与目标场景的差异，输出断点策略、触控适配和内容优先级调整方案。触发词：响应式设计、移动端、断点、跨设备。

**审美编码位置**
- **触控目标尺寸**（Interaction Strategy 节）：`touch targets 44x44px minimum`，无例外
- **最小字体**（Content Strategy 节）：`16px minimum` 用于移动端正文
- **响应断点**（Responsive Breakpoints 节）：`320px-767px / 768px-1023px / 1024px+`，推荐内容驱动断点而非强制使用这些值
- **邮件布局**（Email Adaptation 节）：`600px max width`，仅单列

**与其他 skill 的重叠**
- `audit`：审计维度包含 Responsive Design（触控目标、断点）
- `harden`：硬化阶段也处理多语言文本扩展与响应式布局
- `polish`：最终检查阶段涵盖所有断点的对齐与间距
- `optimize`：性能优化中含懒加载、响应式图片策略

---

### animate

**Token 体量**
- 字符数：7849 | 估算 token：~1962 | 体量级别：**M**

**核心功能**
animate 分析一个功能点并系统地添加有目的的动画与微交互，提升可用性和愉悦感。覆盖入场动画、微交互、状态切换、导航流、反馈引导、取悦时刻六大类别。触发词：动画、过渡、微交互、hover 效果、让界面更有活力。

**审美编码位置**
- **时长规则**（Timing & Easing 节）：
  - `100-150ms` 即时反馈（按钮按下）
  - `200-300ms` 状态变化（hover、菜单打开）
  - `300-500ms` 布局变化（手风琴、模态框）
  - `500-800ms` 入场动画
- **缓动曲线**（具体 CSS 变量）：
  ```
  --ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1)
  --ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1)
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1)
  ```
- **禁止曲线**：`bounce: cubic-bezier(0.34, 1.56, 0.64, 1)`、`elastic: cubic-bezier(0.68, -0.6, 0.32, 1.6)` 明确被标注为"感觉过时俗气"
- **按钮 hover 缩放**：`scale(1.02-1.05)`；click：`0.95 → 1`
- **退出动画**：使用进入时长的约 75%
- **入场错开**：`100-150ms` 延迟

**与其他 skill 的重叠**
- `delight`：delight 也包含微交互和动画，但侧重惊喜感而非系统化
- `overdrive`：overdrive 是动画的超级模式，含 WebGL/Shader
- `fixing-motion-performance`：专注动画性能检查，animate 仅轻提
- `gsap-core`/`gsap-timeline`：GSAP skill 提供具体实现，animate 提供策略方向
- `bolder`：bolder 的 Motion & Animation 小节有入场编舞与过渡

---

### arrange

**Token 体量**
- 字符数：7528 | 估算 token：~1882 | 体量级别：**M**

**核心功能**
arrange 改善布局、间距和视觉节奏，修复单调的网格、不一致的间距和弱视觉层级。系统地评估当前布局的 5 个维度（间距、视觉层级、网格结构、节奏多样性、密度），输出改进方案。触发词：布局感觉不对、间距问题、拥挤的 UI。

**审美编码位置**
- **间距节奏**（Create Visual Rhythm 节）：
  - 相关元素间距：`8-12px`
  - 不同区块之间：`48-96px`
- **响应式网格**（Choose the Right Layout Tool 节）：`repeat(auto-fit, minmax(280px, 1fr))`
- **Flex vs Grid 原则**：明确规定"Flex 用于 1D，Grid 用于 2D"，禁止默认选 Grid
- **禁止模式**：禁止使用所有空间相同的 padding；禁止全都居中；禁止嵌套卡片
- **"英雄指标布局"明确禁止**：`big number + small label + stats + gradient` 模式

**与其他 skill 的重叠**
- `distill`：distill 的 Layout Simplification 节与 arrange 高度重叠（同样强调减少嵌套卡片、使用简单布局）
- `polish`：polish 最终检查的 Visual Alignment & Spacing 节与 arrange 内容高度一致
- `normalize`：normalize 的间距 token 对齐与 arrange 的系统化间距原则相同
- `redesign-existing-projects`：Layout 审计节与 arrange 完全对应

---

### audit

**Token 体量**
- 字符数：7766 | 估算 token：~1942 | 体量级别：**M**

**核心功能**
audit 运行技术质量检查，覆盖可访问性、性能、主题化、响应式设计和 AI 反模式五个维度，生成带 P0-P3 优先级和 0-4 分评分的报告。是纯诊断 skill，不做修复，输出推荐的后续 command。触发词：质量检查、无障碍审查、性能审计。

**审美编码位置**
- **对比度标准**（Accessibility 节）：`<4.5:1` 视为低对比度，AAA 目标 `7:1`
- **触控目标**（Responsive Design 节）：`< 44x44px` 即为问题
- **AI Slop 检测**（Anti-Patterns 节）：明确列出 AI 色盘、渐变文字、glassmorphism、英雄指标、相同卡片网格、通用字体为"AI 生成指纹"
- **评分等级**：18-20 优秀；14-17 良好；10-13 可接受；6-9 差；0-5 关键

**与其他 skill 的重叠**
- `critique`：critique 是设计批评维度，audit 是技术维度，两者输出格式相似（评分 + 优先级问题列表）
- `fixing-accessibility`：fixing-accessibility 专注实施修复，audit 仅诊断记录
- `optimize`：optimize 是 audit 性能维度的实施版
- `harden`：harden 覆盖 audit 的部分边缘案例和健壮性问题

---

### bolder

**Token 体量**
- 字符数：6860 | 估算 token：~1715 | 体量级别：**M**

**核心功能**
bolder 将"太安全"或"无聊"的设计放大为更有视觉冲击力和个性的设计。系统地在排版、色彩、空间、视觉效果、动效、构图六个维度提升影响力，同时明确警告不要陷入 AI 俗套（cyan/purple 渐变、glassmorphism、neon 暗底）。触发词：设计看起来平淡、通用、缺乏个性。

**审美编码位置**
- **字体缩放**（Typography Amplification）：推荐 `3x-5x` 的尺寸差而非 `1.5x`
- **字重对比**：`900 weights + 200 weights`，而非 `600 + 400`
- **空间戏剧性**（Spatial Drama）：`100-200px` 间距（而非 `20-40px`）
- **阴影规范**（Visual Effects）：明确禁止"generic drop shadows on rounded rectangles"
- **禁止渐变**：明确禁止 cyan/purple gradient AI slop 审美
- **过渡缓动**：仍坚持 `ease-out-quart/quint/expo`，明确禁止 bounce/elastic

**与其他 skill 的重叠**
- `quieter`：完全反向操作，quieter 减弱强度，bolder 增强
- `colorize`：colorize 的色彩增强与 bolder 的 Color Intensification 高度重叠
- `overdrive`：overdrive 是更极端的 bolder，加入 WebGL/shader 等技术
- `typeset`：typeset 是 bolder 排版维度的专项实施

---

### clarify

**Token 体量**
- 字符数：6944 | 估算 token：~1736 | 体量级别：**M**

**核心功能**
clarify 识别并改善界面中不清晰、令人困惑或写得不好的文字，使产品更易理解和使用。涵盖错误信息、表单标签、按钮文案、帮助文字、空状态、成功/加载/确认对话框、导航标签等所有 UX 写作场景。触发词：文字令人困惑、标签不清、错误信息差。

**审美编码位置**
- **Bad/Good 示例对比**（多处）：提供了大量具体的重写示例，如 `"Error 403: Forbidden"` → 人性化说明 + 操作建议
- **6条清晰原则**（Apply Clarity Principles）：具体、简洁、主动语态、人性化、有帮助性、一致性
- **禁止模式**：禁止模糊（"Something went wrong"）、禁止被动语态、禁止对用户使用幽默（应共情）

**与其他 skill 的重叠**
- `delight`：delight 的 Personality in Copy 节涉及文案风格，clarify 侧重清晰度
- `onboard`：onboarding 的空状态文案和引导文案与 clarify 重叠
- `harden`：harden 的错误处理要求清晰的错误信息，与 clarify 重叠

---

### colorize

**Token 体量**
- 字符数：7033 | 估算 token：~1758 | 体量级别：**M**

**核心功能**
colorize 战略性地为过于单调或灰暗的设计引入色彩，使界面更有吸引力和表现力。系统地在语义色彩、强调色应用、背景和表面、数据可视化、边框和装饰、排版色彩六个维度引入色彩。触发词：设计太灰、太暗淡、缺乏温度感。

**审美编码位置**
- **OKLCH 色彩推荐**（Background & Surfaces 节）：推荐 `oklch(97% 0.01 60)` 代替 `#f5f5f5`，强调感知均匀性
- **语义色彩**（Semantic Color 节）：
  - Success: emerald/forest/mint 系
  - Error: rose/crimson/coral 系
  - Warning: orange/amber
  - Info: sky/ocean/indigo
- **色彩比例规则**（60/30/10）：主色 60%、辅色 30%、强调色 10%
- **禁止模式**：禁止将纯灰色文字放在彩色背景上（用背景色深色或透明度替代）；禁止纯黑 `#000` 或纯白 `#fff` 大面积使用；禁止 purple-blue 渐变

**与其他 skill 的重叠**
- `bolder`：Color Intensification 节与 colorize 高度重叠
- `quieter`：quieter 的 Color Refinement 节是 colorize 的逆操作
- `distill`：distill 要求减少到 1-2 种颜色，与 colorize 方向相反
- `redesign-existing-projects`：Color and Surfaces 审计节与 colorize 规则对应

---

### critique

**Token 体量**
- 字符数：11374 | 估算 token：~2844 | 体量级别：**L**

**核心功能**
critique 从 UX 视角对设计进行整体评价，涵盖视觉层级、信息架构、情感共鸣、认知负荷等维度，采用 Nielsen 十大启发式原则 0-4 分评分，并通过角色测试（Persona Red Flags）提供具体问题。是四阶段流程（critique → 用户确认 → 推荐命令列表），不直接修复。触发词：评审、critique、review 设计。

**审美编码位置**
- **AI Slop 检测**（Phase 1 第 1 节）：作为"最重要的检查"，对应 frontend-design 的全部 DON'T 列表
- **认知负荷阈值**（Information Architecture 节）：每个决策点可见选项 `> 4` 即需标记
- **情感旅程**（Emotional Journey）：Peak-end rule、Emotional valleys 等概念
- **Nielsen 评分**（Phase 2）：0-4 分，大多数真实界面得分 `20-32`（满分 40）

**与其他 skill 的重叠**
- `audit`：audit 是技术维度，critique 是 UX/设计维度，两者互补，输出格式相似
- `frontend-design`：critique 多次引用 frontend-design 的参考文档
- `harden`：两者都关注边缘状态（空状态、错误状态、成功状态）

---

### delight

**Token 体量**
- 字符数：10327 | 估算 token：~2582 | 体量级别：**L**

**核心功能**
delight 识别机会并添加令人愉悦的瞬间——微交互、个性化文案、插画、有趣的加载状态、庆祝动效、彩蛋——将功能性界面转变为令人难忘的体验。明确区分"精致微交互"、"俏皮个性"、"感官丰富度"三种策略方向。触发词：增加打磨感、个性、让界面有趣。

**审美编码位置**
- **按钮 hover 动效规格**（具体 CSS）：
  ```css
  transition: transform 0.2s cubic-bezier(0.25, 1, 0.5, 1); /* ease-out-quart */
  ```
- **时长约束**：delight 时刻必须 `< 1秒`，否则阻碍核心功能
- **加载文案反模式**（WARNING 节）：明确列举"Herding pixels"、"Teaching robots to dance"等为 AI 俗套文案，要求写产品具体行为的文案
- **缓动一致性**：`ease-out-quart` 而非 bounce/elastic

**与其他 skill 的重叠**
- `animate`：animate 是系统化动画策略，delight 是具体惊喜时刻
- `clarify`：delight 的 Personality in Copy 与 clarify 的错误/空状态文案重叠
- `onboard`：delight 的空状态 + 庆祝时刻与 onboard 的首次体验重叠
- `bolder`：Motion & Animation 的编舞概念相似

---

### distill

**Token 体量**
- 字符数：6370 | 估算 token：~1593 | 体量级别：**M**

**核心功能**
distill 去除不必要的复杂性，将设计剥离至本质。在信息架构、视觉简化、布局简化、交互简化、内容简化、代码简化六个维度系统地删减冗余。核心哲学：简化不是删功能，而是移除用户和目标之间的障碍。触发词：简化、去噪、减少元素、让 UI 更简洁。

**审美编码位置**
- **色彩约束**（Visual Simplification）：最多 `1-2种颜色 + 中性色`，不超过 5-7 种
- **字体约束**：一个字族、最多 `3-4` 个尺寸、`2-3` 个字重
- **禁止装饰**：消除不服务于层级或功能的边框、阴影、背景
- **禁止嵌套卡片**：`never nest cards inside cards`

**与其他 skill 的重叠**
- `quieter`：quieter 减弱视觉强度，distill 删除复杂性，方向相近
- `arrange`：都涉及布局简化和间距系统化
- `harden`：distill 的代码简化（减少组件变体）与 harden 的边缘案例处理相辅相成

---

### extract

**Token 体量**
- 字符数：4041 | 估算 token：~1010 | 体量级别：**M**（接近 S 边界）

**核心功能**
extract 从现有代码中识别可复用的组件、设计 token 和 UI 模式，将其提取并整合到设计系统中。遵循发现 → 计划 → 提取&丰富 → 迁移 → 文档化五步流程。触发词：创建组件、重构重复 UI 模式、构建设计系统。

**审美编码位置**
- **提取阈值**（Assess value 节）：仅提取使用 3+ 次或可能复用的模式，不过度提取
- **token 命名原则**：primitive vs semantic（语义命名），token 必须有语义意义

**与其他 skill 的重叠**
- `normalize`：normalize 是将现有实现对齐到设计系统，extract 是从实现中提炼出系统
- `redesign-existing-projects`：Code Quality 节与 extract 的清理方向一致

---

### frontend-design

**Token 体量**
- 字符数：9702 | 估算 token：~2426 | 体量级别：**L**

**核心功能**
frontend-design 是所有设计 skill 的"宿主" skill，提供设计原则、Anti-patterns 清单和 Context Gathering Protocol。几乎所有 impeccable 系列的 skill 都强制先调用它。包含 AI Slop Test、六大设计维度（排版、色彩、布局、视觉细节、动效、交互）的 DO/DON'T 规则，以及响应式和 UX 写作方向。

**审美编码位置**
- **字体禁令**（Typography）：明确禁止 `Inter, Roboto, Arial, Open Sans, system defaults`
- **色彩禁令**（Color & Theme）：
  - 禁止 `pure black (#000)` 或 `pure white (#fff)`
  - 禁止 AI 色盘：`cyan-on-dark`, `purple-to-blue gradients`, `neon accents on dark backgrounds`
  - 禁止渐变文字（尤其是 metrics 上）
  - 禁止默认暗黑模式 + 发光强调色
- **布局禁令**（Layout & Space）：
  - 禁止所有内容包裹在卡片中
  - 禁止嵌套卡片
  - 禁止"相同卡片网格"（icon + heading + text 无限重复）
  - 禁止"英雄指标布局模板"
  - 禁止所有内容居中
- **动效禁令**（Motion）：禁止 bounce/elastic 缓动；禁止动画布局属性
- **Context Gathering Protocol**：三步检查（当前指令 → `.impeccable.md` → 运行 `/teach-impeccable`）

**与其他 skill 的重叠**
- 被所有 impeccable skill 依赖（adapt, animate, arrange, audit, bolder, clarify, colorize, critique, delight, distill, harden, normalize, onboard, optimize, overdrive, polish, quieter, typeset）

---

### harden

**Token 体量**
- 字符数：9412 | 估算 token：~2353 | 体量级别：**L**

**核心功能**
harden 通过更好的错误处理、i18n 支持、文本溢出处理和边缘案例管理来提升界面健壮性，使其生产就绪。覆盖文本溢出与换行、国际化（i18n）、错误处理、边缘条件管理、输入校验/清理、无障碍弹性、性能弹性七个维度。触发词：生产就绪、边缘案例、错误状态、溢出问题。

**审美编码位置**
- **最小文字尺寸**（Responsive text sizing）：`14px on mobile` 最小可读尺寸
- **i18n 空间预算**：德语文字通常比英语长 `30%`，需预留 `30-40%` 空间
- **RTL 支持**：使用逻辑属性（`margin-inline-start` 而非 `margin-left`）
- **`prefers-reduced-motion`**：明确提供代码片段

**与其他 skill 的重叠**
- `audit`：audit 的 Responsive Design 和 Accessibility 维度与 harden 重叠
- `fixing-accessibility`：都处理可访问性，harden 更宽泛，fixing-accessibility 更聚焦
- `optimize`：两者都有"慢连接"的考虑（但视角不同，optimize 是性能，harden 是用户体验弹性）

---

### normalize

**Token 体量**
- 字符数：4264 | 估算 token：~1066 | 体量级别：**M**（接近 S 边界）

**核心功能**
normalize 审查并重新对齐 UI 以匹配设计系统标准——间距 token、颜色 token、组件模式、响应式行为。强调先发现（深度理解现有设计系统）再执行，覆盖排版、色彩、间距、组件、动效、响应式、无障碍七个维度。触发词：一致性、设计漂移、样式不匹配。

**审美编码位置**
- 规则本身不编码审美值，而是对齐到项目现有设计系统的值
- 强调"如果不清楚就询问，不要猜测设计系统原则"

**与其他 skill 的重叠**
- `extract`：extract 提炼系统，normalize 对齐到系统，两者互补
- `polish`：polish 最终检查与 normalize 对齐任务高度重叠
- `redesign-existing-projects`：两者都在修复现有项目，但 redesign 更激进，normalize 更保守

---

### onboard

**Token 体量**
- 字符数：8576 | 估算 token：~2144 | 体量级别：**L**

**核心功能**
onboard 设计和改善引导流、空状态和首次运行体验，帮助用户快速到达价值点。涵盖初始产品引导、功能发现与采纳、引导式导览、互动教程、文档与帮助五种场景。强调"尽快到达 aha moment"。触发词：引导、首次用户、空状态、激活。

**审美编码位置**
- 每个空状态必须包含 4 个要素：what/why/how/visual interest
- **禁止**：强制用户经历长引导才能使用产品；反复显示已关闭的 tooltip；在引导过程中阻断所有 UI

**与其他 skill 的重叠**
- `clarify`：onboard 的引导文案与 clarify 的 UX 写作重叠
- `delight`：onboard 的空状态 + 完成庆祝与 delight 高度重叠
- `harden`：两者都处理空状态，角度不同（onboard 是引导机会，harden 是健壮性）

---

### optimize

**Token 体量**
- 字符数：8053 | 估算 token：~2013 | 体量级别：**L**

**核心功能**
optimize 诊断并修复 UI 性能问题，覆盖加载速度、渲染、动画、图片和打包体积。明确区分加载性能、渲染性能、动画性能、React/框架优化、网络优化五个子域，并引用 Core Web Vitals 目标值。触发词：慢、卡顿、jank、打包体积、加载时间。

**审美编码位置**
- **Core Web Vitals 指标**：LCP `< 2.5s`、FID `< 100ms`/INP `< 200ms`、CLS `< 0.1`
- **GPU 加速**：使用 `transform` 和 `opacity`，禁止动画布局属性（`width`, `height`, `top`, `left`）
- **图片质量**：`80-85%` 压缩质量通常无感知差异

**与其他 skill 的重叠**
- `audit`：audit 的 Performance 维度是 optimize 的诊断版
- `fixing-motion-performance`：fixing-motion-performance 专注动画性能，optimize 更宽泛
- `harden`：都包含慢连接的考量

---

### overdrive

**Token 体量**
- 字符数：9877 | 估算 token：~2469 | 体量级别：**L**

**核心功能**
overdrive 将界面推向常规限制之外，使用技术雄心勃勃的实现——着色器、弹簧物理、滚动驱动揭示、60fps 动画。工具箱包括 View Transitions API、Scroll-driven animations、WebGL/WebGPU、Canvas/OffscreenCanvas、SVG filter chains、Virtual scrolling、Web Workers、WASM 等。触发词：震撼、令人印象深刻、不惜一切、非凡感受。

**审美编码位置**
- **60fps 底线**：`< 50fps` 就简化
- **`prefers-reduced-motion`** 是"无条件要求，不是建议"
- **渐进增强是"不可谈判的"**：提供 `@supports` 降级
- **必须先提案再实现**：提出 2-3 个方向，用户确认后再写代码（防止 overdrive 误用）

**与其他 skill 的重叠**
- `animate`：animate 是策略性动画，overdrive 是技术极限动画
- `bolder`：bolder 的 Motion 节与 overdrive 有交集，但 overdrive 更技术化
- `optimize`：overdrive 在"性能规则"节与 optimize 高度重叠
- `gsap-scrolltrigger`/`gsap-core`：GSAP skill 是 overdrive 工具箱的具体实现

---

### polish

**Token 体量**
- 字符数：8308 | 估算 token：~2077 | 体量级别：**L**

**核心功能**
polish 是在发布前进行最终质量检查，修复对齐、间距、一致性和微细节问题。系统地遍历视觉对齐、字体、色彩对比、交互状态（8 种）、微交互、内容一致性、图标图片、表单、边缘状态、响应式、性能、代码质量十二个维度，输出完整检查清单。触发词：打磨、收尾、预上线。

**审美编码位置**
- **每个交互元素的 8 种状态**：Default / Hover / Focus / Active / Disabled / Loading / Error / Success
- **字体行长**：`45-75 字符` 为正文理想行长
- **缓动规范**：`ease-out-quart/quint/expo`，明确禁止 bounce/elastic
- **动画帧率**：60fps，仅动画 transform 和 opacity
- **中性色**（Color & Contrast 节）：`不允许纯灰色`——必须添加微量色相（0.01 chroma），"gray on color" 明确禁止

**与其他 skill 的重叠**
- `audit`：audit 是诊断，polish 是执行最终检查
- `arrange`：polish 的 Visual Alignment 节与 arrange 大量重叠
- `normalize`：两者都是对齐标准，polish 更细粒度

---

### quieter

**Token 体量**
- 字符数：5245 | 估算 token：~1311 | 体量级别：**M**

**核心功能**
quieter 降低视觉上过于激进或刺激的设计强度，在保持质量的同时减少视觉噪音。系统地在色彩、视觉重量、简化、动效、构图五个维度降低强度。核心理念："quieter 不是无聊，而是精致、克制"。触发词：太粗犷、太响、太复杂、视觉超载。

**审美编码位置**
- **饱和度目标**（Color Refinement）：从全饱和降到 `70-85%` 饱和度
- **字重减少**：`900 → 600`，`700 → 500`
- **动画距离减少**：`10-20px` 而非 `40px`
- **色彩比例**：中性色做更多工作，强调色 `10%` 规则
- **gray on color 禁止**：与 frontend-design 和 polish 完全一致
- **缓动**：`ease-out-quart` 用于静谧动效

**与其他 skill 的重叠**
- `bolder`：完全相反操作
- `distill`：quieter 减弱视觉强度，distill 删除元素，方向接近
- `colorize`：quieter 的 Color Refinement 与 colorize 的反向操作

---

### teach-impeccable

**Token 体量**
- 字符数：2941 | 估算 token：~735 | 体量级别：**S**

**核心功能**
teach-impeccable 是一次性项目上下文收集 skill，扫描代码库后向用户提问（用户、品牌个性、审美方向、无障碍要求），然后将"Design Context"写入 `.impeccable.md` 并可选地同步到 `.github/copilot-instructions.md`。是所有设计 skill 的前置条件。

**审美编码位置**
- 本身不编码审美规则，而是提问框架：`目标用户 / 品牌个性 3 词 / 参考站点 / 反参考 / 视觉方向 / 浅色/深色模式 / 无障碍要求`

**与其他 skill 的重叠**
- 被所有 impeccable skill 作为前置条件引用

---

### typeset

**Token 体量**
- 字符数：5891 | 估算 token：~1473 | 体量级别：**M**

**核心功能**
typeset 通过修复字体选择、层级、尺寸、字重和可读性来改善排版，让文字感觉是有意识的选择。区分"App UI"（固定 rem 比例）和"营销/内容页面"（流体 clamp()）两种策略。触发词：字体问题、排版不对劲、可读性、文字层级。

**审美编码位置**
- **字体禁令**：`Inter, Roboto, Arial, Open Sans, system defaults` 明确禁止
- **正文最小尺寸**：`16px / 1rem`（禁止使用 px 单位，要用 rem）
- **行长**：`45-75 字符`（用 `max-width: 65ch`）
- **行高范围**：headings `1.1-1.2`，body `1.5-1.7`（深色底可略微增大）
- **App UI vs Marketing 区分**：App UI 使用固定 rem 比例（空间可预测性），marketing 使用 `clamp(min, preferred, max)` 流体尺寸
- **数据排版**：`tabular-nums` 用于数据表格和需要对齐的数字
- **字重限制**：最多 3-4 个字重（Regular/Medium/Semibold/Bold）

**与其他 skill 的重叠**
- `bolder`：bolder 的 Typography Amplification 节与 typeset 高度重叠
- `distill`：distill 要求限制字族数量和尺寸数量
- `polish`：polish 最终检查的 Typography Refinement 节与 typeset 内容高度一致
- `redesign-existing-projects`：Typography 审计节与 typeset 对应

---

## 二、leonxlnx/taste-skill 风格主张 skill

### baseline-ui

**Token 体量**
- 字符数：3616 | 估算 token：~904 | 体量级别：**S**

**核心功能**
baseline-ui 是一套针对 Tailwind CSS 项目的约束检查规则，防止 AI 生成的界面"slop"。覆盖技术栈（必须用 Tailwind + motion/react）、组件（必须用无障碍原语）、动画、排版、布局、性能、设计七个类别，每条规则是可检查的 MUST/NEVER/SHOULD 格式。触发词：UI 组件、CSS 工具类、React 视图。

**审美编码位置**
- **动画上限**：`NEVER exceed 200ms for interaction feedback`
- **动画属性**：仅 `transform` 和 `opacity`，禁止 `width/height/top/left/margin/padding`
- **设计禁令（具体）**：
  - `NEVER use gradients unless explicitly requested`
  - `NEVER use purple or multicolor gradients`
  - `NEVER use glow effects as primary affordances`
  - `SHOULD limit accent color usage to one per view`
- **布局**：`NEVER use h-screen`，始终用 `h-dvh`
- **排版**：`MUST use text-balance for headings`、`MUST use tabular-nums for data`

**与其他 skill 的重叠**
- `design-taste-frontend`：两者都是全局设计约束，但 baseline-ui 是规则列表，design-taste-frontend 是"高机构性"参数驱动
- `frontend-design`：DON'T 列表高度重叠（尤其是渐变、紫色、glow effect）
- `fixing-motion-performance`：动画规则几乎完全相同

---

### design-taste-frontend

**Token 体量**
- 字符数：21366 | 估算 token：~5342 | 体量级别：**XL**

**核心功能**
design-taste-frontend 是一个高机构性的 Senior UI/UX 工程师 skill，通过 3 个全局参数（DESIGN_VARIANCE 8、MOTION_INTENSITY 6、VISUAL_DENSITY 4）驱动所有设计决策，涵盖架构约定、偏差矫正指令（6 条规则）、创意主动性（反 Slop 实现）、性能护栏、技术参考、AI Tells 禁止列表、创意武器库、Bento Motion 范式 9 个章节。

**审美编码位置**
- **排版规则（Rule 1）**：
  - Display/Headlines: `text-4xl md:text-6xl tracking-tighter leading-none`
  - Body: `text-base text-gray-600 leading-relaxed max-w-[65ch]`
  - 禁止 `Inter`；强制 `Geist`/`Outfit`/`Cabinet Grotesk`/`Satoshi`
  - Serif 绝对禁用于 Dashboard/Software UI
- **色彩约束（Rule 2）**：
  - Max 1 Accent Color，Saturation `< 80%`
  - "THE LILA BAN"：AI Purple/Blue 审美严格禁止
  - 使用 Zinc/Slate 作为中性底色
- **布局约束（Rule 3）**：`LAYOUT_VARIANCE > 4` 时居中 Hero/H1 严格禁止
- **卡片规则（Rule 4）**：`VISUAL_DENSITY > 7` 时通用卡片容器严格禁止
- **Bento 范式（Section 9）**：
  - 背景 `#f9fafb`，卡片 `#ffffff` + `border-slate-200/50`
  - 圆角 `rounded-[2.5rem]`
  - 弹簧物理：`type: "spring", stiffness: 100, damping: 20`
  - 响应式容器：`max-w-[1400px] mx-auto`
  - Full-height 节必须使用 `min-h-[100dvh]`
- **AI Tells 禁止（Section 7）**：No neon/outer glows、No pure black (#000000)、No oversaturated accents、No gradient text on large headers、No custom mouse cursors、No Inter Font、No 3-Column Card Layouts

**与其他 skill 的重叠**
- `baseline-ui`：两者都是全局约束，但 design-taste-frontend 更完整、更复杂
- `high-end-visual-design`：两者都追求"高端"美学，但 design-taste-frontend 参数驱动，high-end 是固定的视觉规范
- `stitch-design-taste`：stitch-design-taste 是 design-taste-frontend 的 Stitch 平台输出版本
- `frontend-design`：两者的 DON'T 列表高度重叠

---

### full-output-enforcement

**Token 体量**
- 字符数：2641 | 估算 token：~660 | 体量级别：**S**

**核心功能**
full-output-enforcement 覆盖 LLM 默认的截断行为，强制完整代码生成，禁止占位符模式，处理超过 token 限制时的分割。适用于任何需要完整、未删减输出的任务。不是设计 skill，是输出行为 skill。

**审美编码位置**
- 本身无审美编码，但有具体的"禁止输出模式"：`// ...`、`// rest of code`、`// implement here`、`// TODO`、`/* ... */` 等均为硬性失败

**与其他 skill 的重叠**
- 无功能性重叠，是独立的输出约束 skill

---

### high-end-visual-design

**Token 体量**
- 字符数：10659 | 估算 token：~2665 | 体量级别：**L**

**核心功能**
high-end-visual-design 将 AI 定位为 Awwwards 级别的 Principal UI/UX 架构师，通过"Variance Engine"（三种氛围 × 三种布局）随机选取设计方向，确保每次输出唯一且高端。定义了"双贝塞尔"（Doppelrand）嵌套架构、"岛屿"按钮架构、磁性 hover 物理、滚动插值入场动画等具体实现规范。

**审美编码位置**
- **字体禁令（Section 2）**：`Banned Fonts: Inter, Roboto, Arial, Open Sans, Helvetica`；推荐 `Geist/Clash Display/PP Editorial New/Plus Jakarta Sans`
- **图标禁令**：禁止标准 Lucide/FontAwesome/Material 图标，仅允许超细线条（Phosphor Light/Remix Line）
- **阴影禁令**：禁止 `shadow-md`、`rgba(0,0,0,0.3)` 等生硬深色阴影
- **Section padding**：最低 `py-24`，允许设计大量呼吸空间
- **圆角规范**：`rounded-[2rem]` 用于主要容器，内部元素用 `rounded-[calc(2rem-0.375rem)]`（同心圆角）
- **Bento 卡片弹簧**：`type: "spring", stiffness: 100, damping: 20`
- **过渡曲线**：`cubic-bezier(0.32,0.72,0,1)` 而非默认 linear
- **Mobile 强制**：`min-h-[100dvh]` 禁止 `h-screen`
- **Enter animation**：`translate-y-16 blur-md opacity-0 → translate-y-0 blur-0 opacity-100` over `800ms+`

**与其他 skill 的重叠**
- `design-taste-frontend`：两者都定义高端美学，但角度不同（design-taste-frontend 参数化，high-end 更"建筑师流"）
- `minimalist-ui`/`industrial-brutalist-ui`：三者都是特定美学方向的 skill
- `stitch-design-taste`：stitch-design-taste 中的许多反模式与 high-end 完全相同

---

### industrial-brutalist-ui

**Token 体量**
- 字符数：8548 | 估算 token：~2137 | 体量级别：**L**

**核心功能**
industrial-brutalist-ui 定义工业粗野主义 UI 风格，融合 1960 年代瑞士平面设计与军事终端美学，支持两种范式（Swiss Industrial Print vs Tactical Telemetry CRT Terminal），适用于数据密集仪表板、portfolio 或需要"解密蓝图"感的编辑网站。

**审美编码位置**
- **字体规范（Section 3）**：
  - 宏观排版：`Neue Haas Grotesk/Archivo Black/Monument Extended`，`clamp(4rem, 10vw, 15rem)` 流体尺寸，tracking `−0.03em` 至 `−0.06em`，leading `0.85-0.95`，全大写
  - 微观排版：`JetBrains Mono/IBM Plex Mono/VT323`，`10px-14px`，tracking `0.05em-0.1em`，全大写
- **色彩系统（Section 4）**：
  - Swiss Industrial Light: 背景 `#F4F4F0`/`#EAE8E3`，前景 `#050505-#111111`，唯一强调色 `#E61919`/`#FF2A2A`
  - CRT Terminal Dark: 背景 `#0A0A0A`/`#121212`，前景 `#EAEAEA`，强调色同 `#E61919`，可选 Terminal Green `#4AF626` 仅限单个元素
- **几何约束**：绝对禁止 `border-radius`，所有角必须是 90 度
- **禁止模式**：禁止渐变、软阴影、现代半透明效果
- **Layout（Section 5）**：使用 `display: grid; gap: 1px` + 对比背景色生成分割线

**与其他 skill 的重叠**
- `minimalist-ui`：两者都是特定审美方向，但风格完全相反（brutalist 粗犷，minimalist 精致）
- `high-end-visual-design`：high-end 的"Tactical Telemetry"氛围与 industrial-brutalist 的 CRT 模式有交集

---

### minimalist-ui

**Token 体量**
- 字符数：7986 | 估算 token：~1997 | 体量级别：**M**（接近 L）

**核心功能**
minimalist-ui 定义高端编辑极简主义 UI，类比 Notion/Linear 等顶级工作区平台风格，强制暖色单色调色板、bento 网格、极致平面组件架构和精致的 muted pastel 强调色。

**审美编码位置**
- **禁止字体**：`Inter, Roboto, Open Sans`；推荐 `SF Pro Display/Geist Sans/Helvetica Neue/Switzer`
- **编辑衬线字体**：`Lyon Text/Newsreader/Playfair Display/Instrument Serif`，tracking `-0.02em` 至 `-0.04em`，leading `1.1`
- **正文文字颜色**：禁止绝对黑 `#000000`，使用 `#111111` 或 `#2F3437`，次要文字 `#787774`
- **色板（Section 4）**：
  - Canvas: `#FFFFFF` 或 `#F7F6F3`/`#FBFBFA`
  - 主表面（卡片）: `#FFFFFF` 或 `#F9F9F8`
  - 分割线: `#EAEAEA` 或 `rgba(0,0,0,0.06)`
  - 强调色仅限 desaturated pastel（4 种，附 hex）
- **组件规范（Section 5）**：
  - Bento card: `border: 1px solid #EAEAEA`，border-radius `8px` 或 `12px`，padding `24-40px`
  - 主要 CTA 按钮：背景 `#111111`，文字 `#ffffff`，border-radius `4-6px`，无 box-shadow，hover `→ #333333` 或 `scale(0.98)`
- **动效规范（Section 7）**：
  - 入场：`translateY(12px)` + opacity 0，600ms，`cubic-bezier(0.16, 1, 0.3, 1)`
  - Card hover: `box-shadow 0 2px 8px rgba(0,0,0,0.04)`，200ms
  - Stagger: `animation-delay: calc(var(--index) * 80ms)`
- **禁止阴影**：`shadow-md, shadow-lg, shadow-xl` 禁止

**与其他 skill 的重叠**
- `industrial-brutalist-ui`：两者都是特定审美方向，风格相反
- `high-end-visual-design`：minimalist 对应 high-end 的"Soft Structuralism"氛围
- `distill`：minimalist 的极简化与 distill 的去繁原则高度一致

---

### redesign-existing-projects

**Token 体量**
- 字符数：15238 | 估算 token：~3810 | 体量级别：**L**（接近 XL）

**核心功能**
redesign-existing-projects 是对现有网站/应用进行全面升级的 skill，执行"扫描 → 诊断 → 修复"三步流程，覆盖排版、色彩表面、布局、交互状态、内容、组件模式、图标、代码质量和"AI 经常忘记的内容"九个审计维度，并提供按优先级排序的修复顺序。

**审美编码位置**
- **排版（Typography 审计节）**：
  - 禁止浏览器默认字体或 `Inter`；推荐 `Geist/Outfit/Cabinet Grotesk/Satoshi`
  - 正文最大宽度：约 `65字符`
  - 禁止 400/700 之外的字重缺失（引入 500/600）
  - 数字必须用 `tabular-nums`
- **色彩（Color and Surfaces 节）**：
  - 禁止纯 `#000000` 背景；使用 `#0a0a0a`、`#121212` 或深蓝
  - 饱和度 `< 80%`
  - 仅一个强调色
  - 暖/冷灰不能混用
  - "purple/blue AI gradient" 是最常见 AI 指纹，明确禁止
  - 阴影颜色必须与背景同色调（colored shadows）
- **布局**：
  - 禁止 `height: 100vh`，改用 `min-height: 100dvh`
  - 加 container `1200-1440px max-width`
- **修复优先级顺序**：字体换 → 色板清理 → hover/active 状态 → 布局间距 → 替换通用组件 → 加 loading/empty/error 状态 → 精磨排版

**与其他 skill 的重叠**
- `audit`：redesign 的诊断部分与 audit 的检查维度高度重叠
- `bolder`/`quieter`：美学方向指导来自相同的原则
- `typeset`、`colorize`、`arrange`、`polish`：每个专项 skill 都对应 redesign 的某个审计维度

---

### stitch-design-taste

**Token 体量**
- 字符数：12043 | 估算 token：~3011 | 体量级别：**L**

**核心功能**
stitch-design-taste 是为 Google Stitch 平台生成 `DESIGN.md` 文件的 skill，将 design-taste-frontend 的反 Slop 指令翻译为 Stitch 的自然语言语义设计系统格式。输出涵盖视觉氛围、色彩、排版、组件、布局、动效、反模式七个部分的 DESIGN.md。

**审美编码位置**
- **默认参数**：Variance 8、Motion 6、Density 4（与 design-taste-frontend 完全相同）
- **色彩约束**：Max 1 accent，saturation `< 80%`，禁止 AI Purple/Blue Neon
- **字体约束**：`Inter` 禁止；禁止通用衬线（Times/Georgia/Garamond/Palatino）；允许高端现代衬线（`Fraunces/Gambarino/Editorial New/Instrument Serif`）
- **Hero 节**：禁止居中 Hero（variance > 4）；禁止"Scroll to explore"滚动提示
- **具体禁止模式列表（Section 9）**：与 design-taste-frontend Section 7 基本相同
- **间距**：section gap 使用 `clamp(3rem, 8vw, 6rem)`，触控目标 `44px` 最小

**与其他 skill 的重叠**
- `design-taste-frontend`：几乎是其 Stitch 平台输出版本，核心原则一致
- `high-end-visual-design`：反模式和规则大量重叠

---

## 三、greensock/gsap-skills GSAP 官方 skill

### gsap-core

**Token 体量**
- 字符数：15046 | 估算 token：~3762 | 体量级别：**L**（接近 XL）

**核心功能**
gsap-core 覆盖 GSAP 核心 API：`gsap.to()`、`from()`、`fromTo()`、`set()`、easing、duration、stagger、defaults、`gsap.matchMedia()`（响应式和 prefers-reduced-motion）。这是 GSAP skill 族的入口，其他 GSAP skill 均以此为基础并互相引用。

**审美编码位置**
- **ease 字符串规范**：推荐 `power1.out`（默认）、`power3.inOut`、`back.out(1.7)`、`elastic.out(1, 0.3)`
- **`prefers-reduced-motion` 处理**：必须通过 `gsap.matchMedia()` 处理 `(prefers-reduced-motion: reduce)`，`duration: 0` 或跳过动画
- **禁止动画布局属性**：`width, height, top, left` → 使用 `x, y, scale, rotation`

**与其他 skill 的重叠**
- `gsap-timeline`、`gsap-react`、`gsap-scrolltrigger`、`gsap-plugins`、`gsap-performance`、`gsap-frameworks`、`gsap-utils`：都以 gsap-core 为基础
- `animate`：gsap-core 是 animate skill 推荐的 JavaScript 动画实现之一

---

### gsap-frameworks

**Token 体量**
- 字符数：6741 | 估算 token：~1685 | 体量级别：**M**

**核心功能**
gsap-frameworks 覆盖 Vue/Svelte 等非 React 框架中 GSAP 的生命周期管理、选择器作用域、卸载清理。核心模式：在 `onMounted`/`onMount` 中创建，在 `onUnmounted`/onMount 返回函数中清理，使用 `gsap.context(scope)` 限定选择器范围。

**审美编码位置**
- 本身无审美编码，是框架集成规范

**与其他 skill 的重叠**
- `gsap-react`：gsap-frameworks 是 Vue/Svelte 版本，gsap-react 是 React 版本，逻辑几乎相同
- `gsap-scrolltrigger`：两者都有 ScrollTrigger 清理的说明

---

### gsap-performance

**Token 体量**
- 字符数：4218 | 估算 token：~1055 | 体量级别：**M**（接近 S 边界）

**核心功能**
gsap-performance 专注 GSAP 动画的性能优化：偏好 transform/opacity、`will-change` 用法、批量 DOM 读写、多元素 stagger、`gsap.quickTo()` 用于鼠标追随等高频更新、ScrollTrigger 性能考量。

**审美编码位置**
- **核心规则**：`will-change: transform` 用于即将动画的元素
- `gsap.quickTo()` 用于 mousemove 等高频属性更新

**与其他 skill 的重叠**
- `fixing-motion-performance`：两者高度重叠，但 fixing-motion-performance 更通用，gsap-performance 专注 GSAP
- `optimize`：optimize 的 Animation Performance 节与 gsap-performance 完全重叠
- `baseline-ui`：动画属性约束完全相同

---

### gsap-plugins

**Token 体量**
- 字符数：21265 | 估算 token：~5316 | 体量级别：**XL**

**核心功能**
gsap-plugins 覆盖所有 GSAP 插件：ScrollToPlugin、ScrollSmoother、Flip（FLIP 动画）、Draggable（拖拽+惯性）、Observer（手势）、SplitText（文字分割动画）、ScrambleText（打乱文字效果）、DrawSVG、MorphSVG、MotionPath、Physics2D/PhysicsProps、CustomEase、EasePack、GSDevTools 等。

**审美编码位置**
- **SplitText 无障碍**：`aria: "auto"` 默认给分割元素添加 `aria-label`
- **DrawSVG**：stroke 必须可见才有效果
- **GSDevTools** 禁止上线（仅开发使用）
- **注册顺序**：必须先 `gsap.registerPlugin()` 才能使用

**与其他 skill 的重叠**
- `gsap-core`：CustomEase 在 gsap-core 中已有基本说明，gsap-plugins 是完整版
- `gsap-scrolltrigger`：ScrollSmoother 需要 ScrollTrigger，在 gsap-plugins 中也有说明

---

### gsap-react

**Token 体量**
- 字符数：6700 | 估算 token：~1675 | 体量级别：**M**

**核心功能**
gsap-react 覆盖 React/Next.js 中 GSAP 的最佳实践：优先使用 `useGSAP()` hook（自动清理）、refs 作为目标、依赖数组和 scope、`gsap.context()` 作为 `useEffect` 备选、`contextSafe` 包装事件处理器、SSR 注意事项。

**审美编码位置**
- 本身无审美编码，是 React 集成规范

**与其他 skill 的重叠**
- `gsap-frameworks`：React 版本 vs Vue/Svelte 版本，模式相似

---

### gsap-scrolltrigger

**Token 体量**
- 字符数：18686 | 估算 token：~4672 | 体量级别：**XL**

**核心功能**
gsap-scrolltrigger 覆盖 ScrollTrigger 的完整 API：基础触发、关键配置（trigger/start/end/scrub/toggleActions/pin）、`ScrollTrigger.batch()`（批量处理）、`scrollerProxy()`（第三方平滑滚动集成）、scrub、pin、水平滚动（containerAnimation）、刷新与清理。

**审美编码位置**
- **`ease: "none"` 强制要求**：水平滚动 containerAnimation 的动画必须用 `ease: "none"`
- **`markers: false` 必须在生产**：明确要求
- **pinSpacing 默认 true**：防止布局塌陷

**与其他 skill 的重叠**
- `gsap-core`、`gsap-timeline`：被 gsap-scrolltrigger 依赖
- `gsap-react`、`gsap-frameworks`：都有 ScrollTrigger 清理的说明（重复）
- `overdrive`：overdrive 的 scroll-driven 部分可由 ScrollTrigger 实现

---

### gsap-timeline

**Token 体量**
- 字符数：4501 | 估算 token：~1125 | 体量级别：**M**

**核心功能**
gsap-timeline 覆盖 `gsap.timeline()` 的完整使用：position 参数（绝对位置/相对位置/标签/`<`>`>`）、timeline defaults、labels、嵌套 timeline、播放控制。核心原则：用 timeline 替代 delay 链式动画。

**审美编码位置**
- **ScrollTrigger 只能在顶层**：不能嵌套在 timeline 内部子 tween 中

**与其他 skill 的重叠**
- `gsap-core`：timeline 是 core API 的扩展
- `gsap-scrolltrigger`：scroll-driven timeline 是两者的交集

---

### gsap-utils

**Token 体量**
- 字符数：12377 | 估算 token：~3094 | 体量级别：**L**

**核心功能**
gsap-utils 覆盖 `gsap.utils` 工具函数族：clamp/mapRange/normalize（范围处理）、interpolate（插值）、random/snap/shuffle/distribute（随机和分布）、getUnit/unitize/splitColor（单位和颜色解析）、selector/toArray/pipe/wrap/wrapYoyo（数组和集合操作）。

**审美编码位置**
- **splitColor 支持 oklch 解析**：`splitColor("red")` → `[255, 0, 0]`
- 本身无视觉审美编码，是纯数学/工具 API

**与其他 skill 的重叠**
- `gsap-core`：utils 是 core 的辅助，两者配合使用
- `gsap-scrolltrigger`：mapRange/clamp 常用于 scrub 计算

---

## 四、ibelick/ui-skills UI 约束检查 skill

### fixing-accessibility

**Token 体量**
- 字符数：4853 | 估算 token：~1213 | 体量级别：**M**（接近 S）

**核心功能**
fixing-accessibility 审查并修复 HTML 无障碍问题，覆盖 ARIA 标签、键盘导航、焦点管理、颜色对比、表单错误等，分 9 个优先级类别（critical → low-medium）。提供具体代码修复示例。强调"工具边界"：不重构无关代码，优先使用原生 HTML 而非 ARIA 包装。

**审美编码位置**
- 本身无审美编码，是纯无障碍规范
- 强调"prefer minimal changes"（最小侵入原则）

**与其他 skill 的重叠**
- `audit`：audit 的 Accessibility 维度是 fixing-accessibility 的诊断版
- `harden`：harden 的 Accessibility Resilience 节与 fixing-accessibility 重叠
- `baseline-ui`：baseline-ui 的 Components 节（ARIA label）与 fixing-accessibility 重叠

---

### fixing-metadata

**Token 体量**
- 字符数：4551 | 估算 token：~1138 | 体量级别：**M**（接近 S）

**核心功能**
fixing-metadata 审查并修复 HTML 元数据：页面标题、meta description、canonical URL、Open Graph、Twitter cards、favicon、JSON-LD 结构化数据、robots 指令。分 8 个优先级类别，强调"minimal, scoped diffs"。

**审美编码位置**
- 本身无审美编码，是纯 SEO/metadata 规范

**与其他 skill 的重叠**
- `redesign-existing-projects`：Code Quality 和 Strategic Omissions 节包含缺少 meta tags 的检查

---

### fixing-motion-performance

**Token 体量**
- 字符数：5716 | 估算 token：~1429 | 体量级别：**M**

**核心功能**
fixing-motion-performance 审查并修复动画性能问题：layout thrashing、合成器属性、滚动关联动效、blur 滤镜。分 9 个优先级类别，提供 FLIP 批量读写等具体修复模式。强调"不迁移动画库，在现有栈内修复"。

**审美编码位置**
- **blur 约束**：`keep blur animation small (<=8px)`，一次性效果，禁止持续动画，禁止大表面
- **CSS variable 动画**：禁止动画 CSS 变量用于 transform/opacity/position
- **scroll 处理**：禁止 `scrollTop`/`scrollY` 驱动动画

**与其他 skill 的重叠**
- `gsap-performance`：规则高度重叠（约束完全一致，gsap-performance 是 GSAP 专属版）
- `baseline-ui`：动画约束完全相同
- `optimize`：animate performance 子节完全重叠
- `animate`：animate 的 Technical Implementation → Performance 节内容重叠

---

## 五、better-auth/better-icons

### better-icons

**Token 体量**
- 字符数：3713 | 估算 token：~928 | 体量级别：**S**

**核心功能**
better-icons 提供通过 Iconify 搜索 200+ 图标库并获取 SVG 的 CLI 工具和 MCP 工具。支持 `better-icons search`、`get`、批量下载，以及 MCP 工具（search_icons/get_icon/recommend_icons/find_similar_icons/sync_icon/scan_project_icons）。不是设计 skill，是图标资源获取工具。

**审美编码位置**
- 热门图标集推荐：`lucide/mdi/heroicons/tabler/ph/ri/solar/iconamoon`（这本身是一种图标偏好编码）

**与其他 skill 的重叠**
- `baseline-ui`：baseline-ui 要求"有键盘/焦点行为的元素必须用无障碍组件原语"，图标按钮需要 `aria-label`
- `fixing-accessibility`：icon-only 按钮需要 `aria-label`，与 fixing-accessibility 规则对应
- `redesign-existing-projects`/`design-taste-frontend`/`high-end-visual-design`：都有图标库偏好（禁止 Lucide 作为默认选择）

---

*审计完成。共分析 41 个 skill。*
