(() => {
  "use strict";

  const REPO = "kamanager2012/ai-infra-hegemony";
  const BRANCH = "main";

  // Navigation labels intentionally mirror the canonical Table of Contents.
  const chapters = [
    {n:1,part:1,file:"part-I-ch01-executive-summary.md",zh:"执行摘要",en:"Executive Summary"},
    {n:2,part:1,file:"part-I-ch02-nvidia-system-stack.md",zh:"NVIDIA 系统栈与平台权力",en:"NVIDIA's System Stack and Platform Power"},
    {n:3,part:1,file:"part-I-ch03-resource-gravity.md",zh:"AI 资源重配与 Non-AI Residual Capacity",en:"AI Resource Reallocation and Non-AI Residual Capacity"},
    {n:4,part:1,file:"part-I-ch04-tsmc-advanced-logic.md",zh:"Advanced Logic Allocation——TSMC、N2 与下一单位 Qualified Capacity",en:"Advanced Logic Allocation — TSMC, N2, and the Next Unit of Qualified Capacity"},
    {n:5,part:1,file:"part-I-ch05-hbm-memory.md",zh:"HBM Economics——Manufacturing Intensity、Residual Capacity 与 Memory Scarcity",en:"HBM Economics — Manufacturing Intensity, Residual Capacity, and Memory Scarcity"},
    {n:6,part:1,file:"part-I-ch06-advanced-packaging.md",zh:"Advanced Packaging——Wafer 与 Deliverable System 之间的 Quantity Gate",en:"Advanced Packaging — The Quantity Gate Between Wafers and Deliverable Systems"},
    {n:7,part:1,file:"part-I-ch07-power-constraint.md",zh:"Time-to-Power——从 Rack Density 到 Deployable AI Capacity",en:"Time-to-Power — From Rack Density to Deployable AI Capacity"},
    {n:8,part:1,file:"part-I-ch08-quantitative-framework.md",zh:"Quantitative Framework——Denominator Closure、Stress Test 与 Public-Data Limits",en:"Quantitative Framework — Denominator Closure, Stress Tests, and Public-Data Limits"},
    {n:9,part:1,file:"part-I-ch09-semiconductor-redundancy.md",zh:"全球半导体供应链与制造冗余",en:"Global Semiconductor Supply Chains and Manufacturing Redundancy"},
    {n:10,part:2,file:"part-II-ch10-model-economics.md",zh:"模型单位经济、算法效率与开源竞争",en:"Model Unit Economics, Algorithmic Efficiency, and Open-Source Competition"},
    {n:11,part:2,file:"part-II-ch11-nvidia-ai-factory.md",zh:"NVIDIA 从 Accelerator Vendor 向 AI Factory 扩张",en:"NVIDIA's Expansion from Accelerator Vendor to AI Factory"},
    {n:12,part:2,file:"part-II-ch12-hyperscaler-system-stack.md",zh:"第二类 System Stack——Hyperscaler Substitution 如何真正成立",en:"The Second System Stack — How Hyperscaler Substitution Actually Works"},
    {n:13,part:2,file:"part-II-ch13-anchor-compute-buyer.md",zh:"Anchor Compute Buyers——Long-Duration Demand 如何提前拉动 Infrastructure",en:"Anchor Compute Buyers — How Long-Duration Demand Pulls Infrastructure Forward"},
    {n:14,part:2,file:"part-II-ch14-agent-software.md",zh:"Agent-Native Software 与 AI Software Unit Economics",en:"Agent-Native Software and AI Software Unit Economics"},
    {n:15,part:2,file:"part-II-ch15-physical-ai.md",zh:"Physical AI 与机器人系统的真正瓶颈",en:"Physical AI and the Real Bottlenecks in Robotics"},
    {n:16,part:2,file:"part-II-ch16-differentiated-competitors.md",zh:"AMD、Intel、Qualcomm 与 Apple 的差异化竞争路径",en:"AMD, Intel, Qualcomm, and Apple — Differentiated Competitive Paths"},
    {n:17,part:2,file:"part-II-ch17-china-parallel-stack.md",zh:"中国 Parallel Stack：Production-Grade Substitution 与 Autonomous Frontier Closure",en:"China's Parallel Stack — Production-Grade Substitution vs. Autonomous Frontier Closure"},
    {n:18,part:2,file:"part-II-ch18-antitrust-policy.md",zh:"反垄断、产业政策与 AI 平台权力边界",en:"Antitrust, Industrial Policy, and the Boundaries of AI Platform Power"},
    {n:19,part:3,file:"part-III-ch19-capex-supercycle.md",zh:"AI Infrastructure Capital Formation——Duration Mismatch、Utilization 与 Demand Duration",en:"AI Infrastructure Capital Formation — Duration Mismatch, Utilization, and Demand Duration"},
    {n:20,part:3,file:"part-III-ch20-value-capture-map.md",zh:"AI Infrastructure Stack 的 Value Capture 与 Risk Bearing",en:"Value Capture and Risk Bearing Across the AI Infrastructure Stack"},
    {n:21,part:3,file:"part-III-ch21-consumer-transmission.md",zh:"AI 如何重定价消费电子与其他终端系统",en:"How AI Reprices Consumer Electronics and Other End Systems"},
    {n:22,part:3,file:"part-III-ch22-depreciation-wall.md",zh:"折旧墙与 Duration Mismatch",en:"The Depreciation Wall and Duration Mismatch"},
    {n:23,part:3,file:"part-III-ch23-capital-financing.md",zh:"AI 基础设施资本市场与融资结构",en:"AI-Infrastructure Capital Markets and Financing Structure"},
    {n:24,part:3,file:"part-III-ch24-capital-clearing.md",zh:"Capital Clearing——Lead Indicators、Demand Quality 与 S4 Test",en:"Capital Clearing — Lead Indicators, Demand Quality, and the S4 Test"},
    {n:25,part:3,file:"part-III-ch25-labor-market.md",zh:"AI 与劳动市场——Task-to-Job Translation",en:"AI and Labor Markets — The Task-to-Job Translation Layer"},
    {n:26,part:3,file:"part-III-ch26-education-talent.md",zh:"AI 时代教育与人才体系",en:"Education and Talent Systems in the AI Era"},
    {n:27,part:4,file:"part-IV-ch27-research-method.md",zh:"研究方法与证据架构",en:"Research Method and Evidence Architecture"},
    {n:28,part:4,file:"part-IV-ch28-timeline-2026-2036.md",zh:"2026–2036 时间线与阶段性里程碑",en:"2026–2036 Timeline and Conditional Milestones"},
    {n:29,part:4,file:"part-IV-ch29-monitoring-framework.md",zh:"Monitoring Framework——State Variables、Inflection Tests 与 Scenario Reweighting",en:"Monitoring Framework — State Variables, Inflection Tests, and Scenario Reweighting"},
    {n:30,part:4,file:"part-IV-ch30-scenarios.md",zh:"Scenario Framework——Discriminating S1 to S4",en:"Scenario Framework — Discriminating S1 to S4"},
    {n:31,part:4,file:"part-IV-ch31-strategy-endgame.md",zh:"2036 终局与战略选择权",en:"The 2036 Endgame and Strategic Optionality"},
    {n:32,part:4,file:"part-IV-ch32-master-judgment.md",zh:"Master View——什么决定 AI 基础设施中的产业权力，什么事实会改变判断",en:"Master View — What Determines Industrial Power in AI Infrastructure, and What Would Change the View"}
  ];

  const partNames = {
    zh:["","Part I — 系统权力与物理稀缺","Part II — 需求、替代与第二系统栈","Part III — 资本周期、利润池与外部传导","Part IV — 方法、情景、监测与战略"],
    en:["","Part I — System Power and Physical Scarcity","Part II — Demand, Substitution, and the Second System Stack","Part III — Capital Cycles, Profit Pools, and External Transmission","Part IV — Method, Scenarios, Monitoring, and Strategy"]
  };

  const copy = {
    zh:{
      heroKicker:"AI 基础设施 · 半导体 · 电力 · 资本",
      heroTitle:"AI 买家正在重新定价整个系统栈",
      heroSubtitle:"2026–2036：谁能获得先进逻辑、HBM、封装与电力——以及其他产业还能获得多少剩余供给。",
      formalTitle:"AI基础设施格局重塑：2026–2036结构性产业展望",
      formalSubtitle:"AI 算力扩张如何重配半导体、存储、先进封装、电力、资本与终端产能",
      heroSummary:"核心问题不再是哪颗 accelerator 最快，而是哪套 system stack 能锁定稀缺产能、把它转化为 production workload，并在供给扩张、算法效率提升和替代栈成熟时仍维持经济性。",
      start:"从核心论点开始",master:"阅读总判",print:"打印 / 保存 PDF",
      indexTitle:"研究地图",indexNote:"可从 Ch03 残余产能、Ch12 第二系统栈、Ch17 中国平行栈或 Ch21 消费电子传导进入。",
      back:"报告首页",copyLink:"复制章节链接",copied:"已复制",printChapter:"打印本章",
      prev:"上一章",next:"下一章",
      thesis:[
        ["系统栈，而不是芯片战争","竞争单位是 advanced logic + HBM + packaging + interconnect + runtime + rack + power + capital + workload，而不是单颗 accelerator。"],
        ["总供给增加，其他产业仍可能拿得更少","Non-AI Residual Capacity 关注 priority demand 分配之后，手机、PC、汽车和工业系统实际还能获得多少有效供给。"],
        ["瓶颈会迁移，也会反转","HBM、packaging、networking、power 与 capital 可以依次成为 binding constraint；某一层的短缺之后也可能反转为 headroom 或 oversupply。"],
        ["核心判断必须经受替代路线检验","Hyperscaler custom stack、中国 parallel stack、供给扩张、algorithmic efficiency 与 capital clearing 都是能够削弱当前 baseline 的明确路径。"]
      ]
    },
    en:{
      heroKicker:"AI INFRASTRUCTURE · SEMICONDUCTORS · POWER · CAPITAL",
      heroTitle:"AI Buyers Are Repricing the Stack",
      heroSubtitle:"A 2026–2036 framework for who gets advanced logic, HBM, packaging, power — and what is left for everyone else.",
      formalTitle:"AI Infrastructure Reordering, 2026–2036: A Structural Industry Outlook",
      formalSubtitle:"How the AI Compute Buildout Is Reallocating Semiconductors, Memory, Advanced Packaging, Power, Capital, and End-Market Capacity",
      heroSummary:"The core question is no longer which accelerator is fastest. It is which system stacks can secure scarce capacity, turn it into production workloads, and keep the economics working as supply expands, algorithms improve, and alternative stacks mature.",
      start:"Start with the thesis",master:"Read the master judgment",print:"Print / Save PDF",
      indexTitle:"Research map",indexNote:"Start with Ch03 Residual Capacity, Ch12 the Second System Stack, Ch17 China Parallel Stack, or Ch21 Consumer Transmission.",
      back:"Report home",copyLink:"Copy chapter link",copied:"Copied",printChapter:"Print chapter",
      prev:"Previous",next:"Next",
      thesis:[
        ["System stack, not a chip war","The competitive unit is advanced logic + HBM + packaging + interconnect + runtime + rack + power + capital + workload — not the accelerator alone."],
        ["More supply can still mean less for everyone else","Non-AI Residual Capacity asks what phones, PCs, vehicles, and industrial systems can actually obtain after priority demand is allocated."],
        ["Bottlenecks move — and can reverse","HBM, packaging, networking, power, and capital can become binding in sequence; a shortage at one layer can later flip into headroom or oversupply."],
        ["The thesis has to survive substitution","Hyperscaler custom stacks, China’s parallel stack, supply expansion, algorithmic efficiency, and capital clearing are explicit paths that can weaken the baseline."]
      ]
    }
  };

  const $ = (id) => document.getElementById(id);
  const params = new URLSearchParams(location.search);
  let lang = params.get("lang") === "zh" ? "zh" : "en";
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
    "01-table-of-contents.md",
    "01-list-of-figures.md",
    "02-list-of-tables.md",
    "RESEARCH_BRIEF.md",
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
      .replace(/^en\/publication\//, "")
      .replace(/^publication\//, "")
      .replace(/^en\//, "")
      .replace(/\.en\.md$/i, ".md");
  }

  function documentUrl(key, language = lang) {
    return "?lang=" + language + "&doc=" + encodeURIComponent(normalizeDocumentKey(key));
  }

  function renderMarkdown(md) {
    if (!window.marked || !window.DOMPurify) {
      return '<pre class="raw-markdown">' + escapeHtml(md) + '</pre>';
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
      const chapterKey = clean
        .replace(/^\.\.\//, "")
        .replace(/^en\/publication\//, "")
        .replace(/^publication\//, "")
        .replace(/^en\//, "")
        .replace(/\.en\.md$/i, ".md");
      if (fileMap.has(chapterKey)) {
        const chapter = fileMap.get(chapterKey);
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

    $("heroKicker").textContent = t.heroKicker;
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
    $("printTitle").textContent = t.formalTitle;
    $("printSubtitle").textContent = t.formalSubtitle;

    document.querySelectorAll("#thesisView article").forEach((card, i) => {
      card.querySelector("h2").textContent = t.thesis[i][0];
      card.querySelector("p").textContent = t.thesis[i][1];
    });

    const evidence = lang === "en" ? [
      ["TSMC · 2Q26","66% / 77%","HPC was 66% of revenue; 7 nm and below were 77% of wafer revenue. Revenue mix is not customer wafer allocation."],
      ["HBM · 2026E","≈3×","Micron: same-node / same-bits HBM3E requires ≈3× the wafer supply of DDR5. TrendForce separately estimates HBM wafer input at ~22% (top-three-supplier scope) and HBM bit supply at ~9%; the two scopes are not formally divided."],
      ["LPS · PORTS-Pike","4.25 IT-GW","Initial design capacity planned for phased delivery from 2028. Design / secured capacity is not energized or utilized AI load."],
      ["FINANCE · 2026-08",">US$500B","Third-party-capital mobilization target over time. It is not capital already funded, committed, or deployed."]
    ] : [
      ["TSMC · 2Q26","66% / 77%","HPC 占 revenue 66%；7 nm 及以下占 wafer revenue 77%。这是 revenue mix，不是 customer wafer allocation。"],
      ["HBM · 2026E","≈3×","Micron same-node / same-bits HBM3E ≈3× DDR5 wafer supply；TrendForce 另估 HBM wafer input（前三大供应商口径）约 22%、HBM bit supply 约 9%，两者 scope 不完全一致，不正式相除。"],
      ["LPS · PORTS-Pike","4.25 IT-GW","初始 design capacity，计划自 2028 分阶段交付；design / secured capacity 不等于 energized 或 utilized AI load。"],
      ["FINANCE · 2026-08",">US$500B","third-party-capital mobilization target；不是已经 funded、committed 或 deployed 的资本。"]
    ];
    document.querySelectorAll("#evidenceSnapshot article").forEach((card, i) => {
      card.querySelector("span").textContent = evidence[i][0];
      card.querySelector("h2").textContent = evidence[i][1];
      card.querySelector("p").textContent = evidence[i][2];
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
      document.title = "CH " + String(c.n).padStart(2,"0") + " — " + c[lang] + " | AI Infrastructure Reordering";
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
      document.title = normalized.replace(/\.md$/i, "") + " | AI Infrastructure Reordering";
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
    document.title = (lang === "en" ? "AI Infrastructure Reordering, 2026–2036: A Structural Industry Outlook" : "AI基础设施格局重塑：2026–2036结构性产业展望") + " — 2026 Edition";
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
    document.title = lang === "en"
      ? "AI Infrastructure Reordering | 2026–2036 Industry Outlook Research Report"
      : "AI基础设施格局重塑｜2026–2036产业前瞻研究报告";
  }

  init();
})();