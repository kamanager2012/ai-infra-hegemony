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

      if chapter == "1" then
        table.insert(blocks, pandoc.RawBlock("latex", "\\mainmatter"))
      end

      if part_titles[chapter] then
        table.insert(
          blocks,
          pandoc.RawBlock(
            "latex",
            "\\cleardoublepage\\part*{" .. part_titles[chapter] .. "}\\addcontentsline{toc}{part}{Part " .. part .. "}"
          )
        )
      end

      local new_text = "Chapter " .. chapter .. ": " .. title
      table.insert(blocks, pandoc.Header(1, new_text, el.attr))
      return blocks
    end

    if txt == "Research Transparency, Limitations, and Correction Policy" then
      return {
        pandoc.RawBlock("latex", "\\backmatter"),
        el
      }
    end
  end
end
