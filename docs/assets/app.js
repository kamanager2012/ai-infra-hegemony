(() => {
  "use strict";

  const chapters = [
    {n:1,part:1,file:"part-I-ch01-executive-summary.md",en:"Executive Summary",zh:"执行摘要"},
    {n:2,part:1,file:"part-I-ch02-nvidia-system-stack.md",en:"NVIDIA's System Stack and Platform Power",zh:"NVIDIA 系统栈与平台权力"},
    {n:3,part:1,file:"part-I-ch03-resource-gravity.md",en:"AI Resource Reallocation and Non-AI Residual Capacity",zh:"AI 资源重配与 Non-AI Residual Capacity"},
    {n:4,part:1,file:"part-I-ch04-tsmc-advanced-logic.md",en:"Advanced Logic Allocation — TSMC, N2, and the Next Unit of Qualified Capacity",zh:"Advanced Logic Allocation——TSMC、N2 与下一单位 Qualified Capacity"},
    {n:5,part:1,file:"part-I-ch05-hbm-memory.md",en:"HBM Economics — Manufacturing Intensity, Residual Capacity, and Memory Scarcity",zh:"HBM Economics——Manufacturing Intensity、Residual Capacity 与 Memory Scarcity"},
    {n:6,part:1,file:"part-I-ch06-advanced-packaging.md",en:"Advanced Packaging — The Quantity Gate Between Wafers and Deliverable Systems",zh:"Advanced Packaging——Wafer 与 Deliverable System 之间的 Quantity Gate"},
    {n:7,part:1,file:"part-I-ch07-power-constraint.md",en:"Time-to-Power — From Rack Density to Deployable AI Capacity",zh:"Time-to-Power——从 Rack Density 到 Deployable AI Capacity"},
    {n:8,part:1,file:"part-I-ch08-quantitative-framework.md",en:"Quantitative Framework — What Can Be Measured, What Cannot, and Why",zh:"Quantitative Framework——什么可以量化，什么不能，以及为什么"},
    {n:9,part:1,file:"part-I-ch09-semiconductor-redundancy.md",en:"Semiconductor Supply-Chain Resilience — Equipment, Materials, and Geographic Redundancy",zh:"Semiconductor Supply-Chain Resilience——Equipment、Materials 与 Geographic Redundancy"},
    {n:10,part:2,file:"part-II-ch10-model-economics.md",en:"Model Unit Economics, Algorithmic Efficiency, and Open-Model Competition",zh:"模型单位经济、算法效率与开放模型竞争"},
    {n:11,part:2,file:"part-II-ch11-nvidia-ai-factory.md",en:"NVIDIA's System-Orchestration Strategy Beyond Accelerators",zh:"NVIDIA 的 System-Orchestration Strategy：超越 Accelerator"},
    {n:12,part:2,file:"part-II-ch12-hyperscaler-system-stack.md",en:"The Second System Stack — How Hyperscaler Substitution Actually Works",zh:"第二类 System Stack——Hyperscaler Substitution 如何真正成立"},
    {n:13,part:2,file:"part-II-ch13-anchor-compute-buyer.md",en:"Anchor Compute Buyers — How Long-Duration Demand Pulls Infrastructure Forward",zh:"Anchor Compute Buyers——Long-Duration Demand 如何提前拉动 Infrastructure"},
    {n:14,part:2,file:"part-II-ch14-agent-software.md",en:"Agent-Native Software and AI Software Unit Economics",zh:"Agent-Native Software 与 AI Software Unit Economics"},
    {n:15,part:2,file:"part-II-ch15-physical-ai.md",en:"Physical AI and the Real Bottlenecks in Robotics",zh:"Physical AI 与机器人系统的真正瓶颈"},
    {n:16,part:2,file:"part-II-ch16-differentiated-competitors.md",en:"AMD, Intel, Qualcomm, and Apple — Differentiated Competitive Paths",zh:"AMD、Intel、Qualcomm 与 Apple 的差异化竞争路径"},
    {n:17,part:2,file:"part-II-ch17-china-parallel-stack.md",en:"China's Parallel Stack — Production-Grade Substitution vs. Autonomous Frontier Closure",zh:"中国 Parallel Stack：Production-Grade Substitution 与 Autonomous Frontier Closure"},
    {n:18,part:2,file:"part-II-ch18-antitrust-policy.md",en:"Antitrust, Industrial Policy, and the Boundaries of AI Platform Power",zh:"反垄断、产业政策与 AI 平台权力边界"},
    {n:19,part:3,file:"part-III-ch19-capex-supercycle.md",en:"AI Infrastructure Capital Formation — Utilization, Commitments, and Duration Risk",zh:"AI 基础设施资本形成——Utilization、Commitments 与 Duration Risk"},
    {n:20,part:3,file:"part-III-ch20-value-capture-map.md",en:"Value Capture and Risk Bearing Across the AI Infrastructure Stack",zh:"AI Infrastructure Stack 的 Value Capture 与 Risk Bearing"},
    {n:21,part:3,file:"part-III-ch21-consumer-transmission.md",en:"How AI Reprices Consumer Electronics and Other End Systems",zh:"AI 如何重定价消费电子与其他终端系统"},
    {n:22,part:3,file:"part-III-ch22-depreciation-wall.md",en:"The Depreciation Wall and Duration Mismatch",zh:"折旧墙与 Duration Mismatch"},
    {n:23,part:3,file:"part-III-ch23-capital-financing.md",en:"AI Infrastructure Capital Markets and Financing Structure",zh:"AI 基础设施资本市场与融资结构"},
    {n:24,part:3,file:"part-III-ch24-capital-clearing.md",en:"Capital Clearing — Lead Indicators, Demand Quality, and the S4 Test",zh:"Capital Clearing——Lead Indicators、Demand Quality 与 S4 Test"},
    {n:25,part:3,file:"part-III-ch25-labor-market.md",en:"AI and Labor Markets — The Task-to-Job Translation Layer",zh:"AI 与劳动市场——Task-to-Job Translation"},
    {n:26,part:3,file:"part-III-ch26-education-talent.md",en:"Education and Talent Systems in the AI Era",zh:"AI 时代教育与人才体系"},
    {n:27,part:4,file:"part-IV-ch27-research-method.md",en:"Research Method and Evidence Architecture",zh:"研究方法与证据架构"},
    {n:28,part:4,file:"part-IV-ch28-timeline-2026-2036.md",en:"2026–2036 Timeline and Conditional Milestones",zh:"2026–2036 时间线与阶段性里程碑"},
    {n:29,part:4,file:"part-IV-ch29-monitoring-framework.md",en:"Monitoring Framework — State Variables, Inflection Tests, and Scenario Reweighting",zh:"Monitoring Framework——State Variables、Inflection Tests 与 Scenario Reweighting"},
    {n:30,part:4,file:"part-IV-ch30-scenarios.md",en:"Scenario Framework — Distinguishing S1–S4",zh:"Scenario Framework——S1–S4 判别"},
    {n:31,part:4,file:"part-IV-ch31-strategy-endgame.md",en:"Strategic Implications Across Alternative AI Infrastructure States",zh:"不同 AI 基础设施状态下的战略含义"},
    {n:32,part:4,file:"part-IV-ch32-master-judgment.md",en:"Master View — What Determines Industrial Power in AI Infrastructure, and What Would Change the View",zh:"Master View——什么决定 AI 基础设施中的产业权力，什么事实会改变判断"}
  ];

  const partNames = {
    en:["","Part I — System Power and Physical Scarcity","Part II — Demand, Substitution, and the Second System Stack","Part III — Capital Cycles, Profit Pools, and External Transmission","Part IV — Method, Scenarios, Monitoring, and Strategy"],
    zh:["","Part I — 系统权力与物理稀缺","Part II — 需求、替代与第二系统栈","Part III — 资本周期、利润池与外部传导","Part IV — 方法、情景、监测与战略"]
  };

  const ui = {
    en:{
      heroKicker:"INDUSTRY RESEARCH · ENGLISH CANONICAL EDITION",
      heroTitle:"AI Infrastructure Reordering,\n2026–2036",
      heroSubtitle:"A Structural Industry Outlook",
      heroDek:"How the AI compute buildout is reallocating semiconductors, memory, advanced packaging, power, capital, and end-market capacity.",
      heroSummary:"The report tracks competition at the system-stack level and asks whether supply elasticity, alternative stacks, workload monetization, and capital clearing can loosen today’s concentration before scarcity migrates into the next constrained layer.",
      brief:"Read the Research Brief",executive:"Executive Summary",master:"Master View",
      edition:"2026 EDITION",cutoff:"Evidence cutoff",revision:"Edition revision",baseline:"Current baseline",publication:"Publication",
      scope:"Scope, evidence boundaries & disclaimer →",
      pathsEyebrow:"READER PATHS",pathsTitle:"Start from the decision you need to make",
      pathsNote:"The report is deliberately broad. These paths isolate the load-bearing mechanism relevant to different professional readers.",
      paths:[
        ["Resource allocation","Residual qualified supply, HBM, packaging and power.","Ch03 → Ch08 → Ch21"],
        ["System-stack competition","NVIDIA, hyperscalers, open-model economics and China’s parallel stack.","Ch02 → Ch12 → Ch17"],
        ["Capital formation & clearing","Duration, utilization, financing reflexivity and the S4 test.","Ch19 → Ch24 → Ch30"],
        ["Method & falsification","Evidence grades, denominators, monitoring and scenario reweighting.","Ch27 → Ch30 → Ch32"]
      ],
      evidenceEyebrow:"LOAD-BEARING EVIDENCE",evidenceTitle:"A small number of facts carry most of the current baseline",
      evidenceNote:"Each observation keeps its own denominator, time identity, and evidence boundary.",
      evidence:[
        ["TSMC · 2Q26","66% / 77%","HPC was 66% of total revenue; 7 nm and below were 77% of wafer revenue. The denominators are separate and neither is customer-level wafer allocation."],
        ["HBM · PHYSICAL INTENSITY","≈3×","Micron: at the same technology node and the same number of bits, HBM3E requires approximately 3× the wafer supply of DDR5. It is not a price multiple or a permanent ratio for every HBM generation."],
        ["NVIDIA · 2026","95.2 → 119 → 279","US$B forward supply / capacity commitment family across Jan. 25, Apr. 26 and Jul. 26. Reporting labels, mix and duration are not assumed homogeneous. Terms/cancellability undisclosed; the sequence is a family-scale indicator, not a growth rate."],
        ["FINANCING · RISK EXPOSURE","105 / 4.1","US$B maximum guarantee exposures: NVIDIA PORTS-Pike US$105B; AMD US$4.1B. They are not funded CapEx or additive demand totals; PORTS-Pike’s 4.25 IT-GW is design capacity, not active load."]
      ],
      boundaryEyebrow:"EVIDENCE DISCIPLINE",
      boundaries:[
        ["Revenue mix ≠ wafer allocation.","Economic direction is not physical customer allocation."],
        ["Secured ≠ energized ≠ utilized.","Power and LPS retain delivery-state identity."],
        ["Target ≠ funded capital.","Guarantee exposure, CapEx and independent demand remain separate."],
        ["Substitution ≠ autonomy.","Production-grade deployment and frontier closure are different tests."]
      ],
      indexEyebrow:"FULL REPORT",indexTitle:"32-chapter research map",
      indexNote:"English is the canonical research language. Chinese is the professional parity edition.",
      searchPlaceholder:"Search chapter titles…",searchLabel:"Search chapters",
      libraryEyebrow:"RESEARCH LIBRARY",libraryTitle:"Publication and audit companions",
      libraryNote:"Use the publication layer for reading and the audit companions when you need source identity, hypotheses, or evidence boundaries.",
      library:[
        ["Figures","11 core analytical figures"],["Tables","30 formal tables"],["Glossary","Core terms and model definitions"],
        ["Evidence Ledger","High-impact source-of-truth identities"],["Source Index","Primary and institutional source map"],["Hypothesis Matrix","H1–H19 and falsification structure"]
      ],
      back:"Report home",copy:"Copy link",copied:"Copied",chapters:"Chapters",onPage:"ON THIS PAGE",backTop:"Back to top ↑",
      readerEdition:"2026 EDITION",readerTitle:"32 chapters",prev:"Previous",next:"Next",
      appendix:"PUBLIC RESEARCH APPENDIX",loading:"Loading report…",
      unavailableChapter:"This chapter is unavailable in the current public snapshot.",
      unavailableDoc:"This document is not included in the public publication snapshot.",
      notes:"Notes",
      footerEdition:"Structural Industry Outlook · 2026 edition",
      footerBrief:"Research Brief",footerTransparency:"Transparency & Corrections",
      footerNote:"English is the canonical analytical edition. Public reading does not grant a general reuse license."
    },
    zh:{
      heroKicker:"产业研究 · 中文专业译本",
      heroTitle:"AI基础设施格局重塑：\n2026–2036",
      heroSubtitle:"结构性产业展望",
      heroDek:"AI 算力扩张如何重配半导体、存储、先进封装、电力、资本与终端产能。",
      heroSummary:"本报告以 system stack 为竞争单位，持续追踪 supply elasticity、alternative stack、workload monetization 与 capital clearing，判断当前集中状态能否被削弱，还是稀缺性继续迁移到下一层约束。",
      brief:"阅读 Research Brief",executive:"执行摘要",master:"Master View",
      edition:"2026 版",cutoff:"Evidence cutoff",revision:"Edition revision",baseline:"Current baseline",publication:"出版结构",
      scope:"报告定位、证据边界与免责声明 →",
      pathsEyebrow:"阅读路径",pathsTitle:"从你真正需要判断的问题进入",
      pathsNote:"报告覆盖面很广，但并非所有章节承重相同。以下路径直接进入不同专业读者最相关的机制主链。",
      paths:[
        ["资源配置","Residual qualified supply、HBM、先进封装与 power。","Ch03 → Ch08 → Ch21"],
        ["System-stack competition","NVIDIA、hyperscaler、开放模型经济与中国 parallel stack。","Ch02 → Ch12 → Ch17"],
        ["资本形成与清算","Duration、utilization、Financing Reflexivity 与 S4 test。","Ch19 → Ch24 → Ch30"],
        ["方法与证伪","Evidence grade、denominator、monitoring 与 scenario reweighting。","Ch27 → Ch30 → Ch32"]
      ],
      evidenceEyebrow:"承重证据",evidenceTitle:"当前 baseline 主要由少数高权重事实支撑",
      evidenceNote:"每一个数字都保留自己的 denominator、time identity 与 evidence boundary。",
      evidence:[
        ["TSMC · 2Q26","66% / 77%","HPC 占 total revenue 66%；7 nm 及以下占 wafer revenue 77%。两个 denominator 分开，均不是 customer-level wafer allocation。"],
        ["HBM · PHYSICAL INTENSITY","≈3×","Micron：same technology node / same number of bits 下，HBM3E 约需 DDR5 的 3× wafer supply。它不是价格倍数，也不是所有 HBM generation 的永久比例。"],
        ["NVIDIA · 2026","95.2 → 119 → 279","US$B forward supply / capacity commitment family，对应 1 月 25 日、4 月 26 日、7 月 26 日。不同报告时点的 label、mix 与 duration 不视为同质；条款/可取消性未披露，该序列是 family-scale 指标而非增长率。"],
        ["FINANCING · RISK EXPOSURE","105 / 4.1","US$B maximum guarantee exposure：NVIDIA PORTS-Pike US$105B；AMD US$4.1B。两者不是 funded CapEx 或可加总 demand；PORTS-Pike 4.25 IT-GW 是 design capacity，不是 active load。"]
      ],
      boundaryEyebrow:"证据纪律",
      boundaries:[
        ["Revenue mix ≠ wafer allocation。","经济方向不等于客户物理 wafer allocation。"],
        ["Secured ≠ energized ≠ utilized。","Power / LPS 必须保留 delivery-state identity。"],
        ["Target ≠ funded capital。","Guarantee exposure、CapEx 与 independent demand 分开。"],
        ["Substitution ≠ autonomy。","Production-grade deployment 与 frontier closure 是两套测试。"]
      ],
      indexEyebrow:"完整报告",indexTitle:"32 章研究地图",
      indexNote:"英文是 canonical research language；中文为专业 parity edition。",
      searchPlaceholder:"搜索章节标题…",searchLabel:"搜索章节",
      libraryEyebrow:"研究资料库",libraryTitle:"出版层与审计 companion",
      libraryNote:"阅读正文使用 publication layer；需要核 evidence identity、hypothesis 或 source boundary 时进入 audit companion。",
      library:[
        ["核心 Figure","11 张核心分析图"],["正式 Table","30 张正式表"],["Glossary","核心术语与模型定义"],
        ["核心证据台账","高影响 source-of-truth identity"],["核心参考文献索引","一手与机构来源地图"],["核心假设矩阵","H1–H19 与 falsification structure"]
      ],
      back:"报告首页",copy:"复制链接",copied:"已复制",chapters:"章节",onPage:"本页目录",backTop:"返回顶部 ↑",
      readerEdition:"2026 版",readerTitle:"32 章",prev:"上一章",next:"下一章",
      appendix:"公开研究附录",loading:"正在载入报告…",
      unavailableChapter:"本章当前未包含在公开出版快照中。",
      unavailableDoc:"该文档未包含在公开出版快照中。",
      notes:"注释",
      footerEdition:"结构性产业展望 · 2026 版",
      footerBrief:"Research Brief",footerTransparency:"研究透明度与纠错",
      footerNote:"英文版是唯一 canonical analytical edition。公开阅读不授予一般性转载或再利用许可。"
    }
  };

  const $ = (id) => document.getElementById(id);
  const params = new URLSearchParams(location.search);
  let lang = params.get("lang") === "zh" ? "zh" : "en";
  const chapterNo = Math.min(32, Math.max(1, Number(params.get("chapter") || 1)));
  let sectionObserver = null;
  const bundleCache = new Map();

  const publicDocuments = new Set([
    "00-front-matter.md","01-table-of-contents.md","01-list-of-figures.md","02-list-of-tables.md",
    "RESEARCH_BRIEF.md","03-abbreviations-and-glossary.md","04-research-transparency.md","05-competitive-evidence-matrix.md",
    "核心证据台账.md","核心参考文献索引.md","核心概念与模型索引.md","核心假设矩阵.md","外部研究对照索引.md"
  ]);

  function chapterUrl(n, language = lang) {
    return "?lang=" + language + "&chapter=" + n;
  }

  function documentUrl(key, language = lang) {
    return "?lang=" + language + "&doc=" + encodeURIComponent(normalizeDocumentKey(key));
  }

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
    for (const file of ["appendices-publication.json","appendices-research.json"]) {
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

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, ch => ({
      "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"
    })[ch]);
  }

  function safeId(value) {
    return String(value).trim().replace(/[^a-zA-Z0-9_-]+/g, "-") || "note";
  }

  function extractFootnotes(md) {
    const lines = String(md).replace(/\r\n/g, "\n").split("\n");
    const definitions = new Map();
    const body = [];
    let inFence = false;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      if (/^\s*(?:\x60{3}|~~~)/.test(line)) {
        inFence = !inFence;
        body.push(line);
        continue;
      }

      const match = !inFence && line.match(/^\[\^([^\]]+)\]:\s*(.*)$/);
      if (!match) {
        body.push(line);
        continue;
      }

      const id = match[1];
      const parts = [match[2]];
      while (i + 1 < lines.length) {
        const next = lines[i + 1];
        if (/^\s{2,}\S/.test(next)) {
          parts.push(next.trim());
          i++;
          continue;
        }
        if (next.trim() === "" && i + 2 < lines.length && /^\s{2,}\S/.test(lines[i + 2])) {
          parts.push("");
          i++;
          continue;
        }
        break;
      }
      definitions.set(id, parts.join(" ").trim());
    }

    return {body:body.join("\n"),definitions};
  }

  function renderMarkdown(md) {
    if (!window.marked || !window.DOMPurify) {
      return '<pre class="raw-markdown">' + escapeHtml(md) + '</pre>';
    }

    marked.setOptions({gfm:true,breaks:false});
    const parsed = extractFootnotes(md);
    const refCounts = new Map();

    const bodyWithRefs = parsed.body.replace(/\[\^([^\]]+)\]/g, (full, id) => {
      if (!parsed.definitions.has(id)) return full;
      const safe = safeId(id);
      const count = (refCounts.get(id) || 0) + 1;
      refCounts.set(id, count);
      return '<sup class="fn-ref" id="fnref-' + safe + '-' + count + '"><a href="#fn-' + safe + '" aria-label="Footnote ' + escapeHtml(id) + '">' + escapeHtml(id) + '</a></sup>';
    });

    let html = marked.parse(bodyWithRefs);

    if (parsed.definitions.size) {
      const items = [];
      for (const [id, text] of parsed.definitions.entries()) {
        const safe = safeId(id);
        const rendered = marked.parseInline(text || "");
        items.push(
          '<li id="fn-' + safe + '">' + rendered +
          ' <a class="footnote-backref" href="#fnref-' + safe + '-1" aria-label="Back to reference">↩</a></li>'
        );
      }
      html += '<section class="footnotes" aria-label="' + escapeHtml(ui[lang].notes) + '"><h2>' +
        escapeHtml(ui[lang].notes) + '</h2><ol>' + items.join("") + '</ol></section>';
    }

    return DOMPurify.sanitize(html, {ADD_ATTR:["target","rel","aria-label","loading","decoding"]});
  }

  function rewriteLinks(container, language) {
    const fileMap = new Map(chapters.map(c => [c.file, c]));

    container.querySelectorAll("a[href]").forEach(a => {
      const href = a.getAttribute("href");
      if (!href) return;

      if (/^https?:\/\//i.test(href)) {
        a.target = "_blank";
        a.rel = "noopener noreferrer";
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
        a.href = chapterUrl(fileMap.get(chapterKey).n, language) + fragment;
        return;
      }

      const docKey = normalizeDocumentKey(clean);
      if (publicDocuments.has(docKey)) {
        a.href = documentUrl(docKey, language) + fragment;
        return;
      }

      if (clean.endsWith(".md")) {
        a.removeAttribute("href");
        a.title = language === "en"
          ? "This internal research file is not part of the public publication snapshot."
          : "该内部研究文件不属于公开出版快照。";
      }
    });
  }

  function slugify(text, index) {
    try {
      const slug = String(text).normalize("NFKC").toLowerCase()
        .replace(/[^\p{L}\p{N}]+/gu, "-").replace(/^-+|-+$/g, "");
      return slug || "section-" + index;
    } catch {
      return "section-" + index;
    }
  }

  function enhanceContent(container, language) {
    rewriteLinks(container, language);

    container.querySelectorAll("table").forEach(table => {
      if (table.parentElement && table.parentElement.classList.contains("table-scroll")) return;
      const wrap = document.createElement("div");
      wrap.className = "table-scroll";
      table.parentNode.insertBefore(wrap, table);
      wrap.appendChild(table);
    });

    container.querySelectorAll("img").forEach(img => {
      img.loading = "lazy";
      img.decoding = "async";
      const parent = img.parentElement;
      if (parent && parent.tagName === "P") parent.classList.add("figure-block");
    });

    container.querySelectorAll("p").forEach(p => {
      const first = p.querySelector(":scope > strong:first-child");
      if (!first) return;
      const label = first.textContent.trim();
      if (/^(Figure\s+\d+\s+note|图\s*\d+|Figure\s+note)/i.test(label)) p.classList.add("figure-note");
    });

    const headings = [...container.querySelectorAll("h2,h3")];
    const seen = new Map();
    headings.forEach((heading, index) => {
      let id = slugify(heading.textContent, index + 1);
      const count = (seen.get(id) || 0) + 1;
      seen.set(id, count);
      if (count > 1) id += "-" + count;
      heading.id = id;
    });

    const h2 = headings.filter(h => h.tagName === "H2");
    buildSectionNav(h2.slice(0,24));
    setupSectionObserver(h2);
    updateReadingProgress();

    if (location.hash) {
      requestAnimationFrame(() => {
        const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
        if (target) target.scrollIntoView({block:"start"});
      });
    }
  }

  function buildSectionNav(headings) {
    const nav = $("readerSectionList");
    nav.innerHTML = "";
    const sectionNav = $("sectionNav");
    if (!headings.length) {
      sectionNav.classList.add("hidden");
      return;
    }
    sectionNav.classList.remove("hidden");

    headings.forEach(h => {
      const a = document.createElement("a");
      a.className = "section-link";
      a.href = "#" + h.id;
      a.textContent = h.textContent;
      nav.appendChild(a);
    });
  }

  function setupSectionObserver(headings) {
    if (sectionObserver) sectionObserver.disconnect();
    if (!("IntersectionObserver" in window) || !headings.length) return;

    sectionObserver = new IntersectionObserver(entries => {
      const visible = entries
        .filter(e => e.isIntersecting)
        .sort((a,b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      document.querySelectorAll(".section-link").forEach(a => {
        a.classList.toggle("active", a.getAttribute("href") === "#" + visible.target.id);
      });
    }, {rootMargin:"-90px 0px -72% 0px",threshold:[0,1]});

    headings.forEach(h => sectionObserver.observe(h));
  }

  function updateReadingProgress() {
    const bar = $("readingProgress");
    if (!document.body.classList.contains("chapter-mode")) {
      bar.style.width = "0";
      return;
    }
    const body = $("readerBody");
    if (!body) return;
    const top = body.getBoundingClientRect().top + window.scrollY;
    const total = Math.max(1, body.offsetHeight - window.innerHeight * .55);
    const progress = Math.min(1, Math.max(0, (window.scrollY - top + 100) / total));
    bar.style.width = (progress * 100).toFixed(2) + "%";
  }

  function buildChapterIndex(target, compact = false, query = "") {
    target.innerHTML = "";
    const needle = query.trim().toLocaleLowerCase();
    let matches = 0;

    for (let part = 1; part <= 4; part++) {
      const filtered = chapters.filter(c => {
        if (c.part !== part) return false;
        return !needle || c[lang].toLocaleLowerCase().includes(needle) || String(c.n).includes(needle);
      });
      if (!filtered.length) continue;

      matches += filtered.length;
      const group = document.createElement("section");
      group.className = compact ? "reader-nav-group" : "part-block";

      const title = document.createElement("div");
      title.className = compact ? "reader-nav-part" : "part-title";
      title.textContent = partNames[lang][part];
      group.appendChild(title);

      const list = document.createElement("div");
      list.className = compact ? "reader-nav-list" : "chapter-list";

      filtered.forEach(c => {
        const a = document.createElement("a");
        a.href = chapterUrl(c.n);
        a.className = compact ? "reader-nav-link" : "chapter-card";
        if (compact && params.has("chapter") && c.n === chapterNo) a.classList.add("active");
        a.innerHTML = compact
          ? '<span>' + String(c.n).padStart(2,"0") + '</span><span>' + escapeHtml(c[lang]) + '</span>'
          : '<span class="chapter-no">CH ' + String(c.n).padStart(2,"0") + '</span><span class="chapter-name">' + escapeHtml(c[lang]) + '</span><span class="chapter-arrow">→</span>';
        list.appendChild(a);
      });

      group.appendChild(list);
      target.appendChild(group);
    }

    if (!matches && !compact) {
      target.innerHTML = '<div class="no-results">' + (lang === "en" ? "No chapter title matches this search." : "没有匹配的章节标题。") + '</div>';
    }
  }

  function setLanguageUI() {
    const t = ui[lang];
    document.documentElement.lang = lang === "en" ? "en" : "zh-CN";

    $("homeLink").href = "./?lang=" + lang;
    $("headerBrief").href = documentUrl("RESEARCH_BRIEF.md");
    $("headerMethod").href = chapterUrl(27);
    $("langToggle").textContent = lang === "zh" ? "EN" : "中文";
    $("readerLangToggle").textContent = lang === "zh" ? "EN" : "中文";
  }

  function patchLanguageUI() {
    const t = ui[lang];
    $("readerLangToggle").textContent = lang === "zh" ? "EN" : "中文";
    $("heroKicker").textContent = t.heroKicker;
    $("heroTitle").innerHTML = escapeHtml(t.heroTitle).replace("\n","<br>");
    $("heroSubtitle").textContent = t.heroSubtitle;
    $("heroDek").textContent = t.heroDek;
    $("heroSummary").textContent = t.heroSummary;

    $("researchBrief").textContent = t.brief;
    $("researchBrief").href = documentUrl("RESEARCH_BRIEF.md");
    $("startReading").textContent = t.executive;
    $("startReading").href = chapterUrl(1);
    $("masterJudgment").textContent = t.master;
    $("masterJudgment").href = chapterUrl(32);

    $("editionLabel").textContent = t.edition;
    $("cutoffLabel").textContent = t.cutoff;
    $("revisionLabel").textContent = t.revision;
    $("baselineLabel").textContent = t.baseline;
    $("scopeLabel").textContent = t.publication;
    $("scopeLink").textContent = t.scope;
    $("scopeLink").href = documentUrl("00-front-matter.md");

    $("readingPathsEyebrow").textContent = t.pathsEyebrow;
    $("readingPathsTitle").textContent = t.pathsTitle;
    $("readingPathsNote").textContent = t.pathsNote;
    document.querySelectorAll("#readingPathGrid .path-card").forEach((card,i) => {
      card.querySelector("h3").textContent = t.paths[i][0];
      card.querySelector("p").textContent = t.paths[i][1];
      card.querySelector("b").textContent = t.paths[i][2];
    });
    [3,12,19,27].forEach((n,i) => {
      const card = document.querySelectorAll("#readingPathGrid .path-card")[i];
      if (card) card.href = chapterUrl(n);
    });

    $("evidenceEyebrow").textContent = t.evidenceEyebrow;
    $("evidenceTitle").textContent = t.evidenceTitle;
    $("evidenceNote").textContent = t.evidenceNote;
    document.querySelectorAll("#evidenceSnapshot article").forEach((card,i) => {
      card.querySelector("span").textContent = t.evidence[i][0];
      card.querySelector("h3").textContent = t.evidence[i][1];
      card.querySelector("p").textContent = t.evidence[i][2];
    });

    $("boundaryEyebrow").textContent = t.boundaryEyebrow;
    document.querySelectorAll("#boundaryStrip .boundary-grid p").forEach((p,i) => {
      p.innerHTML = "<strong>" + escapeHtml(t.boundaries[i][0]) + "</strong><br><span>" + escapeHtml(t.boundaries[i][1]) + "</span>";
    });

    $("indexEyebrow").textContent = t.indexEyebrow;
    $("indexTitle").textContent = t.indexTitle;
    $("indexNote").textContent = t.indexNote;
    $("chapterSearch").placeholder = t.searchPlaceholder;
    $("chapterSearchLabel").textContent = t.searchLabel;

    $("libraryEyebrow").textContent = t.libraryEyebrow;
    $("libraryTitle").textContent = t.libraryTitle;
    $("libraryNote").textContent = t.libraryNote;
    const libraryKeys = ["01-list-of-figures.md","02-list-of-tables.md","03-abbreviations-and-glossary.md","核心证据台账.md","核心参考文献索引.md","核心假设矩阵.md"];
    document.querySelectorAll("#libraryGrid a").forEach((a,i) => {
      a.href = documentUrl(libraryKeys[i]);
      a.querySelector("strong").textContent = t.library[i][0];
      a.querySelector("span").textContent = t.library[i][1];
    });

    $("backHome").href = "./?lang=" + lang;
    $("backHome").querySelector("span").textContent = t.back;
    $("copyLink").textContent = t.copy;
    $("readerNavToggle").textContent = t.chapters;
    $("sectionNavLabel").textContent = t.onPage;
    $("backToTop").textContent = t.backTop;
    $("readerNavEdition").textContent = t.readerEdition;
    $("readerNavTitle").textContent = t.readerTitle;

    $("footerEdition").textContent = t.footerEdition;
    $("footerBrief").textContent = t.footerBrief;
    $("footerBrief").href = documentUrl("RESEARCH_BRIEF.md");
    $("footerTransparency").textContent = t.footerTransparency;
    $("footerTransparency").href = documentUrl("04-research-transparency.md");
    $("footerNote").textContent = t.footerNote;
  }

  function showHome() {
    document.body.classList.remove("chapter-mode");
    $("homeShell").classList.remove("hidden");
    $("readerView").classList.add("hidden");
    $("readingProgress").style.width = "0";
    buildChapterIndex($("chapterIndex"), false, $("chapterSearch").value || "");
    document.title = lang === "en"
      ? "AI Infrastructure Reordering, 2026–2036: A Structural Industry Outlook"
      : "AI基础设施格局重塑：2026–2036结构性产业展望";
  }

  async function showReader(n) {
    document.body.classList.add("chapter-mode");
    $("homeShell").classList.add("hidden");
    $("readerView").classList.remove("hidden");
    $("readerNav").classList.remove("open");

    const c = chapters[n - 1];
    $("readerPart").textContent = partNames[lang][c.part];
    $("readerChapterLabel").textContent = "CH " + String(c.n).padStart(2,"0");
    buildChapterIndex($("readerChapterList"), true);

    $("prevChapter").textContent = c.n > 1 ? "← " + ui[lang].prev + " · CH " + String(c.n - 1).padStart(2,"0") : "";
    $("prevChapter").href = c.n > 1 ? chapterUrl(c.n - 1) : "#";
    $("nextChapter").textContent = c.n < 32 ? ui[lang].next + " · CH " + String(c.n + 1).padStart(2,"0") + " →" : "";
    $("nextChapter").href = c.n < 32 ? chapterUrl(c.n + 1) : "#";

    $("readerBody").innerHTML = '<div class="loading">' + escapeHtml(ui[lang].loading) + '</div>';
    $("readerSectionList").innerHTML = "";

    try {
      const md = await fetchChapter(lang, c);
      $("readerBody").innerHTML = renderMarkdown(md);
      enhanceContent($("readerBody"), lang);
      document.title = "CH " + String(c.n).padStart(2,"0") + " — " + c[lang] + " | AI Infrastructure Reordering";
    } catch (err) {
      $("readerBody").innerHTML = '<h1>' + escapeHtml(c[lang]) + '</h1><p>' + escapeHtml(ui[lang].unavailableChapter) + '</p>';
      buildSectionNav([]);
    }
  }

  async function showDocument(key) {
    document.body.classList.add("chapter-mode");
    $("homeShell").classList.add("hidden");
    $("readerView").classList.remove("hidden");
    $("readerNav").classList.remove("open");

    const normalized = normalizeDocumentKey(key);
    $("readerPart").textContent = ui[lang].appendix;
    $("readerChapterLabel").textContent = normalized.replace(/\.md$/i,"");
    buildChapterIndex($("readerChapterList"), true);
    $("prevChapter").textContent = "";
    $("nextChapter").textContent = "";
    $("readerBody").innerHTML = '<div class="loading">' + escapeHtml(ui[lang].loading) + '</div>';
    $("readerSectionList").innerHTML = "";

    try {
      const md = await fetchDocument(lang, normalized);
      $("readerBody").innerHTML = renderMarkdown(md);
      enhanceContent($("readerBody"), lang);
      const first = $("readerBody").querySelector("h1");
      document.title = (first ? first.textContent : normalized.replace(/\.md$/i,"")) + " | AI Infrastructure Reordering";
    } catch (err) {
      $("readerBody").innerHTML = '<h1>' + escapeHtml(normalized.replace(/\.md$/i,"")) + '</h1><p>' + escapeHtml(ui[lang].unavailableDoc) + '</p>';
      buildSectionNav([]);
    }
  }

  function toggleLanguage() {
    const q = new URLSearchParams(location.search);
    q.set("lang", lang === "zh" ? "en" : "zh");
    location.search = q.toString();
  }

  function bindActions() {
    $("langToggle").addEventListener("click", toggleLanguage);
    $("readerLangToggle").addEventListener("click", toggleLanguage);

    $("copyLink").addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(location.href);
        $("copyLink").textContent = ui[lang].copied;
        setTimeout(() => $("copyLink").textContent = ui[lang].copy, 1200);
      } catch {
        window.prompt(lang === "en" ? "Copy link:" : "复制链接：", location.href);
      }
    });

    $("chapterSearch").addEventListener("input", event => {
      buildChapterIndex($("chapterIndex"), false, event.target.value);
    });

    $("readerNavToggle").addEventListener("click", () => {
      $("readerNav").classList.toggle("open");
    });

    $("readerChapterList").addEventListener("click", event => {
      if (event.target.closest("a")) $("readerNav").classList.remove("open");
    });

    document.addEventListener("keydown", event => {
      if (event.key === "Escape") $("readerNav").classList.remove("open");
    });

    window.addEventListener("scroll", updateReadingProgress, {passive:true});
    window.addEventListener("resize", updateReadingProgress, {passive:true});
  }

  async function init() {
    setLanguageUI();
    patchLanguageUI();
    bindActions();

    if (params.has("chapter")) {
      await showReader(chapterNo);
      return;
    }
    if (params.has("doc")) {
      await showDocument(params.get("doc"));
      return;
    }
    showHome();
  }

  init();
})();
