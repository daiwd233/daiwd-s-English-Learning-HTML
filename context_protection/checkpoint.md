# Session Checkpoint

## 文件结构
- `index.html` — 主页面（~66KB, 1760行）
- `cet4_words.js` — CET-4 词库 (7508 词), 变量 `WORDS_DATA_CET4`
- `cet6_words.js` — CET-6 词库 (3991 词), 变量 `WORDS_DATA_CET6`
- `ky_words.js` — 考研英语词库 (9602 词), 变量 `WORDS_DATA_KY`
- `chengyu_words.js` — 高频成语词库 (577 条), 变量 `WORDS_DATA_CY`
- `高频成语.xlsx` — 成语数据源 (589行, 6列)
- `user/pat.txt` — GitHub PAT 令牌
- `.gitignore` — 忽略 user/ 等目录
- `context_protection/checkpoint.md` — 本文件
- `debug.txt` — 操作记录
- `CHANGELOG.txt` — 功能差异

## 模块切换架构
- `MODULES` 对象: `{ cet4, cet6, ky, cy }` 含 `name / label / key`
- `loadVocab(mod)` — 用 `typeof` 守卫安全加载词库变量
- `getDailyCount(mod)` — 返回每日学习数量（cy=30，其他=100）
- `WORDS_PER_DAY()` — 动态函数，根据 currentModule 返回数量
- `currentModule` — 当前模块 id, `loadModulePref()` / `saveModulePref()` 持久化
- `switchModule(mod)` — 切换模块，saveState → 换 currentModule → loadVocab → 重置 state → loadState → refreshAll
- localStorage keys: `eng_learn_cet4 / cet6 / ky / cy` + `eng_learn_module` + `eng_learn_welcomed`

## 已完成功能
- 模块切换（CET-4 / CET-6 / 考研英语 / 高频成语），每个模块独立 localStorage 进度
- CET-4 词库 7508 词，考研词库 9602 词（genkin-he/english-vocabulary 数据源）
- 高频成语词库 577 条（来自 高频成语.xlsx，6字段：词语/词性/解释/例子/近义/反义）
- 成语模块：每日 30 条，富详情弹窗（展示全部6字段），卡片显示截断释义
- 成语模块：搜索支持例子/近义词/反义词匹配，闪卡复习显示例句
- 成语模块：隐藏发音按钮（成语无英文发音）
- Web Speech API 发音：每个单词 🔊 按钮，全部朗读（可暂停）
- 首次访问欢迎弹窗（手动关闭）
- 往期复习：学习记录每个日期可点击"🔄 复习"进入闪卡模式
- 页面底部开源地址链接
- 已推送到 GitHub（最新 commit `c5fa104`）

## 推送方式
- PAT 保存在 `user/pat.txt`，推送时自动读取
- `git clone` 到 `C:\WINDOWS\TEMP\opencode\repo`，复制文件后 commit & push
- **注意**: 当前环境未安装 git，需手动推送

## 待处理/已知问题
- CET-6 词库（3991 词）可从 genkin-he 升级到 5651 词（未做）
- 需手动 git add/commit/push 到 GitHub
