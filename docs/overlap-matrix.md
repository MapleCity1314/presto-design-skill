# Skill 重叠矩阵

> 基于实际读取每个 skill 的 SKILL.md 内容分析，记录功能重叠的 skill 对、重叠程度和具体重叠功能。

---

## 重叠程度说明

- **高**：核心功能直接重叠，存在明显的双重覆盖
- **中**：部分功能章节重叠，但整体定位不同
- **低**：仅有概念或规则上的引用关系，整体功能差异明显

---

## 重叠关系总表

| Skill A | Skill B | 重叠程度 | 重叠功能描述 |
|---------|---------|----------|-------------|
| **audit** | **critique** | 高 | 两者都对设计进行系统评分并输出 P0-P3 优先级问题列表。audit 侧重技术维度（a11y/性能/主题/响应式），critique 侧重 UX 设计维度（视觉层级/信息架构/情感旅程）。两者输出格式几乎相同（分维度评分 + 推荐命令列表），都检查 AI Slop。 |
| **audit** | **fixing-accessibility** | 高 | audit 的 Accessibility 维度（对比度/ARIA/键盘/语义 HTML/表单）与 fixing-accessibility 的全部内容重叠。区别：audit 只诊断记录，fixing-accessibility 执行修复且更细致（9个优先级类别）。 |
| **audit** | **optimize** | 高 | audit 的 Performance 维度（layout thrashing/昂贵动画/lazy loading/bundle size/re-render）与 optimize 的核心内容重叠。区别：audit 诊断，optimize 实施修复。 |
| **animate** | **delight** | 高 | 两者都涉及微交互和动效设计。animate 是系统化策略（6大类别）；delight 专注惊喜感和愉悦时刻，包含动效实现（按钮、toggle、拖拽等）。两者的具体微交互规范（button press、成功动效）大量重叠。 |
| **animate** | **fixing-motion-performance** | 高 | animate 的 Technical Implementation → Performance 节（GPU 加速、只动画 transform/opacity）与 fixing-motion-performance 的核心规则完全相同。区别：animate 是添加动效，fixing-motion-performance 是修复性能问题。 |
| **animate** | **gsap-core** | 中 | animate 推荐 GSAP 作为 JavaScript 动画实现，并引用相同的缓动曲线理念（自然减速，avoid bounce/elastic）。gsap-core 是 animate 策略的具体技术实现。 |
| **bolder** | **quieter** | 高 | 完全相反方向的操作对。bolder 在排版/色彩/空间/视觉效果/动效/构图六个维度增强设计；quieter 在相同六个维度（色彩饱和度/视觉重量/简化/动效/构图）降低设计强度。两者的规则镜像对应。 |
| **bolder** | **colorize** | 中 | bolder 的 Color Intensification 节（增加饱和度/主导色策略/锐利强调色）与 colorize 的战略性引入色彩高度重叠。区别：bolder 是整体设计放大，colorize 专注色彩策略。 |
| **bolder** | **overdrive** | 中 | 两者都追求视觉冲击力。overdrive 是 bolder 的技术极限版，额外引入 WebGL/shader/Web Workers 等技术手段。bolder 更侧重设计美学层面。 |
| **bolder** | **typeset** | 中 | bolder 的 Typography Amplification 节（极端字体缩放 3x-5x、900 vs 200 字重对比）与 typeset 的字体选择和层级建立高度重叠，但方向相反（typeset 建立清晰层级，bolder 夸大戏剧性）。 |
| **arrange** | **distill** | 高 | arrange 的 Layout Simplification（线性流、移除侧边栏、减少嵌套）与 distill 的 Layout Simplification 节几乎相同内容。两者都强调：禁止嵌套卡片、禁止卡片过度使用、使用间距代替容器。 |
| **arrange** | **polish** | 高 | polish 的 Visual Alignment & Spacing 节（像素级对齐、一致间距、光学对齐）与 arrange 的系统化间距改善大量重叠。区别：polish 是最终细节检查，arrange 是布局策略调整。 |
| **arrange** | **normalize** | 中 | normalize 的间距 token 对齐（使用设计系统间距 token）与 arrange 的建立间距系统（使用一致的间距比例）目标相似，但 normalize 对齐到现有系统，arrange 可能创建新系统。 |
| **distill** | **quieter** | 中 | 两者都在"减少"方向操作。quieter 降低视觉强度（饱和度/字重/动效距离），distill 删除不必要元素（冗余信息/装饰/嵌套层级）。quieter 是调节旋钮，distill 是删除操作。 |
| **colorize** | **quieter** | 中 | colorize 的"战略性引入色彩"与 quieter 的"Color Refinement"（减少饱和度、减少色彩种类）是反向操作。两者都强调 gray on color 规则、OKLCH 色彩空间、60/30/10 色彩比例。 |
| **harden** | **fixing-accessibility** | 中 | harden 的 Accessibility Resilience 节（键盘导航/屏幕阅读器/`prefers-reduced-motion`）与 fixing-accessibility 覆盖相同问题。区别：harden 还覆盖 i18n、错误处理、边缘案例；fixing-accessibility 专注可访问性且更深入。 |
| **harden** | **onboard** | 中 | 两者都处理空状态设计。harden 的 Edge Cases → Empty states 要求"提供清晰的下一步操作"；onboard 的 Empty State Design 详细规定 4 个要素（what/why/how/visual interest）。 |
| **harden** | **audit** | 中 | audit 的 Responsive Design 维度（fixed widths/touch targets/horizontal scroll/text scaling）与 harden 的 Responsive text sizing 和 i18n 部分重叠。 |
| **frontend-design** | **design-taste-frontend** | 高 | 两者都是全局设计原则 skill，DON'T 列表高度重叠（禁止相同字体/色彩/布局模式）。区别：frontend-design 是 impeccable 系列的宿主，其他 skill 通过依赖链加载；design-taste-frontend 是独立的参数驱动系统，包含更具体的 CSS 数值规范。 |
| **frontend-design** | **baseline-ui** | 高 | DON'T 规则大量重叠（禁止渐变/紫色/glow/纯黑纯白/hero 指标布局/嵌套卡片）。区别：frontend-design 是设计方向 + context gathering 框架；baseline-ui 是可执行的 MUST/NEVER/SHOULD 规则列表，针对 Tailwind 技术栈。 |
| **frontend-design** | **redesign-existing-projects** | 高 | redesign 的所有审计维度（Typography/Color/Layout/Interactivity/Content）直接实施 frontend-design 的 DON'T 规则。区别：frontend-design 是原则框架，redesign 是可操作的检查清单 + 升级技术。 |
| **typeset** | **polish** | 高 | polish 的 Typography Refinement 节（层级一致性/行长 45-75 字符/行高/孤字处理/字距微调）与 typeset 的全部内容高度重叠。区别：typeset 是专项字体改善，polish 是最终检查的其中一个维度。 |
| **typeset** | **redesign-existing-projects** | 高 | redesign 的 Typography 审计节（禁止 Inter/调整字号/正文最大宽度约 65 字符/引入 Medium/SemiBold 字重/数字 tabular-nums）与 typeset 的改善清单完全对应。 |
| **normalize** | **extract** | 中 | extract 从实现中提炼设计系统（identify patterns → create tokens/components），normalize 将实现对齐到设计系统（align existing implementation to standards）。两者互补但方向相反。 |
| **normalize** | **polish** | 中 | 两者都修复不一致性。normalize 对齐到设计系统标准（系统级），polish 修复细节（像素级）。polish 是 normalize 之后的下一步。 |
| **polish** | **redesign-existing-projects** | 高 | redesign 的升级技术（Typography/Layout/Motion 升级）对应 polish 的多个维度检查清单。两者都是全面的质量提升，区别在于 redesign 针对现有项目进行结构性重新设计，polish 是功能完成后的细节打磨。 |
| **onboard** | **clarify** | 中 | onboard 的引导文案（空状态文案/tooltip/Feature Announcements）与 clarify 的 UX 写作原则（具体/简洁/主动/有帮助）重叠。区别：clarify 专注文字本身的改善，onboard 聚焦首次体验流程设计。 |
| **onboard** | **delight** | 中 | onboard 的 Empty State Design（视觉吸引力、引导行动）和完成庆祝与 delight 的 Celebration Moments、Empty states 大量重叠。两者都强调"首次体验"和"成就达成"场景。 |
| **optimize** | **fixing-motion-performance** | 高 | optimize 的 Animation Performance 节（GPU 加速/只用 transform 和 opacity/requestAnimationFrame/Intersection Observer）与 fixing-motion-performance 的全部规则（never patterns/compositor props/scroll/blur）高度重叠。区别：optimize 覆盖更广（加载/渲染/动画/图片/bundle），fixing-motion-performance 专注动画。 |
| **optimize** | **gsap-performance** | 高 | optimize 的 Animation Performance 节与 gsap-performance 内容几乎相同（prefer transform/opacity、will-change 用法、batch reads/writes、quickTo 用于频繁更新）。区别：optimize 是通用性能，gsap-performance 是 GSAP 专属。 |
| **overdrive** | **gsap-scrolltrigger** | 中 | overdrive 的 scroll-driven animations 工具箱（`animation-timeline: scroll()`）与 gsap-scrolltrigger 功能重叠。overdrive 提供 CSS-only 方案，gsap-scrolltrigger 提供 GSAP 方案。 |
| **design-taste-frontend** | **high-end-visual-design** | 高 | 两者都定义高端 UI 美学，禁止相同字体（Inter/Roboto）、相同色彩模式（purple/neon）、相同布局模式（3列卡片/居中 Hero）。区别：design-taste-frontend 通过 3 个参数（Variance/Motion/Density）驱动所有规则；high-end 通过"Variance Engine"随机选择氛围+布局组合，更侧重"每次输出都不同"的多样性。 |
| **design-taste-frontend** | **stitch-design-taste** | 高 | stitch-design-taste 几乎是 design-taste-frontend 的 Stitch 平台翻译版本，共享相同的默认参数（Variance 8/Motion 6/Density 4）、相同的禁止列表（Inter/pure black/neon/3-column grids）、相同的弹簧物理规范（stiffness 100/damping 20）。区别：stitch-design-taste 输出 DESIGN.md 文件（自然语言描述），design-taste-frontend 输出代码。 |
| **design-taste-frontend** | **minimalist-ui** | 中 | 两者都禁止 Inter、都有色彩饱和度约束、都推荐 Geist/Satoshi 字体族。区别：minimalist-ui 定义了具体的暖色单色调规范和极简组件规范；design-taste-frontend 的默认 Variance 8 意味着更高设计多样性。 |
| **high-end-visual-design** | **stitch-design-taste** | 高 | 两者共享大量反模式（禁止 Inter/Roboto/Arial、禁止通用阴影、禁止 3 列等宽卡片、禁止居中 Hero），以及相同的弹簧物理规范、min-h-[100dvh] 约束。high-end 更侧重具体的视觉组件实现（双贝塞尔架构），stitch 更侧重生成 Stitch 可理解的自然语言规范。 |
| **baseline-ui** | **fixing-motion-performance** | 高 | baseline-ui 的 Animation 节（MUST animate only compositor props/NEVER animate layout properties/NEVER exceed 200ms/MUST pause looping animations when off-screen）与 fixing-motion-performance 的核心规则完全对应。区别：baseline-ui 是预防性约束，fixing-motion-performance 是诊断+修复。 |
| **baseline-ui** | **gsap-performance** | 中 | baseline-ui 的 Performance 节（NEVER animate large blur()/NEVER apply will-change outside active animation）与 gsap-performance 的 will-change 使用规范和 blur 约束重叠。 |
| **gsap-core** | **gsap-timeline** | 中 | gsap-timeline 是 gsap-core 的扩展，timeline 的 defaults、paused、repeat、yoyo、callbacks 都在 gsap-core 中有基础定义。区别：gsap-core 覆盖单个 tween，gsap-timeline 专注多步骤编排（position 参数、标签、嵌套）。 |
| **gsap-react** | **gsap-frameworks** | 高 | 两者解决相同问题（框架中的 GSAP 生命周期管理），但针对不同框架。`useGSAP()` 对应 Vue 的 `onMounted`/`onUnmounted`；`gsap.context(scope)` + cleanup 模式完全相同；selector scoping 规则相同。 |
| **gsap-scrolltrigger** | **gsap-react** | 中 | gsap-react 中有 ScrollTrigger 在 React 中的清理说明（useGSAP 自动清理），gsap-scrolltrigger 的 Cleanup 节也提到 React。两者在 ScrollTrigger + React 场景下有内容重叠。 |
| **gsap-scrolltrigger** | **gsap-frameworks** | 中 | gsap-frameworks 中有 ScrollTrigger 在 Vue/Svelte 中的清理说明和 `ScrollTrigger.refresh()` 时机，gsap-scrolltrigger 是完整的 ScrollTrigger 文档，两者在框架集成部分重叠。 |
| **fixing-accessibility** | **harden** | 中 | harden 的 Accessibility Resilience 节覆盖 fixing-accessibility 的核心内容（ARIA/键盘/屏幕阅读器/prefers-reduced-motion），但 harden 还包含 i18n/错误处理/边缘案例，fixing-accessibility 更深入（9个优先级类别）。 |
| **fixing-motion-performance** | **gsap-performance** | 高 | 两者规则高度一致：禁止动画布局属性（width/height/top/left）、偏好 compositor 属性（transform/opacity）、batch DOM reads/writes、避免持续 blur 动画等。区别：fixing-motion-performance 更通用（含 CSS/WAAPI/rAF 等），gsap-performance 专注 GSAP API（quickTo/stagger 等）。 |
| **critique** | **audit** | 高 | 见第一行，两者是设计评审的两个互补维度（设计 vs 技术），但都输出 P0-P3 优先级问题 + 推荐命令，都检查 AI Slop。实际使用中应同时运行以获得完整评估。 |
| **redesign-existing-projects** | **audit** | 中 | redesign 的 Design Audit 与 audit 的 5 个检查维度大量重叠。区别：audit 是只读诊断（不修复），redesign 是扫描-诊断-修复三步流程，且 redesign 更全面（包含内容、组件模式、图标、代码质量等 audit 不覆盖的维度）。 |
| **redesign-existing-projects** | **normalize** | 中 | 两者都在"对齐/升级现有项目"，但 redesign 更激进（替换通用模式/升级美学），normalize 更保守（对齐到现有设计系统，不引入新模式）。 |
| **teach-impeccable** | **frontend-design** | 中 | frontend-design 的 Context Gathering Protocol 的第 3 步就是运行 teach-impeccable。teach-impeccable 收集并持久化的上下文正是 frontend-design 要求的"必需上下文"（audience/use cases/brand personality）。 |
| **clarify** | **delight** | 低 | clarify 要求清晰、不使用幽默（"对错误要共情而非幽默"），delight 要求在合适时候加入个性化文案和俏皮表达。两者在文案风格上存在策略张力，但适用场景不同。 |
| **better-icons** | **redesign-existing-projects** | 低 | redesign 要求替换 Lucide/Feather 等默认图标，建议使用 Phosphor/Heroicons；better-icons 提供实际获取替代图标的工具。两者在"图标升级"场景下配合使用。 |

---

## 重叠热点分析

以下 skill 是重叠关系最密集的"枢纽节点"：

| Skill | 与之重叠的 skill 数量 | 主要重叠方向 |
|-------|---------------------|-------------|
| **frontend-design** | 18 个（被所有 impeccable skill 依赖） | 原则框架，所有设计 skill 的宿主 |
| **audit** | 6 个 | 诊断与各专项修复 skill 的交集 |
| **polish** | 5 个 | 最终质量检查与各专项改善 skill 重叠 |
| **animate** | 5 个 | 动效策略与性能/实现/风格 skill 重叠 |
| **fixing-motion-performance** | 5 个 | 动画性能规则与各层级 skill 重叠 |
| **redesign-existing-projects** | 5 个 | 全面升级任务与各专项 skill 对应 |
| **harden** | 4 个 | 健壮性与可访问性/性能/边缘状态重叠 |
| **design-taste-frontend** | 4 个 | 高端美学规范与同类风格 skill 重叠 |

---

## 互补而非重叠的关键关系

以下 skill 对看起来相关，但实际定位清晰互补，不存在真正的功能重叠：

| Skill A | Skill B | 关系说明 |
|---------|---------|---------|
| **audit** | **polish** | audit 是诊断评分，polish 是执行修复；audit 应在 polish 之前运行 |
| **teach-impeccable** | 所有设计 skill | teach-impeccable 是一次性上下文收集，其他 skill 消费这个上下文 |
| **extract** | **normalize** | extract 从代码中提炼系统，normalize 对齐到已有系统；两者顺序关系明确 |
| **better-icons** | 所有 skill | better-icons 是图标资源工具，与设计 skill 在工具层面配合，无功能重叠 |
| **full-output-enforcement** | 所有 skill | 输出行为约束，与所有 skill 正交 |
| **fixing-metadata** | 所有 skill | SEO/metadata 专项，与 UI/UX/动画 skill 完全正交 |
| **gsap-utils** | **gsap-core** | utils 是纯工具函数，与 core API 配合但不重叠 |
