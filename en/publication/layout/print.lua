-- Print-only structural filter.
-- It changes presentation, not research content.

local part_titles = {
  ["1"]  = "Part I -- System Power and Physical Scarcity",
  ["10"] = "Part II -- Demand, Substitution, and the Second System Stack",
  ["19"] = "Part III -- Capital Cycles, Profit Pools, and External Transmission",
  ["27"] = "Part IV -- Method, Scenarios, Monitoring, and Strategy"
}

local report_title = "AI Infrastructure Reordering, 2026–2036: A Structural Industry Outlook"

local function stringify(el)
  return pandoc.utils.stringify(el)
end

local function part_divider(chapter, part)
  local title = part_titles[chapter]
  if not title then
    return nil
  end

  return pandoc.RawBlock(
    "latex",
    "\\clearpage\n" ..
    "\\thispagestyle{empty}\n" ..
    "\\vspace*{34mm}\n" ..
    "{\\sffamily\\fontsize{10}{12}\\selectfont\\color{ReportMuted}RESEARCH REPORT / PART " .. part .. "\\par}\n" ..
    "\\vspace{9mm}\n" ..
    "{\\sffamily\\bfseries\\fontsize{29}{34}\\selectfont\\color{ReportNavy}" .. title .. "\\par}\n" ..
    "\\vspace{7mm}\n" ..
    "{\\color{ReportRule}\\rule{\\textwidth}{0.8pt}}\n" ..
    "\\addcontentsline{toc}{part}{" .. title .. "}\n" ..
    "\\clearpage"
  )
end

function Header(el)
  local txt = stringify(el)

  -- The cover already carries the report title.
  if el.level == 1 and txt == report_title then
    return {}
  end

  if el.level == 1 then
    local part, chapter, title = txt:match("^Part ([IVX]+) · Chapter (%d+): (.+)$")
    if part and chapter and title then
      local blocks = {}
      local divider = part_divider(chapter, part)

      if divider then
        table.insert(blocks, divider)
      end

      if chapter == "1" then
        table.insert(
          blocks,
          pandoc.RawBlock("latex", "\\pagenumbering{arabic}\\setcounter{page}{1}")
        )
      end

      local new_text = "Chapter " .. chapter .. ": " .. title
      table.insert(blocks, pandoc.Header(1, new_text, el.attr))
      return blocks
    end

    if txt == "Research Transparency, Limitations, and Correction Policy" then
      return {
        pandoc.RawBlock("latex", "\\clearpage"),
        el
      }
    end
  end
end


function Table(el)
  local columns = 0
  if el.colspecs then
    columns = #el.colspecs
  end

  if columns >= 5 then
    return {
      pandoc.RawBlock("latex", "\\clearpage\\begin{landscape}\\footnotesize"),
      el,
      pandoc.RawBlock("latex", "\\end{landscape}\\clearpage")
    }
  end
end
