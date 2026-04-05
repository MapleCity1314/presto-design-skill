# Token 预算分析

> 估算方法：chars ÷ 4 ≈ token 数（标准 GPT tokenizer 估算，实际可能有 ±15% 偏差）
>
> 体量分级：XS (<500) / S (500-1000) / M (1000-2000) / L (2000-4000) / XL (>4000)

---

## 一、按 Token 量排序（从大到小）

| 排名 | Skill | 字符数 | 估算 Token | 体量级别 |
|------|-------|--------|-----------|----------|
| 1 | **design-taste-frontend** | 21,366 | ~5,342 | XL |
| 2 | **gsap-plugins** | 21,265 | ~5,316 | XL |
| 3 | **gsap-scrolltrigger** | 18,686 | ~4,672 | XL |
| 4 | **redesign-existing-projects** | 15,238 | ~3,810 | L（接近 XL）|
| 5 | **gsap-core** | 15,046 | ~3,762 | L（接近 XL）|
| 6 | **stitch-design-taste** | 12,043 | ~3,011 | L |
| 7 | **gsap-utils** | 12,377 | ~3,094 | L |
| 8 | **critique** | 11,374 | ~2,844 | L |
| 9 | **high-end-visual-design** | 10,659 | ~2,665 | L |
| 10 | **delight** | 10,327 | ~2,582 | L |
| 11 | **frontend-design** | 9,702 | ~2,426 | L |
| 12 | **overdrive** | 9,877 | ~2,469 | L |
| 13 | **harden** | 9,412 | ~2,353 | L |
| 14 | **onboard** | 8,576 | ~2,144 | L |
| 15 | **industrial-brutalist-ui** | 8,548 | ~2,137 | L |
| 16 | **polish** | 8,308 | ~2,077 | L |
| 17 | **optimize** | 8,053 | ~2,013 | L |
| 18 | **minimalist-ui** | 7,986 | ~1,997 | M（接近 L）|
| 19 | **animate** | 7,849 | ~1,962 | M |
| 20 | **audit** | 7,766 | ~1,942 | M |
| 21 | **arrange** | 7,528 | ~1,882 | M |
| 22 | **adapt** | 7,328 | ~1,832 | M |
| 23 | **clarify** | 6,944 | ~1,736 | M |
| 24 | **colorize** | 7,033 | ~1,758 | M |
| 25 | **bolder** | 6,860 | ~1,715 | M |
| 26 | **gsap-frameworks** | 6,741 | ~1,685 | M |
| 27 | **gsap-react** | 6,700 | ~1,675 | M |
| 28 | **distill** | 6,370 | ~1,593 | M |
| 29 | **typeset** | 5,891 | ~1,473 | M |
| 30 | **quieter** | 5,245 | ~1,311 | M |
| 31 | **fixing-motion-performance** | 5,716 | ~1,429 | M |
| 32 | **fixing-accessibility** | 4,853 | ~1,213 | M（接近 S）|
| 33 | **fixing-metadata** | 4,551 | ~1,138 | M（接近 S）|
| 34 | **gsap-timeline** | 4,501 | ~1,125 | M |
| 35 | **normalize** | 4,264 | ~1,066 | M（接近 S）|
| 36 | **gsap-performance** | 4,218 | ~1,055 | M（接近 S）|
| 37 | **extract** | 4,041 | ~1,010 | M（接近 S）|
| 38 | **baseline-ui** | 3,616 | ~904 | S |
| 39 | **better-icons** | 3,713 | ~928 | S |
| 40 | **teach-impeccable** | 2,941 | ~735 | S |
| 41 | **full-output-enforcement** | 2,641 | ~660 | S |

---

## 二、按体量分级统计

### XL（>4000 tokens）— 3 个 skill

| Skill | 估算 Token | 说明 |
|-------|-----------|------|
| design-taste-frontend | ~5,342 | 包含 10 个章节 + 完整参数驱动规则体系 + Bento 范式 |
| gsap-plugins | ~5,316 | 覆盖所有 GSAP 插件（Flip/Draggable/SplitText/MorphSVG 等）+ 大量 API 表格 |
| gsap-scrolltrigger | ~4,672 | 完整 ScrollTrigger API + batch() + scrollerProxy() + 水平滚动等复杂场景 |

**XL 小计：~15,330 tokens**

### L（2000-4000 tokens）— 14 个 skill

| Skill | 估算 Token |
|-------|-----------|
| redesign-existing-projects | ~3,810 |
| gsap-core | ~3,762 |
| gsap-utils | ~3,094 |
| stitch-design-taste | ~3,011 |
| critique | ~2,844 |
| high-end-visual-design | ~2,665 |
| overdrive | ~2,469 |
| delight | ~2,582 |
| frontend-design | ~2,426 |
| harden | ~2,353 |
| onboard | ~2,144 |
| industrial-brutalist-ui | ~2,137 |
| polish | ~2,077 |
| optimize | ~2,013 |

**L 小计：~37,387 tokens**

### M（1000-2000 tokens）— 20 个 skill

| Skill | 估算 Token |
|-------|-----------|
| minimalist-ui | ~1,997 |
| animate | ~1,962 |
| audit | ~1,942 |
| arrange | ~1,882 |
| adapt | ~1,832 |
| colorize | ~1,758 |
| clarify | ~1,736 |
| bolder | ~1,715 |
| gsap-frameworks | ~1,685 |
| gsap-react | ~1,675 |
| distill | ~1,593 |
| typeset | ~1,473 |
| fixing-motion-performance | ~1,429 |
| quieter | ~1,311 |
| fixing-accessibility | ~1,213 |
| fixing-metadata | ~1,138 |
| gsap-timeline | ~1,125 |
| normalize | ~1,066 |
| gsap-performance | ~1,055 |
| extract | ~1,010 |

**M 小计：~30,625 tokens**

### S（500-1000 tokens）— 4 个 skill

| Skill | 估算 Token |
|-------|-----------|
| better-icons | ~928 |
| baseline-ui | ~904 |
| teach-impeccable | ~735 |
| full-output-enforcement | ~660 |

**S 小计：~3,227 tokens**

---

## 三、按来源包分组统计

### pbakaus/impeccable（21 个 skill）

| Skill | 估算 Token | 级别 |
|-------|-----------|------|
| frontend-design | ~2,426 | L |
| critique | ~2,844 | L |
| delight | ~2,582 | L |
| overdrive | ~2,469 | L |
| harden | ~2,353 | L |
| onboard | ~2,144 | L |
| polish | ~2,077 | L |
| optimize | ~2,013 | L |
| animate | ~1,962 | M |
| audit | ~1,942 | M |
| arrange | ~1,882 | M |
| adapt | ~1,832 | M |
| colorize | ~1,758 | M |
| clarify | ~1,736 | M |
| bolder | ~1,715 | M |
| distill | ~1,593 | M |
| typeset | ~1,473 | M |
| quieter | ~1,311 | M |
| normalize | ~1,066 | M |
| extract | ~1,010 | M |
| teach-impeccable | ~735 | S |

**pbakaus/impeccable 总计：~38,924 tokens**
**平均：~1,854 tokens/skill**

---

### leonxlnx/taste-skill（8 个 skill）

| Skill | 估算 Token | 级别 |
|-------|-----------|------|
| design-taste-frontend | ~5,342 | XL |
| redesign-existing-projects | ~3,810 | L |
| stitch-design-taste | ~3,011 | L |
| high-end-visual-design | ~2,665 | L |
| industrial-brutalist-ui | ~2,137 | L |
| minimalist-ui | ~1,997 | M |
| baseline-ui | ~904 | S |
| full-output-enforcement | ~660 | S |

**leonxlnx/taste-skill 总计：~20,526 tokens**
**平均：~2,566 tokens/skill**

---

### greensock/gsap-skills（8 个 skill）

| Skill | 估算 Token | 级别 |
|-------|-----------|------|
| gsap-plugins | ~5,316 | XL |
| gsap-scrolltrigger | ~4,672 | XL |
| gsap-core | ~3,762 | L |
| gsap-utils | ~3,094 | L |
| gsap-timeline | ~1,125 | M |
| gsap-frameworks | ~1,685 | M |
| gsap-react | ~1,675 | M |
| gsap-performance | ~1,055 | M |

**greensock/gsap-skills 总计：~22,384 tokens**
**平均：~2,798 tokens/skill**

---

### ibelick/ui-skills（3 个 skill）

| Skill | 估算 Token | 级别 |
|-------|-----------|------|
| fixing-motion-performance | ~1,429 | M |
| fixing-accessibility | ~1,213 | M |
| fixing-metadata | ~1,138 | M |

**ibelick/ui-skills 总计：~3,780 tokens**
**平均：~1,260 tokens/skill**

---

### better-auth/better-icons（1 个 skill）

| Skill | 估算 Token | 级别 |
|-------|-----------|------|
| better-icons | ~928 | S |

**better-icons 总计：~928 tokens**

---

## 四、全量加载 Token 成本汇总

| 来源包 | Skill 数量 | 总 Token | 占比 |
|--------|-----------|---------|------|
| pbakaus/impeccable | 21 | ~38,924 | 45.0% |
| greensock/gsap-skills | 8 | ~22,384 | 25.9% |
| leonxlnx/taste-skill | 8 | ~20,526 | 23.8% |
| ibelick/ui-skills | 3 | ~3,780 | 4.4% |
| better-auth/better-icons | 1 | ~928 | 1.1% |
| **全部 41 个 skill** | **41** | **~86,542** | **100%** |

> 将所有 41 个 skill 同时加载到上下文中的估算 token 成本约为 **86,500 tokens**（~86.5K）。
>
> 这相当于约 65,000 个英文单词，或一本 200 页书籍的内容量。

---

## 五、按使用场景推荐的 skill 子集

### 最小设计 skill 集（日常 UI 开发）
推荐加载以下 skill，总 token 约 **6,000 tokens**：

| Skill | Token | 用途 |
|-------|-------|------|
| frontend-design | ~2,426 | 设计原则基础 |
| baseline-ui | ~904 | 技术约束规范 |
| fixing-accessibility | ~1,213 | 可访问性检查 |
| full-output-enforcement | ~660 | 输出完整性保障 |
| teach-impeccable | ~735 | 项目上下文收集（一次性） |

### 完整设计流程集（设计重构/新项目）
推荐加载 pbakaus/impeccable 全集 + fixing-* 三件套，总 token 约 **42,700 tokens**。

### GSAP 动画开发集
推荐加载 gsap-core + gsap-timeline + 具体框架 skill（gsap-react 或 gsap-frameworks）+ gsap-scrolltrigger（如需滚动动画），总 token 约 **8,600-12,700 tokens**。

### 快速项目美化集（针对现有项目）
推荐加载 redesign-existing-projects + typeset + colorize + arrange，总 token 约 **9,060 tokens**。

---

## 六、Token 预算注意事项

1. **XL 级 skill 的加载代价**：`design-taste-frontend`（~5.3K）、`gsap-plugins`（~5.3K）、`gsap-scrolltrigger`（~4.7K）单个 skill 就消耗大量上下文。在 token 预算有限时，可按需加载而非全量加载。

2. **S 级 skill 可常驻**：`full-output-enforcement`、`teach-impeccable`、`baseline-ui`、`better-icons` 总计仅 ~3,200 tokens，可以作为常驻规则。

3. **GSAP skill 族的模块化设计**：8 个 GSAP skill 总计 ~22,400 tokens，但每个 skill 独立工作——可以只加载需要的子集（例如：仅做 React 动画只需 gsap-core + gsap-react + gsap-timeline，约 6,500 tokens）。

4. **设计风格 skill 的互斥性**：`industrial-brutalist-ui`、`minimalist-ui`、`high-end-visual-design` 三者定义互斥的审美方向，每次只需加载一个，节省 ~4,000-5,000 tokens。
