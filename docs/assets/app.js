(() => {
  "use strict";

  const REPO = "kamanager2012/ai-infra-hegemony";
  const BRANCH = "main";

  const chapters = [
    {n:1,part:1,file:"part-I-ch01-executive-summary.md",zh:"执行摘要与未来十年核心判断",en:"Executive Summary and Core Judgments for the Next Decade"},
    {n:2,part:1,file:"part-I-ch02-nvidia-system-stack.md",zh:"NVIDIA 系统栈与平台权力",en:"NVIDIA's System Stack and Platform Power"},
    {n:3,part:1,file:"part-I-ch03-resource-gravity.md",zh:"AI Resource Gravity 与 Non-AI Residual Capacity",en:"AI Resource Gravity and Non-AI Residual Capacity"},
    {n:4,part:1,file:"part-I-ch04-tsmc-advanced-logic.md",zh:"TSMC、N2 与先进制造资源分配",en:"TSMC, N2, and Advanced-Manufacturing Resource Allocation"},
    {n:5,part:1,file:"part-I-ch05-hbm-memory.md",zh:"HBM 与存储资源重构",en:"HBM and the Restructuring of Memory Resources"},
    {n:6,part:1,file:"part-I-ch06-advanced-packaging.md",zh:"Advanced Packaging、CoWoS 与系统交付瓶颈",en:"Advanced Packaging, CoWoS, and the System-Delivery Bottleneck"},
    {n:7,part:1,file:"part-I-ch07-power-constraint.md",zh:"从 120 kW Rack 到 GW 级电力约束",en:"From 120 kW Racks to GW-Scale Power Constraints"},
    {n:8,part:1,file:"part-I-ch08-quantitative-framework.md",zh:"AI 基础设施量化框架与 Rolling Bottleneck Cascade",en:"Quantitative Framework for AI Infrastructure and the Rolling Bottleneck Cascade"},
    {n:9,part:1,file:"part-I-ch09-semiconductor-redundancy.md",zh:"全球半导体供应链与制造冗余",en:"Global Semiconductor Supply Chains and Manufacturing Redundancy"},
    {n:10,part:2,file:"part-II-ch10-model-economics.md",zh:"模型单位经济、算法效率与开源竞争",en:"Model Unit Economics, Algorithmic Efficiency, and Open-Source Competition"},
    {n:11,part:2,file:"part-II-ch11-nvidia-ai-factory.md",zh:"NVIDIA 从 Accelerator Vendor 向 AI Factory 扩张",en:"NVIDIA's Expansion from Accelerator Vendor to AI Factory"},
    {n:12,part:2,file:"part-II-ch12-hyperscaler-system-stack.md",zh:"Hyperscaler System-Stack Competition",en:"Hyperscaler System-Stack Competition"},
    {n:13,part:2,file:"part-II-ch13-anchor-compute-buyer.md",zh:"Anchor Compute Buyer Effect——模型公司如何重塑基础设施",en:"Anchor Compute Buyer Effect — How Model Companies Reshape Infrastructure"},
    {n:14,part:2,file:"part-II-ch14-agent-software.md",zh:"Agent-Native Software 与 AI Software Unit Economics",en:"Agent-Native Software and AI Software Unit Economics"},
    {n:15,part:2,file:"part-II-ch15-physical-ai.md",zh:"Physical AI 与机器人系统的真正瓶颈",en:"Physical AI and the Real Bottlenecks in Robotics"},
    {n:16,part:2,file:"part-II-ch16-differentiated-competitors.md",zh:"AMD、Intel、Qualcomm 与 Apple 的差异化竞争路径",en:"AMD, Intel, Qualcomm, and Apple — Differentiated Competitive Paths"},
    {n:17,part:2,file:"part-II-ch17-china-parallel-stack.md",zh:"中国 Parallel Stack：从 Production-Grade Substitution 到 Autonomous Frontier Closure",en:"China's Parallel Stack — From Production-Grade Substitution to Autonomous Frontier Closure"},
    {n:18,part:2,file:"part-II-ch18-antitrust-policy.md",zh:"反垄断、产业政策与 AI 平台权力边界",en:"Antitrust, Industrial Policy, and the Boundaries of AI Platform Power"},
    {n:19,part:3,file:"part-III-ch19-capex-supercycle.md",zh:"AI 基础设施 CapEx 超级周期",en:"The AI-Infrastructure CapEx Supercycle"},
    {n:20,part:3,file:"part-III-ch20-value-capture-map.md",zh:"Value Capture Map——资金流、利润池与风险承担",en:"Value Capture Map — Capital Flows, Profit Pools, and Risk Bearing"},
    {n:21,part:3,file:"part-III-ch21-consumer-transmission.md",zh:"消费电子、整机工业与实体经济的成本传导",en:"Cost Transmission into Consumer Electronics, End Systems, and the Real Economy"},
    {n:22,part:3,file:"part-III-ch22-depreciation-wall.md",zh:"折旧墙与 Duration Mismatch",en:"The Depreciation Wall and Duration Mismatch"},
    {n:23,part:3,file:"part-III-ch23-capital-financing.md",zh:"AI 基础设施资本市场与融资结构",en:"AI-Infrastructure Capital Markets and Financing Structure"},
    {n:24,part:3,file:"part-III-ch24-capital-clearing.md",zh:"泡沫识别、资本清算与 S4",en:"Bubble Identification, Capital Clearing, and S4"},
    {n:25,part:3,file:"part-III-ch25-labor-market.md",zh:"AI 与劳动市场——Task-to-Job Translation",en:"AI and Labor Markets — The Task-to-Job Translation Layer"},
    {n:26,part:3,file:"part-III-ch26-education-talent.md",zh:"AI 时代教育与人才体系",en:"Education and Talent Systems in the AI Era"},
    {n:27,part:4,file:"part-IV-ch27-research-method.md",zh:"研究方法与证据架构",en:"Research Method and Evidence Architecture"},
    {n:28,part:4,file:"part-IV-ch28-timeline-2026-2036.md",zh:"2026–2036 时间线与阶段性里程碑",en:"2026–2036 Timeline and Conditional Milestones"},
    {n:29,part:4,file:"part-IV-ch29-monitoring-framework.md",zh:"核心指标与证据监测框架",en:"Core Metrics and Evidence-Monitoring Framework"},
    {n:30,part:4,file:"part-IV-ch30-scenarios.md",zh:"S1–S4 四类标准情景",en:"The Four Standard Scenarios — S1 to S4"},
    {n:31,part:4,file:"part-IV-ch31-strategy-endgame.md",zh:"2036 终局与战略选择",en:"The 2036 Endgame and Strategic Optionality"},
    {n:32,part:4,file:"part-IV-ch32-master-judgment.md",zh:"总判——从事实、机制到可证伪的长期判断",en:"Master Judgment — The Industrial End-State of AI Infrastructure and the Conditions That Would Falsify It"}
  ];

  const partNames = {
    zh:["","Part I — 系统权力与物理稀缺","Part II — 需求、替代与第二系统栈","Part III — 资本周期、利润池与外部传导","Part IV — 方法、情景、监测与战略"],
    en:["","Part I — System Power and Physical Scarcity","Part II — Demand, Substitution, and the Second System Stack","Part III — Capital Cycles, Profit Pools, and External Transmission","Part IV — Method, Scenarios, Monitoring, and Strategy"]
  };

  const copy = {
    zh:{
      heroTitle:"AI基础设施霸权时代",
      heroSubtitle:"全球算力、半导体、存储、先进封装、电力与资本配置的结构性重构",
      heroSummary:"一份以事实、机制、情景与可证伪标准为核心的长期行业研究报告。研究 AI 从单颗 accelerator 竞争上移到完整 system stack 后，如何改变上游资源配置、资本形成、传统终端与未来十年的产业结构。",
      start:"开始阅读",master:"直接看总判",print:"打印 / 保存 PDF",
      indexTitle:"32 章正式版",indexNote:"推荐先读 Ch01 → Ch32 → Ch30，再按主题进入完整章节。",
      back:"报告首页",copyLink:"复制章节链接",copied:"已复制",printChapter:"打印本章",
      prev:"上一章",next:"下一章",
      thesis:[
        ["竞争单元已经上移","竞争不再只发生在 accelerator，而是 advanced logic、HBM、advanced packaging、interconnect、runtime、rack、power、capital 与 workload 的完整系统栈。"],
        ["供给增长不等于传统产业获得更多资源","报告用 Non-AI Residual Capacity 描述 AI/HPC 对共享或相邻上游资源优先级的结构性重排。"],
        ["物理瓶颈会滚动迁移","先进制程、HBM、CoWoS、互联、电力、LPS 与资本并非单点约束，而是 Rolling Bottleneck Cascade。"],
        ["长期判断必须可证伪","事实、假设、机制、情景与 falsification 分层处理；未来判断可以大胆，但证据身份、分母和触发条件必须明确。"]
      ]
    },
    en:{
      heroTitle:"The Age of AI Infrastructure Hegemony",
      heroSubtitle:"Structural Reallocation of Compute, Semiconductors, Memory, Advanced Packaging, Power, and Capital",
      heroSummary:"A long-form industry research report built around facts, mechanisms, scenarios, and falsification criteria. It examines how the shift from individual accelerators to complete system stacks changes upstream resource allocation, capital formation, traditional end markets, and the industrial structure of the next decade.",
      start:"Read the report",master:"Go to Master Judgment",print:"Print / Save PDF",
      indexTitle:"Formal 32-Chapter Edition",indexNote:"For the fastest path, read Ch01 → Ch32 → Ch30, then enter the full report by topic.",
      back:"Report home",copyLink:"Copy chapter link",copied:"Copied",printChapter:"Print chapter",
      prev:"Previous",next:"Next",
      thesis:[
        ["The competitive unit has moved upward","Competition now spans advanced logic, HBM, advanced packaging, interconnect, runtime, rack architecture, power, capital, and workload — not the accelerator alone."],
        ["More total supply does not guarantee more residual supply","Non-AI Residual Capacity tracks how AI/HPC can reprioritize shared or adjacent upstream resources even while total capacity expands."],
        ["Physical bottlenecks migrate","Advanced logic, HBM, CoWoS, interconnect, power, LPS, and capital form a Rolling Bottleneck Cascade rather than a single permanent constraint."],
        ["Long-run judgments must be falsifiable","Facts, hypotheses, mechanisms, scenarios, and falsification are separated so that bold forecasts still have explicit evidence identity, denominators, and reversal conditions."]
      ]
    }
  };

  const $ = (id) => document.getElementById(id);
  const params = new URLSearchParams(location.search);
  let lang = params.get("lang") === "en" ? "en" : "zh";
  const chapterNo = Math.min(32, Math.max(1, Number(params.get("chapter") || 0)));
  const printMode = params.get("print") === "1";

  function chapterUrl(n, language = lang) {
    return "?lang=" + language + "&chapter=" + n;
  }

  function printUrl(language = lang) {
    return "?lang=" + language + "&print=1";
  }

  const bundleCache = new Map();
  const publicDocuments = new Set([
    "00-front-matter.md",
    "02-list-of-tables.md",
    "03-abbreviations-and-glossary.md",
    "04-research-transparency.md",
    "05-competitive-evidence-matrix.md",
    "核心证据台账.md",
    "核心参考文献索引.md",
    "核心概念与模型索引.md",
    "核心假设矩阵.md",
    "外部研究对照索引.md"
  ]);

  async function fetchJson(url) {
    if (!bundleCache.has(url)) {
      bundleCache.set(url, fetch(url, {cache:"no-store"}).then(res => {
        if (!res.ok) throw new Error("HTTP " + res.status + " for " + url);
        return res.json();
      }));
    }
    return bundleCache.get(url);
  }

  async function fetchChapter(language, chapter) {
    const bundle = await fetchJson("./content/" + language + "/part-" + chapter.part + ".json");
    const md = bundle && bundle.chapters && bundle.chapters[String(chapter.n)];
    if (typeof md !== "string") throw new Error("Chapter missing from public snapshot.");
    return md;
  }

  async function fetchDocument(language, key) {
    const normalized = normalizeDocumentKey(key);
    const files = ["appendices-publication.json", "appendices-research.json"];
    for (const file of files) {
      const bundle = await fetchJson("./content/" + language + "/" + file);
      if (bundle && bundle.documents && typeof bundle.documents[normalized] === "string") {
        return bundle.documents[normalized];
      }
    }
    throw new Error("Document missing from public snapshot.");
  }

  function normalizeDocumentKey(value) {
    return decodeURIComponent(String(value || ""))
      .split("#")[0]
      .replace(/^\.\//, "")
      .replace(/^\.\.\//, "")
      .replace(/\.en\.md$/i, ".md");
  }

  function documentUrl(key, language = lang) {
    return "?lang=" + language + "&doc=" + encodeURIComponent(normalizeDocumentKey(key));
  }

  function renderMarkdown(md) {
    if (!window.marked || !window.DOMPurify) {
      throw new Error("Markdown renderer failed to load.");
    }
    marked.setOptions({gfm:true, breaks:false});
    return DOMPurify.sanitize(marked.parse(md), {ADD_ATTR:["target","rel"]});
  }

  function rewriteLinks(container, language) {
    const fileMap = new Map(chapters.map(c => [c.file, c]));
    container.querySelectorAll("a[href]").forEach(a => {
      const href = a.getAttribute("href");
      if (!href) return;
      if (/^https?:\/\//i.test(href)) {
        a.target = "_blank";
        a.rel = "noreferrer";
        return;
      }
      if (href.startsWith("#") || href.startsWith("mailto:")) return;

      const fragment = href.includes("#") ? "#" + href.split("#").slice(1).join("#") : "";
      const clean = href.split("#")[0].replace(/^\.\//, "");
      if (fileMap.has(clean)) {
        const chapter = fileMap.get(clean);
        a.href = chapterUrl(chapter.n, language) + fragment;
        return;
      }

      const docKey = normalizeDocumentKey(clean);
      if (publicDocuments.has(docKey)) {
        a.href = documentUrl(docKey, language) + fragment;
        return;
      }

      if (clean.endsWith(".md")) {
        a.removeAttribute("href");
        a.removeAttribute("target");
        a.removeAttribute("rel");
        a.title = language === "en"
          ? "This internal research file is not part of the public publication snapshot."
          : "该内部研究文件不属于公开出版快照。";
      }
    });
  }

  function setLanguageUI() {
    const t = copy[lang];
    document.documentElement.lang = lang === "en" ? "en" : "zh-CN";
    $("langToggle").textContent = lang === "zh" ? "EN" : "中文";
    $("readerLangToggle").textContent = lang === "zh" ? "EN" : "中文";

    $("heroTitle").textContent = t.heroTitle;
    $("heroSubtitle").textContent = t.heroSubtitle;
    $("heroSummary").textContent = t.heroSummary;
    $("startReading").textContent = t.start;
    $("startReading").href = chapterUrl(1);
    $("masterJudgment").textContent = t.master;
    $("masterJudgment").href = chapterUrl(32);
    $("printReport").textContent = t.print;
    $("printReport").href = printUrl();
    $("indexTitle").textContent = t.indexTitle;
    $("indexNote").textContent = t.indexNote;
    $("backHome").querySelector("span").textContent = t.back;
    $("copyLink").textContent = t.copyLink;
    $("printChapter").textContent = t.printChapter;
    $("printTitle").textContent = t.heroTitle;
    $("printSubtitle").textContent = t.heroSubtitle;

    document.querySelectorAll(".thesis-grid article").forEach((card, i) => {
      card.querySelector("h2").textContent = t.thesis[i][0];
      card.querySelector("p").textContent = t.thesis[i][1];
    });
  }

  function buildChapterIndex(target, compact = false) {
    target.innerHTML = "";
    for (let part = 1; part <= 4; part++) {
      const group = document.createElement("section");
      group.className = compact ? "reader-nav-group" : "part-block";

      const title = document.createElement("div");
      title.className = compact ? "reader-nav-part" : "part-title";
      title.textContent = partNames[lang][part];
      group.appendChild(title);

      const list = document.createElement("div");
      list.className = compact ? "reader-nav-list" : "chapter-list";

      chapters.filter(c => c.part === part).forEach(c => {
        const a = document.createElement("a");
        a.href = chapterUrl(c.n);
        a.className = compact ? "reader-nav-link" : "chapter-card";
        if (compact && c.n === chapterNo) a.classList.add("active");
        a.innerHTML = compact
          ? '<span>' + String(c.n).padStart(2,"0") + '</span><span>' + escapeHtml(c[lang]) + '</span>'
          : '<span class="chapter-no">CH ' + String(c.n).padStart(2,"0") + '</span><span class="chapter-name">' + escapeHtml(c[lang]) + '</span><span class="chapter-arrow">→</span>';
        list.appendChild(a);
      });

      group.appendChild(list);
      target.appendChild(group);
    }
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, ch => ({
      "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"
    })[ch]);
  }

  async function showReader(n) {
    document.body.classList.add("chapter-mode");
    $("homeView").classList.add("hidden");
    $("thesisView").classList.add("hidden");
    $("indexView").classList.add("hidden");
    $("printView").classList.add("hidden");
    $("readerView").classList.remove("hidden");

    const c = chapters[n - 1];
    $("readerPart").textContent = partNames[lang][c.part];
    $("readerChapterLabel").textContent = "CH " + String(c.n).padStart(2,"0");
    buildChapterIndex($("readerChapterList"), true);

    $("prevChapter").textContent = c.n > 1 ? "← " + copy[lang].prev + " · CH " + String(c.n - 1).padStart(2,"0") : "";
    $("prevChapter").href = c.n > 1 ? chapterUrl(c.n - 1) : "#";
    $("nextChapter").textContent = c.n < 32 ? copy[lang].next + " · CH " + String(c.n + 1).padStart(2,"0") + " →" : "";
    $("nextChapter").href = c.n < 32 ? chapterUrl(c.n + 1) : "#";

    $("readerBody").innerHTML = '<div class="loading">Loading report…</div>';
    try {
      const md = await fetchChapter(lang, c);
      $("readerBody").innerHTML = renderMarkdown(md);
      rewriteLinks($("readerBody"), lang);
      document.title = "CH " + String(c.n).padStart(2,"0") + " — " + c[lang] + " | AI Infrastructure Hegemony";
    } catch (err) {
      $("readerBody").innerHTML =
        '<h1>' + escapeHtml(c[lang]) + '</h1>' +
        '<p>' + (lang === "en"
          ? "This chapter is unavailable in the current public snapshot."
          : "本章当前未包含在公开出版快照中。") + '</p>';
    }
  }

  async function showDocument(key) {
    document.body.classList.add("chapter-mode");
    $("homeView").classList.add("hidden");
    $("thesisView").classList.add("hidden");
    $("indexView").classList.add("hidden");
    $("printView").classList.add("hidden");
    $("readerView").classList.remove("hidden");

    const normalized = normalizeDocumentKey(key);
    $("readerPart").textContent = lang === "en" ? "PUBLIC RESEARCH APPENDIX" : "公开研究附录";
    $("readerChapterLabel").textContent = normalized.replace(/\.md$/i, "");
    buildChapterIndex($("readerChapterList"), true);
    $("prevChapter").textContent = "";
    $("nextChapter").textContent = "";
    $("readerBody").innerHTML = '<div class="loading">Loading document…</div>';

    try {
      const md = await fetchDocument(lang, normalized);
      $("readerBody").innerHTML = renderMarkdown(md);
      rewriteLinks($("readerBody"), lang);
      document.title = normalized.replace(/\.md$/i, "") + " | AI Infrastructure Hegemony";
    } catch (err) {
      $("readerBody").innerHTML =
        '<h1>' + escapeHtml(normalized.replace(/\.md$/i, "")) + '</h1>' +
        '<p>' + (lang === "en"
          ? "This document is not included in the public publication snapshot."
          : "该文档未包含在公开出版快照中。") + '</p>';
    }
  }

  async function showPrintEdition() {
    document.body.classList.remove("chapter-mode");
    $("homeView").classList.add("hidden");
    $("thesisView").classList.add("hidden");
    $("indexView").classList.add("hidden");
    $("readerView").classList.add("hidden");
    $("printView").classList.remove("hidden");
    $("printBody").innerHTML = '<div class="loading">Preparing 32 chapters for print…</div>';

    const sections = [];
    for (const c of chapters) {
      try {
        const md = await fetchChapter(lang, c);
        const wrap = document.createElement("section");
        wrap.className = "print-chapter";
        wrap.dataset.chapter = String(c.n);
        wrap.innerHTML = renderMarkdown(md);
        rewriteLinks(wrap, lang);
        sections.push(wrap.outerHTML);
      } catch (err) {
        sections.push(
          '<section class="print-chapter"><h1>CH ' + String(c.n).padStart(2,"0") + ' — ' + escapeHtml(c[lang]) + '</h1>' +
          '<p>' + (lang === "en" ? "Chapter unavailable in the public snapshot." : "本章未包含在公开出版快照中。") + '</p></section>'
        );
      }
    }
    $("printBody").innerHTML = sections.join("\n");
    document.title = (lang === "en" ? "The Age of AI Infrastructure Hegemony" : "AI基础设施霸权时代") + " — 2026 Edition";
  }

  function toggleLanguage() {
    const next = lang === "zh" ? "en" : "zh";
    const q = new URLSearchParams(location.search);
    q.set("lang", next);
    if (!q.has("chapter") && !q.has("print")) q.delete("chapter");
    location.search = q.toString();
  }

  function bindActions() {
    $("langToggle").addEventListener("click", toggleLanguage);
    $("readerLangToggle").addEventListener("click", toggleLanguage);
    $("copyLink").addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(location.href);
        const old = $("copyLink").textContent;
        $("copyLink").textContent = copy[lang].copied;
        setTimeout(() => $("copyLink").textContent = old, 1300);
      } catch {
        prompt("Copy link:", location.href);
      }
    });
    $("printChapter").addEventListener("click", () => window.print());
  }

  async function init() {
    setLanguageUI();
    buildChapterIndex($("chapterIndex"), false);
    bindActions();

    if (printMode) {
      await showPrintEdition();
      return;
    }
    if (params.has("chapter")) {
      await showReader(chapterNo);
      return;
    }
    if (params.has("doc")) {
      await showDocument(params.get("doc"));
      return;
    }

    document.body.classList.remove("chapter-mode");
    $("readerView").classList.add("hidden");
    $("printView").classList.add("hidden");
    document.title = (lang === "en" ? "The Age of AI Infrastructure Hegemony" : "AI基础设施霸权时代") + " — 2026 Research Report";
  }

  init();
})();